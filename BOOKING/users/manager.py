from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone, email, first_name, last_name, password):

        if not phone:
            raise ValueError ('You must have phone number!')

        if not email:
            raise ValueError ('You must have email!')

        if not first_name:
            raise ValueError ('this field is required!')

        if not last_name:
            raise ValueError('this field is required!')

        user = self.model(phone=phone, email=self.normalize_email(email), first_name= first_name, last_name= last_name)
        user.set_password(password)
        user.save(using= self.db)
        return user


    def create_superuser(self, phone, email, first_name, last_name, password):
        user = self.create_user(phone, email, first_name, last_name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user














