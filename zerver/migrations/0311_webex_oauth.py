from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zerver", "0310_jsonfield"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="webex_token",
            field=models.JSONField(default=None, null=True),
        ),
    ]
