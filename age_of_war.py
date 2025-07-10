from itertools import permutations
from typing import List


class Platoon:
    advantage_map = {
        "Militia": ["Spearmen", "LightCavalry"],
        "Spearmen": ["LightCavalry", "HeavyCavalry"],
        "LightCavalry": ["FootArcher", "CavalryArcher"],
        "HeavyCavalry": ["Militia", "FootArcher", "LightCavalry"],
        "CavalryArcher": ["Spearmen", "HeavyCavalry"],
        "FootArcher": ["Militia", "CavalryArcher"]
    }

    def __init__(self, unit_class: str, soldier_count: int):
        self.unit_class = unit_class
        self.soldier_count = soldier_count

    def __str__(self):
        return f"{self.unit_class}#{self.soldier_count}"

    def has_advantage_over(self, opponent) -> bool:
        return opponent.unit_class in Platoon.advantage_map.get(self.unit_class, [])

    def effective_strength_against(self, opponent) -> int:
        if self.has_advantage_over(opponent):
            return self.soldier_count * 2
        return self.soldier_count


class BattleSimulator:
    def __init__(self, own_platoons: List[Platoon], opponent_platoons: List[Platoon]):
        self.own_platoons = own_platoons
        self.opponent_platoons = opponent_platoons

    @staticmethod
    def simulate_battle(own: Platoon, opponent: Platoon) -> str:
        own_strength = own.effective_strength_against(opponent)
        opponent_strength = opponent.effective_strength_against(own)
        if own_strength > opponent_strength:
            return "Win"
        elif own_strength == opponent_strength:
            return "Draw"
        else:
            return "Loss"

    def find_winning_arrangement(self) -> List[Platoon] or None:
        for perm in permutations(self.own_platoons):
            wins = 0
            for own, opponent in zip(perm, self.opponent_platoons):
                if self.simulate_battle(own, opponent) == "Win":
                    wins += 1
            if wins >= 3:
                return list(perm)
        return None


def parse_platoons(input_line: str) -> List[Platoon]:
    return [Platoon(*item.split("#")[0:2]) for item in input_line.split(";")]


def main():
    input_own = input("Enter your platoons: ").strip()
    input_opponent = input("Enter opponent platoons: ").strip()

    own_platoons = [Platoon(p.split('#')[0], int(p.split('#')[1])) for p in input_own.split(';')]
    opponent_platoons = [Platoon(p.split('#')[0], int(p.split('#')[1])) for p in input_opponent.split(';')]

    simulator = BattleSimulator(own_platoons, opponent_platoons)
    winning_arrangement = simulator.find_winning_arrangement()

    if winning_arrangement:
        print("Winning arrangement:", ";".join(str(p) for p in winning_arrangement))
    else:
        print("There is no chance of winning")

    print("\nBattle Outcomes:")
    for i, (own, opponent) in enumerate(zip(winning_arrangement, opponent_platoons), 1):
        result = simulator.simulate_battle(own, opponent)
        print(f"Battle {i}: {own} vs {opponent} → {result}")


if __name__ == "__main__":
    main()
