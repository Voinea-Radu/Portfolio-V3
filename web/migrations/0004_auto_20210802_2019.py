# Generated by Django 3.2.5 on 2021-08-02 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20210802_2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10000)),
                ('url', models.CharField(max_length=10000)),
                ('description', models.TextField()),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subEntries', to='web.entry')),
            ],
        ),
        migrations.DeleteModel(
            name='EntrySubClass',
        ),
    ]