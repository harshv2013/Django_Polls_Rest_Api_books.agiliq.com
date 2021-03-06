# # in urls.py
# from django.urls import path
# from .views import polls_list, polls_detail
#
# urlpatterns = [
#     path("polls/", polls_list, name="polls_list"),
#     path("polls/<int:pk>/", polls_detail, name="polls_detail")
# ]


from django.urls import path

from .apiviews import  ChoiceList, CreateVote, PollList, PollDetail

from rest_framework.routers import DefaultRouter
from .apiviews import PollViewSet

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

# urlpatterns = [
#     path("polls/", PollList.as_view(), name="polls_list"),
#     path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
#     path("choices/", ChoiceList.as_view(), name="choice_list"),
#     path("vote/", CreateVote.as_view(), name="create_vote"),
# ]

# urlpatterns = [
#     path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
#     path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
#
# ]

urlpatterns = [
    path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),

]

urlpatterns += router.get_urls()
