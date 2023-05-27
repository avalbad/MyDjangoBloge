from django.urls import path
from . import views

app_name = "a31"
urlpatterns = [
    path('',views.articles_list, name ="a3" ),
    path('create',views.create_article,name ="create" ),
    path('<slug>',views.amir_detail, name = "a2"),
    # path('about/', views.about,name = "about"),

]
