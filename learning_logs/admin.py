from django.contrib import admin

# Register your models here.
from .models import Topic

admin.site.register(Topic)

from django.contrib import admin
from .models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
     path('admin/', admin.site.urls),
     path('', include('learning_logs.urls')),
]
