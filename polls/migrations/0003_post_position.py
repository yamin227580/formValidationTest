# Generated by Django 2.0 on 2020-10-29 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='position',
            field=models.CharField(choices=[('Developer', 'Developer'), ('Engineer', 'Engineer'), ('PHPDeveloper', 'PHPDeveloper')], default='Developer', max_length=20),
        ),
    ]
