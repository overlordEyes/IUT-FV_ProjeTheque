# Generated by Django 4.2 on 2023-06-04 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0017_alter_stage_cood_gps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(blank=True, choices=[('chef_dept', 'Chef de département'), ('responsable', 'Responsable de niveau'), ('encadreur', 'Encadreur')], max_length=50, null=True),
        ),
    ]