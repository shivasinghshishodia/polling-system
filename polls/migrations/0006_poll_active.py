from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
