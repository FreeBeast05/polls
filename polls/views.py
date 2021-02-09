from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Question, Choice, Polls_table
from django.urls import reverse
from django.views import generic


class Polls_output(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_polls_list'

    def get_queryset(self):
        return Polls_table.objects.order_by('-pub_date')

def detail(request, polls_id):
    latest_question_list = Question.objects.filter(poll=polls_id)[:]
    context = {'latest_question_list': latest_question_list,
               'polls_id': polls_id}
    return render(request, 'polls/detail.html', context)


def answer(request, polls_id, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question,
               'polls_id': polls_id,
               'question_id': question_id}
    return render(request, 'polls/answer_question.html', context)


def results(request, polls_id, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question,
                                                  'polls_id': polls_id,
                                                  'question_id': question_id})


def vote(request, polls_id, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(polls_id, question.id,)))
