from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name="home"),
    path('single/<int:id>/',views.single_post,name="single"),
    path('category/<str:category_name>/', views.category, name='category'), 
    path('search-result/',views.search_result,name='search_result'),
    path('create_post/',views.create_post,name='create_post'),
    path('delete_post/<int:id>',views.delete_post,name='delete_post'),

]