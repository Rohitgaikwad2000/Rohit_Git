from django.shortcuts import  render, redirect
from .forms import NewUserForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			return redirect("homepage")
	form = NewUserForm()                     # else using get method    OR (create html form)
	print(form)                            # for check html form
	return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect("home")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})




	