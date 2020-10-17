# Generated by Django 3.1.1 on 2020-10-07 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crawler_story', '0009_auto_20200930_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('categorys', models.CharField(blank=True, max_length=15, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_story', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.URLField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=15, null=True)),
                ('author', models.CharField(blank=True, max_length=30, null=True)),
                ('content_story', models.TextField(blank=True, null=True)),
                ('date_refresh', models.DateTimeField()),
                ('categorys', models.ManyToManyField(to='crawler_story.Category')),
            ],
        ),
        migrations.RemoveField(
            model_name='truyện',
            name='thể_loại',
        ),
        migrations.RenameField(
            model_name='chaper',
            old_name='nội_dung',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='chaper',
            old_name='tac_gia',
            new_name='name_chap',
        ),
        migrations.RemoveField(
            model_name='chaper',
            name='tên_chap',
        ),
        migrations.RemoveField(
            model_name='chaper',
            name='tên_truyện',
        ),
        migrations.AddField(
            model_name='chaper',
            name='create_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chaper',
            name='status',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='chaper',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Thể_loại',
        ),
        migrations.DeleteModel(
            name='Truyện',
        ),
        migrations.AlterField(
            model_name='chaper',
            name='name_story',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crawler_story.story'),
        ),
    ]
