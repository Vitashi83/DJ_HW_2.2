from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20210810_2316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='teachers',
            new_name='teacher',
        ),
    ]
