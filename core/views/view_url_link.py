from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.utils import *
from django.core.paginator import Paginator, InvalidPage

# Register URL
@login_required()
def url_link(request):
    data_subcategory = model_subcategory.list_all_data()
    
    dt_subcategory_dataFrame = {}
    dt_lst = []
    for dt in data_subcategory:
        dt_lst.append(dt.to_dict())
    dt_subcategory_dataFrame = dt_lst
    
    context = {
        'data_subcategory': dt_subcategory_dataFrame,
    }
    return render(request, "core/url_link.html", context)

# List URL
ITEMS_PER_PAGE = 1
@login_required()
def list_url(request):
    data_list_url = model_url_link.list_all_data()
    
    dt_list_url = {}
    dt_lst = []
    for dt in data_list_url:
        dt_lst.append(dt.to_dict())
    dt_list_url = dt_lst
    
    # Paginator
    posts = dt_list_url
    p = Paginator(posts, 5)  
    
    page_number = request.GET.get('page') 
    try: 
        page_obj = p.get_page(page_number)  
    except PageNotAnInteger: 
      page_obj = p.page(1) 
    except EmptyPage: 
      page_obj = p.page(p.num_pages) 
      
    context = {
        'page_obj': page_obj
    }
    
    return render(request, "core/list_url.html", context)

# Add Data Base URL
def set_url(request):
    name = request.POST.get('name')
    url = request.POST.get('url')
    description = request.POST.get('description')
    subcategory = request.POST.get('subcategory')
    tags = request.POST.get('tags')
    model_url_link.insert_data(name, url, description, subcategory, tags)
    messages.success(request, "Dados inseridos com sucesso!")
    return redirect('/url_link/')

# Delete Data Base URL
def delete_url(request, id):
    if request.method == 'GET':
        model_url_link.delete_data(id)
    return redirect("/list_url/")