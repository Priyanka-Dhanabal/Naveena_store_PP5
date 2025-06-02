from django.db import models

# Create your models here.


class Faq(models.Model):

    question = models.CharField(max_length=254)
    answer = models.TextField(max_length=2000, blank=False)

    def __str__(self):
        return self.question