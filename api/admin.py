from django.contrib import admin
from .models import Category, Question, Answer, Upvote, Downvote

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Upvote)
admin.site.register(Downvote)
