# Generated by Django 4.2.7 on 2023-11-13 01:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_alter_room_amenities_alter_room_category_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('experiences', '0003_alter_experience_category_alter_experience_host_and_more'),
        ('wishlists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='experiences',
            field=models.ManyToManyField(related_name='whishlists', to='experiences.experience'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='rooms',
            field=models.ManyToManyField(related_name='whishlists', to='rooms.room'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='whishlists', to=settings.AUTH_USER_MODEL),
        ),
    ]
