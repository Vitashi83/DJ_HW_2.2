from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20210808_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='scopes',
        ),
        migrations.AddField(
            model_name='article',
            name='scope',
            field=models.ManyToManyField(through='articles.ArticlesTags', to='articles.Tag', verbose_name='Раздел'),
        ),
    ]
