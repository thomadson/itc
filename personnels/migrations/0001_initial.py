# Generated by Django 3.1.3 on 2020-11-24 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personnels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identite', models.CharField(max_length=200)),
                ('poste', models.CharField(max_length=200)),
                ('adresse_mail', models.CharField(max_length=200)),
                ('photo_url', models.CharField(max_length=5000)),
            ],
        ),
    ]
