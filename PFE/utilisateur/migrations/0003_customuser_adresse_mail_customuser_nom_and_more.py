# Generated by Django 4.2 on 2023-05-11 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0002_customuser_type_utilisateur'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='adresse_mail',
            field=models.EmailField(default='test@test.com', max_length=255),
        ),
        migrations.AddField(
            model_name='customuser',
            name='nom',
            field=models.CharField(default='nom test', max_length=255),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='type_utilisateur',
            field=models.CharField(choices=[('vis', 'visiteur'), ('et', 'etudiant'), ('ad', 'administration')], default='vis', max_length=3),
        ),
    ]