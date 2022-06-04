from rest_framework import serializers

from eduquestapi.models import (Category, Question, Answer, AnswerComment)


class CategorySerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    slug = serializers.SlugField(read_only=True)
    count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = '__all__'

    def get_count(self, instance):
        return instance.questions.count()


class QuestionSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    author = serializers.StringRelatedField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    answers_count = serializers.SerializerMethodField()
    user_has_answered = serializers.SerializerMethodField()

    class Meta:
        model = Question
        exclude = ['id']

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_updated_at(self, instance):
        return instance.updated_at.strftime("%B %d, %Y")

    def get_answers_count(self, instance):
        return instance.answers.count()

    def get_user_has_answered(self, instance):
        request = self.context.get("request")
        return instance.answers.filter(author=request.user).exists()


class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    created_at = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    user_has_liked_answer = serializers.SerializerMethodField()
    question_slug = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        exclude = ['id','question', 'upvoters', 'updated_at']

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_likes_count(self, instance):
        return instance.upvoters.count()

    def get_user_has_liked_answer(self, instance):
        request = self.context.get("request")
        return instance.upvoters.filter(pk=request.user.pk).exists()

    def get_question_slug(self, instance):
        return instance.question.slug


class AnswerCommentSerializer(serializers.ModelSerializer):
    commenter = serializers.StringRelatedField()
    answer = serializers.StringRelatedField()
    class Meta:
        model = AnswerComment
        exclude = ['id', 'updated_at']
