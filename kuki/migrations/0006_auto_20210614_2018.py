# Generated by Django 2.2.14 on 2021-06-14 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuki', '0005_auto_20210605_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('remarks', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.DeleteModel(
            name='models',
        ),
    ]
