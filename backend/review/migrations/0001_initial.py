# Generated by Django 2.2.7 on 2020-10-03 01:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('heritage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('heritage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='heritage_reviews', to='heritage.Heritage')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_review', to=settings.AUTH_USER_MODEL)),
                ('user_recommend', models.ManyToManyField(blank=True, related_name='recommend_reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
