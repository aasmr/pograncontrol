# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Case(models.Model):
    msg_id = models.IntegerField()
    case_mes_id = models.IntegerField(blank=True, null=True)
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


class CaseText(models.Model):
    msg_id = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    tag = models.CharField(max_length=45, blank=True, null=True)
    author = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'case_text'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MessagesInfo(models.Model):
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


class PogranVisualisationPograncontrol(models.Model):
    age = models.CharField(max_length=3)
    cause = models.CharField(max_length=100)
    vus = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    kpp = models.CharField(max_length=50)
    yservice = models.CharField(db_column='yService', max_length=15)  # Field name made lowercase.
    voenk = models.CharField(max_length=50)
    kategory = models.CharField(max_length=3)
    katz = models.CharField(db_column='katZ', max_length=1)  # Field name made lowercase.
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'pogran_visualisation_pograncontrol'
