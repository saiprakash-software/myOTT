from django.contrib import admin



from .models import Video, DeletedVideo

admin.site.register(Video)
admin.site.register(DeletedVideo)
