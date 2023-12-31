# Generated by Django 3.2.21 on 2023-09-11 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20230911_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('AN', 'Anambra'), ('OG', 'Ogun'), ('DL', 'Delta'), ('ON', 'Ondo'), ('NG', 'Niger'), ('LG', 'Lagos')], max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('BG', 'Bags'), ('OT', 'Others'), ('BW', 'Baby Clothes'), ('SH', 'Shoe'), ('CL', 'Clothes')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='producer',
            field=models.CharField(choices=[('CK', 'Calvin Klein'), ('AD', 'Addidas'), ('VS', 'Versace'), ('DG', 'Dolce and Gabanna'), ('GC', 'Gucci'), ('RX', 'Rolex'), ('LV', 'Louis Vuitton'), ('LC', 'Lacosta'), ('HR', 'Hermes'), ('SP', 'Supreme'), ('GV', 'Givenchy'), ('FL', 'Fila')], max_length=2),
        ),
    ]
