from django.conf.urls import patterns, url
from AppRating import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^ranklist/',views.rankList,name='ranklist'),
                       url(r'^all-apps/',views.allapps,name='allApps'),
                       url(r'^about/',views.about,name='about'),
                       url(r'^login/$',views.user_login,name='login'),
                       url(r'^logout/$',views.user_logout,name='logout'),
                       url(r'^app/(?P<appid>[\w\-]+)/$',views.app,name='app'),
                       url(r'^search/',views.search,name='search'),
                       url(r'^addcomment/$',views.addComment,name='addcomment'),
                       url(r'^like/$',views.like,name='like'),
                       url(r'^dislike/$',views.dislike,name='dislike'),
                       url(r'^history/(?P<username>[\w\-]+)/$',views.history,name='history'),

                       )
