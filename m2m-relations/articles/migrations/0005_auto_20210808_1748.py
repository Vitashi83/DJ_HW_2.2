from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20210808_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='scope',
            field=models.ManyToManyField(through='articles.ArticlesTags', to='articles.Tag'),
        ),
        migrations.AlterField(
            model_name='articlestags',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article'),
        ),
    ]
