# Generated by Django 3.2.21 on 2023-09-15 01:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20230913_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('LG', 'Lagos'), ('ON', 'Ondo'), ('OG', 'Ogun'), ('NG', 'Niger'), ('AN', 'Anambra'), ('DL', 'Delta')], max_length=20),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Cancel', 'Cancel'), ('Packed', 'Packed'), ('On the Way', 'On the Way'), ('Pending', 'Pending'), ('Delivered', 'Delivered'), ('Accepted', 'Accepted')], default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('OT', 'Others'), ('SH', 'Shoe'), ('CL', 'Clothes'), ('BG', 'Bags'), ('BW', 'Baby Clothes')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='producer',
            field=models.CharField(choices=[('LV', 'Louis Vuitton'), ('VS', 'Versace'), ('SP', 'Supreme'), ('GC', 'Gucci'), ('CK', 'Calvin Klein'), ('AD', 'Addidas'), ('LC', 'Lacosta'), ('FL', 'Fila'), ('DG', 'Dolce and Gabanna'), ('GV', 'Givenchy'), ('HR', 'Hermes'), ('RX', 'Rolex')], max_length=2),
        ),
    ]
