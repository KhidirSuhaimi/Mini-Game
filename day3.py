print("Welcome to Treasure Island!\nYour mission is to find the treasure.")
first_choice=input("You're at a cross road. Where do you want to go? Type \"Left\" or \"Right\"\n").capitalize()

if first_choice == "Left":
    print("You reached a lake and see a random island in the middle.")
    second_choice = input("Do you \"Swim\" or \"Wait\" for divine Inspiration?\n").capitalize()
    if second_choice == "Swim":
        print("Haha, you got eaten by a bullshark! You died noob!")
    else:
        print("3 miraculous doors appeared!")
        third_choice = input('Which door do you choose? "Red" or "Blue" or "Yellow"?\n').capitalize()
        if third_choice == "Yellow":
            print("Congratulations, you win a wife!")
        else:
            print("Unfortunately, you died a Virgin.")

else:
    print("You got eaten by the Bear , You died loser!")


