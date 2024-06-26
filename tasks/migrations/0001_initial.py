# Generated by Django 4.2.13 on 2024-06-16 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
        ('accounts', '0001_initial'),
        ('management', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('object_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True, verbose_name='Public identifier')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(db_index=True, max_length=500)),
                ('description', models.TextField(blank=True, db_index=True, null=True)),
                ('planned_start_date', models.DateTimeField(blank=True, null=True)),
                ('planned_end_date', models.DateTimeField(blank=True, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('active', models.BooleanField(blank=True, default=False)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_deleted', to=settings.AUTH_USER_MODEL)),
                ('owners', models.ManyToManyField(blank=True, db_index=True, related_name='%(app_label)s_%(class)s_owners', to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_status', to='management.dropdown')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('object_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True, verbose_name='Public identifier')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(db_index=True, max_length=500)),
                ('description', models.TextField(blank=True, db_index=True, null=True)),
                ('planned_start_date', models.DateField(blank=True, null=True)),
                ('planned_end_date', models.DateField(blank=True, null=True)),
                ('estimated_work_hours', models.PositiveIntegerField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('worked_hours', models.JSONField(default=dict)),
                ('comments', models.ManyToManyField(blank=True, related_name='%(app_label)s_%(class)s_comments', to='comments.comment')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_deleted', to=settings.AUTH_USER_MODEL)),
                ('owners', models.ManyToManyField(blank=True, db_index=True, related_name='%(app_label)s_%(class)s_owners', to=settings.AUTH_USER_MODEL)),
                ('plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_plan', to='tasks.plan')),
                ('priority', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_priority', to='management.dropdown')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_status', to='management.dropdown')),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_team', to='accounts.teams')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
