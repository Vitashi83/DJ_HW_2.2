from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20210808_1748'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlestags',
            old_name='title',
            new_name='article',
        ),
    ]
