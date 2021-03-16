from django.db import models
import os

# Create your models here.
class Post(models.Model):
    # pk 필드 자동 생성. 레코드 고유값.
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField() #문자열의 길이 제한 없음

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d', blank=True)
    # 파일이 많은 폴더에서 찾는건 오래걸림. 폴더를 여러개 만들어서 타고 가는게 빠름
    # 이미지 필드 사용을 위해서는 Pillow 라이브러리 필요함. 파이썬 이미지 처리 라이브러리

    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d', blank=True)

    created_at = models.DateTimeField(auto_now_add=True) #월, 일, 시, 분, 초 생성마다
    updated_at = models.DateTimeField(auto_now=True) # 수정 마다

    # string 선언하면 admin 페이지에서 볼 때, 목록에 보여지는 이름을 뭐로 할지 정할 수 있음
    def __str__(self):
        return f'[{self.pk}]{self.title}' #[번호]제목

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]