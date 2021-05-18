from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def process(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['favLang'] = request.POST['favLang']
    request.session['travel'] = request.POST['travel']
    request.session['music'] = request.POST['music']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')

def result(request):
    context = {
        "name": request.session['name'],
        "location": request.session['location'],
        "favLang": request.session['favLang'],
        "travel": request.session['travel'],
        "music": request.session['music'],
        "comment": request.session['comment'],
    }
    return render(request, 'result.html', context)

def catch_all(request, url):        #The catch all view, "url" must be passed in
    return HttpResponse("There is no page here. You have made an error.")