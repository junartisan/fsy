import csv
from django.core.management.base import BaseCommand
from participants.models import Participant
from datetime import datetime
from django.utils import timezone

class Command(BaseCommand):
    help = "Import FSY participants from CSV (timezone-safe)"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def parse_datetime(self, dt_str):
        """
        Convert CSV datetime string to timezone-aware datetime.
        If invalid or empty, return None.
        """
        try:
            naive_dt = datetime.strptime(dt_str.strip(), "%m/%d/%Y %H:%M:%S")
            return timezone.make_aware(naive_dt, timezone.get_default_timezone())
        except Exception:
            return None

    def parse_date(self, date_str):
        """
        Convert CSV date string to Python date object.
        If invalid or empty, return None.
        """
        try:
            return datetime.strptime(date_str.strip(), "%m/%d/%Y").date()
        except Exception:
            return None

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        with open(csv_file, newline='', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            next(reader)  # skip header

            for row in reader:
                try:
                    timestamp = self.parse_datetime(row[0])
                    birthday = self.parse_date(row[5])

                    Participant.objects.update_or_create(
                        email=row[1].strip(),
                        defaults={
                            "timestamp": timestamp,
                            "first_name": row[2].strip(),
                            "last_name": row[3].strip(),
                            "preferred_name": row[4].strip(),
                            "birthday": birthday,
                            "gender": row[6].strip(),
                            "application_type": row[7].strip(),
                            "phone": row[8].strip(),
                            "guardian_name": row[9].strip(),
                            "guardian_email": row[10].strip(),
                            "guardian_phone": row[11].strip(),
                            "emergency_contact_name": row[12].strip(),
                            "emergency_contact_email": row[13].strip(),
                            "emergency_contact_phone": row[14].strip(),
                            "stake_district_mission": row[15].strip(),
                            "ward_branch": row[16].strip(),
                            "bishop": row[17].strip(),
                            "medical_info": row[18].strip(),
                            "dietary_info": row[19].strip(),
                            "requires_attention": row[20].strip(),
                            "tshirt_size": row[21].strip(),
                            "agreed_terms_text": row[22].strip(),
                        }
                    )
                except Exception as e:
                    self.stderr.write(f"❌ Error importing {row[1]}: {e}")

        self.stdout.write(self.style.SUCCESS("✅ CSV import completed successfully"))
