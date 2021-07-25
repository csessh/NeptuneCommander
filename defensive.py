#!/usr/bin/env python3
from lib.battle import Battle
from lib.combatant import Combatant


SUCCESS_RETURN_CODE = 0


def main(attacker_tech: int, attacker_size: int, defender_tech: int, verbose: bool=False) -> int:
    attacker = Combatant(attacker_tech, attacker_size)
    defender = Combatant(defender_tech, 0, is_defender=True)
    battle = Battle(attacker, defender)
    defender.size = battle.ships_to_defend()

    print(f'Required number of ships to defend against a fleet of {attacker.size} at level {attacker.tech} is {defender.size}')
    battle.resolve()
    return SUCCESS_RETURN_CODE


if __name__ == '__main__':
    import sys
    import argparse

    parser = argparse.ArgumentParser('Return the minimum number of ships needed to successfully defend against an attack')
    parser.add_argument('attacker_size', type=int, help='Attacker fleet size')
    parser.add_argument('attacker_tech', type=int, help='Attacker weapon technology level')
    parser.add_argument('defender_tech', type=int, help='Defender weapon technology level')

    args = parser.parse_args()

    sys.exit(
        main(
            attacker_size=args.attacker_size,
            attacker_tech=args.attacker_tech,
            defender_tech=args.defender_tech
        )
    )
