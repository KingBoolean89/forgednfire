# Generated by Django 2.2.7 on 2019-12-20 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forged',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('length', models.IntegerField()),
                ('blade', models.CharField(max_length=100)),
                ('steelgrade', models.CharField(max_length=100)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
