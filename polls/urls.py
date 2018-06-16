from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index_page'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail_view'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='result_view'),
    path('<int:question_id>/vote/', views.vote, name='vote_view'),
]