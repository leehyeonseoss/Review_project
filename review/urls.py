from django.urls import path


from . import views
from .views import index, create_review, mypage, delete, edit
from django.contrib.auth.views import LoginView
app_name = "review"


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:review_id>/', views.detail, name='detail'),
    path('create/', views.create.as_view(), name='create'),
    path('create/', create_review, name='create_review'),
    path('mypage/', mypage, name='mypage'),
    path('login/', LoginView.as_view(), name='login'),
    path('<int:review_id>/edit/', edit, name='edit'),
    path('<int:review_id>/delete/', delete, name='delete'),
    # path('delete/<int:review_id>/', delete_review, name='delete_review'),
]
