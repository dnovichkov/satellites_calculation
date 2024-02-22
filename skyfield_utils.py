from datetime import datetime, timezone, timedelta

from skyfield.api import EarthSatellite, load, wgs84, Topos

from tle_utils import TleData


def print_locations_skyfield(tle: TleData, time_point):
    now = load.timescale().from_datetime(time_point)
    satellite = EarthSatellite(tle.tle_1, tle.tle_2, tle.name, load.timescale())
    geocentric = satellite.at(now)
    # print(geocentric.position.km)

    lat, lon = wgs84.latlon_of(geocentric)
    print('Latitude:', lat)
    print('Longitude:', lon)


def print_locations_range_skyfield(tle: TleData, time_start, time_end, step_in_secs):
    ts = load.timescale()
    satellite = EarthSatellite(tle.tle_1, tle.tle_2, tle.name, ts)
    while time_start <= time_end:
        # TODO: Check this method - it can be slow
        now = ts.from_datetime(time_start)
        geocentric = satellite.at(now)
        # print(geocentric.position.km)

        lat, lon = wgs84.latlon_of(geocentric)
        # print('Latitude:', lat)
        # print('Longitude:', lon)
        print(f'{time_start=}, {lat=}, {lon=}')
        time_start += timedelta(seconds=step_in_secs)


def print_observations_skyfield(tle: TleData, time_start, time_end, latitude_degrees, longitude_degrees):
    # https://rhodesmill.org/skyfield/api-satellites.html
    observer = Topos(latitude_degrees=latitude_degrees, longitude_degrees=longitude_degrees)
    ts = load.timescale()
    satellite = EarthSatellite(tle.tle_1, tle.tle_2, tle.name, ts)
    # Поиск временных интервалов пролета
    start = ts.from_datetime(time_start)
    end = ts.from_datetime(time_end)
    t, events = satellite.find_events(observer, start, end, altitude_degrees=10)

    # Вывод временных интервалов
    for ti, event in zip(t, events):
        name = ('Start', 'culminate', 'Finish')[event]
        print(ti.utc_datetime(), name)


if __name__ == '__main__':
    # https://rhodesmill.org/skyfield/earth-satellites.html

    tle_1 = '1 25544U 98067A   24051.57306753  .00017164  00000-0  30622-3 0  9993'
    tle_2 = '2 25544  51.6401 178.2264 0001870 289.0710 164.3741 15.50171695440310'
    zarya_tle = TleData('ISS (ZARYA)', tle_1, tle_2)
    start_time = datetime.now(tz=timezone.utc)
    print_locations_skyfield(zarya_tle, start_time)
    london_coords = (51.5074, 0.1278)
    print_observations_skyfield(zarya_tle, start_time, start_time + timedelta(days=1),
                                london_coords[0], london_coords[1])
