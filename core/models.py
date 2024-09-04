from django.db import models
from django.contrib.auth.models import User


class Text(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    predictions = models.TextField()
    hate = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    not_hate = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Clean the text field before saving
        self.text = self.text.replace('$', '')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.text
