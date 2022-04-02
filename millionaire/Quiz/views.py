from django.shortcuts import redirect, render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.http import HttpResponse
from django.core.paginator import Paginator
    

# Create your views here.
def home(request):
    question_list = QuesModel.objects.all()
    paginator = Paginator(question_list, 1) # Show one question per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Get current question and evaluate user input for correct answer
    
    if request.method == 'POST':
        score = 0
        page_question = paginator.page(1).object_list
        print(page_question)
        for q in page_question:
            # print(q.ans)
            # print(q.point_value)
            # print(request.POST.get(q.question))
            # print(q)
            if q.ans == request.POST.get(q.question):
                score=q.point_value
        
            return render(request, 'Quiz/home.html', {'page_obj': page_obj})
    else:
        return render(request, 'Quiz/home.html', {'page_obj': page_obj})
    # if request.method == 'POST':
    #     print(request.POST)
    #     questions=QuesModel.objects.all()
    #     print(type(questions))
    #     score=0
    #     wrong=0
    #     correct=0
    #     total=0
    #     for q in questions:
    #          total+=1
    #          if q.ans == request.POST.get(q.question):
    #              score=q.point_value
    #              correct+=1
    #          else:
    #              wrong+=1
    #     context = {
    #         'score':score,
    #         'correct':correct,
    #         'wrong':wrong,
    #         'total':total
    #     }
    #     return render(request,'Quiz/result.html',context)
    # else:
    #     questions = QuesModel.objects.all()
    #     context = {
    #         'question': questions
    #     }
    #     return render(request, 'Quiz/home.html', context)
 
def addQuestion(request):    
    if request.user.is_staff:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'Quiz/addQuestion.html',context)
    else: 
        return redirect('home') 
 
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form = createuserform()
        if request.method=='POST':
            form = createuserform(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('login')
        context={
            'form':form,
        }
        return render(request,'Quiz/register.html',context)
 
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'Quiz/login.html',context)
 
def logoutPage(request):
    logout(request)
    return redirect('/')