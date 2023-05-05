# Generated by Django 4.2 on 2023-05-04 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Brick",
            fields=[
                ("brick_id", models.IntegerField(primary_key=True, serialize=False)),
                ("part_num", models.CharField(max_length=30)),
                ("image_link", models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="BrickInCollectionQuantity",
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
                (
                    "brick",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="bsf.brick"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="BrickInSetQuantity",
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
                (
                    "brick",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="bsf.brick"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Color",
            fields=[
                ("color_id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=60)),
                ("rgb", models.CharField(max_length=6)),
                ("is_transparent", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="ExchangeOffer",
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
                (
                    "author_state",
                    models.IntegerField(
                        choices=[(0, "Pending"), (1, "Accepted"), (2, "Exchanged")],
                        default=1,
                    ),
                ),
                (
                    "receiver_state",
                    models.IntegerField(
                        choices=[(0, "Pending"), (1, "Accepted"), (2, "Exchanged")],
                        default=0,
                    ),
                ),
                ("exchanged", models.BooleanField(default=False)),
                (
                    "offer_author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="authored_offers",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "offer_receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="received_offers",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LegoSet",
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
                ("number", models.CharField(max_length=20)),
                ("name", models.CharField(max_length=256)),
                ("image_link", models.CharField(max_length=256)),
                ("inventory_id", models.IntegerField()),
                ("theme", models.CharField(max_length=256)),
                ("quantity_of_bricks", models.IntegerField()),
                (
                    "bricks",
                    models.ManyToManyField(
                        through="bsf.BrickInSetQuantity", to="bsf.brick"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SetInCollectionQuantity",
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
                (
                    "brick_set",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="bsf.legoset"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Wishlist",
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
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserCollection",
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
                (
                    "bricks",
                    models.ManyToManyField(
                        through="bsf.BrickInCollectionQuantity", to="bsf.brick"
                    ),
                ),
                (
                    "sets",
                    models.ManyToManyField(
                        through="bsf.SetInCollectionQuantity", to="bsf.legoset"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
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
        migrations.CreateModel(
            name="SetInOfferQuantity",
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
                    "offer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bsf.exchangeoffer",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="setincollectionquantity",
            name="collection",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="bsf.usercollection"
            ),
        ),
        migrations.CreateModel(
            name="BrickStats",
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
                ("likes", models.IntegerField()),
                ("min_recommended_age", models.IntegerField()),
                ("build_time", models.IntegerField()),
                (
                    "brick_set",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="bsf.legoset"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BrickInWishlistQuantity",
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
                    "brick",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="bsf.brick"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="wishlist_bricks",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="brickinsetquantity",
            name="brick_set",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="bsf.legoset"
            ),
        ),
        migrations.CreateModel(
            name="BrickInOfferQuantity",
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
                    "brick",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="bsf.brick"
                    ),
                ),
                (
                    "offer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bsf.exchangeoffer",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="brickincollectionquantity",
            name="collection",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="bsf.usercollection"
            ),
        ),
        migrations.AddField(
            model_name="brick",
            name="color",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="bsf.color"
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
            unique_together={("user", "legoset", "side")},
        ),
        migrations.AddConstraint(
            model_name="setinofferquantity",
            constraint=models.CheckConstraint(
                check=models.Q(("quantity__gt", 0)),
                name="check_quantity_positive_offer_set",
            ),
        ),
        migrations.AddConstraint(
            model_name="exchangeoffer",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("offer_author", models.F("offer_receiver")), _negated=True
                ),
                name="check_author_receiver_different",
            ),
        ),
        migrations.AddConstraint(
            model_name="brickinwishlistquantity",
            constraint=models.CheckConstraint(
                check=models.Q(("quantity__gt", 0)),
                name="check_quantity_positive_wishlist",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="brickinwishlistquantity",
            unique_together={("user", "brick", "side")},
        ),
        migrations.AddConstraint(
            model_name="brickinofferquantity",
            constraint=models.CheckConstraint(
                check=models.Q(("quantity__gt", 0)),
                name="check_quantity_positive_offer_brick",
            ),
        ),
    ]
