from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


@dataclass
class TleData:
    name: str
    id: int
    tle_1: str
    tle_2: str


@dataclass
class EarthObject:
    name: str
    id: int
    latitude: float
    longitude: float
    altitude: float
    angle: float


@dataclass
class Passage:
    space_object_id: int
    earth_object_id: int
    start: datetime
    end: datetime
    distance: float
    angle: float
    velocity: float


def get_tle_data(filename: str) -> List[TleData]:
    result: List[TleData] = []
    with open(filename, encoding='utf-8') as fp:
        lines = [line.rstrip() for line in fp]
        lines_count = len(lines)
        if lines_count % 3:
            print(f'!!! Странное число строк в файле - {lines_count}')
            return []
        for i in range(0, lines_count, 3):
            name = lines[i]
            tle_1 = lines[i + 1]
            tle_2 = lines[i + 2]
            result.append(TleData(name, tle_1, tle_2))
    return result


def get_data_by_name(name: str, all_tle: List[TleData]) -> Optional[TleData]:
    for tle in all_tle:
        if name == tle.name:
            return tle
    return None


if __name__ == '__main__':
    all_data = get_tle_data('tle_catalog.txt')
    print(all_data)
    zarya_tle = get_data_by_name('ISS (ZARYA)', all_data)
    print(zarya_tle)
    empty_tle = get_data_by_name('SOME_NAME', all_data)
    print(empty_tle)
