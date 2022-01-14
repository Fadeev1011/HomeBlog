# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Main(models.Model):
    id = models.IntegerField(db_index=True, primary_key=True)
    name = models.CharField(max_length=1, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'main'


class SecondTable(models.Model):
    id = models.IntegerField(db_index=True, primary_key=True)
    main = models.ForeignKey(Main, models.DO_NOTHING, db_column='main')
    name = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'second_table'
