from django.contrib import admin
from django.urls import path, include
from blog.views import hello_world

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('home/', hello_world, name='hello_world'),
]