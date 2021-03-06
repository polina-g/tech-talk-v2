# Generated by Django 3.2.9 on 2021-11-29 19:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_rename_name_comment_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comment_text',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='date_added',
            new_name='date_posted',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='blogentry',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='username',
        ),
        migrations.AddField(
            model_name='comment',
            name='blog_entry',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.blogentry'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
