# Generated by Django 2.2.2 on 2019-06-12 03:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20190612_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False),
        ),
    ]
