# Lotto 번호 생성기
import time
from datetime import datetime
import random


def produce():

    start_time = time.time()

    total_number = []

    while len(total_number) < 5:
        
        chosen_number = []

        while len(chosen_number) < 6:       
            num = random.randrange(1, 46)
            if num in chosen_number:
                continue
            chosen_number.append(num)
            
        chosen_number.sort()
        total_number.append(chosen_number)


    for i, num in enumerate(total_number):
        print(f'{i+1} 번째 테이블', num)

    end_time = time.time()
    print(f'time: {end_time-start_time}')
    print(f"today:{datetime.now()}")


if __name__ == "__main__":
    produce()