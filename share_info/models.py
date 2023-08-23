from django.db import models

class Info(models.Model):
    """
    title: 제목
    content: 내용
    author: 작성자
    like_count: 좋아요 카운트
    pub_date: 배포일
    major: 전공
    """
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now=True)
    major = models.CharField(max_length=100)  # 전공 필드 추가

    def __str__(self):
        return self.title