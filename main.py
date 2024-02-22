from datetime import datetime, timezone, timedelta

from pyorbital_main import print_locations_pyorbital, print_locations_range_pyorbital
from skyfield_main import print_locations_skyfield, print_locations_range_skyfield
from tle_utils import TleData


def calculate_iss_pyorbital(tle: TleData, time_point, count):
    for _ in range(count):
        print_locations_pyorbital(tle, time_point)


def calculate_iss_skyfield(tle: TleData, time_point, count):
    for _ in range(count):
        print_locations_skyfield(tle, time_point)


if __name__ == '__main__':
    tle_1 = '1 25544U 98067A   24053.24726206  .00018436  00000-0  32753-3 0  9998'
    tle_2 = '2 25544  51.6401 169.9296 0002171 300.6974 142.1526 15.50235092440574'
    zarya_tle = TleData('ISS (ZARYA)', tle_1, tle_2)
    now = datetime.now(tz=timezone.utc)
    range_end = now + timedelta(seconds=3600)
    print("SKYFIELD:")
    print_locations_skyfield(zarya_tle, now)

    print("PYORBITAL:")
    print_locations_pyorbital(zarya_tle, now)

    # start_pyorbital = datetime.now()
    # calculate_iss_pyorbital(zarya_tle, now, 10000)
    # end_pyorbital = datetime.now()
    # pyorbital_delta = end_pyorbital - start_pyorbital
    #
    # start_skyfield = datetime.now()
    # calculate_iss_skyfield(zarya_tle, now, 10000)
    # end_skyfield = datetime.now()
    # skyfield_delta = end_skyfield - start_skyfield
    # print(f'{pyorbital_delta=}, {skyfield_delta=}')

    start_pyorbital = datetime.now()
    print_locations_range_pyorbital(zarya_tle, now, range_end, 60)
    end_pyorbital = datetime.now()
    pyorbital_range_delta = end_pyorbital - start_pyorbital
    print(f'{pyorbital_range_delta=}')

    start_skyfield = datetime.now()
    print_locations_range_skyfield(zarya_tle, now, range_end, 10)
    end_skyfield = datetime.now()
    skyfield_range_delta = end_skyfield - start_skyfield
    print(f'{skyfield_range_delta=}')
    print(f'{pyorbital_range_delta=}, {skyfield_range_delta=}')
