# Population of a town today is 100000. The population has increased
# steadily at the rate of 10 % per year for last 10 years. Write a program to
# determine the population at the end of each year in the last decade.

population = 100000
for i in range(10):
    population += int(population*10/100)
    print('Year', i+1, ':', population)