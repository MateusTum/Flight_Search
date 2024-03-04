from flights.models import City, Airport
from django.db.models import Min
import datetime
from bs4 import BeautifulSoup

# This file is just for devlopment purposes
def add_stuff(request):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for letter in letters:

        url = f"https://en.wikipedia.org/wiki/List_of_airports_by_IATA_airport_code:_{letter}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        airports = {}
        for row in soup.findAll("tr"):
            cells = row.findAll("td")
            if len(cells) > 1:
                iata_code = cells[0].text.strip()
                airport_name = cells[2].text.strip()

                airport_location = cells[3].text.strip()
                parts = airport_location.split(',')
                first_word = parts[0].strip()
                last_word = parts[-1].strip()

                airports[iata_code] = {'name': airport_name, 'location': {'city': first_word, 'country': last_word}}

        html = f"<html><body>added stuff</body></html>"

        my_url = 'http://localhost:8000/flights/cities/'

        city_instances = [
        City(name=info['location']['city'], country=info['location']['country'])
        for iata_code, info in airports.items()
        ]
        City.objects.bulk_create(city_instances)

        # Identify the IDs of the first city for each name to keep
        cities_to_keep = City.objects.values('name').annotate(min_id=Min('id')).values('min_id')
        # Delete cities whose ID is not in the list of IDs to keep
        City.objects.exclude(id__in=cities_to_keep).delete()

        data_instances = [
        Airport(iata_code=iata_code, name=info['name'], city=City.objects.get(name=info['location']['city']))
        for iata_code, info in airports.items()
        ]
        Airport.objects.bulk_create(data_instances)


        return HttpResponse(html)