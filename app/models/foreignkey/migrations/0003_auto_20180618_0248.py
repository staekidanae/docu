# Generated by Django 2.0.6 on 2018-06-18 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foreignkey', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='foreignkey.User'),
        ),
    ]
