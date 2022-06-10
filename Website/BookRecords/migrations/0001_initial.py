# Generated by Django 4.0.5 on 2022-06-10 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allbooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=500)),
                ('authorname', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fiction', models.CharField(max_length=200)),
                ('nonfiction', models.CharField(max_length=200)),
                ('types', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookRecords.allbooks')),
            ],
        ),
    ]
