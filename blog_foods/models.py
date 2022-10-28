from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.models import enums
from datetime import datetime
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.

# khởi tạo mô hình User tiêu chuẩn https://docs.djangoproject.com/en/3.2/ref/contrib/auth/#django.contrib.auth.models.User
User = get_user_model()

# Profile của người dùng
class Profile(models.Model):
    id_user = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(blank = True)
    profileimg = models.ImageField(upload_to='profile_image', default = 'blank-profile-picture.png')

    def __str__(self):
        return self.user.username
        #self.user lấy 

# Cấu trúc của mỗi bài Post
class Post(models.Model):
    user = models.CharField(max_length = 100)
    image = models.ImageField(null = True,blank=True,upload_to = 'images/')
    caption = models.CharField(max_length= 100)
    summary = RichTextField(blank=True)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now)
    no_of_like = models.IntegerField(default=0)
    rate = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )
    description = RichTextField(blank=True)
    price = models.IntegerField(
    default=1,
    validators=[
        MinValueValidator(1)
    ]
    )

    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
        verbose_name="posted by", on_delete=models.SET_NULL)

    def __str__(self):
        return self.caption + ' | ' + str(self.user)
    def get_absolute_url(self):
        return reverse("index", kwargs={"pk": self.pk})
    

# Lưu trữ người dùng đã like bài post chưa. Nếu like rồi thi ấn thêm sẻ xóa, nếu chưa thì lưu vào
class LikePost(models.Model):
    post_id = models.CharField(max_length = 500)
    username = models.CharField(max_length = 500)

    def __str__(self):
        return self.username
class UpProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_user = models.ImageField(upload_to='image_user', default = 'blank-profile-picture.png')
    Facebook = models.CharField(max_length = 100)
    Instagram = models.CharField(max_length = 100)
    summary_user = models.CharField(max_length = 1000) 
    def __str__(self):
        return self.user.username
