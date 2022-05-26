# Generated by Django 4.0.4 on 2022-05-21 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_cadeiras'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadeira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('realizacao', models.CharField(max_length=9)),
                ('topicos', models.CharField(max_length=500)),
                ('pofessor', models.CharField(max_length=25)),
                ('ects', models.IntegerField()),
                ('classicicacao', models.IntegerField()),
                ('ano', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Cadeiras',
        ),
    ]