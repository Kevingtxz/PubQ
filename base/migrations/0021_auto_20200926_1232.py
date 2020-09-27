# Generated by Django 3.1.1 on 2020-09-26 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_remove_standarduser_questions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='right_answear',
        ),
        migrations.AlterField(
            model_name='answear',
            name='deslike_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='answear',
            name='deslikes',
            field=models.ManyToManyField(blank=True, to='base.Deslike'),
        ),
        migrations.AlterField(
            model_name='answear',
            name='is_public',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='answear',
            name='like_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='answear',
            name='likes',
            field=models.ManyToManyField(blank=True, to='base.Like'),
        ),
        migrations.AlterField(
            model_name='answear',
            name='reports',
            field=models.ManyToManyField(blank=True, to='base.Report'),
        ),
        migrations.AlterField(
            model_name='book',
            name='comments',
            field=models.ManyToManyField(blank=True, to='base.Commentary'),
        ),
        migrations.AlterField(
            model_name='book',
            name='deslike_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='deslikes',
            field=models.ManyToManyField(blank=True, to='base.Deslike'),
        ),
        migrations.AlterField(
            model_name='book',
            name='is_public',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='like_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='likes',
            field=models.ManyToManyField(blank=True, to='base.Like'),
        ),
        migrations.AlterField(
            model_name='book',
            name='reports',
            field=models.ManyToManyField(blank=True, to='base.Report'),
        ),
        migrations.AlterField(
            model_name='commentary',
            name='deslike_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='commentary',
            name='deslikes',
            field=models.ManyToManyField(blank=True, to='base.Deslike'),
        ),
        migrations.AlterField(
            model_name='commentary',
            name='is_public',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='commentary',
            name='like_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='commentary',
            name='likes',
            field=models.ManyToManyField(blank=True, to='base.Like'),
        ),
        migrations.AlterField(
            model_name='commentary',
            name='reports',
            field=models.ManyToManyField(blank=True, to='base.Report'),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='base.Subject'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='comments',
            field=models.ManyToManyField(blank=True, to='base.Commentary'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='deslike_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='exam',
            name='deslikes',
            field=models.ManyToManyField(blank=True, to='base.Deslike'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='is_public',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='like_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='exam',
            name='likes',
            field=models.ManyToManyField(blank=True, to='base.Like'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='reports',
            field=models.ManyToManyField(blank=True, to='base.Report'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='right_answears_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='exam',
            name='subject',
            field=models.ManyToManyField(blank=True, to='base.Subject'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='wrong_answears_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='notification',
            name='message',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='not_pic',
            field=models.ImageField(blank=True, default='notification.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='answears',
            field=models.ManyToManyField(blank=True, to='base.Answear'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answears_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='comments',
            field=models.ManyToManyField(blank=True, to='base.Commentary'),
        ),
        migrations.AlterField(
            model_name='question',
            name='deslike_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='deslikes',
            field=models.ManyToManyField(blank=True, to='base.Deslike'),
        ),
        migrations.AlterField(
            model_name='question',
            name='is_public',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='like_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(blank=True, to='base.Like'),
        ),
        migrations.AlterField(
            model_name='question',
            name='reports',
            field=models.ManyToManyField(blank=True, to='base.Report'),
        ),
        migrations.AlterField(
            model_name='question',
            name='wrong_answears_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='standarduser',
            name='color',
            field=models.CharField(blank=True, choices=[('W', 'White'), ('B', 'Black'), ('G', 'Grey')], default='W', max_length=1),
        ),
        migrations.AlterField(
            model_name='standarduser',
            name='notifications',
            field=models.ManyToManyField(blank=True, to='base.Notification'),
        ),
        migrations.AlterField(
            model_name='standarduser',
            name='reports',
            field=models.ManyToManyField(blank=True, to='base.Report'),
        ),
        migrations.AlterField(
            model_name='university',
            name='comments',
            field=models.ManyToManyField(blank=True, to='base.Commentary'),
        ),
        migrations.AlterField(
            model_name='university',
            name='deslike_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='university',
            name='deslikes',
            field=models.ManyToManyField(blank=True, to='base.Deslike'),
        ),
        migrations.AlterField(
            model_name='university',
            name='like_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='university',
            name='likes',
            field=models.ManyToManyField(blank=True, to='base.Like'),
        ),
        migrations.AlterField(
            model_name='university',
            name='questions',
            field=models.ManyToManyField(blank=True, to='base.Question'),
        ),
        migrations.AlterField(
            model_name='university',
            name='reports',
            field=models.ManyToManyField(blank=True, to='base.Report'),
        ),
    ]
