# Generated by Django 2.2.14 on 2021-06-18 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuki', '0018_auto_20210618_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='klc.jpg', upload_to='avatars'),
        ),
    ]
