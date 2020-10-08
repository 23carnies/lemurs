from django.db import models
from django.urls import reverse
from datetime import date

FOODS = (
    ('B', 'Bamboo'),
    ('F', 'Fruits'),
    ('S', 'Seeds'),
    ('N', 'Nectar')
)

# Create your models here.

class Toy(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=25)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})

class Lemur(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("detail", kwargs={"lemur_id":self.id})
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(FOODS)

class Feeding(models.Model):
    date = models.DateField('Feeding date')
    food = models.CharField(
        max_length=1,
        choices=FOODS,
        default=FOODS[0][0]
    )

    lemur = models.ForeignKey(Lemur, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_food_display()} on {self.date}"
    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    lemur = models.ForeignKey(Lemur, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for lemur_id: {self.lemur_id} @{self.url}"