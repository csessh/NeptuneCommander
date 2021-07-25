#!/usr/bin/python
from typing import Union


class Combatant:
    def __init__(self) -> None:
        self._weapon_tech = 1
        self._fleet_size = 0

    def attack(self, opponent: Union[Attacker, Defender]) -> None:
        pass
        

class Attacker(Combatant):
    def __init__(self) -> None:
        super().__init__()
        self._weapon_tech += 1 


class Defender(Combatant):
    def __init__(self) -> None:
        super().__init__()


if __name__ == '__main__':
    pass