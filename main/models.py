from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=200)
    categories = (('HUMANITIES','HUMANITIES'),('EDUCATION','EDUCATION'),('ENVIRONMENT','ENVIRONMENT'),('HEALTH','HEALTH'),('CHARITY','CHARITY'),('RELIGION','RELIGION'),('SERVICES','SERVICES'),('OTHER','OTHER'))
    category = models.CharField(choices=categories,max_length=100)
    description=models.TextField()
