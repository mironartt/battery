from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from .views import index

urlpatterns = [
    path('example/', index.IndexViewExample.as_view(), name='index_example'),
    path('blog/', index.BlobView.as_view(), name='blog_index'),
    path('blog/<int:pk>', index.BlogPageView.as_view(), name='blog_index'),
    # path('contacts/', index.BlogPageView.as_view(), name='contacts'),
    path('', index.IndexView.as_view(), name='index'),
]