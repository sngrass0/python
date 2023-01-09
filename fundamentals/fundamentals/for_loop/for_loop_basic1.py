#1 Basic
def basic():
    for x in range(151):
        print(x)

#2 Multiples of Five
def multiples_of_five():
    for x in range(5, 1001):
        if x % 5 == 0:
            print(x)

#3 Counting the Dojo Way
def counting_the_dojo_way():
    for x in range(1, 101):
        if x % 10 == 0:
            print("Coding Dojo")
        elif x % 5 == 0:
            print("Coding")
        else:
            print(x)

#4 Whoa. That Sucker's Huge!
def sucker():
    total = 0
    for x in range(0, 500001):
        if x % 2 != 0:
            total += x
    print(total)

#5 Countdown by Four
def countdown_by_four():
    for x in range(2018, 0, -4):
        print(x)
        
#6 Flexible Counter
def flexible_counter(lowNum, highNum, mult):
    for x in range(lowNum, highNum + 1):
        if x % mult == 0:
            print(x)

# FUNCTION CALLS #
basic()
multiples_of_five()
counting_the_dojo_way()
sucker()
countdown_by_four()
flexible_counter(2,9,3)
