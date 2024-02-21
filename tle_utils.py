from dataclasses import dataclass
from typing import List


@dataclass
class TleData:
    name: str
    tle_1: str
    tle_2: str


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


if __name__ == '__main__':
    all_data = get_tle_data('tle_catalog.txt')
    print(all_data)
