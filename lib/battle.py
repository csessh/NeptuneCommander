from typing import Tuple
from lib.combatant import Combatant


class Battle:
    def __init__(self, attacker: Combatant, defender: Combatant) -> None:
        self._attacker = attacker
        self._defender = defender

    def resolve(self) -> None:
        """
        Play out this battle. Verbose option enables turn-by-turn combat results.
        """
        turn_tracker = 0
        while self._attacker.size > 0 and self._defender.size > 0:
            turn_tracker += 1

            if not self._defender.destroy(self._attacker):
                self._attacker.destroy(self._defender)

            print(f'Turn #{turn_tracker}: Attacker ({self._attacker.size}) - ({self._defender.size}) Defender')

    def ships_to_defend(self) -> int:
        """
        How many ships do you need to defend against an attack of given size and tech?
        """
        attacker_turns = self._attacker.size // self._defender.tech
        required_ships = attacker_turns + 1 * self._attacker.tech
        return required_ships

    def ships_to_attack(self) -> int:
        """
        How many ships do you need to successfully take over a planet?
        """
        return None
