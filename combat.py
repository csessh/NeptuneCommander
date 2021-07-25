#!/usr/bin/env python3
from battle import Battle
from combatant import Combatant


SUCCESS_RETURN_CODE = 0


def main(attacker_tech: int, attacker_size: int, defender_tech: int, defender_size: int) -> int:
    attacker = Combatant(attacker_tech, attacker_size)
    defender = Combatant(defender_tech, defender_size, is_defender=True)

    battle = Battle(attacker, defender)
    attacker, defender = battle.resolve(verbose=True)

    return SUCCESS_RETURN_CODE


if __name__ == '__main__':
    import sys
    import argparse

    parser = argparse.ArgumentParser('Combat calculator')
    parser.add_argument('attacker_size', type=int, help='Attacker fleet size')
    parser.add_argument('attacker_tech', type=int, help='Attacker weapon technology level')
    parser.add_argument('defender_size', type=int, help='Defender fleet size')
    parser.add_argument('defender_tech', type=int, help='Defender weapon technology level')

    args = parser.parse_args()

    sys.exit(
        main(
            attacker_size=args.attacker_size,
            attacker_tech=args.attacker_tech,
            defender_size=args.defender_size,
            defender_tech=args.defender_tech
        )
    )
