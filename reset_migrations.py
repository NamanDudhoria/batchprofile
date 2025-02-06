from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("DROP TABLE IF EXISTS django_migrations;")