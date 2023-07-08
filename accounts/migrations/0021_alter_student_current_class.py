# Generated by Django 4.2.2 on 2023-07-06 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_alter_student_current_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='current_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='accounts.classroom'),
        ),
    ]
