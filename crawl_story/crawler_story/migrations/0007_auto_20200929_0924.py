# Generated by Django 3.1.1 on 2020-09-29 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crawler_story', '0006_auto_20200927_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thể_loại',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thể_loại', models.CharField(blank=True, max_length=15, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Truyện',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tên_truyện', models.CharField(blank=True, max_length=50, null=True)),
                ('trạng_thái', models.CharField(blank=True, max_length=15, null=True)),
                ('tác_giả', models.CharField(blank=True, max_length=30, null=True)),
                ('dẫn_truyện', models.TextField(blank=True, null=True)),
                ('thể_loại', models.ManyToManyField(to='crawler_story.Thể_loại')),
            ],
        ),
        migrations.RemoveField(
            model_name='truyen',
            name='the_loai',
        ),
        migrations.RemoveField(
            model_name='chaper',
            name='noi_dung',
        ),
        migrations.RemoveField(
            model_name='chaper',
            name='ten_chap',
        ),
        migrations.RemoveField(
            model_name='chaper',
            name='ten_truyen',
        ),
        migrations.AddField(
            model_name='chaper',
            name='nội_dung',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chaper',
            name='tên_chap',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.DeleteModel(
            name='The_loai',
        ),
        migrations.DeleteModel(
            name='Truyen',
        ),
        migrations.AddField(
            model_name='chaper',
            name='tên_truyện',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crawler_story.truyện'),
        ),
    ]
