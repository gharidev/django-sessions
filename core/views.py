from django.shortcuts import render, redirect
from django.http.response import HttpResponse

from core.forms import EmailLogin

def visit_count(request):
    page_count = int(request.COOKIES.get("page_count", 1))
    page_count += 1
    response = HttpResponse(f"Page visit count: {page_count}")
    response.set_cookie("page_count", page_count)
    return response

def clear_count(request):
    response = HttpResponse("Cookie cleared...")
    response.delete_cookie("page_count")
    return response

def email_login(request):
    if "email" in request.session:
        return redirect("profile")
    if request.method == "GET":
        form = EmailLogin()
    else:
        form = EmailLogin(request.POST)
        if form.is_valid():
            request.session["email"] = form.cleaned_data["email"]
            return redirect("profile")
    return render(request, "core/login.html", {"form": form})

def profile(request):
    return render(request, "core/profile.html")

def logout(request):
    request.session.pop("email")
    return HttpResponse("Logged out!")