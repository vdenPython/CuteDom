from django.db import models


class Account(models.Model):
    cd_account_short_title = models.CharField('short title',max_length=50)
    cd_account_title = models.CharField('title', max_length=125)


