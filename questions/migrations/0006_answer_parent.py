# Generated by Django 3.2 on 2022-01-19 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20220119_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.answer'),
        ),
    ]
