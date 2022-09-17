# defining the gravitational constant
G = 6.674e-11

# Reading weight and distance
m1 = float(input('Enter weight of first body (Kg): '))
m2 = float(input('Enter weight of second body (Kg): '))
r = float(input('Enter distance (m): '))

# Calculating Gravitational Force
F = G * m1 * m2 / r**2

print('Gravitational Force in newton =', F)
