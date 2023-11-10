from django.urls import path
from app import views
# from .views import update

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('treatments',views.treatments,name='treatments'),
    path('faqs',views.faqs,name='faqs'),
    path('mudras',views.mudras,name='mudras'),
    path('color',views.color,name='color'),
    
    path('ggml',views.AI_GGML,name='ggml'),
    path('chatbot/',views.chatbot,name='chatbot'),
    path('login',views.handlelogin,name='handlelogin'),
    path('logout',views.handlelogout,name='handlelogout'),
    path('signup',views.handlesignup,name='handlesignup'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('edit/<int:id>', views.edit,name='edit'),  
    # path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
    
]

