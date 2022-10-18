def electron_distributor(electrons):
    all_shells = []
    electrons_left = electrons
    for shell in range(1, electrons + 1):
        shell_capacity = 2 * shell ** 2
        if electrons_left < shell_capacity:
            all_shells.append(abs(electrons_left))
            electrons_left -= shell_capacity
            if electrons_left <= 0:
                return all_shells
        elif electrons_left > shell_capacity:
            electrons_left -= shell_capacity
            diff = electrons_left - shell_capacity
            all_shells.append(electrons_left - diff)
            if electrons_left <= 0:
                return all_shells
        elif electrons_left == shell_capacity:
            all_shells.append(electrons_left)
            electrons_left -= electrons_left
            if electrons_left <= 0:
                return all_shells
    return all_shells


num_of_electrons = int(input())
print(electron_distributor(num_of_electrons))
