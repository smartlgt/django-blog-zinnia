from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zinnia', '0006_alter_entry_options_alter_entry_related'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'get_latest_by': 'publication_date', 'ordering': ['-publication_date'], 'permissions': (
                ('can_view_all', 'Can view all entries'), 
                ('can_change_status', 'Can change status'), 
                ('can_change_author', 'Can change author(s)')
            ), 'verbose_name': 'entry', 'verbose_name_plural': 'entries'},
        ),
    ]
