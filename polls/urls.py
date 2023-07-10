from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.QuestionViewList.as_view(), name='polls_list'),
    path('<int:pk>/', views.QuestionDetailView.as_view(), name='polls_detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='polls_results'),
    path('<int:question_id>/vote/', views.vote, name='polls_vote'),
]
