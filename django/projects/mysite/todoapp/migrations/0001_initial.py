# Generated by Django 4.0.3 on 2023-09-06 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nickname', models.TextField()),
                ('password', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField()),
                ('contents', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoapp.user')),
            ],
        ),
    ]