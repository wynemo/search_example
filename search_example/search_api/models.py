from django.db import models

# Create your models here.
class Candidate(models.Model):
    id = models.AutoField(
        primary_key=True
    )

    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        db_index=True
    )

    score = models.FloatField(
        null=False,
        blank=False
    )

    skill = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'candidate'
