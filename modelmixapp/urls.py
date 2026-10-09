from django.urls import path
from modelmixapp import views


urlpatterns =[
    path('',views.AllStatusAddView.as_view()),
    path('<int:pk>',views.StatusRetriveUpdateDeleteView.as_view()),
]