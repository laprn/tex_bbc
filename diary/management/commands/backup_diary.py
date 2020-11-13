import csv
import datetime
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from ...models import Diary


class Command(BaseCommand):
    help ='Backup Diary data'

    def handle(self, *args, **options):
        date = datetime.date.today().strftime('%Y%m%d')
        file_path = settings.BACKUP_PATH + 'diary' + date + '.csv'
        os.mkdir(settings.BACKUP_PATH, exist_ok=True)

        with open(file_path, 'w') as file:
            writer = csv.writer(file)

            header = [field.name for field in Diary._meta.fields]
            writer.writerow(header)
            diaries = Diary.objects.all()

            for diary in diaries:
                writer.writerow([str(diary.user),
                                 diary.title,
                                 diary.content,
                                 str(diary.created_at),
                                 str(diary.updated_at)
                                 ])

            files = os.listdir(settings.BACKUP_PATH)
            if len(files) >= settings.NUM_SAVED_BACKUP:
                files.sort()
                os.remove(settings.BACKUP_PATH + files[0])