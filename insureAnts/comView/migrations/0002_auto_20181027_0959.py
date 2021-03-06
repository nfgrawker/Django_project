# Generated by Django 2.1.2 on 2018-10-27 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comView', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='post',
            name='insurance_type',
            field=models.CharField(choices=[('Life', (('term', 'Term'), ('full', 'Full'))), ('Auto', (('sixmonth', 'Six Month'), ('monthly', 'Monthly'))), ('Home', (('escrow', 'Escrow'), ('fullyear', 'Full Year'), ('sixmonth', 'Six Month')))], max_length=100),
        ),
    ]
