from pyorbital.orbital import Orbital
from datetime import datetime


def simplest_satellite_position():
    """
    https://pyorbital.readthedocs.io/en/feature-moon-phase/satellite_position.html
    :return:
    """
    orb = Orbital("noaa 18")
    now = datetime.utcnow()

    # Get normalized position and velocity of the satellite:
    print("current_position: ", orb.get_position(now))

    # Get longitude, latitude and altitude of the satellite:
    print("current_lot_lang_alt: ", orb.get_lonlatalt(now))


def get_iss_projection():
    # https://live.ariss.org/tle/ - ISS (ZARYA)
    tle_1 = '1 25544U 98067A   24051.57306753  .00017164  00000-0  30622-3 0  9993'
    tle_2 = '2 25544  51.6401 178.2264 0001870 289.0710 164.3741 15.50171695440310'
    # Нас интересует текущий момент времени
    utc_time = datetime.utcnow()

    orb = Orbital("N", line1=tle_1, line2=tle_2)
    # Get normalized position and velocity of the satellite:
    print("current_position: ", orb.get_position(utc_time))
    # Get longitude, latitude and altitude of the satellite:
    print("current_lot_lang_alt: ", orb.get_lonlatalt(utc_time))
    # Compare with: https://spacegid.com/media/iss_tracker/


if __name__ == '__main__':
    # simplest_satellite_position()
    get_iss_projection()
