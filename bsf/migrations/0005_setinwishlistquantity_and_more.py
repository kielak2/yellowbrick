# Generated by Django 4.2 on 2023-04-30 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("bsf", "0004_exchangeoffer_brickinwishlistquantity_and_more"),
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
            ],
        ),
        migrations.RemoveConstraint(
            model_name="brickinwishlistquantity",
            name="check_quantity_positive_wishlist",
        ),
        migrations.AddConstraint(
            model_name="brickinwishlistquantity",
            constraint=models.CheckConstraint(
                check=models.Q(("quantity__gt", 0)),
                name="brick_check_quantity_positive_wishlist",
            ),
        ),
        migrations.AddField(
            model_name="setinwishlistquantity",
            name="legoset",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="bsf.legoset"
            ),
        ),
        migrations.AddField(
            model_name="setinwishlistquantity",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="wishlist_sets",
                to=settings.AUTH_USER_MODEL,
            ),
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
            unique_together={("user", "legoset")},
        ),
    ]
