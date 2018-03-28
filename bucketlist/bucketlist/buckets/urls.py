from django.conf.urls import url
from . import views
app_name = "buckets"
urlpatterns = [
    url(
        regex=r'^$',
        view=views.ListAllBucket.as_view(),
        name='all_buckets'
    ),
    url(
        regex=r'^(?P<bucket_id>[0-9]+)/$',
        view=views.BucketDetail.as_view(),
        name='bucket_detail'
    ),
    url(
        regex=r'^(?P<bucket_id>[0-9]+)/likes/$',
        view=views.LikeBucket.as_view(),
        name='like_bucket'
    ),
    url(
        regex=r'^(?P<bucket_id>[0-9]+)/unlikes/$',
        view=views.UnLikeBucket.as_view(),
        name='unlike_bucket'
    ),
    url(
        regex=r'^(?P<bucket_id>[0-9]+)/comments/$',
        view=views.CommentOnBucket.as_view(),
        name='comment_bucket'
    ),
    url(
        regex=r'^(?P<bucket_id>[0-9]+)/comments/(?P<comment_id>[0-9]+)$',
        view=views.ModerateComments.as_view(),
        name='comment_bucket'
    ),
    url(
        regex=r'^comments/(?P<comment_id>[0-9]+)/$',
        view=views.Comment.as_view(),
        name='comment'
    ),
    url(
        regex=r'^search/$',
        view=views.Search.as_view(),
        name='search'
    )
]
