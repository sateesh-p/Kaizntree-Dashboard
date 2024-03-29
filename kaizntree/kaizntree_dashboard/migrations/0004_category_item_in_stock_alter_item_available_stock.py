# Generated by Django 5.0.2 on 2024-02-12 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaizntree_dashboard', '0003_tag_item_delete_dashboard'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='in_stock',
            field=models.DecimalField(decimal_places=3, default=20, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='available_stock',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
