# Generated by Django 3.0.4 on 2020-04-02 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200330_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userportfolio',
            name='security',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='core.Security'),
        ),
        migrations.AlterField(
            model_name='userportfolio',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='security', to='core.User'),
        ),
    ]
