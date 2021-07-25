#!/usr/bin/env python3
from lib.battle import Battle
from lib.combatant import Combatant


SUCCESS_RETURN_CODE = 0


def main(attacker_tech: int, defender_size: int, defender_tech: int) -> int:
    attacker = Combatant(attacker_tech, 0)
    defender = Combatant(defender_tech, defender_size, is_defender=True)
    battle = Battle(attacker, defender)
    attacker.size = battle.ships_to_attack()

    print(f'Required number of ships to attack a fleet of {defender.size} at level {defender.tech} is {attacker.size}')
    battle.resolve()
    return SUCCESS_RETURN_CODE


if __name__ == '__main__':
    import sys
    import argparse

    parser = argparse.ArgumentParser('Return the minimum number of ships needed to successfully defend against an attack')
    parser.add_argument('defender_size', type=int, help='Defender fleet size')
    parser.add_argument('defender_tech', type=int, help='Defender weapon technology level')
    parser.add_argument('attacker_tech', type=int, help='Attacker weapon technology level')

    args = parser.parse_args()

    sys.exit(
        main(
            defender_size=args.defender_size,
            defender_tech=args.defender_tech,
            attacker_tech=args.attacker_tech
        )
    )
