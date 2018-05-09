from django.urls import path
from api import views
from api.views import (
    CategoryListView,
    QuestionListView,
    QuestionCreateView,
    QuestionDeleteView,
    AnswerListView,
    AnswerCreateView,
    AnswerDeleteView,
    UpvoteQuestionCreateView,
    UpvoteQuestionListView,
    DownvoteQuestionCreateView,
    DownvoteQuestionListView,
    UpvoteAnswerCreateView,
    UpvoteAnswerListView,
    DownvoteAnswerCreateView,
    DownvoteAnswerListView,
    UserRegisterView,
    LoginAPIView,
    FollowCategoryCreateView,
    FollowCategoryListView,
    FollowQuestionCreateView,
    FollowQuestionListView,
    FollowUserCreateView,


    )

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='api-category_list'),
    path('question/list/<int:category_id>/', QuestionListView.as_view(), name='api-question_list'),
    path('question/create/', QuestionCreateView.as_view(), name='api-question-create'),
    path('question/delete/<int:question_id>/', QuestionDeleteView.as_view(), name='api-question-delete'),
    path('answer/list/<int:question_id>/', AnswerListView.as_view(), name='api-answer_list'),
    path('answer/create/', AnswerCreateView.as_view(), name='api-answer-create'),
    path('answer/delete/<int:answer_id>/', AnswerDeleteView.as_view(), name='api-answer-delete'),
    path('register/', UserRegisterView.as_view(), name='api-register'),
    path('login/', LoginAPIView.as_view(), name='api-login'),
    path('follow/category/', FollowCategoryCreateView.as_view(), name='api-follow-category'),
    path('follow/category/list/<int:category_id>/', FollowCategoryListView.as_view(), name='api-follow-category-list'),
    path('follow/question/', FollowQuestionCreateView.as_view(), name='api-follow-question'),
    path('follow/question/list/<int:question_id>/', FollowQuestionListView.as_view(), name='api-follow-question-list'),
    path('follow/user/', FollowUserCreateView.as_view(), name='api-follow-user'),
    path('upvote/question/', UpvoteQuestionCreateView.as_view(), name='api-upvote-question'),
    path('upvote/question/list/<int:question_id>/', UpvoteQuestionListView.as_view(), name='api-upvote-question-list'),
    path('downvote/question/', DownvoteQuestionCreateView.as_view(), name='api-downvote-question'),
    path('downvote/question/list/<int:question_id>/', DownvoteQuestionListView.as_view(), name='api-downvote-question-list'),
    path('upvote/answer/', UpvoteAnswerCreateView.as_view(), name='api-upvote-answer'),
    path('upvote/answer/list/<int:answer_id>/', UpvoteAnswerListView.as_view(), name='api-upvote-answer-list'),
    path('downvote/answer/', DownvoteAnswerCreateView.as_view(), name='api-downvote-answer'),
    path('downvote/answer/list/<int:answer_id>/', DownvoteAnswerListView.as_view(), name='api-downvote-answer-list'),


]


# path('userprofile/', UserProfileView.as_view(), name='api-user-profile'),
# path('searchbox/', SearchBoxView.as_view(), name='api-search-box'),
# path('allcontent/', AllContentListView.as_view(), name='api-all-content'),
