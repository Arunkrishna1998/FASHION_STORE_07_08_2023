# Generated by Django 4.2.3 on 2023-07-15 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_colorvariant_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sizevariant',
            name='Color_id',
        ),
        migrations.RemoveField(
            model_name='colorvariant',
            name='product_id',
        ),
        migrations.AddField(
            model_name='colorvariant',
            name='product_id',
            field=models.ManyToManyField(blank=True, to='store.sizevariant'),
        ),
    ]