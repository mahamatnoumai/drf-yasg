# Generated by Django 2.1.7 on 2019-03-16 14:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snippets', '0002_auto_20181219_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='SnippetViewer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snippet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viewers', to='snippets.Snippet')),
                ('viewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snippet_views', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
