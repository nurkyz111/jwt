from django.db import models


# import datetime
# from django.utils import timezone
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class App(models.Model):

    class Meta:
        verbose_name = 'App'
        verbose_name_plural = 'Apps'
        ordering = ['id']

    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Quiz title')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        ordering = ['id']

    app = models.ForeignKey(App, related_name='question', on_delete=models.CASCADE)
    question_title = models.CharField(max_length=255, verbose_name='Question title')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='date_created')

    def __str__(self):
        return self.question_title

    # def was_published_recently(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1) <= self.pub_date <= now
    #
    # was_published_recently.admin_order_field = 'pub_date'
    # was_published_recently.boolean = True
    # was_published_recently.short_description = 'Published recently?'


class Answer(models.Model):
    verbose_name = 'Answer'
    verbose_name_plural = 'Answers'
    ordering = ['id']

    question = models.ForeignKey(Question, related_name='answer',  on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200, verbose_name='Answer Text')
    is_right = models.BooleanField(default=False)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.answer_text
