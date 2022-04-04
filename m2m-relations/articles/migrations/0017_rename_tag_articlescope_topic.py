from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0016_auto_20210811_0003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlescope',
            old_name='tag',
            new_name='topic',
        ),
    ]
