'''
Author: <Nikki Diguardi>
Date: <06.15.2022>
Class: APCV 320

Description:
Create a class car with three or more methods including a randommizer 
for paint color. Use the random library and one method will return a value.
'''
import random

class Car:
    '''Write a class Car'''
    def __init__(self, fabricant, brand, year, color, engine, fuel):
        '''Car will contain the below methods of unique objects. This is the initializer method.'''
        self.fabricant = fabricant
        self.brand = brand
        self.year = year   
        self.mileage = random.randrange(10000, 100000) # This does make it an integer instead of a float
        # I tried adding decimals but the random range ddin't work
        self.color = color  
        self.engine = engine
        self.fuel = fuel
        return None

    def __repr__(self):
        '''When called Car will print the string in the format to represent all
        instance variables printed
        parameter: self
        return: the string formatted print'''
        display = ('-' *10) + self.brand + ('-' *10) + '\n'
        display += '  Manufacturer: ' + self.fabricant + '\n'
        display += 'Year: ' + self.year + '   Color: ' + self.color + '\n'
        miles = str(self.mileage)
        display += 'Mileage: ' + miles + '   Engine: ' + self.engine + '\n'
        display += '\t Fuel: ' + self.fuel + '\n'
        return display

    def carPaint(self):
        '''Write a method that will choose the paint color randomly.
        parameter: none
        return: new color statement
        '''
        # Start with a list of different colors
        colour = ['White', 'Black', 'Blue', 'Green', 'Red', 'Brown', 'Purple', 'J-Spec Wrap']
        num = random.randrange(0, len(colour)) # Use the random range to generate a index
        paint = colour[num]
        shop = 'The shop has painted the ' + self.brand + ' from ' + self.color + ' to ' + paint + '\n'
        self.color = paint # The color changed for the car therefore the car.color will change
        return shop

    def race(self, other):
        '''I thought it would be fun to have a race method.'''

        win = self.brand + ' Wins the race against '+ other.brand + '\n'
        lose = other.brand + ' Wins the race against '+ self.brand + '\n'
        if self.color == 'red': # red cars are always faster that's why they pay more insurance
            return win
        elif other.color == 'red':
            return lose
        # The car with the lower mileage (which is random generated) will win the race
        elif self.mileage < other.mileage:
            return win
        elif self.mileage > other.mileage:
            return lose



#==========================================================
def main():
    '''
    Call your methods and functions to have three cars generated.
    '''

    geoffery = Car('Hyundai', 'Sonata', '2005', 'White', 'V6', 'Gas')
    print(geoffery)
    misty = Car('Subaru', 'Forester', '2017', 'Black', 'I4', 'Gas')
    print(misty)
    naomi = Car('Nissan', '350z', '2003', 'Yellow', 'V8', 'Gas')
    print(naomi)
    # request input from the user on if they want to race or paint
    ch = input('Would you like to enter the shop or race?\n')
    ch = ch.upper()
    if 'R' in ch:
        print('\t  ** RACE **  \n')
        one = input('Choose which car: 1,2,3\n')
        two = input('Choose which car '+ one + ' should go agaist:\n')
        if one == two:
        # ensure the user inputted two different numbers
            print('Cannot race the same car\n')
        elif one == '1':
            if two == '2':
                racing = geoffery.race(misty)
                print(racing)
            else:
                racing = geoffery.race(naomi)
                print(racing)
        elif one == '2':
            if two == '1':               
                racing = misty.race(geoffery)
                print(racing)  
            else:
                racing = misty.race(naomi)
                print(racing)
        else:
            if two == '1':
                racing = naomi.race(geoffery)
                print(racing)
            else:
                racing = naomi.race(misty)
                print(racing)
        return None # close the program
    # enter the shop to change the paint
    elif 'S' in ch:
        print(' *Entering the paint shop*\n')
        painting = input('Choose which car: 1,2,3\n')
        if painting == '1':
            paint = geoffery.carPaint()
            print(paint)
        elif painting == '2':
            paint = misty.carPaint()
            print(paint)
        else:
            paint = naomi.carPaint()
            print(paint)
    return None # close the program
if __name__ == '__main__':
    main()
