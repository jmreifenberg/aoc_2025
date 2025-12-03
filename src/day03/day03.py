from pathlib import Path
import csv

class JoltageFinder:
    max_joltages: list[int]
    battery_banks: list[str]

    def __init__(self, file_path: Path):
        self.battery_banks = []
        with open(file_path) as file:
            reader = csv.reader(file)
            for row in reader:
                self.battery_banks.append(row[0])

    def calculate_max_joltages(self):
        self.max_joltages = []
        for bank in self.battery_banks:
            self.max_joltages.append(self.calculate_max_joltage(bank))
    
    def calculate_max_joltage(self, battery_bank: str):
        joltages = [int(joltage) for joltage in battery_bank]
        bank_length = len(joltages)
        
        num_unused_digits = 0
        current_digit_index = 0

        joltage = ""

        for digit in joltages:
            max_index_for_digit = bank_length - (12 + num_unused_digits) + current_digit_index + 1
            if digit == max(joltages[current_digit_index:max_index_for_digit]) or bank_length - num_unused_digits == 12:
                joltage += str(digit) if len(joltage) < 12 else ""
            else:
                num_unused_digits += 1
            current_digit_index += 1
        return int(joltage)
    


if __name__ == '__main__':
    joltage_finder = JoltageFinder(Path(__file__).parent / 'input.txt')
    joltage_finder.calculate_max_joltages()
    print(sum(joltage_finder.max_joltages)) 
