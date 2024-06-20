def get_starting_number():
    while True:#while version
        number = input("Give a number to start with(in range of 1 to 99):").strip()
        if number.isdigit():
            number = int(number)
            if number >0 and number <100:
                return number
            else:
                print("Sorry, invalid response. Please enter an integer between 1 and 99")
        else:
            print("Sorry, invalid response. Please enter an integer between 1 and 99")

def sing(num_bottles):
    i = num_bottles
    while i > 0:
        if i > 1:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            if i-1 == 1:
                print(f"Take one down, pass it around, {i-1} bottle of beer on the wall.")
            else:
                print(f"Take one down, pass it around, {i-1} bottles of beer on the wall.")
            print()
        if i == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
        i -= 1