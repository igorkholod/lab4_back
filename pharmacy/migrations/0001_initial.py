# Generated by Django 3.0.5 on 2020-04-10 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('composition', models.TextField(default='')),
                ('dosage_form', models.CharField(default='', max_length=200)),
                ('farma_group', models.TextField(default='')),
                ('indication', models.TextField(default='')),
                ('anti_indication', models.TextField(default='')),
                ('appliance', models.TextField(default='')),
                ('expiration_date', models.CharField(default='', max_length=20)),
                ('conditions', models.TextField(default='')),
                ('package', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('license', models.CharField(default='', max_length=50)),
                ('description', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='description_drugs', to='pharmacy.Description')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('adress', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DrugPharmacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drug_stocks', to='pharmacy.Drug')),
                ('pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pharmacy_stocks', to='pharmacy.Pharmacy')),
            ],
        ),
        migrations.AddField(
            model_name='drug',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manufacturer_drugs', to='pharmacy.Manufacturer'),
        ),
        migrations.AddField(
            model_name='drug',
            name='pharmacy',
            field=models.ManyToManyField(related_name='pharmacy_drugs', through='pharmacy.DrugPharmacy', to='pharmacy.Pharmacy'),
        ),
    ]