# Generated by Django 2.2.2 on 2019-07-05 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cli', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_name', models.CharField(max_length=200)),
                ('agent_type', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='command',
            name='agent_id',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='cli.Agent'),
            preserve_default=False,
        ),
    ]