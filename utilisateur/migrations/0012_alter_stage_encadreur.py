# Generated by Django 4.2 on 2023-05-22 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0011_stage_encadreur_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='encadreur',
            field=models.CharField(max_length=255),
        ),
    ]
