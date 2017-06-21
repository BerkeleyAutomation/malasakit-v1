# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-14 17:55
from __future__ import unicode_literals

from django.db import migrations


def make_empty_string_to_null_forward(model_name, field_name):
    def empty_string_to_null_forward(apps, schema_editor):
        model = apps.get_model('pcari', model_name)
        db_alias = schema_editor.connection.alias

        for instance in model.objects.using(db_alias).all():
            value = getattr(instance, field_name)
            if value is not None and len(value.strip()) == 0:
                setattr(instance, field_name, None)
                instance.save()
    return empty_string_to_null_forward


class Migration(migrations.Migration):

    dependencies = [
        ('pcari', '0054_locations_nullable'),
    ]

    operations = [
        migrations.RunPython(make_empty_string_to_null_forward('Comment', 'message')),
        migrations.RunPython(make_empty_string_to_null_forward('Respondent', 'location')),
    ]