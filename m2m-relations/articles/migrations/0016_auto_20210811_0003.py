from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0015_auto_20210810_2355'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlescope',
            old_name='topic',
            new_name='tag',
        ),
        migrations.AlterField(
            model_name='articlescope',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scope', to='articles.article'),
        ),
    ]
