# Generated by Django 4.2 on 2023-05-14 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0006_alter_customuser_cursus_alter_customuser_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entreprise', models.CharField(max_length=255)),
                ('raison_sociale', models.CharField(max_length=255)),
                ('contact_email', models.EmailField(max_length=255)),
                ('contact_telephone', models.CharField(max_length=20)),
                ('attestation_fin_stage', models.FileField(blank=True, null=True, upload_to='attestations/')),
                ('rapport_stage', models.FileField(blank=True, null=True, upload_to='rapports/')),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('nombre_stagiaires', models.PositiveIntegerField(blank=True, null=True)),
                ('date_stage', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='stage',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='utilisateur.stage'),
        ),
    ]
