from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_rename_tag_scope_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleScope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articlescopes', to='articles.article')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.tag')),
            ],
        ),
        migrations.DeleteModel(
            name='Scope',
        ),
        migrations.AlterField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(related_name='article', through='articles.ArticleScope', to='articles.Tag'),
        ),
    ]
