from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^api/v1/forged/(?P<pk>[0-9]+)$',
        views.get_delete_update_forged,
        name='get_delete_update_forged'
    ),

    url(
        r'^api/v1/forged/$',
        views.get_post_forged,
        name='get_post_forged'
    )
]