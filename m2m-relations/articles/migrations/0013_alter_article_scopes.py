from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_alter_scope_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(related_name='article', through='articles.Scope', to='articles.Tag'),
        ),
    ]
