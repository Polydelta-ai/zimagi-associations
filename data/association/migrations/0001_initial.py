# Generated by Django 4.1.2 on 2022-11-16 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0002_alter_organization_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Association',
            fields=[
                ('organization_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='organization.organization')),
                ('year_founded', models.IntegerField(default=None, null=True)),
                ('url', models.URLField(default=None, max_length=256, null=True)),
                ('member_count', models.IntegerField(default=None, null=True)),
                ('budget', models.CharField(default=None, max_length=256, null=True)),
                ('bio', models.TextField(default=None, null=True)),
                ('staff_count', models.IntegerField(default=None, null=True)),
                ('type', models.CharField(default=None, max_length=256, null=True)),
            ],
            options={
                'verbose_name': 'association',
                'verbose_name_plural': 'associations',
                'db_table': 'associations_association',
                'ordering': ['id'],
                'abstract': False,
            },
            bases=('organization.organization',),
        ),
    ]
