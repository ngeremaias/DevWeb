from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=200,verbose_name='Texto da Questão')
    pub_date=models.DateTimeField('Data de Publicação')
    def __str__(self):
        return self.question_text
    def foi_publicado_recentemente(self):
        return self.pub_date>=timezone.now()-datetime.timedelta(days=1)
class Choise(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choise_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.choise_text