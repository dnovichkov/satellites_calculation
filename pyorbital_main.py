from pyorbital.orbital import Orbital
from datetime import datetime


def simplest_satellite_position():
    orb = Orbital("noaa 18")
    now = datetime.utcnow()

    # Get normalized position and velocity of the satellite:
    print("current_position: ", orb.get_position(now))

    # Get longitude, latitude and altitude of the satellite:
    print("current_lot_lang_alt: ", orb.get_lonlatalt(now))


if __name__ == '__main__':
    simplest_satellite_position()
