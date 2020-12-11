# Generated by Django 3.0.5 on 2020-12-11 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_landingpage_topaccomplishments'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer', models.CharField(max_length=200)),
                ('work', models.CharField(max_length=2000)),
            ],
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
