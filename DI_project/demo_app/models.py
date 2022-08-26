from django.db import models

class School(models.Model):
    # 學派名稱
    school_name = models.CharField(max_length=20)
    # 中心價值
    core_value = models.CharField(max_length=100)
    # 人數
    num_member = models.IntegerField()

class Ancient_People(models.Model):
    # 學派
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    # 名字
    name = models.CharField(max_length=10)
    # 名言
    statement = models.CharField(max_length=100)
    # 歲數
    age = models.IntegerField()
