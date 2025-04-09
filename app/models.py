from django.db import models

# class Question(models.Model):
#     text = models.TextField()
#     answer = models.TextField(blank=True, null=True)
#     is_answered = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.text[:100]


### models.py

import uuid
from django.db import models

class UploadBatch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    filename = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Batch {self.id} - {self.filename}"


class Question(models.Model):
    batch = models.ForeignKey(UploadBatch, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    answer = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ['batch', 'text']

    def __str__(self):
        return self.text