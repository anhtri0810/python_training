from random import choice
from time import perf_counter

pas = input("send the password: ")
keys = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z', '@', '!', '#', '$', '%',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

pwg = ""
attempts = 0
start_time = perf_counter()

for target in pas:
    while True:
        guess = choice(keys)
        attempts += 1

        if guess == target:
            pwg += guess
            break

    print(f"Found: {pwg}")

total_time = perf_counter() - start_time

print("\n========== RESULT ==========")
print(f"The pass is: {pwg}")
print(f"Total Attempts: {attempts:,}")
print(f"Time taken: {total_time:.6f} seconds")
