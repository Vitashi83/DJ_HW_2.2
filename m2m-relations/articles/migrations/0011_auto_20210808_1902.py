from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20210808_1840'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Scopes',
            new_name='Scope',
        ),
        migrations.RemoveField(
            model_name='article',
            name='tag',
        ),
        migrations.AddField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(through='articles.Scope', to='articles.Tag'),
        ),
    ]
