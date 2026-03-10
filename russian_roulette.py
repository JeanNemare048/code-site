import random
import sys

def safe_input(prompt: str) -> str:
    """Read input and exit early if the user types 'end'."""
    try:
        s = input(prompt)
    except EOFError:
        # treat EOF as exit
        print("Run ended (EOF).")
        sys.exit(0)
    if s is None:
        return ''
    if s.strip().lower() == 'end':
        print("Run ended by user.")
        sys.exit(0)
    return s


players_count = int(safe_input("Entrez le nombre de joueurs : "))
# Valider que le nombre de joueurs est entre 2 et 6 (inclus)
while not (2 <= players_count <= 6):
    players_count = int(input("Entrez un nombre de joueurs entre 2 et 6 : "))


# Nombre de chambres du barillet (ex: 6)
chambers_count = 6

# Nombre de balles (ne peut pas dépasser le nombre de chambres)
max_bullets = min(3, chambers_count)
# use safe_input so typing 'end' exits
bullets_count = int(safe_input(f"Entrez le nombre de balles dans le barillet (1 à {max_bullets}) : "))
# Valider que le nombre de balles est entre 1 et max_bullets (inclus)
while not (1 <= bullets_count <= max_bullets):
    bullets_count = int(input(f"Entrez un nombre de balles compris entre 1 et {max_bullets} : "))

print("action: self--> 1, autre joueur--> 2")

# Initialize players' alive status (1-indexed)
players_alive = [False] + [True] * players_count
current_player = 1

def next_alive(start):
    """Return the next alive player index after start (wraps around)."""
    idx = start
    for _ in range(players_count):
        idx = idx % players_count + 1
        if players_alive[idx]:
            return idx
    return None

while True:
    # Check game end conditions
    alive_count = sum(1 for a in players_alive[1:] if a)
    if alive_count <= 1:
        if alive_count == 1:
            winner = next(i for i, a in enumerate(players_alive) if a and i != 0)
            print(f"Partie terminée. Gagnant: Joueur {winner}")
        else:
            print("Partie terminée. Aucun joueur en vie.")
        break
    if bullets_count <= 0:
        print("Plus de balles disponibles. Fin du jeu.")
        break

    # Skip dead players
    if not players_alive[current_player]:
        nxt = next_alive(current_player)
        if nxt is None:
            print("Plus de joueurs vivants. Fin du jeu.")
            break
        current_player = nxt
        continue

    player_turn_moveon = f"Joueur {current_player}"
    print(player_turn_moveon)

    player_action = safe_input("Entrez votre action (1 pour self, 2 pour autre) : ").strip()

    if player_action == "1":
        # Self shot
        bullets = bullets_count
        sample_size = min(bullets, chambers_count)
        chambers = set(random.sample(range(1, chambers_count + 1), sample_size))
        roll = random.randint(1, chambers_count)
        if roll in chambers:
            print("pow")
            # current player dies
            players_alive[current_player] = False
            turn_result = "pow"
        else:
            print("click")
            turn_result = "click"
        # reduce bullets/chambers after shot
        chambers_count = max(1, chambers_count - 1)
        # If it was a click on self-shot, the same player goes again
        if turn_result == "click":
            print(f"{player_turn_moveon} rejoue (click).")
            # do not change current_player; loop will prompt them again
            continue
        # otherwise (pow) advance to next alive player
        nxt = next_alive(current_player)
        if nxt is None:
            print("Plus de joueurs vivants. Fin du jeu.")
            break
        current_player = nxt
        continue

    elif player_action == "2":
        # Shoot another player
        try:
            target_player = int(safe_input("Qui tirer ? (Entrez le numéro du joueur cible) : "))
        except ValueError:
            print("Entrée invalide — réessayez.")
            continue
        if not (1 <= target_player <= players_count):
            print("Numéro de joueur invalide — réessayez.")
            continue
        if not players_alive[target_player]:
            print("Le joueur ciblé est déjà mort — choisissez un autre.")
            continue
        if target_player == current_player:
            print("Vous ne pouvez pas vous cibler avec l'action 2 — utilisez 1 pour self.")
            continue

        bullets = bullets_count
        sample_size = min(bullets, chambers_count)
        chambers = set(random.sample(range(1, chambers_count + 1), sample_size))
        roll = random.randint(1, chambers_count)
        if roll in chambers:
            print(f"Joueur {target_player} : pow")
            players_alive[target_player] = False
        else:
            print(f"Joueur {target_player} : click")
        chambers_count = max(1, chambers_count - 1)
        # advance to next alive player after the shooter
        nxt = next_alive(current_player)
        if nxt is None:
            print("Plus de joueurs vivants. Fin du jeu.")
            break
        current_player = nxt
        continue

    else:
        print("Action invalide. Entrez 1 (self) ou 2 (autre).")
        continue