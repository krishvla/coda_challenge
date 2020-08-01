from django.db import models
# Create your models here.

class admincode(models.Model):
    code = models.TextField(null=False)

    def __str__(self):
        params = {
            'code': self.code
        }
        return '{code}'.format(**params)

class hackers(models.Model):
    level_choice = (
        (1,'1 - Low'),
        (2,'2 - Normal'),
        (3,'3 - Meium'),
        (4,'4 - High'),
        (5,'5 - Expert'),
    )
    name = models.CharField(max_length=30, null=False)
    challenges = models.IntegerField(null=True)
    expert_python = models.IntegerField(choices=level_choice,null=True)
    expert_dsa = models.IntegerField(choices=level_choice,null=True)
    expert_c = models.IntegerField(choices=level_choice,null=True)
    expert_django = models.IntegerField(choices=level_choice,null=True)

    def __str__(self):
        params = {
            'pk':self.pk,
            'name':self.name
        }
        return '{pk} - {name}'.format(**params)

class votes(models.Model):
    candidate = models.ForeignKey(hackers,on_delete=models.CASCADE)
    ip_addr = models.GenericIPAddressField() 
    voted = models.BooleanField(default=False, blank=True, null=True)
    def __str__(self):
        params = {
            'pk':self.pk,
            'name':self.candidate
        }
        return '{pk} - {name}'.format(**params)