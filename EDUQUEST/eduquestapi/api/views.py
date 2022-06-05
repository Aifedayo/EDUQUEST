from unicodedata import category
from eduquestapi.api.permissions import IsAuthorOrReadOnly
from eduquestapi.api.serializers import (
    CategorySerializer, QuestionSerializer, AnswerSerializer, 
        AnswerCommentSerializer)
from eduquestapi.models import (
    Category, Question, Answer, AnswerComment)
from rest_framework import generics, viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get('name')
        category = Category.objects.all()
        if category.name.exists():
            raise ValidationError("Category Name already exists")
        serializer.save(author=request_user)

    
class QuestionCreateAPIView(generics.CreateAPIView):
    queryset = Question.objects.all().order_by('-created_at')
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "slug"

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get('slug')
        category = get_object_or_404(Category, slug=kwarg_slug)
        serializer.save(author=request_user, category=category)


class QuestionListAPIView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("slug")
        return Question.objects.filter(category__slug=kwarg_slug)


class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    lookup_field = "slug"


class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get('slug')
        question = get_object_or_404(Question, slug=kwarg_slug)
        if question.answers.filter(author=request_user).exists():
            raise ValidationError("You have answered this question")

        serializer.save(author=request_user, question=question)


class AnswerListAPIView(generics.ListAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("slug")
        return Answer.objects.filter(question__slug=kwarg_slug)


class AnswerRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    lookup_field = "uuid"


class AnswerLikeAPIView(APIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, uuid):
        answer = get_object_or_404(Answer, uuid=uuid)
        answer.upvoters.add(request.user)
        answer.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(answer, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, uuid):
        answer = get_object_or_404(Answer, uuid=uuid)
        answer.upvoters.remove(request.user)
        answer.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(answer, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class AnswerCommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = AnswerComment.objects.all().order_by('id')
    serializer_class = AnswerCommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("uuid")
        answer_comment = AnswerComment.objects.filter(answer__uuid=kwarg_slug)
        print(answer_comment)
        return answer_comment

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_uuid = self.kwargs.get('uuid')
        answer = get_object_or_404(Answer, uuid = kwarg_uuid)
        serializer.save(commenter=request_user, answer=answer)


class AnswerCommentRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnswerComment.objects.all()
    serializer_class = AnswerCommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    lookup_field = 'uuid'
