# Generated by Django 3.1 on 2020-08-14 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backstage', '0006_class_create_teacher'),
        ('login', '0014_auto_20200814_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='to_class',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='backstage.class'),
        ),
    ]