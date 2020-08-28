from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


class UserRole(models.TextChoices):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    class Meta:
        verbose_name = 'User role'
        verbose_name_plural = 'User roles'


class User(AbstractUser):
    bio = models.TextField('Users bio', blank=True)
    email = models.EmailField('Users email', unique=True)
    role = models.CharField('Users role', max_length=200, choices=UserRole.choices, default=UserRole.USER)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return 'Users mail - {}, role - {}'.format(self.email, self.role)


class Category(models.Model):
    name = models.CharField('Category name', max_length=200)
    slug = models.SlugField('Category slug', unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return 'Category name - {}, slug - {}'.format(self.name, self.slug)


class Genre(models.Model):
    name = models.CharField('Genre name', max_length=200)
    slug = models.SlugField('Genre slug', unique=True)

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return 'Genre name - {}, slug - {}'.format(self.name, self.slug)


class Title(models.Model):
    name = models.CharField('Title name', max_length=200)
    year = models.IntegerField('Title year', null=True, blank=True, db_index=True)
    genre = models.ManyToManyField(Genre, blank=True, related_name='titles', verbose_name='Title genre')
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, related_name='titles',
                                 verbose_name='Title category')
    description = models.TextField('Title description', blank=True)

    class Meta:
        verbose_name = 'Title'
        verbose_name_plural = 'Titles'

    def __str__(self):
        return 'Title name - {}, year - {}, genre - {}, category - {}'.format(self.name, self.year,
                                                                              self.genre, self.category)


class Review(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='reviews', verbose_name='Review title')
    text = models.TextField('Review text')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', verbose_name='Review author')
    score = models.PositiveSmallIntegerField('Review score', validators=[MinValueValidator(0), MaxValueValidator(10)])
    pub_date = models.DateTimeField('Review publication date', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return 'Reviewed title - {}, review author - {}, review score - {}'.format(self.title, self.author, self.score)


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments', verbose_name='Comment review')
    text = models.TextField('Comment text')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Comment author')
    pub_date = models.DateTimeField('Comment publication date', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return 'Commented review - {}, comment author - {}'.format(self.review, self.author)
