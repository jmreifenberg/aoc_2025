from src.day01.day01 import SafeDial
from unittest.mock import MagicMock
from pathlib import Path
import csv

class TestSafeDial:
    def test_rotate_direction(self):
        safeDial = SafeDial()
        safeDial.rotate_left = MagicMock()
        safeDial.rotate_right = MagicMock()

        safeDial.rotate('L42')
        safeDial.rotate('R67')

        safeDial.rotate_left.assert_called_once_with(42)
        safeDial.rotate_right.assert_called_once_with(67)
    
    def test_password_detection(self):
        safeDial = SafeDial()
        with open(Path(__file__).parent / 'test_input.txt') as file:
            reader = csv.reader(file)
            for row in reader:
                safeDial.rotate(row[0])
        assert len(safeDial.key_positions) == 6
