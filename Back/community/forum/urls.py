from django.urls import path
from . import views
app_name = "forum"

urlpatterns = [
    path('', views.home, name="home"),
    path('create', views.create, name="create"),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
]