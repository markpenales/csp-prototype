from playground.models import Laboratory

laboratories = {
    "Acad 1 - 103": None,
    "Acad 1 - 104": None,
    "Room 1": None,
    "Room 2": None,
    "Room 3": None,
    "Room 4": None,
    "MAC Lab": ["Multimedia Systems", "Mobile Technology 1"],
    "IT Lab 1": [
        "Data Structures and Algorithms",
        "Advanced Database Systems",
        "Information Management 1",
    ],
    "IT Lab 2": [
        "Data Structures and Algorithms",
        "Advanced Database Systems",
        "Information Management 1",
    ],
    "NAS Lab": [
        "Networking 1",
        "Networking 2",
    ],
    "CS Lab": ["Digital Forensics 1", "Introduction to Computing"],
    "RISE Lab": ["Introduction to Artificial Intelligence", "Operating System"],
    "ERP Lab": None,
    "LIS Lab": [
        "Introduction to Library and Information Science",
        "Database Design for Libraries",
        "Preservation of Information Resources",
    ],
    "Open Lab": ["Computer Science Thesis 2"],
    "Field": None,
}


def laboratory_seeder():
    for lab, courses in laboratories.items():
        Laboratory(
            name=lab,
            course=f"{', '.join(courses).split(', ') if courses is not None else ''}",
        ).save()
