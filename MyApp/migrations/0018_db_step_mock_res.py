# Generated by Django 2.2 on 2020-11-30 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0017_auto_20201102_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_step',
            name='mock_res',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]