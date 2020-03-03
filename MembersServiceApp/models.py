# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class MembersModel(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    phone_number = models.IntegerField(null=False)
    client_member_id = models.IntegerField(null=False)
    account_id = models.IntegerField(null=False)

    class Meta:
        db_table = 'membersData'
        unique_together = ('phone_number', 'client_member_id')

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.id)
