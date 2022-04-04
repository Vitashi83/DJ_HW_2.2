from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_rename_scope_article_tag'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ArticleScopeTag',
            new_name='Scopes',
        ),
    ]
