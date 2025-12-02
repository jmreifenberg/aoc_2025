from src.day02.day02 import IdDetector
from unittest.mock import MagicMock
from pathlib import Path
import csv

class TestSafeDial:
    def test_id_detection(self):
        with open(Path(__file__).parent / 'test_input.txt') as file:
            reader = csv.reader(file, delimiter=',')
            id_ranges = next(reader)
        
        id_detector = IdDetector(id_ranges)
        id_detector.check_ranges_for_invalid_ids()

        assert id_detector.invalid_ids == [11, 22, 99, 111, 999, 1010, 1188511885, 222222, 446446, 38593859, 565656, 824824824, 2121212121]
        assert sum(id_detector.invalid_ids) == 4174379265
