# Generated by Django 2.2.10 on 2021-01-04 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20210104_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='cancellationDeadline',
            field=models.DateTimeField(verbose_name='Cancellation deadline'),
        ),
        migrations.AlterField(
            model_name='event',
            name='registrationDeadline',
            field=models.DateTimeField(verbose_name='Registration deadline'),
        ),
    ]
