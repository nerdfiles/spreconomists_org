# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import imagestore.utils
from django.conf import settings
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        migrations.swappable_dependency(settings.IMAGESTORE_ALBUM_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Charge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('amount', models.DecimalField(null=True, max_digits=10, decimal_places=5, blank=True)),
                ('currency', models.CharField(help_text=b'"USD", "EUR", etc. Review https://support.stripe.com/questions/which-currencies-does-stripe-support for more detail.', max_length=10)),
                ('description', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MiniChargeImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, null=True, verbose_name='Title', blank=True)),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('tags', tagging.fields.TagField(max_length=255, verbose_name='Tags', blank=True)),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=imagestore.utils.FilePathGenerator(to='imagestore/'), max_length=255, verbose_name='File')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created', null=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated', null=True)),
                ('album', models.ForeignKey(related_name='images', verbose_name='Album', blank=True, to=settings.IMAGESTORE_ALBUM_MODEL, null=True)),
                ('user', models.ForeignKey(related_name='images', verbose_name='User', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('order', 'id'),
                'abstract': False,
                'db_table': 'mini_charge_image',
                'permissions': (('moderate_images', 'View, update and delete any image'),),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MiniChargePluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('charge', models.ForeignKey(related_name='plugins', to='mini_charge.Charge')),
            ],
            options={
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='charge',
            name='work',
            field=models.ManyToManyField(to=settings.IMAGESTORE_IMAGE_MODEL),
            preserve_default=True,
        ),
    ]
