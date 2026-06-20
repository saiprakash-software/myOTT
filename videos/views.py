from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from .models import Video, DeletedVideo

# Homepage with search
def home(request):
    query = request.GET.get('q')
    if query:
        videos = Video.objects.filter(title__icontains=query) | Video.objects.filter(description__icontains=query)
    else:
        videos = Video.objects.all().order_by('-uploaded_at')
    return render(request, 'videos/home.html', {'videos': videos, 'query': query})

# Upload video
def upload_video(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        video_file = request.FILES['video_file']
        thumbnail = request.FILES['thumbnail']
        video = Video(title=title, description=description, video_file=video_file, thumbnail=thumbnail)
        video.save()
        return redirect('home')
    return render(request, 'videos/upload.html')

# Video detail page with view count
def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    video.views += 1
    video.save()
    return render(request, 'videos/video_detail.html', {'video': video})

# Register user
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'videos/register.html', {'form': form})

# Login user with warning message
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'videos/login.html', {'form': form})

# Logout user
def logout_view(request):
    logout(request)
    return redirect('home')

# Manage videos
def video_manager(request):
    videos = Video.objects.all()
    return render(request, 'manage.html', {'videos': videos})

# Delete video (POST)
def delete_video(request, video_id):
    if request.method == 'POST':
        video = get_object_or_404(Video, id=video_id)

        # Save deleted video info
        DeletedVideo.objects.create(
            title=video.title,
            description=video.description
        )

        # Delete files
        if video.video_file:
            video.video_file.delete()
        if video.thumbnail:
            video.thumbnail.delete()

        video.delete()

    return redirect('video_manager')
