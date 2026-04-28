from django.contrib import admin
from .models import Category, Label, Task, User


admin.site.register(Category)
admin.site.register(Label)
admin.site.register(Task)
admin.site.register(User)