from django.core.management.base import BaseCommand, CommandParser

from playground.models import (
    Course,
    Instructor,
    Laboratory,
    Program,
    Section,
    SectionName,
    Year,
)
from playground.seeder.course_seeder import course_seeder
from playground.seeder.instructor_seeder import instructor_seeder
from playground.seeder.laboratory_seeder import laboratory_seeder
from playground.seeder.program_seeder import program_seeder
from playground.seeder.section_seeder import section_seeder
from playground.seeder.year_seeder import year_seeder


class Command(BaseCommand):
    help = "Seed the database"

    def add_arguments(self, parser: CommandParser) -> None:
        return (parser.add_argument("--mode", type=str, help="Mode"),)

    def handle(self, *args, **options):
        self.stdout.write("seeding data...")
        run_seed(self)
        self.stdout.write("done.")


def clear_data():
    Program.objects.all().delete()
    Year.objects.all().delete()
    SectionName.objects.all().delete()
    Section.objects.all().delete()
    Course.objects.all().delete()
    Laboratory.objects.all().delete()
    Instructor.objects.all().delete()


def seed():
    program_seeder()
    year_seeder()
    section_seeder()
    course_seeder()
    laboratory_seeder()
    instructor_seeder()


def run_seed(self):
    clear_data()
    seed()
