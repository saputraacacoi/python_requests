# Generated by Django 2.0.7 on 2018-07-13 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0003_mataperkuliahan'),
    ]

    operations = [
        migrations.AddField(
            model_name='mahasiswa',
            name='born_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mahasiswa',
            name='gender',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='mahasiswa',
            name='nim',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]