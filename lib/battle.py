from typing import Tuple
from lib.combatant import Combatant


class Battle:
    def __init__(self, attacker: Combatant, defender: Combatant) -> None:
        self._attacker = attacker
        self._defender = defender

    def resolve(self, verbose: bool=False) -> Tuple[Combatant, Combatant]:
        if verbose:
            turn_tracker = 0
            while self._attacker.size > 0 and self._defender.size > 0:
                turn_tracker += 1

                if not self._defender.destroy(self._attacker):
                    self._attacker.destroy(self._defender)

                print(f'Turn #{turn_tracker}: Attacker ({self._attacker.size}) - ({self._defender.size}) Defender')
        else:
            turns_for_defender = self._defender.size // self._attacker.tech
            turns_for_attacker = self._attacker.size // self._defender.tech

            if turns_for_attacker > turns_for_defender:
                # attacker wins
                self._defender.size = 0
                self._attacker.size -= (turns_for_defender * self._defender.tech)
            else:
                # defender wins
                self._attacker.size = 0
                self._defender.size -= (turns_for_attacker * self._attacker.tech)
        return self._attacker, self._defender

    def ships_to_defend(self) -> int:
        attacker_turns = self._attacker.size // self._defender.tech
        required_ships = attacker_turns + 1 * self._attacker.tech
        return required_ships