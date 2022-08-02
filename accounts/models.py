from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        #creating error logic for lack of email
        if not email:
            raise ValueError("User must have an email address")

        if not username:
            raise ValueError("User must have username")


# self.normalize_email(email) normalizes the emails when the letters are bigger
        user = self.model(
        email = self.normalize_email(email),
        username = username,
        first_name = first_name,
        last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, password):
        user = self.create_user(
        email = self.normalize_email(email),
        user_name = username,
        password = password,
        first_name = first_name,
        last_name = last_name
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save()



# create account model and account manager
class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    first_lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=50)

# these fields are mandatory when creating a custom user model
    #required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.DateTimeField(default=False)
    is_staff = models.DateTimeField(default=False)
    is_active = models.DateTimeField(default=False)
    is_superadmin = models.DateTimeField(default=False)

# be able to login with email as username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

# functions being defined
def _str_(self):
    return self.email

def has_perm(self, perm, obj=None):
    return self.is_admin

def has_module_perms(self, add_label):
    return True
