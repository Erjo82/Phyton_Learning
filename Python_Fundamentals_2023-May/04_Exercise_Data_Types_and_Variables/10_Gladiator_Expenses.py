total_lost_fight = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
for current_lost_fight in range(1, total_lost_fight +1):
    if current_lost_fight % 2 == 0:
        expenses += helmet_price
    if current_lost_fight % 3 == 0:
        expenses +=sword_price
    if current_lost_fight % 6 == 0:
        expenses += shield_price
    if current_lost_fight % 12 == 0:
        expenses += armor_price

print(f'Gladiator expenses: {expenses:.2f} aureus')
