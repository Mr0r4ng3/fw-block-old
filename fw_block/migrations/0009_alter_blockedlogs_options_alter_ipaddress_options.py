# Generated by Django 5.0.7 on 2024-07-16 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fw_block', '0008_alter_blockedlogs_action'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blockedlogs',
            options={'ordering': ['-datetime']},
        ),
        migrations.AlterModelOptions(
            name='ipaddress',
            options={'permissions': (('search_ipaddress', 'Can search IPs'),), 'verbose_name': 'Dirección IP', 'verbose_name_plural': 'Direcciones IP'},
        ),
    ]
