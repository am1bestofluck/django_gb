# Generated by Django 5.0.2 on 2024-02-16 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_models', '0002_alter_article_content_alter_article_publication_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='full_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='corporis ea sapiente sed hic minima laborum perferendis repellat voluptates doloremque impedit maiores unde animi fugit ipsam quia dolorem voluptate'),
        ),
        migrations.AlterField(
            model_name='article',
            name='publication_date',
            field=models.DateField(verbose_name='2020-03-20'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.CharField(default='nihil accusamus delectus', max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default='repellat aperiam reprehenderit ea iusto', max_length=200),
        ),
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=models.TextField(default='ducimus suscipit eius recusandae neque nisi ullam consectetur necessitatibus consequuntur doloribus eaque corporis tempore illum iste dicta similique reiciendis ab'),
        ),
        migrations.AlterField(
            model_name='author',
            name='birt_date',
            field=models.DateField(default='1968-01-05'),
        ),
    ]
