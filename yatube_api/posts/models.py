"""Posts models."""
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import UniqueConstraint

User = get_user_model()


class Group(models.Model):
    """Group model."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    class Meta():
        """Group model Meta."""

        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self) -> str:
        """Group title return."""
        return self.title


class Post(models.Model):
    """Post model."""

    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author_posts',
        verbose_name='Автор',
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='group_posts',
        blank=True,
        null=True,
        verbose_name='Группа',
        help_text='Выберите группу'
    )
    image = models.ImageField(
        'Картинка',
        upload_to='posts/',
        blank=True
    )

    class Meta:
        """Post model Meta."""

        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('id',)

    def __str__(self):
        """Post title return."""
        return self.text[:15]


class Comment(models.Model):
    """Comment model."""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        blank=True,
        null=True,
        verbose_name='Автор'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        blank=True,
        null=True,
        verbose_name='Комментарий'
    )
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        """Comment model Meta."""

        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
        ordering = ('id',)


class Follow(models.Model):
    """Follow model."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        blank=True,
        null=True,
        verbose_name='Subscriber'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        blank=True,
        null=True,
        verbose_name='Subscribed',)

    class Meta:
        """Follow model Meta."""

        UniqueConstraint(fields=['user', 'author'], name='unique_users')
        constraints = [
            models.CheckConstraint(
                check=~models.Q(user=models.F('author')),
                name='Not author',
            ),
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
