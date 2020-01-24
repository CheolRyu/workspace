import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

  def __str__(self):
    return self.question_text
    
  def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice = models.IntegerField(default=0)

  def __str__(self):
     return str(self.choice)


class Insulin(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  high_insulin = models.ForeignKey(Choice, on_delete=models.CASCADE)
  def __str__(self):
    return '{}, answer: {}'.format(self.question, str(self.high_insulin))

class Thyroid(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  thyroid = models.ForeignKey(Choice, on_delete=models.CASCADE)
  def __str__(self):
    return '{}, {}'.format(self.question, str(self.thyroid))

class High_Cortisal(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  high_cortisal = models.ForeignKey(Choice, on_delete=models.CASCADE)
  def __str__(self):
    return '{}, {}'.format(self.question, str(self.high_cortisal))

class Low_Cortisal(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  low_cortisal = models.ForeignKey(Choice, on_delete=models.CASCADE)
  def __str__(self):
    return '{}, {}'.format(self.question, str(self.low_cortisal))

class High_Androgen(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  high_androgen = models.ForeignKey(Choice, on_delete=models.CASCADE)
  def __str__(self):
    return '{},{}'.format(self.question, str(self.high_androgen))

class Low_Androgen(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  low_androgen = models.ForeignKey(Choice, on_delete=models.CASCADE)
  def __str__(self):
    return '{},{}'.format(self.question, str(self.low_androgen))

class Estrogen_Progenence(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  progenence = models.ForeignKey(Choice, on_delete=models.CASCADE)
  def __str__(self):
    return '{},{}'.format(self.question, str(self.progenence))

class Estrogen_Dominence(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  dominence = models.ForeignKey(Choice, on_delete=models.CASCADE)
  def __str__(self):
    return '{},{}'.format(self.question, str(self.dominence))





















