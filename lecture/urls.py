from django.conf.urls import url
from lecture import views
from django.urls import path

app_name = 'lecture'

urlpatterns = [
    path('', views.index, name='index'),
    path('classroom/', views.classroom, name='classroom'),
    path('video/', views.video, name='video'),
    path('desktop/', views.desktop, name='desktop'),
    path('collaboration/', views.collaboration, name='collaboration'),
    path('evaluation/', views.evaluation, name='evaluation'),
    path('answer/', views.answer, name='answer'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('create_coursepack/', views.create_coursepack, name='create_coursepack'),

    path('<int:course_id>', views.detail, name='detail'),
    path('<int:course_id>/favorite', views.favorite, name='favorite'),
    path('<int:course_id>podcasts/(^P<filter_by>[a-zA_Z]$)', views.podcasts, name='podcasts'),
    path('<int:course_id>/create_podcast', views.create_podcast, name='create_podcast'),
    path('<int:course_id>/delete_podcast/(^P<podcast_id>[0-9]$)', views.delete_podcast, name='delete_podcast'),
    path('<int:course_id>/favorite_course', views.favorite_course, name='favorite_course'),
    path('<int:course_id>/delete_course', views.delete_course, name='delete_course'),

]