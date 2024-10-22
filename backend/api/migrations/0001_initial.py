# Generated by Django 5.1.1 on 2024-10-22 07:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="propModel",
            fields=[
                (
                    "id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=2000)),
                ("location", models.CharField(max_length=200)),
                ("surface", models.CharField(max_length=200)),
                ("type", models.CharField(max_length=50)),
                ("price", models.DecimalField(decimal_places=2, max_digits=15)),
                (
                    "numberOfRooms",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ]
                    ),
                ),
                (
                    "numberOfBathR",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ]
                    ),
                ),
                ("img1", models.CharField(max_length=200)),
                ("img2", models.CharField(max_length=200)),
                ("img3", models.CharField(max_length=200)),
                ("img4", models.CharField(max_length=200)),
                ("mapImg", models.CharField(max_length=200)),
                ("garage", models.BooleanField(default=False)),
                ("terraza", models.BooleanField(default=False)),
                ("trastero", models.BooleanField(default=False)),
                ("garden", models.BooleanField(default=False)),
                ("elevator", models.BooleanField(default=False)),
                ("pool", models.BooleanField(default=False)),
                ("forSale", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="reviewModel",
            fields=[
                (
                    "name",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                (
                    "rating",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ]
                    ),
                ),
                ("job", models.CharField(max_length=50)),
                ("title", models.CharField(max_length=100)),
                ("review", models.TextField(max_length=300)),
                ("img", models.CharField(max_length=100)),
            ],
        ),
    ]
