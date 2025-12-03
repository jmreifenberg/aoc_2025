from src.day03.day03 import JoltageFinder
from pathlib import Path

class TestSafeDial:
    def test_init(self):
        joltage_finder = JoltageFinder(Path(__file__).parent / 'test_input.txt')
        assert joltage_finder.battery_banks == [
            '987654321111111',
            '811111111111119',
            '234234234234278',
            '818181911112111'
        ]
    
    def test_calculate_max_joltages(self):
        joltage_finder = JoltageFinder(Path(__file__).parent / 'test_input.txt')
        joltage_finder.calculate_max_joltages()
        assert joltage_finder.max_joltages == [987654321111, 811111111119, 434234234278, 888911112111]
        assert sum(joltage_finder.max_joltages) == 3121910778619
