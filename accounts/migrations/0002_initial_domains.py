from django.db import migrations

def create_initial_domains(apps, schema_editor):
    Domain = apps.get_model('accounts', 'Domain')
    domains = [
        ('FINANCE', 'Finance'),
        ('CONSULTING', 'Consulting'),
        ('RESEARCH', 'Research'),
        ('DATA_ANALYSIS', 'Data Analysis'),
        ('GENERAL', 'General')
    ]
    
    for code, name in domains:
        Domain.objects.get_or_create(name=code)

class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0001_initial'),  # Adjust this to your previous migration
    ]

    operations = [
        migrations.RunPython(create_initial_domains),
    ]