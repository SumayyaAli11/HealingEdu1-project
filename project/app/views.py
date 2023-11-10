from django.shortcuts import render,HttpResponse,redirect
#from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import Userform
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
from django.http import JsonResponse
from .models import *

#from .models import CustomUser
# Create your views here.
# @login_required(login_url='/')
@never_cache
def index(request):
    if not request.user.is_authenticated :
        return render(request,'login.html')
    else:
        if request.user.is_superuser:
            return render(request,'admin_home.html')
        else:
            return render(request,'index.html')

def about(request):
    return render(request,'about.html')
def color(request):
    return render(request, 'color.html')
def mudras(request):
    return render(request, 'mudras.html')
"""
from django.views.generic import TemplateView

class ChatbotView(TemplateView):
    template_name = "chatbot.html"
    """

def chatbot(request):
    return render(request,'chatbot.html')

def treatments(request):
    return render(request,'treatments.html')
def faqs(request):
    return render(request,'faqs.html')

# @login_required(login_url='/login')
@never_cache
def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Success")
    return redirect('/login')

# @login_required(login_url='/login')

def handlelogin(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        pass1=request.POST.get("pass1")
        myuser=authenticate(username=uname,password=pass1)
        if myuser is not None:
            if myuser.is_superuser:
                login(request,myuser)
                messages.success(request,"Login Success")
                return redirect('admin_home')
            else:
                login(request,myuser)
                messages.success(request,"Login Success")
                return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/login')
    
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request,'admin_home.html')
    elif request.user.is_authenticated and not request.user.is_superuser: 
        return render(request,'index.html')        
    else:        
        return render(request,'login.html')
    
def handlesignup(request):
    # User=get_user_model()
    if request.method=="POST":
        uname=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("pass1")
        confirmpassword=request.POST.get("pass2")
        #print(uname,email,password,confirmpassword)
        if password!=confirmpassword:
            messages.warning(request,"Password is Incorrect")
            return redirect('/signup')
        
        try:
            if User.objects.get(username=uname):
                messages.info(request,"UserName is Taken")
                return redirect('/signup')
        except:
            pass
        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is Taken")
                return redirect('/signup')
        except:
            pass
        
        myuser=User.objects.create_user(username=uname,email=email,password=password)
        myuser.save()
        messages.success(request,"SignUp Success. Please login")
        return redirect('/login')
    return render(request,'signup.html')

@never_cache
#@login_required(login_url='/admin_home')
def admin_home(request):
    # User=get_user_model()    
    dests = User.objects.all().order_by('id')
    return render(request,'admin_home.html',{'dests':dests})
def destroy(request, id):  
    # User=get_user_model()
    employee = User.objects.get(id=id)  
    employee.delete()  
    return redirect("admin_home")  
def edit(request, id):  
    # User=get_user_model()
    
    employee = User.objects.get(id=id)
    if request.method == 'POST':
        username=request.POST['username']  
        email=request.POST['email']  
        user=User(id=id,username=username,email=email)
        user.save()
        return redirect('admin_home')
    else:
        return render(request,'edit.html', {'User':employee})  

#@login_required(login_url='/')

# def update(request, id):
#     User=get_user_model()
#     employee = User.objects.get(id=id)
    
#     if request.method == 'POST':
#         form = Userform(request.POST, instance=employee)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Record Updated Successfully..')
#             return render(request, 'edit.html', {'employee': employee})
#     else:
#         form = Userform(instance=employee)
    
#     return render(request, 'edit.html', {'form': form, 'employee': employee}) 
import streamlit as st
from streamlit_chat import message
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import CTransformers
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory

#load the pdf files from the path

def AI_GGML(request):  
    query = request.GET['query']
        
    st.title("HealthCare ChatBot 🧑🏽‍⚕️")
    
    
    
    if 'history' not in st.session_state:
        st.session_state['history'] = []

    if 'generated' not in st.session_state:
        st.session_state['generated'] = ["Hello! Ask me anything about Acupuncture🤗"]

    if 'past' not in st.session_state:
        st.session_state['past'] = ["Hey! 👋"]
        
    reply_container = st.container()
    container = st.container()

    with container:
        with st.form(key='my_form', clear_on_submit=True):
            user_input = st.text_input("Question:", placeholder="Ask about Acupuncture", key='input')
            submit_button = st.form_submit_button(label='Send')

        if submit_button and user_input:
            output = conversation_chat(user_input)

            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)

    if st.session_state['generated']:
        with reply_container:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="thumbs")
                message(st.session_state["generated"][i], key=str(i), avatar_style="fun-emoji")
    return render(request, 'chatbot.html')

def conversation_chat(query):
    loader = DirectoryLoader('data/',glob="*.pdf",loader_cls=PyPDFLoader)
    documents = loader.load()

#split text into chunks
    text_splitter  = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
    text_chunks = text_splitter.split_documents(documents)

#create embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",
                                   model_kwargs={'device':"cpu"})

#vectorstore
    vector_store = FAISS.from_documents(text_chunks,embeddings)


   #create llm
    llm = CTransformers(model="llama-2-7b-chat.ggmlv3.q4_0.bin",model_type="llama",
                    config={'max_new_tokens':128,'temperature':0.01})

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    chain = ConversationalRetrievalChain.from_llm(llm=llm,chain_type='stuff',
                                              retriever=vector_store.as_retriever(search_kwargs={"k":2}),
                                              memory=memory)
    result = chain({"question": query, "chat_history": st.session_state['history']})
    st.session_state['history'].append((query, result["answer"]))
    return result["answer"]


def chatbot(request):
    return render(request, 'chatbot.html')
def initialize_session_state():
    if 'history' not in st.session_state:
        st.session_state['history'] = []

    if 'generated' not in st.session_state:
        st.session_state['generated'] = ["Hello! Ask me anything about Acupuncture🤗"]

    if 'past' not in st.session_state:
        st.session_state['past'] = ["Hey! 👋"]
