from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.
# there are two model types created for user account manager and basemanager
class MyAccountManager(BaseUserManager, PermissionsMixin):
    # creating the normal user
    def create_user(self, first_name, last_name, username, email, password=None):
        #creating error logic for lack of email
        if not email:
            raise ValueError("User must have an email address")

        if not username:
            raise ValueError("User must have username")

# creating a model for the user
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


# creating the super user
    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
        email = self.normalize_email(email),
        username = username,
        password = password,
        first_name = first_name,
        last_name = last_name
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self.db)
        return user

    def has_module_perms(self, add_label):
        return True



# create account model to work on functions of user accounts
class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=50)

# these fields are mandatory when creating a custom user model
    #required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

# be able to login with email as username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']


    objects = MyAccountManager()

# functions being defined
def _str_(self):
    return self.email

def has_perm(self, perm, obj=None):
    return self.is_admin

def has_module_perms(self, add_label):
    return True
