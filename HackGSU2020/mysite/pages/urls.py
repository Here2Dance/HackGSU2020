# pages/urls.py
from django.urls import path
from .views import HomePageView, FirstStepsInStemView, FurtherResourcesView, ForumsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('firststepsinstem/', FirstStepsInStemView.as_view(), name='firststepsinstem'),
    path('furtherresources/', FurtherResourcesView.as_view(), name='furtherresources'),
    path('forums/', ForumsView.as_view(), name='forums')
]