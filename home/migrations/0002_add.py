# Generated by Django 4.0.2 on 2022-02-27 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(blank=True, null=True)),
                ('prod_name', models.CharField(max_length=120)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]