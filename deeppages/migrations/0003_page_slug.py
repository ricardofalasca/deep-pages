# Generated by Django 2.1.5 on 2019-02-08 07:12

import autoslug.fields

from django.db import migrations


def populate_slug(apps, schema_editor):
    Page = apps.get_model('deeppages', 'Page')
    for p in Page.objects.all():
        p.save()


class Migration(migrations.Migration):

    dependencies = [
        ('deeppages', '0002_auto_20180719_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=autoslug.fields.AutoSlugField(
                default='',
                always_update=True,
                populate_from='name',
                unique=False),
            preserve_default=False,
        ),

        migrations.RunPython(populate_slug, migrations.RunPython.noop),

        migrations.AlterField(
            model_name='page',
            name='slug',
            field=autoslug.fields.AutoSlugField(
                always_update=True,
                default=None,
                editable=False,
                help_text=('Unique identifier to be used on imports and other '
                           'references'),
                populate_from='name'),
        ),
    ]
