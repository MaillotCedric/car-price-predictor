# Generated by Django 4.2 on 2023-05-04 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carburant',
            fields=[
                ('id_carburant', models.AutoField(primary_key=True, serialize=False)),
                ('type_carburant', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'carburant',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id_categorie', models.AutoField(primary_key=True, serialize=False)),
                ('nom_categorie', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'categorie',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Couleur',
            fields=[
                ('id_couleur', models.AutoField(primary_key=True, serialize=False)),
                ('nom_couleur', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'couleur',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DetailsVoiture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'details_voiture',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='IntervalleProduction',
            fields=[
                ('id_intervalle_production', models.AutoField(primary_key=True, serialize=False)),
                ('debut', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'intervalle_production',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Marque',
            fields=[
                ('id_marque', models.AutoField(primary_key=True, serialize=False)),
                ('nom_marque', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'marque',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ouverture',
            fields=[
                ('id_ouverture', models.AutoField(primary_key=True, serialize=False)),
                ('type_ouverture', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'ouverture',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RoueMotrice',
            fields=[
                ('id_roue_motrice', models.AutoField(primary_key=True, serialize=False)),
                ('type_roue_motrice', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'roue_motrice',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('id_transmission', models.AutoField(primary_key=True, serialize=False)),
                ('type_transmission', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'transmission',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Voiture',
            fields=[
                ('id_voiture', models.AutoField(primary_key=True, serialize=False)),
                ('prix', models.IntegerField(blank=True, null=True)),
                ('levy', models.IntegerField(blank=True, null=True)),
                ('interieur_cuir', models.BooleanField(default=False, null=True)),
                ('cylindree', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('nombre_cylindres', models.IntegerField(blank=True, null=True)),
                ('kilometrage', models.IntegerField(blank=True, null=True)),
                ('nombre_airbags', models.IntegerField(blank=True, null=True)),
                ('id_carburant', models.ForeignKey(db_column='id_carburant', on_delete=django.db.models.deletion.CASCADE, to='app.carburant')),
                ('id_categorie', models.ForeignKey(db_column='id_categorie', on_delete=django.db.models.deletion.CASCADE, to='app.categorie')),
                ('id_couleur', models.ForeignKey(db_column='id_couleur', on_delete=django.db.models.deletion.CASCADE, to='app.couleur')),
                ('id_intervalle_production', models.ForeignKey(db_column='id_intervalle_production', on_delete=django.db.models.deletion.CASCADE, to='app.intervalleproduction')),
                ('id_marque', models.ForeignKey(db_column='id_marque', on_delete=django.db.models.deletion.CASCADE, to='app.marque')),
                ('id_ouverture', models.ForeignKey(db_column='id_ouverture', on_delete=django.db.models.deletion.CASCADE, to='app.ouverture')),
                ('id_roue_motrice', models.ForeignKey(db_column='id_roue_motrice', on_delete=django.db.models.deletion.CASCADE, to='app.rouemotrice')),
                ('id_transmission', models.ForeignKey(db_column='id_transmission', on_delete=django.db.models.deletion.CASCADE, to='app.transmission')),
            ],
            options={
                'db_table': 'voiture',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Modele',
            fields=[
                ('id_modele', models.AutoField(primary_key=True, serialize=False)),
                ('nom_modele', models.CharField(blank=True, max_length=50, null=True)),
                ('id_marque', models.ForeignKey(db_column='id_marque', on_delete=django.db.models.deletion.CASCADE, to='app.marque')),
            ],
            options={
                'db_table': 'modele',
                'managed': True,
            },
        ),
        migrations.AddConstraint(
            model_name='intervalleproduction',
            constraint=models.UniqueConstraint(fields=('debut',), name='unique date de début'),
        ),
        migrations.AddField(
            model_name='detailsvoiture',
            name='id_modele',
            field=models.ForeignKey(db_column='id_modele', on_delete=django.db.models.deletion.CASCADE, to='app.modele'),
        ),
        migrations.AddField(
            model_name='detailsvoiture',
            name='id_voiture',
            field=models.ForeignKey(db_column='id_voiture', on_delete=django.db.models.deletion.CASCADE, to='app.voiture'),
        ),
    ]
