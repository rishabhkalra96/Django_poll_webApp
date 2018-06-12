from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index_page'),
    path('<int:question_id>/', views.detail, name='detail_view'),
    path('<int:question_id>/results/', views.results, name='result_view'),
    path('<int:question_id>/vote/', views.vote, name='vote_view'),
]