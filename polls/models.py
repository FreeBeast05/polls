from django.db import models

class Polls_table(models.Model):
    poll_name = models.CharField(max_length=200)
    pub_date=models.DateTimeField(null=True)
    end_date=models.DateTimeField(null=True)
    poll_description = models.CharField(max_length=200)
    def __str__(self):
        return self.poll_name

class Question(models.Model):
    poll = models.ForeignKey(Polls_table,related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    question_type= models.CharField(max_length=200)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text