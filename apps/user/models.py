from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    '''Interfaz que proporcionan las operaciones de consulta de la base de datos para Usuarios'''
    def create_user(self, username, first_name, last_name, password=None):
        '''función para crear usuarios'''
        user = self.model(username=username,first_name=first_name,last_name=last_name)
        user.save()
        return user

    def create_superuser(self, username, first_name, last_name, password):
        '''función para crear un super usuario (comando: createsuperuser)'''
        user = self.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    STATUS_CHOICES = (
        (1, 'Activo'),
        (2, 'Inactivo'),
        (3, 'Eliminado'),
    )
    username = models.CharField(unique=True, max_length=15, blank=True, null=True)
    first_name = models.CharField(blank=False,max_length=32,verbose_name='nombres') # nombres completos
    last_name = models.CharField(blank=False,max_length=32,verbose_name='apellidos') # apellidos completos
    is_admin = models.BooleanField(blank=True,default=False,verbose_name='super administrador')
    # estado de super administrador del usuario
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False,verbose_name='super usuario')
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=1)
    # estado del usuario
    created = models.DateTimeField(auto_now_add=True,verbose_name='fecha de creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='fecha de actualización')

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name','last_name']

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
        ordering = ['first_name']

    def __str__(self): return f'{self.first_name} {self.last_name}'