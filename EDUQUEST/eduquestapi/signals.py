from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string
from django.utils.text import slugify

from .models import (Category, Question, Answer, AnswerComment)


@receiver(pre_save, sender=Category)
def add_slug_to_category(sender, instance, *args, **kwargs):