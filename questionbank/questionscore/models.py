# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from users.models import CustomUser


#Descrição das perguntas e tipo que será a pergunta
class Question(models.Model):
	user = models.ForeignKey(CustomUser)
	question_description = models.TextField('Descrição da Questão', blank=False)
	question_type = models.CharField('Tipo de Questão', 
		choices=[
			('multiple-choice', 'Multipla Escolha'),
			('discursive', 'Discursiva')
		],
		max_length=50,
		default='discursive')
	question_public = models.BooleanField(default=True)

#Caso a pergunta seja de multipla escolha as respostas serão ligadas a ela
class Answers(models.Model):
	user = models.ForeignKey(CustomUser)
	question = models.ForeignKey(Question, verbose_name='Pergunta', related_name='resposta')
	answer_description = models.TextField('Descrição da Resposta', blank=False)
	is_right = models.BooleanField(default=False)

#Caso o usuário queira montar uma prova é só ligar as perguntas nesta tabela
class Exam(models.Model):
	user = models.ForeignKey(CustomUser)
	question = models.ForeignKey(Question, verbose_name='Pergunta', related_name='prova')