# Generated by Django 4.2.2 on 2023-07-04 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_student_current_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='current_class',
            field=models.ForeignKey(default='first', on_delete=django.db.models.deletion.CASCADE, to='accounts.classroom'),
        ),
    ]
