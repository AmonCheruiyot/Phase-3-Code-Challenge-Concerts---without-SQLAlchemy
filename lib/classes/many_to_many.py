# band.py
class Band:
    def __init__(self, name, hometown):
        self._name = name
        self._hometown = hometown
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        else:
            raise ValueError("Name must be a non-empty string.")

    @property
    def hometown(self):
        return self._hometown

    @property
    def concerts(self):
        return self._concerts

    def play_in_venue(self, venue, date):
        new_concert = Concert(date, self, venue)
        self._concerts.append(new_concert)
        venue.concerts.append(new_concert)
        return new_concert

    def all_introductions(self):
        introductions = []
        for concert in self._concerts:
            introductions.append(concert.introduction())
        return introductions

    def venues(self):
        venues_set = set()
        for concert in self._concerts:
            venues_set.add(concert.venue)
        return list(venues_set)

# venue.py
class Venue:
    def __init__(self, name, city):
        self._name = name
        self._city = city
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        else:
            raise ValueError("Name must be a non-empty string.")

    @property
    def city(self):
        return self._city

    @property
    def concerts(self):
        return self._concerts

    def concert_on(self, date):
        for concert in self._concerts:
            if concert.date == date:
                return concert
        return None

    def bands(self):
        bands_set = set()
        for concert in self._concerts:
            bands_set.add(concert.band)
        return list(bands_set)

    def concert_on(self, date):
        for concert in self._concerts:
            if concert.date == date:
                return concert
        return None

    def concerts_on_date(self, date):
        concerts_on_date = []
        for concert in self._concerts:
            if concert.date == date:
                concerts_on_date.append(concert)
        return concerts_on_date

# concert.py
class Concert:
    def __init__(self, date, band, venue):
        self._date = date
        self._band = band
        self._venue = venue

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, new_date):
        if isinstance(new_date, str) and len(new_date) > 0:
            self._date = new_date
        else:
            raise ValueError("Date must be a non-empty string.")

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, new_band):
        self._band = new_band

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, new_venue):
        self._venue = new_venue

    def hometown_show(self):
        return self.venue.city == self.band.hometown

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"