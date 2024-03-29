# Generated by Django 5.0.2 on 2024-02-19 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_models', '0011_alter_article_content_alter_article_publication_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(default='necessitatibus illum tenetur optio cupiditate quibusdam hic non dignissimos iste officia perspiciatis libero eaque minus accusantium saepe facilis sapiente ex'),
        ),
        migrations.AlterField(
            model_name='article',
            name='publication_date',
            field=models.DateField(default='2022-01-24'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.CharField(default='at earum quis', max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default='veritatis aspernatur temporibus velit beatae', max_length=200),
        ),
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=models.TextField(default='aliquid esse fugit quidem earum molestias omnis quibusdam enim veniam voluptas quasi ullam cupiditate iure sequi nemo laboriosam consequuntur et'),
        ),
        migrations.AlterField(
            model_name='author',
            name='birth_date',
            field=models.DateField(default='1939-07-03'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(default='inventore nisi cum recusandae quasi id dolores pariatur necessitatibus vel officia ipsum quod eos omnis non quisquam doloremque magni delectus'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_created',
            field=models.DateTimeField(default='2024-01-22 06:06'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_edited',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
