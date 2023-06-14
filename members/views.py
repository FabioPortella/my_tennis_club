from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Member
from plans.models import Plan


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def add(request):
    myplans = Plan.objects.all().values()
    template = loader.get_template('add.html')
    context = {
        'myplans': myplans,
    }
    return HttpResponse(template.render(context, request))

def addrecord(request):
    first = request.POST['first']
    last = request.POST['last']
    phone = request.POST['phone']
    joined_date = datetime.now()
    plano = Plan.objects.filter(id=request.POST['plan']).first()

    member = Member(
        firstname=first, 
        lastname=last, 
        phone=phone, 
        joined_date=joined_date, 
        plan=plano)
    member.save()
    return HttpResponseRedirect(reverse('members'))

def update(request, id):
    member = Member.objects.get(id=id)
    plans = Plan.objects.all().values()
    template = loader.get_template('update.html')
    context = {
        'member': member,
        'plans': plans,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    phone = request.POST['phone']
    plan = request.POST['plan']

    member = Member.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.phone = phone
    member.plan = Plan.objects.get(id=plan)
    member.save()
    return HttpResponseRedirect(reverse('members'))

def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('members'))
