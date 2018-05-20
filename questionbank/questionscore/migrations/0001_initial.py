# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-20 14:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_description', models.TextField(verbose_name='Descri\xe7\xe3o da Resposta')),
                ('is_right', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_description', models.TextField(verbose_name='Descri\xe7\xe3o da Quest\xe3o')),
                ('question_type', models.CharField(choices=[('multiple-choice', 'Multipla Escolha'), ('discursive', 'Discursiva')], default='discursive', max_length=50, verbose_name='Tipo de Quest\xe3o')),
                ('question_public', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prova', to='questionscore.Question', verbose_name='Pergunta'),
        ),
        migrations.AddField(
            model_name='exam',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resposta', to='questionscore.Question', verbose_name='Pergunta'),
        ),
        migrations.AddField(
            model_name='answers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
