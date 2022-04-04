from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlesTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название тега')),
            ],
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
        migrations.AddField(
            model_name='articlestags',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.tag'),
        ),
        migrations.AddField(
            model_name='articlestags',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article'),
        ),
        migrations.AddField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(through='articles.ArticlesTags', to='articles.Tag'),
        ),
    ]
