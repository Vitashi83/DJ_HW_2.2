from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_rename_teachers_student_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='teacher',
            new_name='teachers',
        ),
    ]
