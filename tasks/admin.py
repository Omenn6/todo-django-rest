from django.contrib import admin
from .models import Category, Label, Task, User, Comment


admin.site.register(Category)
admin.site.register(Label)
admin.site.register(Task)
admin.site.register(User)
admin.site.register(Comment)
