from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True, default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/dept/{self.slug}'

class Major(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True, default='')
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)
    require_for_grad = models.TextField()

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return f'/{self.department}/{self.slug}/'

class Display_info(models.Model):
    major = models.ForeignKey(Major, null=True, on_delete=models.SET_NULL )
    title=models.TextField(max_length=100)
    address = models.TextField(max_length=100)
    date = models.DateField()
    link=models.URLField()
    image = models.ImageField(upload_to='gradpage/images/%Y/%m/%d/')

# class Archive(models.Model):
#     major = models.ForeignKey(Major, null=True, on_delete=models.SET_NULL)
#     title=models.TextField(max_length=100)
#     team_name = models.CharField(max_length=30, default='')
#     team_member = models.CharField(max_length=100, default='')
#     description=models.TextField()
#     image = models.ImageField(upload_to='gradpage/images/%Y/%m/%d/')

class Archive(models.Model):
    major = models.ForeignKey(Major, null=True, on_delete=models.SET_NULL)
    exhibit_title = models.TextField(max_length=100)  # 전시회 이름
    service_title = models.TextField(max_length=100, default='')  # 서비스 이름
    team_name = models.CharField(max_length=30, default='팀명을 작성해주세요.')
    team_member = models.CharField(max_length=100, default='팀원을 작성해주세요. (여러명일 경우 모두)')
    description = models.TextField()  # 설명
    file = models.ImageField(upload_to='gradpage/images/%Y/%m/%d/')  # 사진

