from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
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
    score = 0
    correct = 0
    message = ""
    
    if request.method == 'POST':
        if page_number == None or page_number == 1:
            page_number = 1
            score = 0
        else:
            page_number = request.GET.get('page')
            previous_page = paginator.get_page(page_number).previous_page_number()
            previous_page_obj = paginator.get_page(previous_page)
            for q in previous_page_obj:
                score = q.point_value
            
        page_question = paginator.page(page_number).object_list
        for q in page_question:
            print(q.ans)
            print(request.POST.get(q.question))
            if q.ans == request.POST.get(q.question):
                correct += 1
                message = "Correct! Please click next."
                score=q.point_value
                if score == 1000000:
                    context = {
                        'score': score,
                        'correct': correct
                    }
                    return render(request, 'Quiz/result.html', context)
            else:
                score = score
                save_score = Scores(score=score)
                save_score.save()
                scores = Scores.objects.filter(score__gt=0)
                score_list = []
                for s in scores:
                    score_list.append(s.score)
                score_list.sort(reverse=True)
                print(score_list)
                context = {
                    'score': score,
                    'correct': correct,
                    'score_list': score_list
                }
                return render(request, 'Quiz/result.html', context)
            print(score)
            context = {
                'page_obj': page_obj,
                'message': message,
                'score': score
            }
            return render(request, 'Quiz/home.html', context)
    else:
        return render(request, 'Quiz/home.html', {'page_obj': page_obj})


def addQuestion(request):
    if request.user.is_staff:
        form = addQuestionform()
        if request.method == "POST":
            form = addQuestionform(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/")
        context = {"form": form}
        return render(request, "Quiz/addQuestion.html", context)
    else:
        return redirect("home")


def registerPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        form = createuserform()
        if request.method == "POST":
            form = createuserform(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect("login")
        context = {
            "form": form,
        }
        return render(request, "Quiz/register.html", context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
        context = {}
        return render(request, "Quiz/login.html", context)


def logoutPage(request):
    logout(request)
    return redirect("/")


# phone a friend function
def phone_friend(request):
    print("hint")
    return HttpResponse("""<html><script>console.log("Hi!")</script></html>""")


# 50/50 function
def fifty_fifty_lifeline(request):
    print("50_50")
