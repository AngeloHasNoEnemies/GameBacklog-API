from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('platform', models.CharField(max_length=100)),
                ('status', models.CharField(
                    choices=[('Planned', 'Planned'), ('Playing', 'Playing'), ('Finished', 'Finished')],
                    default='Planned',
                    max_length=20,
                )),
                ('hours_played', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
