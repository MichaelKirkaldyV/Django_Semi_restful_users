# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from models import *

def users(request):
	context = {
		"users": Users.objects.all()
	}
	return render(request, 'restful/users.html', context)

def new(request):
	return render(request, 'restful/new.html')

def create(request):
	first_name = request.POST['first_name']
	last_name = request.POST['last_name']
	email = request.POST['email']

	errors = Users.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
			return redirect('/users/new')
	else:
		Users.objects.create(first_name=first_name, last_name=last_name, email=email)
		return redirect('/users')


def show(request, id):
	return render(request, 'restful/show.html', {"users": Users.objects.get(id=id)})

def update(request):
	#grabs the id from the update form and uses the following queries to update and save the info.
	a = Users.objects.get(id=request.POST['id'])
	a.first_name = request.POST['first_name']
	a.last_name = request.POST['last_name']
	a.email = request.POST['email']
	a.save()

	return redirect('/users')

def edit(request, id):
	return render(request, 'restful/edit.html', {"users": Users.objects.get(id=id)})

def destroy(request, id):
	a = Users.objects.get(id=id)
	a.delete()
	return redirect('/users')
