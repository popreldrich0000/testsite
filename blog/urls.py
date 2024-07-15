from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.say_hello),
    path('giffo/',views.output_gif),
    path('laugho/',views.image_show),
    path('', views.post_list, name='post_list'),
    path('create_blog/',views.create_view),
    path('list_blog/',views.list_view),
    path('list_blog/<id>',views.detail_view),
    path('<id>', views.update_view),
    path('<id>/delete/', views.delete_view),
    
    
]