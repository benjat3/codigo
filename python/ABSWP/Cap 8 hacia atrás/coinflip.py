import random
number_of_streaks = 0
for experiment_number in range(10000):  # Run 100,000 experiments total.
    listaexp = []
    # Code that creates a list of 100 'heads' or 'tails' values
    for i in range(100):
        listaexp.append(random.choice(['H','T']))
        # Code that checks if there is a streak of 6 heads or tails in a row
        if listaexp[i-6:i] == ['H']*6 or listaexp [i-6:i] == ['T']*6:
            number_of_streaks += 1
            break

print('Chance of streak: %s%%' % (number_of_streaks / 100))
