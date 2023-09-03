route = input().split("||")
start_fuel = int(input())
start_amu = int(input())

for x in range(len(route)):
    if route[x].split()[0] == "Travel":
        light_years = route[x].split()[1]
        if start_fuel >= int(light_years):
            start_fuel-=int(light_years)
            print(f"The spaceship travelled {light_years} light-years.")
        else:
            print("Mission failed.")
            break

    elif route[x].split()[0] == "Enemy":
        armour = route[x].split()[1]
        if start_amu >= int(armour):
            start_amu-=int(armour)
            print(f"An enemy with {armour} armour is defeated.")
        else:
            if start_fuel>=2*int(armour):
                start_fuel-=2*int(armour)
                print(f"An enemy with {armour} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break
    elif route[x].split()[0] == "Repair":
        added_amu = int(route[x].split()[1]) * 2
        added_fuel = int(route[x].split()[1])
        start_amu += added_amu
        start_fuel += added_fuel
        print(f"Ammunitions added: {added_amu}.")
        print(f"Fuel added: {added_fuel}.")

    elif route[x].split()[0] == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break

        #print(route[x].split()[1])

#starting_ammunition = int(input())
#var1,var2 = route[0].split()
