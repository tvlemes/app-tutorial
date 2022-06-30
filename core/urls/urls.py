from django.urls import path
from core.views import *

import core

urlpatterns = [

    # Admin
    path('', view_signin.signin_page, name='signin'),

    # Signin
    path('signin_page/', view_signin.signin_page),
    path('signout_page/', view_signin.signout_page),
    path('login_page/', view_signin.login_page),

    # Index
    path('index/', view_signin.index, name='index'),
    
    
    # Category 
    path('category/', view_category.category, name='category'),
    path('category/add', view_category.set_category, name='category/add'),
    
    # SubCategory 
    path('subcategory/', view_subcategory.sub_category, name='subcategory'),
    path('subcategory/add', view_subcategory.set_subcategory,  name='subcategory/add'),
    
    # URL
    path('url_link/', view_url_link.url_link, name='url_link'),
    path('url_link/add', view_url_link.set_url, name='url_link/add'),
    path('list_url/', view_url_link.list_url, name='list_url'),
    path('list_url/del/<id>/', view_url_link.delete_url),
    
    
]