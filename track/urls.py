from django.urls.conf import path
from track import views

app_name = 'track'
urlpatterns = [
     path('', views.start, name='start'),
     path('save/', views.save, name='save'),
#    path('', views.IndexView.as_view(), name='index'),
#    path('specs/<int:pk>/', views.DetailView.as_view(), name='detail'),
#    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#    path('<int:question_id>/vote/', views.vote, name='vote'),   
]