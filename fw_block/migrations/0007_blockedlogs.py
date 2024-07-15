# Generated by Django 5.0.7 on 2024-07-15 16:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fw_block', '0006_alter_ipaddress_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockedLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('block', 'Block'), ('unblock', 'Unblock')], default='block', max_length=7)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('firewall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fw_block.firewall')),
                ('ip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fw_block.ipaddress')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
