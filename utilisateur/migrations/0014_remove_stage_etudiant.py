# Generated by Django 4.2 on 2023-05-26 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0013_alter_customuser_role_alter_stage_etudiant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stage',
            name='etudiant',
        ),
    ]