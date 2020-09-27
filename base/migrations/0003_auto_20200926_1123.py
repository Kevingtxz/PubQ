# Generated by Django 3.1.1 on 2020-09-26 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_auto_20200926_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighborhood', models.CharField(max_length=200)),
                ('number', models.CharField(blank=True, max_length=20, null=True)),
                ('complement', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Answear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=5000)),
                ('like_count', models.IntegerField(blank=True, default=0)),
                ('deslike_count', models.IntegerField(blank=True, default=0)),
                ('is_public', models.BooleanField(blank=True, default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(max_length=100)),
                ('note', models.CharField(blank=True, max_length=400, null=True)),
                ('like_count', models.IntegerField(blank=True, default=0)),
                ('deslike_count', models.IntegerField(blank=True, default=0)),
                ('is_public', models.BooleanField(blank=True, default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Commentary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('text', models.CharField(max_length=2000)),
                ('like_count', models.IntegerField(blank=True, default=0)),
                ('deslike_count', models.IntegerField(blank=True, default=0)),
                ('answear', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.answear')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('teacher_name', models.CharField(max_length=200)),
                ('education_Level', models.CharField(choices=[('M', 'Master'), ('H', 'High School'), ('P', 'Phd'), ('D', 'Degree'), ('T', 'Tecnical'), ('F', 'Fundamental')], max_length=1)),
                ('university_name', models.CharField(blank=True, max_length=200, null=True)),
                ('like_count', models.IntegerField(blank=True, default=0)),
                ('deslike_count', models.IntegerField(blank=True, default=0)),
                ('right_answears_count', models.IntegerField(blank=True, default=0)),
                ('wrong_answears_count', models.IntegerField(blank=True, default=0)),
                ('is_public', models.BooleanField(blank=True, default=True)),
                ('pic_1', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic_3', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic_4', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic_5', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('not_pic', models.ImageField(blank=True, default='notification.png', null=True, upload_to='')),
                ('message', models.CharField(blank=True, default='Hi, see it', max_length=1000, null=True)),
                ('answear', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.answear')),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.book')),
                ('comments', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.commentary')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('text', models.CharField(max_length=10000)),
                ('teacher_name', models.CharField(max_length=200)),
                ('education_Level', models.CharField(choices=[('M', 'Master'), ('H', 'High School'), ('P', 'Phd'), ('D', 'Degree'), ('T', 'Tecnical'), ('F', 'Fundamental')], max_length=1)),
                ('is_public', models.BooleanField(blank=True, default=True)),
                ('correct_answear', models.CharField(blank=True, max_length=10000, null=True)),
                ('university_name', models.CharField(blank=True, max_length=200, null=True)),
                ('like_count', models.IntegerField(blank=True, default=0)),
                ('deslike_count', models.IntegerField(blank=True, default=0)),
                ('correct_answears_count', models.IntegerField(blank=True, default=0)),
                ('wrong_answears_count', models.IntegerField(blank=True, default=0)),
                ('pic_1', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic_2', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='StandardUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='profile1.png', null=True, upload_to='')),
                ('nickname', models.CharField(blank=True, default='Student', max_length=200)),
                ('firstname', models.CharField(blank=True, max_length=100)),
                ('lastname', models.CharField(blank=True, max_length=200)),
                ('birth', models.CharField(blank=True, max_length=8)),
                ('phone', models.CharField(blank=True, max_length=11)),
                ('sex', models.CharField(blank=True, max_length=1, null=True)),
                ('education_title', models.CharField(blank=True, max_length=100, null=True)),
                ('color', models.CharField(blank=True, choices=[('W', 'White'), ('B', 'Black'), ('G', 'Grey')], default='W', max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initials', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('discipline_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, default='profile1.png', null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('name', models.CharField(max_length=200)),
                ('initials', models.CharField(max_length=10)),
                ('addresses', models.ManyToManyField(blank=True, to='base.Address')),
            ],
        ),
        migrations.CreateModel(
            name='UserPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('permission', models.CharField(choices=[('S', 'Student'), ('T', 'Teacher'), ('P', 'Poster'), ('O', 'Owner')], max_length=1)),
                ('answear', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.answear')),
                ('commentary', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.commentary')),
                ('exam', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.exam')),
                ('notification', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.notification')),
                ('question', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.question')),
                ('standarduser', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='base.standarduser')),
                ('university', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.university')),
            ],
        ),
        migrations.CreateModel(
            name='Requisition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(max_length=200)),
                ('about', models.CharField(max_length=200)),
                ('standarduser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.standarduser')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('note', models.CharField(max_length=2000)),
                ('answear', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.answear')),
                ('commentary', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.commentary')),
                ('exam', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.exam')),
                ('notification', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.notification')),
                ('question', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.question')),
                ('standarduser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.standarduser')),
                ('university', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.university')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='subject',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.PROTECT, to='base.subject'),
        ),
        migrations.AddField(
            model_name='notification',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.question'),
        ),
        migrations.AddField(
            model_name='notification',
            name='university',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.university'),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('answear', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.answear')),
                ('commentary', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.commentary')),
                ('exam', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.exam')),
                ('notification', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.notification')),
                ('question', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.question')),
                ('standarduser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.standarduser')),
                ('university', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.university')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='questions',
            field=models.ManyToManyField(blank=True, to='base.Question'),
        ),
        migrations.AddField(
            model_name='exam',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='base.Subject'),
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subjects', models.ManyToManyField(blank=True, to='base.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Deslike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('answear', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.answear')),
                ('commentary', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.commentary')),
                ('exam', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.exam')),
                ('notification', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.notification')),
                ('question', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.question')),
                ('standarduser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.standarduser')),
                ('university', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.university')),
            ],
        ),
        migrations.AddField(
            model_name='commentary',
            name='exam',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.exam'),
        ),
        migrations.AddField(
            model_name='commentary',
            name='question',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.question'),
        ),
        migrations.AddField(
            model_name='commentary',
            name='standarduser',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.standarduser'),
        ),
        migrations.AddField(
            model_name='commentary',
            name='university',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.university'),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.state')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='questions',
            field=models.ManyToManyField(blank=True, to='base.Question'),
        ),
        migrations.AddField(
            model_name='book',
            name='subject',
            field=models.ManyToManyField(blank=True, to='base.Subject'),
        ),
        migrations.AddField(
            model_name='answear',
            name='question',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.question'),
        ),
        migrations.AddField(
            model_name='answear',
            name='standarduser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.standarduser'),
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.city'),
        ),
    ]
