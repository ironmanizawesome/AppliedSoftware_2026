from django.db import models
import os

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    head_image = models.ImageField(upload_to= 'blog/images/%Y/%m/%d/', blank=True  )
    file_upload = models.FileField(upload_to= 'blog/files/%Y/%m/%d/', blank=True   ) #파일들, admin에서 업로드 완
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):      # FBV엔 없던 부분임 (CBV 하면서 추가함)
        # FBV 땐 템플릿에 href="/blog/3/" 처럼 주소를 직접 박았음.
        # CBV는 만들어두면 템플릿/리다이렉트가 알아서 이 주소를 씀.
        return f'/blog/{self.pk}/'
    
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
    
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
