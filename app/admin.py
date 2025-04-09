# from django.contrib import admin
# from .models import Question

# admin.site.register(Question)


### admin.py

from django.contrib import admin
from .models import Question, UploadBatch

admin.site.register(UploadBatch)
admin.site.register(Question)