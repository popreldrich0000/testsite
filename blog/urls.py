from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.say_hello),
    path('giffo/',views.output_gif),
    path('laugho/',views.image_show),
    path('', views.post_list, name='post_list')
]