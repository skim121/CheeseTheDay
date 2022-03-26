from django.db import models

MILK_CHOICES = (
    ("cow", "cow"),
    ("sheep", "sheep"),
    ("goat", "goat")
)

TYPE_CHOICES = (
    ("fresh","fresh"),
    ("soft", "soft"),
    ("semi-firm", "semi-firm"),
    ("hard", "hard"),
    ("blue", "blue")
)

# Create your models here.
class Cheese(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length = 250)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    milk = models.CharField(max_length=100, choices = MILK_CHOICES)
    origin = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

    class Meta: 
        ordering = ['name']
