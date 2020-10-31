# To create a postgis extension in the database
from django.contrib.postgres.operations import CreateExtension
from django.db import migrations


class Migration(migrations.Migration):

    operations = [CreateExtension("postgis")]
