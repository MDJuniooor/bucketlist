from django.conf.urls import url

from . import views

app_name = 'users'

urlpatterns = [
    url(
        regex=r'^(?P<username>\w+)/delete/$',
        view=views.DeleteUser.as_view(),
        name='delete_user'
    ),
    url(
        regex=r'^(?P<username>\w+)/donate/$',
        view=views.DonateUser.as_view(),
        name='donate_user'
    )
        ,
    url(    
        regex=r'^explore/$',
        view=views.ExploreUsers.as_view(),
        name='explore_users'
    ),
    url(
        regex=r'^signup/$',
        view=views.SignUpUser.as_view(),
        name='signup_user'
    ),
    url(
    regex=r'^login/facebook/$',
    view=views.FacebookLogin.as_view(),
    name='fb_login'
    ),
]
