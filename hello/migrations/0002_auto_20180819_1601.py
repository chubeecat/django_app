# Generated by Django 2.0.5 on 2018-08-19 07:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import hello.models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=300)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('pub_date',),
            },
        ),
        migrations.AlterField(
            model_name='friend',
            name='age',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(150)]),
        ),
        migrations.AlterField(
            model_name='friend',
            name='name',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(1), hello.models.number_only]),
        ),
        migrations.AddField(
            model_name='message',
            name='friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.Friend'),
        ),
    ]
