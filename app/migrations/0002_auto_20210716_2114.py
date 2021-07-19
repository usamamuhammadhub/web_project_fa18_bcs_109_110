# Generated by Django 3.2 on 2021-07-16 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_us',
            name='status',
            field=models.CharField(choices=[('read', 'read'), ('later', 'later')], default='unread', max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='message',
            field=models.TextField(default='none', null=True),
        ),
    ]