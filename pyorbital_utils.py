from datetime import datetime, timezone, timedelta
import typing
from pyorbital.orbital import Orbital

from tle_utils import TleData, EarthObject, Passage


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


def print_locations_pyorbital(tle: TleData, time_point):
    orb = Orbital(tle.name, line1=tle.tle_1, line2=tle.tle_2)
    # Get normalized position and velocity of the satellite:
    print("current_position: ", orb.get_position(time_point))
    # Get longitude, latitude and altitude of the satellite:
    print("current_lot_lang_alt: ", orb.get_lonlatalt(time_point))
    # Compare with: https://spacegid.com/media/iss_tracker/


def print_locations_range_pyorbital(tle: TleData, time_start, time_end, step_in_secs):
    orb = Orbital(tle.name, line1=tle.tle_1, line2=tle.tle_2)
    while time_start <= time_end:
        # Get normalized position and velocity of the satellite:
        # print("current_position: ", orb.get_position(time_start))
        # # Get longitude, latitude and altitude of the satellite:
        # print("current_lot_lang_alt: ", orb.get_lonlatalt(time_start))
        lon, lat, alt = orb.get_lonlatalt(time_start)
        print(f'{time_start=}, {lat=}, {lon=}')
        time_start += timedelta(seconds=step_in_secs)
    # Compare with: https://spacegid.com/media/iss_tracker/


def print_observations_pyorbital(tle: TleData, time_start, time_end, latitude_degrees, longitude_degrees):
    orb = Orbital(tle.name, line1=tle.tle_1, line2=tle.tle_2)
    result = orb.get_next_passes(time_start, 24, longitude_degrees, latitude_degrees, 0)
    for rec in result:
        print(rec[0], 'Start')
        print(rec[2], 'culminate')
        print(rec[1], 'Finish')
    # delta_time = timedelta(minutes=1)  # Шаг времени для проверки пролета (в данном случае - минута)
    #
    # # Находим временные интервалы пролета
    # while time_start < time_end:
    #     lon, lat, alt = orb.get_lonlatalt(time_start)
    #
    #     # Проверяем, находится ли космический аппарат над указанным районом
    #     if abs(lat - latitude_degrees) < 10 and abs(lon - longitude_degrees) < 10:
    #         print("Космический аппарат находится над указанным районом в", time_start)
    #
    #     time_start += delta_time


def get_passages(tle: TleData, earth_object: EarthObject,
                 time_start: datetime.datetime, time_end: datetime.datetime) -> typing.List[Passage]:
    result = []

    return result


if __name__ == '__main__':
    # simplest_satellite_position()
    # get_iss_projection()
    # all_data = get_tle_data('tle_catalog.txt')
    # zarya_tle = get_data_by_name('ISS (ZARYA)', all_data)
    tle_1 = '1 25544U 98067A   24051.57306753  .00017164  00000-0  30622-3 0  9993'
    tle_2 = '2 25544  51.6401 178.2264 0001870 289.0710 164.3741 15.50171695440310'
    zarya_tle = TleData('ISS (ZARYA)', tle_1, tle_2)

    start_time = datetime.now(tz=timezone.utc)
    # print_locations_pyorbital(zarya_tle, start_time)

    london_coords = (51.5074, 0.1278)
    print_observations_pyorbital(zarya_tle, start_time, start_time + timedelta(days=1),
                                 london_coords[0], london_coords[1])
