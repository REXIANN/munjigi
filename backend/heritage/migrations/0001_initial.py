# Generated by Django 2.2.7 on 2020-09-22 06:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Heritage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('k_name', models.CharField(max_length=50)),
                ('h_name', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('imageurl', models.URLField()),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('era', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=150)),
                ('clsfc_code', models.IntegerField()),
                ('clsfc_name', models.CharField(max_length=50)),
                ('sido', models.CharField(max_length=50)),
                ('hit', models.IntegerField(default=0, null=True)),
                ('dib_users', models.ManyToManyField(blank=True, related_name='dibs_heritages', to=settings.AUTH_USER_MODEL)),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_heritages', to=settings.AUTH_USER_MODEL)),
                ('visit_users', models.ManyToManyField(blank=True, related_name='visited_heritages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tagging', models.ManyToManyField(blank=True, related_name='tag_heritages', to='heritage.Heritage')),
            ],
        ),
        migrations.CreateModel(
            name='Heritage_picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageurl', models.URLField()),
                ('heritage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heritage.Heritage')),
            ],
        ),
    ]
