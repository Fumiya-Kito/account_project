from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENDER_CHOICES = [
    ('1','男性'),
    ('2','女性'),
    ('3','その他'),
]
DUTIES_CHOICES = [
    ('1','リーダー'),
    ('2','ベテラン'),
    ('3','新人'),
]

class Account(models.Model):
    """ アカウント情報 """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(verbose_name='名前', max_length=50)
    gender = models.CharField(verbose_name='性別', max_length=1, choices=GENDER_CHOICES, default='1')
    duties =  models.CharField(verbose_name='役職', max_length=1, choices=DUTIES_CHOICES, default='3')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('account_detail', kwargs={'pk': self.pk})
