from django.db import models

class Book(models.Model):
    title = models.CharField(verbose_name = 'укажите количество книг:', max_length = 20)
    image = models.ImageField(verbose_name = 'загрузите фото профиля:', upload_to = 'book/')
    description = models.TextField(verbose_name='укажите описание блога:', blank = True)
    author_email = models.EmailField(verbose_name='укажите свою почту:', default = '_@gmail.com')
    CATEGORIES = (
        ('Детектив', 'Детектив'),
        ('Ужастик', 'Ужастик'),
        ('Комедия', 'Комедия')
    )
    categories = models.CharField(verbose_name='Выберите категорию блога:',
                                   choices = CATEGORIES,
                                     default = 'Комедия')

    url_blog = models.URLField(verbose_name = 'Есть ссылка на ютуб?', blank = True)
    created_ad = models.DateField(auto_now_add = True)

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'список блогов' 

    def __str__(self):
        return self.title
   

