#!/usr/bin/env python3
"""
Simple CLI slot machine (no real money).
- 3 reels, configurable symbols
- slow reveal: symbols displayed one after another with a short delay
- betting and credits
- `--demo` mode shows a deterministic spin for testing

Usage:
  python3 slot_machine.py        # interactive play
  python3 slot_machine.py --demo # single deterministic demo spin

Controls in interactive mode:
- type a bet amount (integer <= credits)
- type 'quit' or 'end' to exit
"""
import argparse
import random
import sys
import time

SYMBOLS = ['🍒', '🍋', '🔔', '⭐', '7', '🍊']

# Default payout multipliers (multiply the bet). You can customize these at start.
DEFAULT_PAYOUTS = {
    '🍊': {'two': 1.2, 'three': 7},
    '🍋': {'two': 1.5, 'three': 8},
    '🍒': {'two': 2, 'three': 10},
    '🔔': {'two': 4, 'three': 12},
    '⭐': {'two': 5, 'three': 15},
    '7':   {'two': 10, 'three': 500},
}

def slow_reveal(reels, delay=0.6):
    """Print each reel symbol with a delay so it looks like a slot machine revealing."""
    out = []
    for i, s in enumerate(reels, start=1):
        # show partial placeholders for unrevealed reels
        placeholders = ['[ ]'] * len(reels)
        for j in range(i-1):
            placeholders[j] = reels[j]
        print('\r' + ' '.join(placeholders), end='', flush=True)
        time.sleep(delay)
    # final show
    print('\r' + ' '.join(reels))


def payout(bet, reels, payouts=DEFAULT_PAYOUTS):
    """Return payout (credits) based on reels result and payout multipliers.

    - three of a kind: use payouts[symbol]['three'] * bet
    - two of a kind: use payouts[symbol]['two'] * bet (symbol is the one that appears twice)
    - else: 0
    """
    # count symbols
    counts = {}
    for s in reels:
        counts[s] = counts.get(s, 0) + 1
    # three of a kind
    for sym, cnt in counts.items():
        if cnt == 3:
            mult = payouts.get(sym, {}).get('three', 0)
            return int(bet * mult)
    # two of a kind
    for sym, cnt in counts.items():
        if cnt == 2:
            mult = payouts.get(sym, {}).get('two', 0)
            return int(bet * mult)
    return 0


def spin_random(chambers=SYMBOLS):
    return [random.choice(chambers) for _ in range(3)]


def demo_spin():
    # deterministic example: pick some fixed values
    return ['7', '7', '7']


def interactive_loop(starting_credits=1000):
    credits = starting_credits
    print(f"Welcome to the slot machine — start with {credits} credits.")
    print("Type 'end' or 'quit' to exit anytime.")
    # Ask the player if they really want to play (must answer 'oui' or 'non')
    while True:
        start_ans = input("veut-tu vraiment jouer?: ").strip().lower()
        if start_ans == 'oui':
            break
        if start_ans == 'non':
            print("D'accord, à la prochaine.")
            return credits
        print("oui ou non?")
    # Ask whether to customize payouts
    payouts = DEFAULT_PAYOUTS.copy()
    customize = 'n'
    if customize in ('o', 'y'):
        print("Entrez les multiplicateurs pour chaque symbole. Exemple: pour 2 cerises tapez 3 pour 3x la mise.")
        for sym in SYMBOLS:
            # two-of-a-kind
            while True:
                val = input(f"Multiplicateur pour 2x {sym} (actuel {payouts.get(sym, {}).get('two')}) > ").strip()
                if val == '':
                    break
                try:
                    two = float(val)
                    payouts.setdefault(sym, {})['two'] = two
                    break
                except ValueError:
                    print("Entrée invalide — entrez un nombre (ex: 2 ou 2.5) ou rien pour garder la valeur actuelle.")
            # three-of-a-kind
            while True:
                val = input(f"Multiplicateur pour 3x {sym} (actuel {payouts.get(sym, {}).get('three')}) > ").strip()
                if val == '':
                    break
                try:
                    three = float(val)
                    payouts.setdefault(sym, {})['three'] = three
                    break
                except ValueError:
                    print("Entrée invalide — entrez un nombre (ex: 10) ou rien pour garder la valeur actuelle.")
    while True:
        print(f"\nCredits: {credits}")
        if credits <= 0:
            print("No credits left. Game over.")
            break
        bet_raw = input("Place your bet (integer) > ").strip()
        if bet_raw.lower() in ('quit', 'end'):
            print("Exiting. Thanks for playing!")
            break
        if not bet_raw.isdigit():
            print("Please enter a positive integer bet or 'quit'.")
            continue
        bet = int(bet_raw)
        if bet <= 0 or bet > credits:
            print("Invalid bet (must be > 0 and <= your credits).")
            continue
        # spin
        reels = spin_random()
        slow_reveal(reels, delay=0.6)
        win = payout(bet, reels, payouts=payouts)
        if win > 0:
            print(f"You win {win} credits!")
            credits += (win - bet)
        else:
            print(f"No win. You lost {bet} credits.")
            credits -= bet
    return credits


def main():
    parser = argparse.ArgumentParser(description='Simple CLI slot machine')
    parser.add_argument('--demo', action='store_true', help='Run a demo deterministic spin and exit')
    parser.add_argument('--credits', type=int, default=1000, help='Starting credits for interactive play')
    args = parser.parse_args()

    if args.demo:
        bet = 1
        print("Demo mode — deterministic spin")
        reels = demo_spin()
        slow_reveal(reels, delay=0.7)
        win = payout(bet, reels, payouts=DEFAULT_PAYOUTS)
        print(f"Reels: {' '.join(reels)}")
        print(f"Bet: {bet} -> Payout: {win}")
        return

    try:
        interactive_loop(starting_credits=args.credits)
    except (KeyboardInterrupt, EOFError):
        print("\nInterrupted. Exiting.")


if __name__ == '__main__':
    main()