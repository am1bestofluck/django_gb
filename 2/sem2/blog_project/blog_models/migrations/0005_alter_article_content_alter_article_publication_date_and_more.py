# Generated by Django 5.0.2 on 2024-02-16 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_models', '0004_alter_article_content_alter_article_publication_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='perspiciatis et at ducimus odio optio deserunt voluptatem necessitatibus nisi magni quaerat quidem laudantium maiores aliquam dicta quis ullam deleniti'),
        ),
        migrations.AlterField(
            model_name='article',
            name='publication_date',
            field=models.DateField(verbose_name='2017-05-19'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.CharField(default='totam saepe distinctio', max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default='ducimus natus deleniti amet nostrum', max_length=200),
        ),
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=models.TextField(default='quam corrupti a optio quidem voluptates ullam blanditiis quia asperiores tenetur molestiae totam obcaecati rerum at officiis laborum placeat illum'),
        ),
        migrations.AlterField(
            model_name='author',
            name='birt_date',
            field=models.DateField(default='1939-06-30'),
        ),
        migrations.AlterField(
            model_name='author',
            name='full_name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
