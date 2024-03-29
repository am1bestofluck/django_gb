# Generated by Django 5.0.2 on 2024-02-16 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='culpa perspiciatis recusandae reprehenderit ratione fuga dolore corrupti repellendus consequatur molestias quis tempora nisi enim natus sequi veritatis non quae'),
        ),
        migrations.AlterField(
            model_name='article',
            name='publication_date',
            field=models.DateField(verbose_name='2023-09-01'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.CharField(default='ad dolorem rerum', max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default='recusandae amet nostrum vitae provident', max_length=200),
        ),
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=models.TextField(default='molestiae soluta mollitia laborum velit optio similique nisi tempora earum inventore natus accusamus quos amet commodi cum error veritatis laudantium'),
        ),
        migrations.AlterField(
            model_name='author',
            name='birt_date',
            field=models.DateField(verbose_name='1961-07-28'),
        ),
    ]
