from playground.models import Year


def year_seeder():
    for year in range(1, 5):
        Year(year=year).save()
