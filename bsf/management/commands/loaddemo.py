from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from bsf.models import LegoSet, Color, Brick, UserCollection


class Command(BaseCommand):
    help = "Loads demo database"

    def handle(self, *args, **options):
        Color.objects.all().delete()
        Brick.objects.all().delete()
        LegoSet.objects.all().delete()
        UserCollection.objects.all().delete()
        User.objects.all().delete()

        color0 = Color.objects.create(color_id=0, name='Black', rgb='05131D')
        color4 = Color.objects.create(color_id=4, name='Red', rgb='C91A09')

        # Example Brick objects
        brick1 = Brick.objects.create(brick_id=1, part_num='3024', color=color0,
                                      image_link="https://cdn.rebrickable.com/media/parts/elements/302426.jpg")
        brick2 = Brick.objects.create(brick_id=2, part_num='3020', color=color0,
                                      image_link="https://cdn.rebrickable.com/media/parts/elements/302026.jpg")
        brick3 = Brick.objects.create(brick_id=3, part_num='4070', color=color4,
                                      image_link="https://cdn.rebrickable.com/media/parts/ldraw/4/4070.png")

        # Example LegoSet object
        lego_set1 = LegoSet.objects.create(number='10290-1', name='Pickup Truck',
                                           image_link='https://cdn.rebrickable.com/media/sets/10290-1.jpg',
                                           inventory_id=1)
        lego_set1.bricks.add(brick1, through_defaults={'quantity': 10})
        lego_set1.bricks.add(brick2, through_defaults={'quantity': 5})
        lego_set1.bricks.add(brick3, through_defaults={'quantity': 5})
        lego_set2 = LegoSet.objects.create(number='10312-1', name='Jazz Club',
                                           image_link='https://cdn.rebrickable.com/media/sets/10312-1.jpg',
                                           inventory_id=2)
        lego_set2.bricks.add(brick1, through_defaults={'quantity': 100})
        lego_set2.bricks.add(brick2, through_defaults={'quantity': 20})
        lego_set2.bricks.add(brick3, through_defaults={'quantity': 5})

        # Example UserCollection object
        user = User.objects.create(username='example_user')
        user_collection = UserCollection.objects.create(user=user)
        user_collection.bricks.add(brick1, through_defaults={'quantity': 20})
        user_collection.bricks.add(brick2, through_defaults={'quantity': 10})
        user_collection.sets.add(lego_set1, through_defaults={'quantity': 1})

        self.stdout.write(
            self.style.SUCCESS('Successfully created demo database')
        )
