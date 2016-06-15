from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'), #/bunker/ (main feed view)
    url(r'^(?P<pk>[0-9]+)/$',views.UserFeedView.as_view(), name="user_feed"),#/bunker/id/user_feed
]

