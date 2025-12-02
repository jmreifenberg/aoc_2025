from pathlib import Path
import csv

class IdDetector:
    id_ranges: list[str]
    invalid_ids: list[int]
    
    def __init__(self, id_ranges: list[str]):
        self.id_ranges = id_ranges
        self.invalid_ids = []

    def check_ranges_for_invalid_ids(self):
        for range in self.id_ranges:
            start_end_id = range.split('-')
            start_id, end_id = int(start_end_id[0]), int(start_end_id[1])
            self.check_range_for_invalid_ids(start_id, end_id)

    def check_range_for_invalid_ids(self, start_id: int, end_id: int):
        for id in range(start_id, end_id + 1):
            if self.is_invalid_id(id):
                self.invalid_ids.append(id)
    
    def is_invalid_id(self, id):
        str_id = str(id)
        mid_index = int(len(str_id) / 2) + 1
        
        for chunk_length in range(1, mid_index):
            id_chunks = self.get_id_chunks(str_id, chunk_length)
            if len(set(id_chunks)) == 1:
                return True

        return False
    
    @staticmethod
    def get_id_chunks(str_id: str, chunk_length: int):
        id_chunks = []
        for i in range(len(str_id)):
            chunk = str_id[i*chunk_length:i*chunk_length+chunk_length]
            if chunk != '':
                id_chunks.append(chunk)
        return id_chunks

if __name__ == '__main__':
    with open(Path(__file__).parent / 'input.txt') as file:
        reader = csv.reader(file, delimiter=',')
        id_ranges = next(reader)
    
    id_detector = IdDetector(id_ranges)
    id_detector.check_ranges_for_invalid_ids()
    print(sum(id_detector.invalid_ids)) 
