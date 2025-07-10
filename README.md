# age-of-war-casa-assignment
This is a simple Python simulation of a battle between two armies made up of different types of platoons. Each platoon has a unit type and a number of soldiers. The simulator checks whether there's a permutation (reordering) of your platoons that can defeat the opponent's platoons in at least 3 out of 5 battles.

#Requirements
Python 3.6 or later
No external libraries are required other than the Python standard library.

#How to Run
Save the script to a file, for example: battle_simulator.py
Run the script using Python:
python age_of_war.py

#Sample Input
Enter your platoons: Spearmen#10;Militia#30;FootArcher#20;LightCavalry#1000;HeavyCavalry#120
Enter opponent platoons: Militia#10;Spearmen#10;FootArcher#1000;LightCavalry#120;CavalryArcher#100

#Sample Output
Winning arrangement: Spearmen#10;Militia#30;FootArcher#20;HeavyCavalry#120;LightCavalry#1000

Battle Outcomes:
Battle 1: Spearmen#10 vs Militia#10 → Loss
Battle 2: Militia#30 vs Spearmen#10 → Win
Battle 3: FootArcher#20 vs FootArcher#1000 → Loss
Battle 4: HeavyCavalry#120 vs LightCavalry#120 → Win
Battle 5: LightCavalry#1000 vs CavalryArcher#100 → Win
