# Generated by Django 5.0.7 on 2024-07-15 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fw_block', '0005_alter_ipaddress_asn'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ipaddress',
            options={'permissions': (('search_ipadress', 'Can search IPs'),), 'verbose_name': 'Dirección IP', 'verbose_name_plural': 'Direcciones IP'},
        ),
        migrations.AlterModelOptions(
            name='protectednetworks',
            options={'verbose_name': 'Red protegida', 'verbose_name_plural': 'Redes protegidas'},
        ),
        migrations.RemoveField(
            model_name='blocked',
            name='blocked_at',
        ),
        migrations.RemoveField(
            model_name='blocked',
            name='is_blocked',
        ),
        migrations.RemoveField(
            model_name='blocked',
            name='unblocked_at',
        ),
        migrations.AddField(
            model_name='ipaddress',
            name='is_blocked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='firewall',
            name='context',
            field=models.CharField(max_length=100, verbose_name='Contexto'),
        ),
        migrations.AlterField(
            model_name='firewall',
            name='ip',
            field=models.GenericIPAddressField(verbose_name='IP'),
        ),
        migrations.AlterField(
            model_name='firewall',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='ipaddress',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='ipaddress',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='País'),
        ),
        migrations.AlterField(
            model_name='ipaddress',
            name='ip',
            field=models.GenericIPAddressField(db_index=True, unique=True, verbose_name='IP'),
        ),
        migrations.AlterField(
            model_name='ipaddress',
            name='organization',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Organización'),
        ),
        migrations.AlterField(
            model_name='ipaddress',
            name='region',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='protectednetworks',
            name='cidr',
            field=models.CharField(max_length=18, verbose_name='CIDR'),
        ),
    ]
