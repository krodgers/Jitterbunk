from django.conf.urls import url
from . import views


urlpatterns = [
    # login
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    # log out
    url(r'^logout/$', views.logout_view, name="logout"),
    #/bunker/ (main feed view)
    url(r'^$', views.IndexView.as_view(), name='index'),
    #/bunker/id/user_feed
    url(r'^(?P<pk>[0-9]+)/$',views.UserFeedView.as_view(), name="user_feed"),
    #/bunker/id/add_bunk
    url(r'^(?P<user_id>[0-9]+)/add_bunk/$', views.add_bunk, name="add_bunk"),
    #/bunker/bunked
    url(r'^bunked', views.bunked, name="bunked"),
]

