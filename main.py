from datetime import datetime, timezone

from pyorbital_main import print_locations_pyorbital
from skyfield_main import print_locations_skyfield
from tle_utils import TleData


if __name__ == '__main__':
    tle_1 = '1 25544U 98067A   24051.57306753  .00017164  00000-0  30622-3 0  9993'
    tle_2 = '2 25544  51.6401 178.2264 0001870 289.0710 164.3741 15.50171695440310'
    zarya_tle = TleData('ISS (ZARYA)', tle_1, tle_2)
    now = datetime.now(tz=timezone.utc)
    print("SKYFIELD:")
    print_locations_skyfield(zarya_tle, now)

    print("PYORBITAL:")
    print_locations_pyorbital(zarya_tle, now)
