# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Case(models.Model):
    id = models.IntegerField(primary_key=True)
    msg_id = models.IntegerField()
    case_type = models.CharField(max_length=45, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=45, blank=True, null=True)
    cause = models.TextField(blank=True, null=True)
    army_relations = models.TextField(blank=True, null=True)
    vus = models.TextField(blank=True, null=True)
    army_type = models.TextField(blank=True, null=True)
    army_sec_type = models.TextField(blank=True, null=True)
    army_other = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=45, blank=True, null=True)
    kpp = models.CharField(max_length=45, blank=True, null=True)
    yservice = models.CharField(db_column='yService', max_length=10, blank=True, null=True)  # Field name made lowercase.
    voenk_region = models.CharField(max_length=100, blank=True, null=True)
    voenk_city = models.CharField(max_length=100, blank=True, null=True)
    voenk_district = models.CharField(max_length=100, blank=True, null=True)
    kategory_h = models.CharField(max_length=45, blank=True, null=True)
    kategory_z = models.CharField(max_length=45, blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'case'


class MessagesInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    msg_id = models.IntegerField()
    tag = models.CharField(max_length=45, blank=True, null=True)
    author = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messages_info'


class MessagesTable(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.TextField(blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messages_table'
