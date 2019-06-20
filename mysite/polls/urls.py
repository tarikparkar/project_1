from django.urls import path
from . import views
urlpatterns = [
        #path for polls
    path('',views.index,name='index'),
        # path for /polls/5/
    path('<int:question_id>/',views.detail,name ='detail'),
        # path for /polls/5/results
    path('<int:question_id>/results/',views.results,name ='results'),
        # path for /polls/5/vote
    path('<int:question_id>/vote/',views.vote,name ='vote'),
]
