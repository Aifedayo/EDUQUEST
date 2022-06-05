from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views as qv

router = DefaultRouter()
router.register(r"categories", qv.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path(
        'categories/<slug:slug>/question/',
        qv.QuestionCreateAPIView.as_view(),
        name='create-question'),

    path(
        'categories/<slug:slug>/questions/',
        qv.QuestionListAPIView.as_view(),
        name='list-questions'),

    path(
        'question/<slug:slug>/', 
        qv.QuestionDetailView.as_view(), 
        name='question-detail'),

    path(
        'question/<slug:slug>/answer/', 
        qv.AnswerCreateAPIView.as_view(),
        name='create-answer'),

    path(
        'question/<slug:slug>/answers/', 
        qv.AnswerListAPIView.as_view(),
        name='list-answers'),

    path(
        'answers/<uuid:uuid>/', 
        qv.AnswerRUDAPIView.as_view(), 
        name='answer-detail'),

    path(
        'answers/<uuid:uuid>/like/',
        qv.AnswerLikeAPIView.as_view(),
        name='answer-like'),

    path(
        'answers/<uuid:uuid>/comments/',
        qv.AnswerCommentListCreateAPIView.as_view(),
        name='answer-comments'),

    path(
        'comment/<uuid:uuid>/',
        qv.AnswerCommentRUDAPIView.as_view(),
        name='answer-detail'),
]
