from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.utils import model_category

# Register Category
@login_required()
def category(request):
    return render(request, "core/category.html")

# Add Data Base Category
def set_category(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    tags = request.POST.get('tags')
    model_category.insert_data(name.title(), description, tags.lower())
    messages.success(request, "Dados inseridos com sucesso!")
    return  redirect('/category/')


