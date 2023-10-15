from playground.models import Section
from playground.models import SectionName
from playground.models import Year
from playground.models import Program

sections = [
    "BSCS 1A",
    "BSCS 1B",
    "BSCS 2A",
    "BSCS 2B",
    "BSCS 3A",
    "BSCS 3B",
    "BSCS 4A",
    "BSCS 4B",
    "BSIT 1A",
    "BSIT 1B",
    "BSIT 1C",
    "BSIT 1D",
    "BSIT 1E",
    "BSIT 1F",
    "BSIT 1G",
    "BSIT 1H",
    "BSIT 2A",
    "BSIT 2B",
    "BSIT 2C",
    "BSIT 2D",
    "BSIT 2E",
    "BSIT 2F",
    "BSIT 2G",
    "BSIT 2H",
    "BSIT 3A",
    "BSIT 3B",
    "BSIT 3C",
    "BSIT 3D",
    "BSIT 3E",
    "BSIT 3F",
    "BSIT 4A",
    "BSIT 4B",
    "BSIT 4C",
    "BSIT 4D",
    "BLIS 1A",
    "BLIS 2A",
    "BLIS 3A",
    "BLIS 4A",
    "BLIS 4B",
    "BSIS 1A",
    "BSIS 1B",
    "BSIS 1C",
    "BSIS 2A",
    "BSIS 2B",
    "BSIS 2C",
    "BSIS 3A",
    "BSIS 3B",
    "BSIS 3C",
    "BSIS 4A",
    "BSIS 4B",
]


def section_seeder():
    for section in sections:
        section_list = section.split(" ")
        code = section_list[0]
        year = section_list[1][0]
        section = section_list[1][1]

        program = Program.objects.get(code=code)
        y = Year.objects.get(year=year)
        section_name = SectionName.objects.filter(name=section)

        if not section_name.exists():
            section_name = SectionName(name=section).save()
        section_name = SectionName.objects.get(name=section)

        Section(program=program, year=y, section_name=section_name).save()
