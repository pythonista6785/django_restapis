from django.conf.urls import url

from .views import (
	StatusAPIView, 
	StatusCreateAPIView,
	StatusDetailAPIView,

)

urlpatterns = [
    url(r'^$', StatusAPIView.as_view()),
    url(r'^create/$',StatusCreateAPIView.as_view()),
    url(r'^(?P<pk>.*)/$', StatusDetailAPIView.as_view()),
    #url(r'^(?P:<id>.*)/$', StatusUpdateAPIView.as_view()),
    #url(r'^(?P:<id>.*)/$', StatusDeleteAPIView.as_view()),
]


# Start With
# /api/status/ -> List
# /api/status/create ->  Create
# /api/status/12/ -> Detail
# /api/status/12/delete/ -. Delete

# End With
# /api/status/ -> List -> CRUD
# /api/status/1/ -> Detail -> CRUD

# Final
# /api/status/ -> CRUD & LS

 #