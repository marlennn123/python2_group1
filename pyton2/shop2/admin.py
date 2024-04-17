from django.contrib import admin
from .models import *

model_names = [name for name in dir() if isinstance(eval(name), type) and issubclass(eval(name), models.Model)]


for name in model_names:
    admin.site.register(eval(name))