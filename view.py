from django.http import HttpResponse
from django.shortcuts import render
global t
def index(request):
    s='l'

    return render(request ,'index.html',{'s':''})
def charcount(request):
    global t
    t = request.POST['num1']
    t1 = request.POST['num2']
    t2=request.POST['num3']
    if t2!=t1:
        return render(request, 'index.html', {'s': 'Incorrect Password'})
    else:
        return render(request, 'rules.html', {'s': t})
def quiz(request):
    global t
    return render(request, 'quiz.html', {'s': t})
    pass
def check(request):
    global t
    m=0
    if request.POST['question-1-answers']=='B':
        m+=1
    if request.POST['question-2-answers'] == 'B':
        m += 1
    if request.POST['question-3-answers'] == 'D':
        m += 1
    if request.POST['question-4-answers'] == 'B':
        m += 1
    if request.POST['question-5-answers'] == 'D':
        m += 1
    if m in [0,1,2]:
        return render(request, 'result.html', {'s': t, 're': m,'q':'Poor'})
    elif m in [4,3]:
        return render(request, 'result.html', {'s': t, 're': m, 'q': 'Average'})
    else:
        return render(request, 'result.html', {'s': t, 're': m, 'q': 'Very Good'})
    pass


