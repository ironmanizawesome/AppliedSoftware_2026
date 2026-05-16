from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):      # FBV엔 없던 부분임 (CBV 하면서 추가함)
        # FBV 땐 템플릿에 href="/blog/3/" 처럼 주소를 직접 박았음.
        # CBV는 만들어두면 템플릿/리다이렉트가 알아서 이 주소를 씀.
        return f'/blog/{self.pk}/'
