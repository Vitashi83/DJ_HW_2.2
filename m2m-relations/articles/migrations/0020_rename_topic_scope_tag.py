from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0019_alter_scope_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scope',
            old_name='topic',
            new_name='tag',
        ),
    ]
