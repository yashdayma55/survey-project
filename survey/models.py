from django.db import models

class Survey(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    raffle = models.CharField(max_length=255, blank=True, null=True)  # Comma-separated numbers
    email = models.EmailField()
    url = models.URLField(blank=True, null=True)
    survey_date = models.DateField()
    likes = models.CharField(max_length=255, blank=True, null=True)  # Comma-separated list
    interest = models.CharField(max_length=100, blank=True, null=True)
    other_text = models.CharField(max_length=255, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    recommendation = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Survey by {self.first_name} {self.last_name} on {self.survey_date}"