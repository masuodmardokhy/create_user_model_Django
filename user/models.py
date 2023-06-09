from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self,email,username,phone,password):  #صقحه ثبت نام برای اربران عادی است این متد
        if not email:
            raise ValueError('plz email')
        if not username:
            raise ValueError('plz username')
        if not phone:
            raise ValueError('plz phone')
        user = self.model(email=self.normalize_email(email), username=username, phone=phone)
        user.set_password(password)
        user.save(using=self._db)   # یعنی بیا از دیتابیس فعال ما استفاده کن
        return user

    def create_superuser(self,email,username,phone,password):
        user = self.create_user(email,username,phone,password)
        user.is_admin = True   
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone']
    objects = UserManager()    #بخاطر اینکه در قسمت یوزر مدل بالا اسم این مدل را برده ایم تا کلاس بالا این کلاس مدل را بشناسد

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):  #permisstion #object  #ایا کاربران دستری ب یکسری موارد رو دارن یا نه
        return True

    def has_module_perms(self, app_label):  #مجوز دسترسی به مدلهای مارا دارند
        return True

    @property
    def is_staff(self):   #چه کاربرهای مجوز دسترسی به ادمین پنل رو دارن
        return self.is_admin

