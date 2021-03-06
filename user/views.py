from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, ListView
from user.models import User
from user.forms import UserRegistrationForm
from django.urls import reverse_lazy


# Create your views here.

# view for home page
class IndexView(View):
    def get(self, request):
        return render(request, "home.html")


# view to create user data
class UserView(CreateView):
    model = User
    template_name = "user_home.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("user list")


# view to list the created users list
class UserListView(ListView):
    model = User
    template_name = "user_list.html"
    context_object_name = "users"


# view to delete the user from table
def remove_user(request, id):
    users = User.objects.get(id=id)
    users.delete()
    return redirect("user list")
