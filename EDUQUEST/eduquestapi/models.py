import uuid as uuid_lib

from core.models import TimeStampedModel
from django.conf import settings
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    context = models.TextField()
    avatar = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
                                    related_name='categories')

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
class Question(TimeStampedModel):
    category = models.ForeignKey(Category, related_name='questions',
                                         on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid_lib.uuid4, editable=False)
    title = models.CharField(max_length=255)
    avatar = models.ImageField(null=True, blank=True)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(
                            settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
                            related_name='questions')

    def __str__(self):
        return self.title


class Answer(TimeStampedModel):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, 
                                editable=False)
    body = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, 
                                    related_name="answers")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
                                    related_name='answers')
    upvoters = models.ManyToManyField(
                    settings.AUTH_USER_MODEL, related_name='likes')

    def __str__(self):
        return self.author.username


class AnswerComment(TimeStampedModel):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, 
                                related_name='answer')
    commenter = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
                                    related_name='comments'
    )
    comment = models.TextField()

    def __str__(self):
        return self.comment[:25]
