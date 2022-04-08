from django.db import models
from django.utils import timezone


class Post(models.Model):
    # ForeignKey 지정 방법(app-name.model-name)이 특이함.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # blank: 유효성검사에서 사용(데이터의 공백 허용여부 지정)
    # null: DBMS에서 사용(null 저장여부 지정)
    published_at = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_at = timezone.now()
        self.save()
        
    def __str__(self):
        return f'POST({self.id}: {self.title})'