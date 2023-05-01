# Generated by Django 4.2 on 2023-05-01 00:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("bsf", "0005_alter_brickinwishlistquantity_user_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="SetInWishlistQuantity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField()),
                ("side", models.IntegerField(choices=[(0, "Offered"), (1, "Wanted")])),
                (
                    "legoset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="bsf.legoset"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="wishlist_sets",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="setinwishlistquantity",
            constraint=models.CheckConstraint(
                check=models.Q(("quantity__gt", 0)),
                name="set_check_quantity_positive_wishlist",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="setinwishlistquantity",
            unique_together={("user", "legoset", "side")},
        ),
    ]
