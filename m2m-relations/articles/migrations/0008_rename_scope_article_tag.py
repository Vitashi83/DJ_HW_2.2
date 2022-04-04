from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20210808_1806'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='scope',
            new_name='tag',
        ),
    ]
