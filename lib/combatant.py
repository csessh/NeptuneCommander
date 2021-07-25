class Combatant:
    DEFENSE_BONUS = 1

    def __init__(self, weapon_tech: int, fleet_size: int, is_defender: bool=False) -> None:
        if type(weapon_tech) is not int:
            raise ValueError(f'Weapon tech level must be an integer. {weapon_tech} is obviously not an integer.')

        if type(fleet_size) is not int:
            raise ValueError(f'Fleet size must be an integer. {fleet_size} is obviously not an integer.')

        if type(is_defender) is not bool:
            raise ValueError(f'Defender indicator must be a boolean. {is_defender} is obviously not a boolean.')

        self._weapon_tech = weapon_tech
        self._fleet_size = fleet_size
        self._is_defender = is_defender

    def destroy(self, opponent: 'Combatant') -> bool:
        """
        The fleet deals the number of damage equals to the level of weapon they currently have
        """
        opponent.size -= self.tech
        return opponent.size <= 0

    @property
    def tech(self) -> int:
        """
        Defending troops gain a weapon tech bonus
        """
        tech = self._weapon_tech
        if self._is_defender:
            tech += Combatant.DEFENSE_BONUS

        return tech

    @property
    def size(self) -> int:
        """
        Return current fleet size
        """
        return self._fleet_size

    @size.setter
    def size(self, value:int) -> None:
        if type(value) is not int:
            raise ValueError(f'Fleet size must be an integer. {value} is obviously not an integer.')

        if value < 0:
            value = 0
        self._fleet_size = value

    def __str__(self) -> str:
        if self._is_defender:
            return f'Fleet of {self._fleet_size} ships with level {self._weapon_tech} weapon technology with defender bonus'
        return f'Fleet of {self._fleet_size} ships with level {self._weapon_tech} weapon technology'
