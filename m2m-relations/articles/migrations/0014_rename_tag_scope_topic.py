from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_alter_article_scopes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scope',
            old_name='tag',
            new_name='topic',
        ),
    ]
