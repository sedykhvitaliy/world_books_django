# Generated by Django 3.2.19 on 2023-05-20 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Введите имя автора', max_length=100, verbose_name='Имя автора')),
                ('last_name', models.CharField(help_text='Введите фамилию автора', max_length=100, verbose_name='Фамилию автора')),
                ('date_of_birth', models.DateField(blank=True, help_text='Введите дату ролждения', null=True, verbose_name='Дата рождения')),
                ('date_of_death', models.DateField(blank=True, help_text='Введите дату смерти', null=True, verbose_name='Дата смерти')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название книги', max_length=100, verbose_name='Название книги')),
                ('isbn', models.CharField(help_text='Должно быть 13 символов', max_length=13, verbose_name='ISBN книги')),
                ('summary', models.TextField(help_text='Введите краткое описание книги', max_length=1000, verbose_name='Аннотация книги')),
                ('author', models.ManyToManyField(help_text='Выберите автора книги', null=True, to='catalog.Author', verbose_name='Автор книги')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите жанр книги', max_length=100, verbose_name='Жанр книги')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите язык книги', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите статус', max_length=100, verbose_name='Статус')),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(help_text='Введите инвентарный номер', max_length=20, null=True, verbose_name='Инвентарный номер')),
                ('imprint', models.CharField(help_text='Введите издательство', max_length=200, verbose_name='Издательство')),
                ('due_back', models.DateField(blank=True, help_text='Введите дату окончания статуса', null=True, verbose_name='Дата окончания статуса')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.book')),
                ('status', models.ForeignKey(help_text='Введите состояние экземпляра', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.status', verbose_name='Статус')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(help_text='Выберите жанр книги', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.genre', verbose_name='Жанр книги'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(help_text='Выберите язык книги', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.language', verbose_name='Язык книги'),
        ),
    ]
