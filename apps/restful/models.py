# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}

		if len(postData['first_name']) < 2:
			errors['first_name'] = "First name has to be more than 2 characters"
		if len(postData['last_name']) < 2:
			errors['first_name'] = "Last name has to be more than 2 characters"
		if len(postData['email']) < 4:
			error['email'] = "Email must be more than 4 characters"

		return errors

class Users(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	#allows the user class to inherit the UserManager class and the function for validation within it. 
	objects = UserManager()

