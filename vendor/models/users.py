from xmlrpc.client import Boolean
from django.db import models
from django.contrib.auth.models import PermissionsMixin,UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext as _
from django.core.validators import RegexValidator
from django.core import validators
import re


class Roles(models.Model):
    class Meta:
        db_table = 'roles'
    id         = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=50, null=True, blank=True)
    is_active  = models.BooleanField(('active'), default=True )
    is_deleted = models.BooleanField(('delete'), default=False)

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):

    class Meta:
       db_table  = "users"
    id         =     models.AutoField(primary_key=True)
    username        = models.CharField(_('username'), max_length=75, unique=True, help_text=_('Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters'), validators = [ validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'), 'invalid') ])
    first_name      = models.CharField(('first_name'),validators=[RegexValidator("^[a-zA-Z]{1,50}")], max_length=50, null=True,blank=True)
    last_name       = models.CharField(('last_name'),validators=[RegexValidator("^[a-zA-Z]{1,50}")], max_length=50,null=True,blank=True)
    name      = models.CharField(('name'),validators=[RegexValidator("^[a-zA-Z]{1,50}")], max_length=100, null=True,blank=True)
    email           = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    is_staff        = models.BooleanField(default=0)
    is_active       = models.BooleanField(('active'), default=True, help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    contact_details               = models.TextField(null=True,blank=True)
    phone_verified = models.BooleanField( default=True)
    email_verified =  models.BooleanField(default=True)
    address = models.TextField(null=True,blank=True)
    vendor_code = models.CharField(null=True, unique=True, max_length=10, default=None)
    on_time_delivery_rate = models.FloatField(null=True,default=None)
    quality_rating_avg = models.FloatField(null=True,default=None)
    average_response_time = models.FloatField(null=True, default=None)
    fulfillment_rate = models.FloatField(null=True, default=None)
    role = models.ForeignKey(Roles, on_delete=models.DO_NOTHING,default= 2, related_name='role_id',related_query_name="user_role")
    otp   = models.IntegerField(validators=[RegexValidator( '^[0-9]{4}$')],null=True,blank=False)
    onetime_token = models.CharField(blank=True, null=True, unique=True, max_length=254, default=None)
    created_on      = models.DateTimeField(auto_now_add=True, null=True,)
    updated_on      = models.DateTimeField(auto_now=True, null=True,)

    objects         = UserManager()
    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.first_name+" "+self.last_name

    def get_short_name(self):
        return self.first_name
    def __unicode__(self):
        return self.email