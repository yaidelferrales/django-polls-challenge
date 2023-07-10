from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (ListView, DetailView)
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators  import login_required


from .models import Question, Choice

class QuestionViewList(LoginRequiredMixin, ListView):
    model = Question
    template_name = 'polls/index.html'
    queryset = Question.objects.all()
    context_object_name = 'latest_question_list'
    paginate_by=5
    
class QuestionDetailView(LoginRequiredMixin, DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(LoginRequiredMixin, DetailView):
    model = Question
    template_name = 'polls/results.html'

@login_required
def vote(request: HttpRequest, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_list = request.POST.getlist('choice') 
        if selected_list:    
            choice_obj = []
            for selected in selected_list:
                obj_result = question.choice_set.get(pk=selected)
                if obj_result:
                    choice_obj.append(obj_result)
        else:
            raise KeyError     
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        for selected in choice_obj:
            selected.votes += 1
            selected.save()
        return HttpResponseRedirect(reverse('polls:polls_results', args=(question.id,)))
