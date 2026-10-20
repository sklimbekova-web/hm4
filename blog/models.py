from django.db import models


class Blog(models.Model):
    title = models.CharField(verbose_name='укажите название блога', max_length=20)
    image = models.ImageField(verbose_name='загрузите фото блога', upload_to='blog/')
    description = models.TextField(verbose_name='укажите описание блога', blank=True)
    author_email = models.EmailField(verbose_name='укажите свою почту', default='_@gmail.com')
    CATEGORIES = (
        ('Детектив', 'Детектив'),
        ('Фантастика', 'Фантастика'),
        ('Комедия', 'Комедия')
    )
    categories = models.CharField(verbose_name='выберите категорию блога',
                                   choices=CATEGORIES,
                                   default='Комедия', max_length=100)
    url_blog = models.URLField(verbose_name='Есть ссылка на youtube?', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0, null=True)

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'список блогов'

    def __str__(self):
        return self.title
    
