# Джеси решава, че иска да се занимава с баскетбол, но за да тренира е нужна екипировка. Напишете програма, която изчислява какви разходи ще има Джеси, ако започне да тренира, като знаете колко е таксата за тренировки по баскетбол за период от 1 година. Нужна екипировка:
#     • Баскетболни кецове – цената им е 40% по-малка от таксата за една година
#     • Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
#     • Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
#     • Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка

# Годишната такса за тренировки по баскетбол – цяло число в интервала [0… 9999]
basketball_taxes = int(input())
shoes = basketball_taxes * 0.6
equip = shoes * 0.8
basket_ball = equip * 0.25
basket_accessoires = basket_ball  * 0.20

# Да се отпечата на конзолата колко ще са разходите на Джеси, ако започне да спортува баскетбол.

print(basketball_taxes + shoes + equip + basket_ball + basket_accessoires)