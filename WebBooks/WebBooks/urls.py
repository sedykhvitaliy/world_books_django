from django.contrib import admin
from django.urls import path
from catalog import urls

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns = urlpatterns+urls.urlpatterns
