from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """用户学习的主题"""
    text=models.CharField(max_length=200)#由字符或文本组成的数据
    date_added=models.DateTimeField(auto_now_add=True)# 记录日期和时间的数据
    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        """返回模型的字符串表示"""
        return  self.text

class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='entries'

    def __str__(self):
        """返回模型的字符串表示"""
        return  self.text[:50]+"..."
