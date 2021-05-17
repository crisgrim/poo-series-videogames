from TvSeries import TvSeries
from Videogame import VideoGame


# Create array with series
def prepare_series():
    bb = TvSeries('Breaking Bad', 5, 'Crime', 'Vince Gilligan')
    tt = TvSeries('True detective', 3, 'Mistery', 'Nic Pizzolatto')
    gt = TvSeries('Game of thrones', 8, 'Drama', 'David Benioff & D.B. Weiss')
    sh = TvSeries('Sherlock', 4, 'Mistery', 'Mark Gatiss & Steven Moffat')
    fa = TvSeries('Fargo', 4, 'Crime', 'Noah Hawley')

    return [bb, tt, gt, sh, fa]


# Create array with videogames
def prepare_videogames():
    fa = VideoGame('Fallout 4', 100, 'Role', 'Bethesda')
    sk = VideoGame('Skyrim', 200, 'Role', 'Bethesda')
    bi = VideoGame('Bioshock', 40, 'First person', 'Irrational games')
    hk = VideoGame('Hollow Knight', 40, 'Action adventure', 'Team Cherry')
    mo = VideoGame('Mario Odissey', 40, 'Adventure', 'Nintendo')

    return [fa, sk, bi, hk, mo]


# Execute deliver method to change the borrowed property
def deliver_items(items):
    items[2].deliver()
    items[4].deliver()
    items[8].deliver()
    items[9].deliver()


# Check if item is delivered
def check_delivered_status(item):
    return item.is_delivered


# Count delivered items and return them
def count_delivered_items(series, videogames):
    delivered_series = list(filter(check_delivered_status, series))
    delivered_videogames = list(filter(check_delivered_status, videogames))

    print(f' Hay {len(delivered_series)} series entregadas')
    print(f' Hay {len(delivered_videogames)} juegos entregados')

    return delivered_series, delivered_videogames


# Check which is the highest item base on compare_to() method
def check_highest(items):
    highest = None
    for index, item in enumerate(items):
        if index == 0:
            highest = item

        if item.compare_to(highest):
            highest = item

    return highest


# Check highest items and display them
def display_highest(series, videogames):
    highest_serie = check_highest(series)
    highest_videogame = check_highest(videogames)

    print(f' La serie con mayor número de temporadas es: \n  - {highest_serie}')
    print(f' El videojuego con mayor estimación de horas es: \n  - {highest_videogame}')


# Run all methods needed in this application
def run_application():
    series = prepare_series()
    videogames = prepare_videogames()

    deliver_items(series + videogames)
    count_delivered_items(series, videogames)

    display_highest(series, videogames)


if __name__ == '__main__':
    run_application()
