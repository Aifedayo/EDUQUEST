from django.contrib import admin
from .models import Category, Question, Answer, AnswerComment
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('content',)}


admin.site.register(Answer)
admin.site.register(AnswerComment)