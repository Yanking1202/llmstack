# Generated by Django 4.2.1 on 2023-09-07 06:57

from django.db import migrations

from apps.models import AppAccessPermission


class Migration(migrations.Migration):

    def create_permissions_from_accessible_by(apps, schema_editor):
        App = apps.get_model('apps', 'App')
        for app in App.objects.all():
            if app.accessible_by and len(app.accessible_by) > 0:
                if app.access_permission == AppAccessPermission.READ and not app.read_accessible_by:
                    app.read_accessible_by = app.accessible_by
                elif app.access_permission == AppAccessPermission.WRITE and not app.write_accessible_by:
                    app.write_accessible_by = app.accessible_by
                app.save()

    dependencies = [
        ('apps', '0006_app_read_accessible_by_app_write_accessible_by'),
    ]

    operations = [
        migrations.RunPython(
            create_permissions_from_accessible_by, migrations.RunPython.noop),
    ]
