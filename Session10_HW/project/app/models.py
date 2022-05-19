from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, default='')
    content = models.TextField(default='')
    hit = models.PositiveIntegerField(default=0)
        
    def __str__(self):
        return str(self.title)




class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()

    #comment라는 모델이 어떤 모델을 참조하고 있느냐. 
    #on_delete 참조하고 있는 모델이 삭제되었을 경우, 어떻게 할 것이냐. CASCADE 전체 삭제하기 
    #related_name 포스트에서도 코멘트를 사용할 수 있고, Comment에서도 사용할 수 있도록 하는 것/ 포스트에서 커멘트를 찾고자 한다면 모든 코멘트를 찾고자하는 것.


    def __str__(self):
        return self.content

