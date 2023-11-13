from django.contrib.auth.models import User

# Uniqe email field
User._meta.get_field("email")._unique = True
