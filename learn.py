#trying to practice what I've learnt

def main():
    x = int(input())
    y = int(input())
    name = input("What's your name patner? ")
    food = input("What's your favourite food? ")
    print("Hello there,", name.strip().title())
    print("Your favourite food is", food.strip())
    print( x + y )
    print( round((x / y), 3 ))
    print( x * y )
    print( x - y )


main()

