def largest_power_of_two(N):
    power = 0
    value = 1
    while value * 2 <= N:
        value *= 2
        power += 1
    print(power, value)
largest_power_of_two(20)