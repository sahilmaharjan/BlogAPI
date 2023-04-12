from django.urls import path
# from accounts.views import UserRegistrationView, LogInView, AllUserProfileView,UserProfileView, UserChangePasswordView,UserPasswordResetView, SendPasswordEmailView
from .views import CreateBlog, BlogList, UpdateBlog, MyBlog, DeleteBlog
urlpatterns = [
    path('create/', CreateBlog.as_view(), name= 'create-blog'),
    path('delete/<int:pk>/',DeleteBlog.as_view(), name= 'delete-blog'),
    path('list/', BlogList.as_view(), name= 'list-blog'),
    path('<int:pk>/', BlogList.as_view(), name= 'single-blog'),
    path('update/<int:pk>/', UpdateBlog.as_view(), name= 'update-blog'),
    path('my-blogs/', MyBlog.as_view(), name= 'my-blogs'),

]