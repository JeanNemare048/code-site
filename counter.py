#!/usr/bin/env python3
import sys
import time
import signal
import random

duration = 60

counterNumber = 0
TorF = False
heads = "Heads"
tails = "Tails"

def _timeout_handler(signum, frame):
    raise TimeoutError

signal.signal(signal.SIGALRM, _timeout_handler)

try:
    while True:
        try:
            # Arm the inactivity alarm before waiting for input.
            signal.alarm(duration)
            line = input("cmd:").strip()
            # Cancel the alarm immediately after input is received.
            signal.alarm(0)
        except TimeoutError:
            # Alarm fired due to inactivity.
            break
        except EOFError:
            break

        if line.lower() == "end":
            print("Exiting.")
            sys.exit()

        if not line:
            print("Empty input.")
            continue

        if line.lower() == "true":
            TorF = True
            print(f"Counter: {counterNumber}, TrueFalse: {TorF}")
            continue
        elif line.lower() == "false":
            TorF = False
            print(f"Counter: {counterNumber}, TrueFalse: {TorF}")
            continue

        # RNG command — choose mode: cf (coin flip), int (random int min..max), float (random float min..max)
        if line.lower() == "rng":
            print("what rng mode? (cf/number):")
            mode = input().strip().lower()
            if mode in ("cf", "coin"):
                rand_face = random.choice([heads, tails])
                print(f"Random choice: {rand_face}")
                continue

            if mode == "":
                mode = "number"

            # Ask for both bounds
            print("lowest value?:")
            low_val = input().strip()
            print("highest value?:")
            high_val = input().strip()

            try:
                if mode == "number":
                    low = int(low_val)
                    high = int(high_val)
                elif mode == "float":
                    low = float(low_val)
                    high = float(high_val)
                else:
                    print("Unknown RNG mode.")
                    continue
            except ValueError:
                print("Invalid bounds.")
                continue

            # Ensure low <= high
            if low > high:
                low, high = high, low

            if mode == "number":
                rand_num = random.randint(low, high)
            else:  # float
                rand_num = random.uniform(low, high)

            print(f"Random number ({mode}): {rand_num}")
            continue

        first = line[0].upper()   # P or M (case-insensitive)
        rest_str = line[1:].strip()   # everything after the first letter

        if rest_str == "":
            rest = 1
        else:
            try:
                rest = int(rest_str)
            except ValueError:
                try:
                    rest = float(rest_str)
                except ValueError:
                    print("Invalid number after command.")
                    continue

        if first == "P":
            counterNumber += rest
        elif first == "M":
            counterNumber -= rest
        else:
            print("First character is neither P nor M.")
        print(f"Counter: {counterNumber}, TrueFalse: {TorF}")
        continue
finally:
    signal.alarm(0)

print("\nStopped because of inactivity.")
print("\nFinal State:", counterNumber, TorF)
sys.exit()
