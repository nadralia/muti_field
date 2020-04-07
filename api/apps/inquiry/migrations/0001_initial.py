# Generated by Django 3.0.3 on 2020-04-07 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('inquirystatus', models.IntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inquiry_client', to='accounts.Client')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inquiry_company', to='accounts.Company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inquiry_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'inquiries',
            },
        ),
    ]
