from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.utils import *

# Register SubCategory
@login_required()
def sub_category(request):
    data_category = model_category.list_all_data()
    
    dt_dataFrame = {}
    dt_lst = []
    for dt in data_category:
        dt_lst.append(dt.to_dict())
    dt_dataFrame = dt_lst
    
    context = {
        'data': dt_dataFrame
    }
    
    return render(request, "core/sub_category.html", context)

# Add Data Base SubCategory
def set_subcategory(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    category = request.POST.get('category')
    tags = request.POST.get('tags')
    model_subcategory.insert_data(name, description, category, tags)
    messages.success(request, "Dados inseridos com sucesso!")
    return redirect('/subcategory/')