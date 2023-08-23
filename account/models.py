from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class MyAccountManager(BaseUserManager):
    # 일반 user 생성, username 이 userID를 의미함
    def create_user(self, username, name, email, phonenumber, birthdate, password=None):
        if not username:
            raise ValueError("Users must have an userID.")
        if not name:
            raise ValueError("Users must have an name.")
        user = self.model(
            username=username,
            name=name,
            email=self.normalize_email(email),
            phonenumber=phonenumber,
            birthdate=birthdate,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 User 생성
    def create_superuser(self, username, name, email, phonenumber, birthdate, password, **extra_fields):
        user = self.create_user(
            username=username,
            name=name,
            email=email,
            phonenumber=phonenumber,
            birthdate=birthdate,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=40, null=False, blank=False)
    email = models.EmailField(max_length=100, unique=True)
    phonenumber = models.CharField(max_length=11)
    birthdate = models.DateField()
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyAccountManager()  # 헬퍼 클래스 사용

    USERNAME_FIELD = 'username'  # 로그인 ID로 사용할 필드
    REQUIRED_FIELDS = ['name', 'email', 'phonenumber', 'birthdate']  # 필수 작성 필드

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_lable):
        return True
