import csv

class SafeDial:
    position: int
    key_positions: list[int] = []

    def __init__(self, position = 50):
        self.position = position

    def rotate(self, rotation_str: str):
        direction = rotation_str[0]
        amount = int(rotation_str[1:]) 

        full_rotations = int(amount / 100)
        self.append_full_rotations(full_rotations, rotation_str)

        effective_amount = amount % 100
        
        if direction == 'L':
            self.rotate_left(effective_amount)
        else:
            self.rotate_right(effective_amount)

    def append_full_rotations(self, amount, position):
        for i in range(amount):
            self.key_positions.append(position)

    def rotate_right(self, amount: int):
        tmp_position = self.position + amount
        if tmp_position > 99:
            self.key_positions.append(f'R{amount}')
            tmp_position = tmp_position - 100
        self.position = tmp_position

    def rotate_left(self, amount: int):
        tmp_position = self.position - amount
        if tmp_position < 0:
            self.key_positions.append(f'L{amount}') if self.position != 0 else None
            tmp_position = tmp_position + 100
        if tmp_position == 0:
            self.key_positions.append(f'L{amount}')
        self.position = tmp_position

if __name__ == '__main__':
    safeDial = SafeDial()
    with open('/home/jreifenberg/advent_of_code_2025/day01/src/input.txt') as file:
        reader = csv.reader(file)
        for row in reader:
            safeDial.rotate(row[0])
    print(safeDial.key_positions)
    print(len(safeDial.key_positions))