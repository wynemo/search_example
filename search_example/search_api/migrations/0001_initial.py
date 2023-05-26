# Generated by Django 4.2.1 on 2023-05-25 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('score', models.FloatField()),
                ('skill', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'candidate',
            },
        ),
    ]