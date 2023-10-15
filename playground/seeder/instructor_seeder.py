from playground.models import Instructor
from playground.models import Course


instructor_data = [
    ["Ms. ", "Ichelle F. Baluis", ["Capstone Project 2"]],
    ["Ms. ", "Brenda D. Benosa", ["Methods of Research in Computing"]],
    [
        "Ms. ",
        "Kay Angeline O. Broqueza",
        ["Information Literacy", "Management of Libraries and Information Centers I"],
    ],
    ["Ms. ", "Charmane Recah V. De lima-Millano", []],
    [
        "Ms. ",
        "Kaela Marie N. Fortuno",
        [
            "Data Structures and Algorithms",
            "Algorithms and Complexity",
            "Architecture and Organization",
        ],
    ],
    [
        "Ms. ",
        "Ayra A. Gonowon",
        ["Indexing and Abstracting", "Introduction to Records Management and Archives"],
    ],
    ["Ms. ", "Leni Girlie M. Idian", []],
    [
        "Ms. ",
        "Josefina H. LLagas",
        ["Introduction to Computing", "Systems Integration and Architecture 1"],
    ],
    ["Ms. ", "Shiela Dona S. Manlapaz", ["Information Assurance and Security 1"]],
    ["Ms. ", "Rosel O. Onesa", ["Computer Science Thesis 2"]],
    [
        "Ms. ",
        "Maricris L. Ramizares",
        ["Capstone Project 2", "Systems Integration and Architecture 1"],
    ],
    [
        "Ms. ",
        "Tiffany Lyn O. Pandes",
        [
            "Software Engineering 1",
            "Fundamentals of Programming",
            "Automata Theory and Formal Languages",
        ],
    ],
    [
        "Ms. ",
        "Kezia Abegail T. Velasco",
        ["Networking 1", "Data Structures and Algorithms"],
    ],
    ["Ms. ", "Laiza Mae R. Agnote", ["Advanced Database Systems"]],
    ["Ms. ", "Ms. maria Rica B. Arce", []],
    ["Ms. ", "Suzanne S. Causapin", ["Network Security"]],
    ["Ms. ", "Cathyrine D. Chua", ["Computer Programming 1"]],
    ["Ms. ", "Karen E. Comprado", ["Quantitative Methods"]],
    ["Ms. ", "Maria Theresa B. Goleta", ["Business Process Management"]],
    [
        "Ms. ",
        "Mercy O. Gonowon",
        [
            "Systems Analysis and Design in Libraries and Information Centers",
            "Platform Security",
            "Information Processing and Handling in Libraries and Information Centers",
        ],
    ],
    ["Ms. ", "Mary France D. Raluta", ["Operating Systems"]],
    [
        "Ms. ",
        "Marivic L. Ramizares",
        ["Computer Programming 1", "Information Management 1"],
    ],
    ["Ms. ", "Mae Ann Ll. Tagum", ["Object Oriented Programming"]],
    [
        "Ms. ",
        "Rosemarie C. Vidal",
        [
            "IT Infrastructure and Network Technologies",
        ],
    ],
    [
        "Ms. ",
        "Mildred A. Volante",
        [
            "Introduction to Library and Information Science",
            "Information Resources and Services 1",
        ],
    ],
    ["Ms. ", "Joyce Arbaja", ["Information Management 1"]],
    ["Ms. ", "Mae. M. Bayobo", []],
    ["Ms. ", "Maria Daisy R. Belardo", ["Discrete Structures 2"]],
    ["Ms. ", "Kathleen May Corbito", ["Linear Algebra"]],
    ["Ms. ", "Mary Chie A. De La Cruz", ["Accounting for ITE"]],
    ["Ms. ", "Mariane Christine C. Lico", ["Professional Issues in IS"]],
    [
        "Ms. ",
        "Jillian N. Orante",
        [
            "Social issues and Professional Practice 1",
        ],
    ],
    ["Ms. ", "Jeniffer R. Sevilla", ["Preservation of Information Resources"]],
    ["Ms. ", "Elaine Mae G. Tormes", ["Foreign Language"]],
    ["Dr. ", "Ian P. Benitez", ["Systems Administration and Maintenance"]],
    ["Dr. ", "Challiz D. Omorog", ["Methods of Research in Computing"]],
    [
        "Mr. ",
        "Jonuel Rey N. Colle",
        ["Advanced Database Systems", "Distributed Database Management"],
    ],
    ["Mr. ", "Rey T. Cortez", ["Networking 1"]],
    ["Mr. ", "Niño jeffrey L. Luzon", ["IS Project Management 1"]],
    ["Mr. ", "Jeremy Jireh S. Neo", ["Enterprice Architecture"]],
    ["Mr. ", "Joseph Jessie S. Oñate", ["Introduction to Artificial Intelligence"]],
    ["Mr. ", "Freddie B. Prianes", []],
    ["Mr. ", "Vencel Angelo R. Sanglay", ["Multimedia Systems"]],
    ["Mr. ", "Philip Alger M. Serrano", []],
    ["Mr. ", "James Nicolo S. Sias", []],
    ["Ms. ", "Marilyn B. Villoso", ["Data Structures and Algorithms"]],
    ["Ms. ", "Mhelrose B. Prades", ["Introduction to Computing"]],
    ["Ms. ", "Joanna H. Estallo", ["Computer Programming 1"]],
    [
        "Mr. ",
        "Jayvee Niel S. Sias",
        ["Mobile Technology 1", "Business Process Progeramming 1"],
    ],
    [
        "Mr. ",
        "Jethro Ralph N. Abonal",
        [
            "Introduction to Computing",
            "Digital Foensics 1",
        ],
    ],
    ["Mr. ", "Kevin Von Erick D. Albania", []],
    ["Mr. ", "Jonathan Balbuena", ["Networking 2"]],
    ["Mr. ", "Guilbert Corporal", ["Computer Programming 1"]],
    [
        "Mr. ",
        "Mark Anthony S. Dancalan",
        ["Data Structures and Algorithm", "Organization and Management Concepts"],
    ],
    [
        "Mr. ",
        "Eisen Rose D. Galvante ",
        ["Multimedia Systems", "Information Management 1"],
    ],
    [
        "Mr. ",
        "Allan O. Ibo Jr.",
        [
            "Fundamentals of Programming",
            "Modelling and Simulation",
            "Defensive Programming",
        ],
    ],
    ["Mr. ", "Jay-R H. Leonidas", ["Quantitative Methods"]],
    [
        "Mr. ",
        "Mark Kenneth R. Limjoco",
        [
            "Introduction to Computing",
            "Data Structures and Algorithm",
            "Web Systems and Technologies 2",
        ],
    ],
    ["Mr. ", "Mark Joseph B. Norvadez", ["Integrative Programming and Technologies 2"]],
    ["Mr. ", "Richard F. Nonato", ["Event Driven Programming"]],
    [
        "Mr. ",
        "Noel B. Paguio Jr.",
        ["Web Systems and Technologies 2", "Information Assurance and Security 1"],
    ],
    ["Mr. ", "Leomir K. Paz", ["Object Oriented Programming"]],
    ["Mr. ", "Lawrence A. Rebulado", ["Mobile Technology 1"]],
    ["Mr. ", "Jp Remaro R. Serrano", ["Introduction to Computing"]],
    [
        "Mr. ",
        "Mark Anthony Taduran",
        [
            "Multimedia Systems",
        ],
    ],
    ["Mr. ", "Nelson P. Vargas", ["Application Development And Emerging Technologies"]],
    [
        "Mr. ",
        "Domingo J. Vinluan Jr.",
        ["Philosophies and Principles of Teaching", "Quantitative methods"],
    ],
    ["Mr. ", "Jonie M. Beriña", ["Operating System", "Database Design for Libraries"]],
    [
        "Mr. ",
        "Mark Kevin P. Candelaria",
        ["IT Infrastructure and Network Technologies", "Introduction to Computing"],
    ],
    ["Mr. ", "Vincent B. Cortez", ["Web Systems and Technologies 2"]],
    [
        "Mr. ",
        "Yves Aristeo A. Febres",
        ["Organization Of Information Resources 1", "School/Academic Librarianship"],
    ],
    ["Mr. ", "Derick S. Parañal", ["Multimedia Systems"]],
    ["Mr. ", "Leo Pol Ramos", ["Multimedia Systems"]],
    ["Mr. ", "Mae M. Bayobo", ["Educational Technology"]],
    ["Mr. ", "Janden Albalate", ["Networking 2"]],
]


def instructor_seeder():
    for title, name, expertise in instructor_data:
        for course in expertise:
            Instructor(
                name=name, expertise=Course.objects.filter(name=course).first()
            ).save()
