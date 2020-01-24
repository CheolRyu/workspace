from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from django.utils import timezone
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):

	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

	def get_queryset(self):
		"""
		Excludes any questions that aren't published yet.
		"""
		return Question.objects.filter(pub_date__lte=timezone.now())

def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
  # Redisplay the question voting form.
    return render(request, 'polls/detail.html', {
      'question': question,
			'error_message': "You didn't select a choice.",
		})
  if question_id == 1:
    print(selected_choice, "is the choice")
    high_insulin = Insulin.objects.create(question=question, high_insulin=selected_choice)
    high_insulin.save()
    thyroid = Thyroid(question=question, thyroid=selected_choice)
    thyroid.save()
    high_androgen = High_Androgen(question=question, high_androgen=selected_choice)
    high_androgen.save()
  if question_id == 2:
    print(selected_choice, "is the choice")
    high_insulin = Insulin.objects.create(question=question, high_insulin=selected_choice)
    high_insulin.save()
    thyroid = Thyroid(question=question, thyroid=selected_choice)
    thyroid.save()
    high_androgen = High_Androgen(question=question, high_androgen=selected_choice)
    high_androgen.save()
  if question_id == 3:
    print(selected_choice, "is the choice")
    high_insulin = Insulin.objects.create(question=question, high_insulin=selected_choice)
    high_insulin.save()
    thyroid = Thyroid(question=question, thyroid=selected_choice)
    thyroid.save()
    high_androgen = High_Androgen(question=question, high_androgen=selected_choice)
    high_androgen.save()
  if question_id == 4:
    print(selected_choice, "is the choice")
    high_insulin = Insulin.objects.create(question=question, high_insulin=selected_choice)
    high_insulin.save()
    thyroid = Thyroid(question=question, thyroid=selected_choice)
    thyroid.save()
    high_androgen = High_Androgen(question=question, high_androgen=selected_choice)
    high_androgen.save()
  if question_id == 5:
    print(selected_choice, "is the choice")
    high_insulin = Insulin.objects.create(question=question, high_insulin=selected_choice)
    high_insulin.save()
    thyroid = Thyroid(question=question, thyroid=selected_choice)
    thyroid.save()
    high_androgen = High_Androgen(question=question, high_androgen=selected_choice)
    high_androgen.save()
    return render(request, 'polls/index.html')
  else:
    return redirect(reverse('polls:detail', args=(question.id + 1,)))


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
