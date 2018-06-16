from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views import generic

from polls.models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.order_by('-published_date')[:5]

#def index(request):
#   print("Rendered index")
#    latest_question_list = Question.objects.order_by('-published_date')
# Required for creating a teplate render request
#    template = loader.get_template('polls/index.html')
#    context = {
#        'latest_question_list': latest_question_list,
#    }
#    return render(request, 'polls/index.html', context)
# return HttpResponse(template.render(context,request))

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


#def detail(request, question_id):
#    print("Rendered detail")
    #The below line is same as
#    question = get_object_or_404(Question, pk=question_id)
    #question = Question.objects.get(pk=question_id)
#    context = {'question': question}
#    return render(request, 'polls/detail.html',context )
# Another way to raise 404 errors
#    question_text = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/detail.html', {'QUESTION_TEXT': question_text})
#OR
# return HttpResponse("You are looking at question %s." % question_id)

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    print("Rendered results")
#    #return HttpResponse(response % question_id)
#    return render(request, 'polls/results_view', {'question': question})


def vote(request, question_id):
    print("Rendered vote")
    question = get_object_or_404(Question, pk=question_id)
    try:
        print("In try block")
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the question voting form
        context = {'question': question,'error_message': "You did not select a choice" , }
        return render(request, 'polls/detail.html', context)

    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:result_view', args=(question.id,)))

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

# The render() function takes the request object as its ﬁrst argument,
# a template name as its second argument and a dictionary as its optional third argument.
# It returns an HttpResponse object of the given template rendered with the given context.
