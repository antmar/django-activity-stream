from django.conf import settings


# Django 1.5 compatibility utilities, providing support for custom User models.
# Since get_user_model() causes a circular import if called when app models are
# being loaded, the user_model_label should be used when possible, with calls
# to get_user_model deferred to execution time. The user may also specify that
# they are using a custom table name for their user model - this is used in
# migrations.

user_model_label = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')
user_model_table = getattr(settings, 'AUTH_USER_TABLE', None)

try:
    from django.contrib.auth import get_user_model
except ImportError:
    from django.contrib.auth.models import User
    get_user_model = lambda: User

try:
    from django.utils.encoding import smart_text
except ImportError:
    from django.utils.encoding import smart_unicode as smart_text
