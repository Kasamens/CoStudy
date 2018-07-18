from django.db import models 

class Thought(models.Model):
    thought_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.thought_text

class Post(Thought):
    pass
    


class Comment(Thought):
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE)
        