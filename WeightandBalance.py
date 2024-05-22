from wandb import weightinp, lengthinp

if __name__ == "__main__":
    emptyWraw = input('Weight of the aircraft when empty: ')
    emptyAraw = input('Moment arm of the aircraft when empty: ')
    weight = weightinp(emptyWraw)
    moment = lengthinp(emptyAraw) * weight

    while True:
        load = input('Weight of new load: ')
        arm = input('Arm of new load: ')
        cont = input('Would you like to continue adding a new load? (Y/N): ')
        weight += weightinp(load)
        moment += lengthinp(arm) * weightinp(load)
        if cont == 'N':
            break
        print(f'The final weight of the aircraft is {weight} kg and the centre of gravity is {moment / weight} m aft of the datum')