from django.apps import AppConfig
from django.db.models.signals import post_migrate

class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'

    def ready(self):
        # Import everything inside ready() to avoid AppRegistryNotReady
        from .models import Book
        from django.contrib.auth.models import Group, Permission
        from django.contrib.contenttypes.models import ContentType

        def create_groups(sender, **kwargs):
            content_type = ContentType.objects.get_for_model(Book)

            # Create/get permissions
            can_view = Permission.objects.get_or_create(
                codename='can_view',
                name='Can view',
                content_type=content_type
            )[0]

            can_create = Permission.objects.get_or_create(
                codename='can_create',
                name='Can create',
                content_type=content_type
            )[0]

            can_edit = Permission.objects.get_or_create(
                codename='can_edit',
                name='Can edit',
                content_type=content_type
            )[0]

            can_delete = Permission.objects.get_or_create(
                codename='can_delete',
                name='Can delete',
                content_type=content_type
            )[0]

            # Create/get groups
            editors, _ = Group.objects.get_or_create(name='Editors')
            viewers, _ = Group.objects.get_or_create(name='Viewers')
            admins, _ = Group.objects.get_or_create(name='Admins')

            # Assign permissions to groups
            editors.permissions.set([can_create, can_edit])
            viewers.permissions.set([can_view])
            admins.permissions.set([can_view, can_create, can_edit, can_delete])

        post_migrate.connect(create_groups, sender=self)

