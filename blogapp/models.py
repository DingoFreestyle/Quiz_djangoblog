from django.db import models

# Create your models here.
class ArticleModel(models.Model):
    class Meta:
        db_table = "Articles"

        title = models.TextField(max_length=60, null=False) ## 제목
        # category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)  ## 카테고리
        contents = models.TextField(max_length=180, null=False)  ## 제목
