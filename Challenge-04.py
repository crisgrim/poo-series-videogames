class TvSeries():
    # Properties
    title = ''
    seasons = 3
    genre = ''
    creator = ''
    delivered = False

    # Constructor
    def __init__(self, title, seasons, genre, creator):
        self.title = title
        self.seasons = seasons
        self.genre = genre
        self.creator = creator

    # Magic method
    def __str__(self):
        return f'Title: {self.title}, Seasons: {self.seasons}, Genre: {self.genre}, Creator: {self.creator}'

    # Getters / Setters
    @property
    def title(self):
        return self.title

    @property
    def seasons(self):
        return self.seasons

    @property
    def genre(self):
        return self.genre

    @property
    def creator(self):
        return self.creator

    @title.setter
    def title(self, title):
        self.title = title

    @seasons.setter
    def seasons(self, seasons):
        self.seasons = seasons

    @genre.setter
    def genre(self, genre):
        self.genre = genre

    @creator.setter
    def creator(self, creator):
        self.creator = creator


class VideoGame():
    # Properties
    title = ''
    estimated_hours = 10
    genre = ''
    company = ''
    delivered = False

    # Constructor
    def __init__(self, title, estimated_hours, genre, company):
        self.title = title
        self.estimated_hours = estimated_hours
        self.genre = genre
        self.company = company

    # Magic method
    def __str__(self):
        return f'Title: {self.title},' \
               f'Estimated hours: {self.estimated_hours},' \
               f'Genre: {self.genre},' \
               f'Company: {self.company} '

    # Getters / Setters
    @property
    def title(self):
        return self.title

    @property
    def estimated_hours(self):
        return self.estimated_hours

    @property
    def genre(self):
        return self.genre

    @property
    def company(self):
        return self.company

    @title.setter
    def title(self, title):
        self.title = title

    @estimated_hours.setter
    def estimated_hours(self, estimated_hours):
        self.estimated_hours = estimated_hours

    @genre.setter
    def genre(self, genre):
        self.genre = genre

    @company.setter
    def company(self, company):
        self.company = company


class Deliverable():
    # Properties
    borrowed = False

    # Getters / Setters
    @property
    def is_delivered(self):
        return self.borrowed

    # Methods
    def deliver(self):
        self.borrowed = True

    def give_back(self):
        self.borrowed = False

series = []
bb_serie = TvSeries('Breaking Bad', 5, 'Crime', 'Vince Gilligan')
# tt_serie = TvSeries('True detective', 3, 'Mistery', 'Nic Pizzolatto')
# gt_serie = TvSeries('Game of thrones', 8, 'Drama', 'David Benioff & D.B. Weiss')
# sh_serie = TvSeries('Sherlock', 4, 'Mistery', 'Mark Gatiss & Steven Moffat')
# fa_serie = TvSeries('Fargo', 4, 'Crime', 'Noah Hawley')

print(bb_serie)
# series.append(bb_serie)
# series.append(tt_serie)
# series.append(gt_serie)
# series.append(sh_serie)
# series.append(fa_serie)
#
# videogames = []
# fallout = VideoGame('Fallout 4', 100, 'Role', 'Bethesda')
# skyrim = VideoGame('Skyrim', 200, 'Role', 'Bethesda')
# bioshock = VideoGame('Bioshock', 40, 'First person', 'Irrational games')
# hollow_night = VideoGame('Hollow Knight', 40, 'Action adventure', 'Team Cherry')
# mario_odissey = VideoGame('Mario Odissey', 40, 'Adventure', 'Nintendo')
#
# print(fallout)
# videogames.append(fallout)
# videogames.append(skyrim)
# videogames.append(bioshock)
# videogames.append(hollow_night)
# videogames.append(mario_odissey)
