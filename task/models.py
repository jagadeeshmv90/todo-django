from django.db import models


class Task(models.Model):
    persons = (

        ('Me', 'me'),
        ('Njan', 'Njan'),
        ('Swayam', 'Swayam'),
        ('Than', 'Than')
    )
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False, blank=True)
    person = models.CharField(choices=persons, max_length=10)
    important = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} : created by {self.person}."