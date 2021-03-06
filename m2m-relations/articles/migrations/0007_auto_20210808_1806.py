from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_rename_title_articlestags_article'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ArticlesTags',
            new_name='ArticleScopeTag',
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]
