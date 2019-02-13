# Generated by Django 2.1.5 on 2019-02-13 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_auto_20190209_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catgeory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='category_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]