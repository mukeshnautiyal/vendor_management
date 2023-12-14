# Generated by Django 4.2.8 on 2023-12-09 11:25

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters', max_length=75, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$'), 'Enter a valid username.', 'invalid')], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]{1,50}')], verbose_name='first_name')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]{1,50}')], verbose_name='last_name')),
                ('name', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]{1,50}')], verbose_name='name')),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('is_staff', models.BooleanField(default=0)),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('contact_details', models.CharField(blank=True, max_length=12, null=True, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]{10}$')])),
                ('phone_verified', models.BooleanField(default=True)),
                ('email_verified', models.BooleanField(default=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('vendor_code', models.CharField(default=None, max_length=10, null=True, unique=True)),
                ('on_time_delivery_rate', models.FloatField(default=None, null=True)),
                ('quality_rating_avg', models.FloatField(default=None, null=True)),
                ('average_response_time', models.FloatField(default=None, null=True)),
                ('fulfillment_rate', models.FloatField(default=None, null=True)),
                ('otp', models.IntegerField(null=True, validators=[django.core.validators.RegexValidator('^[0-9]{4}$')])),
                ('onetime_token', models.CharField(blank=True, default=None, max_length=254, null=True, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'db_table': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='delete')),
            ],
            options={
                'db_table': 'roles',
            },
        ),
        migrations.CreateModel(
            name='Order_Purchase',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('po_number', models.CharField(blank=True, max_length=20, unique=True)),
                ('order_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('delivery_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('items', models.JSONField(default=None, null=True)),
                ('qauntity', models.IntegerField(default=None, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], default='1', max_length=30)),
                ('quality_rating', models.FloatField(default=None, null=True)),
                ('acknowledgment_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('issue_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='vendor_id', related_query_name='vendor_user_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'order_purchase',
            },
        ),
        migrations.CreateModel(
            name='Historical_Performance',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('ontime_delivery_date', models.DateTimeField(auto_now=True, null=True)),
                ('quality_rating_avg', models.FloatField(default=None, null=True)),
                ('average_response_time', models.FloatField(default=None, null=True)),
                ('fulfillment_rate', models.FloatField(default=None, null=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='history_vendor_id', related_query_name='history_vendor_user_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'historical_performance',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, related_name='role_id', related_query_name='user_role', to='vendor.roles'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]