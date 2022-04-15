from django.urls import path
from user import views
# url added for registration,list,and delete views
urlpatterns = [
    path('register', views.UserView.as_view(), name="user home"),
    path('all', views.UserListView.as_view(), name="user list"),
    path('delete/<int:id>', views.remove_user, name="deleteuser"),
    path('', views.IndexView.as_view(), name="index"),
]
