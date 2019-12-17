from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from cost.forms import ShareForm
from django.views.generic import TemplateView


def Home(request):
	form=ShareForm(request.POST or None)
	no_of_shares=0
	if form.is_valid():
		obj=form.save(commit=False)
		obj.save()
		form=ShareForm()
	
	
		price=int(request.POST.get('price'))
		capital=int(request.POST.get('capital'))
		leverage=int(request.POST.get('leverage'))
		margin_amount=leverage*capital
		no_of_shares=margin_amount/price

	template_name='home.html'
	context={'form':form,'no_of_shares':no_of_shares}


	return render(request,template_name,context)