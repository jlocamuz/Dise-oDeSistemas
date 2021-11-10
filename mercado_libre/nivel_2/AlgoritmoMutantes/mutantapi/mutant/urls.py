from .views import MutantView
from django.urls import path


urlpatterns = [
    path('', MutantView.as_view()),

]