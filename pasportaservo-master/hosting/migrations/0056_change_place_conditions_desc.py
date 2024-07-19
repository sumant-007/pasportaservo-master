# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-02 05:10
from __future__ import unicode_literals

from django.db import migrations, models
import hosting.validators


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0055_change_profile_gender_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='conditions',
            field=models.ManyToManyField(
                blank=True,
                help_text='You are welcome to expand on the conditions in your home in the description.',
                to='hosting.Condition',
                verbose_name='conditions'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.TextField(
                blank=True,
                help_text='Description or remarks about your place and its surroundings. Consider that your guests, for example, might have an allergy for animal fur or an arachnophobia, or have trouble scaling multiple flights of stairs.',
                verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='place',
            name='city',
            field=models.CharField(
                blank=True,
                # Only a full stop is added to the field's description, no other change.
                help_text='Name in the official language, not in Esperanto (e.g.: Rotterdam).',
                max_length=255,
                validators=[hosting.validators.validate_not_all_caps, hosting.validators.validate_not_too_many_caps],
                verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='whereabouts',
            name='name',
            field=models.CharField(
                # Only a full stop is added to the field's description, no other change.
                help_text='Name in the official language, not in Esperanto (e.g.: Rotterdam).',
                max_length=255,
                verbose_name='name'),
        ),
    ]
