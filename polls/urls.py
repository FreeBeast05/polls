from  django.urls import path

from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.Polls_output.as_view(), name='index'),
    path('<int:polls_id>/', views.detail, name='detail'),
    path('<int:polls_id>/<int:question_id>/results/', views.results, name='results'),
    path('<int:polls_id>/<int:question_id>', views.answer, name='answer'),
    path('<int:polls_id>/<int:question_id>/vote/', views.vote, name='vote'),
]