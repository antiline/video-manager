# Generated by Django 2.2.6 on 2019-10-28 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subtitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.TextField(unique=True, verbose_name='파일경로')),
                ('encoding_type', models.CharField(max_length=10, verbose_name='인코딩 타입')),
            ],
            options={
                'verbose_name': '자막',
                'verbose_name_plural': '자목록록',
                'db_table': 'subtitle',
            },
        ),
    ]
