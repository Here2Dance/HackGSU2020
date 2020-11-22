from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class ForumsView(TemplateView):
	template_name = 'forums.html'


class FirstStepsInStemView(TemplateView):
	template_name = 'first_steps_in_stem.html'


class FurtherResourcesView(TemplateView):
	template_name = 'further_resources.html'
