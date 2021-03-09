from django.db import models

# Create your models here.
class Post(models.Model):
    # pk 필드 자동 생성. 레코드 고유값.
    title = models.CharField(max_length=30)
    content = models.TextField() #문자열의 길이 제한 없음

    created_at = models.DateTimeField(auto_now_add=True) #월, 일, 시, 분, 초 생성마다
    updated_at = models.DateTimeField(auto_now=True) # 수정 마다

    # string 선언하면 admin 페이지에서 볼 때, 목록에 보여지는 이름을 뭐로 할지 정할 수 있음
    def __str__(self):
        return f'[{self.pk}]{self.title}' #[번호]제목