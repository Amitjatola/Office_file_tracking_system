# Generated by Django 3.2.9 on 2021-11-23 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201002_0237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('slug', models.SlugField(editable=False, max_length=30, unique=True)),
                ('abbreviation', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_student',
            field=models.BooleanField(default=True, verbose_name='Student'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('Teacher', 'Teacher'), ('Faculty Advisor', 'Faculty Advisor'), ('Dean', 'Dean'), ('Head of department', 'Head of department'), ('Admin', 'Admin')], default='S', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='Active'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.department', verbose_name='Department'),
        ),
    ]
