# Generated by Django 4.2.1 on 2023-05-25 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearnapp', '0002_alter_studentprofile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='message_app',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=255, null=True)),
                ('reciever', models.CharField(max_length=255, null=True)),
                ('message_content', models.TextField(max_length=255, null=True)),
            ],
        ),
    ]
