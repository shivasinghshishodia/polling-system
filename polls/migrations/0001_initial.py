import datetime
from django.db import migrations, models
from django.utils.timezone import zoneinfo


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2019, 1, 16, 16, 59, 36, 459183 ))),
            ],
        ),
    ]
