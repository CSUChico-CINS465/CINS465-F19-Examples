# Generated by Django 2.2.5 on 2019-09-19 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='suggestion2',
            field=models.CharField(default='old_suggestion', max_length=240),
            preserve_default=False,
        ),
    ]
