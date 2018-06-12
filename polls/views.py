from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render
from django.template import loader


from polls.models import Question


def index(request):
    print("Rendered index")
    latest_question_list = Question.objects.order_by('-published_date')
    #Required for creating a teplate render request
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : latest_question_list,
    }
    return render(request, 'polls/index.html', context)
    #return HttpResponse(template.render(context,request))

def detail(request, question_id):
    print("Rendered detail")
    return HttpResponse("You are looking at question %s." % question_id)

def results(request, question_id):
    response = "You are looking at the results of the question details %s."
    print("Rendered results")
    return HttpResponse(response % question_id)

def vote(request, question_id):
    print("Rendered vote")
    if question_id >= 5 :
        template = loader.get_template('polls/404Error.html')
        return HttpResponseNotFound(template.render({},request))
    return HttpResponse("You are voting on the question : %s." % Question.objects.get(pk=question_id))

# This is the simplest view possible in Django. To call the view,
# we need to map it to a URL - and for this we need a URLconf.
# To create a URLconf in the polls directory, create a file called urls.py
#
# When somebody requests a page from your website – say, “/polls/34/”,
# Django will load the mysite.urls Python module because it’s pointed
# to by the ROOT_URLCONF setting. It finds the variable named urlpatterns
# and traverses the patterns in order. After finding the match at 'polls/',
# it strips off the matching text ("polls/") and sends the remaining
# text – "34/" – to the ‘polls.urls’ URLconf for further processing.
# There it matches '<int:question_id>/', resulting in a call to the detail() view like so:
