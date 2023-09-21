# Generated by Django 3.2.21 on 2023-09-19 02:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0015_auto_20230918_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('NG', 'Niger'), ('ON', 'Ondo'), ('LG', 'Lagos'), ('DL', 'Delta'), ('OG', 'Ogun'), ('AN', 'Anambra')], max_length=20),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Cancel', 'Cancel'), ('Packed', 'Packed'), ('On the Way', 'On the Way'), ('Accepted', 'Accepted')], default='Pending', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='payapp',
            name='address',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='payapp',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='payapp',
            name='receipt',
            field=models.ImageField(upload_to='receipt'),
        ),
        migrations.AlterField(
            model_name='payapp',
            name='state',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='payapp',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('BW', 'Baby Clothes'), ('SH', 'Shoe'), ('BG', 'Bags'), ('OT', 'Others'), ('CL', 'Clothes')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='producer',
            field=models.CharField(choices=[('FL', 'Fila'), ('DG', 'Dolce and Gabanna'), ('HR', 'Hermes'), ('LV', 'Louis Vuitton'), ('RX', 'Rolex'), ('VS', 'Versace'), ('CK', 'Calvin Klein'), ('AD', 'Addidas'), ('LC', 'Lacosta'), ('GC', 'Gucci'), ('GV', 'Givenchy'), ('SP', 'Supreme')], max_length=2),
        ),
    ]
