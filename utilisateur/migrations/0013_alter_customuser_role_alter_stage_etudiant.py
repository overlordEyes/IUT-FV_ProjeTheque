# Generated by Django 4.2 on 2023-05-22 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0012_alter_stage_encadreur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(blank=True, choices=[('chef_dept', 'Chef de département'), ('responsable', 'Responsable de niveau'), ('enca', 'Encadreur')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stage',
            name='etudiant',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]