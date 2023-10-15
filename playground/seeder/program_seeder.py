from playground.models import Program

programs = {
    "BSCS": "Bachelor of Science in Computer Science",
    "BSIT": "Bachelor of Science in Information Technology",
    "BSIS": "Bachelor of Science in Information Science",
    "BLIS": "Bachelor of Library and Information Science",
}


def program_seeder():
    for code, program in programs.items():
        Program(name=program, code=code).save()
