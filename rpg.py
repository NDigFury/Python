'''
Author: <Nikki Diguardi>
Date: <04.24.2022>
Class: ISTA 130
Section Leader: <Sara Cielaszyk>

Description:
<Write a program that will simulate a combat for a simple RPG
The will be one class of character: Fighter. Each fighter will have HP
and when ran there will be damage between the two fighters. The order of attack
is based on 6 sided dice track the HP and fight then determine a winner if any during 
rounds>
'''
import random

class Fighter:
    '''Write a class called Fighter'''
    def __init__(self, name):
        '''Write the initializer method taking two parameters
        parameter: 2 all methods in self and name string of fighter
        return: none'''
        self.name = name
        self.hit_points = 10


    def __repr__(self):
        '''Write a method that takes one parameter and returns a string showing
        the name and hit points
        parameter: 1 self
        return: string with name and hit points'''
        output = self.name + ' (HP: '+ str(self.hit_points) + ')'
        return output

    def take_damage(self, damage_amount):
        '''Write a method that takes two parameters the fighter instance that
        calls the method and the damage ammount which is the number which the 
        damage has been dealt and reduces the hit points. Checks for a death instance
        parameters: 2 the self method  fighter name, and a int of damage
        reutrn: none'''

        self.hit_points = (self.hit_points - damage_amount)
        if self.hit_points <= 0:
            death = '\tAlas, '+ self.name + ' has fallen!'
            print(death)
        else:
            struck = '\t' + self.name + ' has ' + str(self.hit_points) + ' hit points remaining.'
            print(struck)



    def attack(self, other):
        '''Write a method that takes two parameters, self and other which is the
        attacker The method will print the name of the attacker and attacked
        parameter: 2 the self fighter method, and other the name of the attacker
        reutrn: none'''
        round = self.name + ' attacks ' + other.name + '!'
        print(round)
        roll = random.randrange(1,20)
        if roll > 11:
            hit = random.randrange(1,6)
            inflict = '\tHits for ' + str(hit) + ' hit points!'
            print(inflict)
            other.take_damage(hit)
        else:
            print('\tMisses!')



    def is_alive(self):
        '''takes one parameter self. The method returns true if HP > 0 false if <
        parameter: self
        return: true is hp is positive and false if negative'''

        if self.hit_points >= 1:
            return True
        else:
            return False
    
def combat_round(death, pain):
    '''Write a function that takes two parameters. The first fighter and the
    second fighter. the function will determine who attacks first with random int.
    if they are equal print. then call attack method and deal in combat
    parameter: two fighters
    returns: none'''

    p1_roll = random.randrange(1,6)
    p2_roll = random.randrange(1,6)
    if p1_roll == p2_roll:
        print('Simultaneous!')
        death.attack(pain)
        pain.attack(death)
    elif p1_roll > p2_roll:
        death.attack(pain)
        if pain.is_alive() == True:
            pain.attack(death)
    else:
        pain.attack(death)
        if death.is_alive() == True:
            death.attack(pain)


#==========================================================
def main():
    '''
    Create two instances of the fighter class. Repeat print round number
    print fighters info. use the input function to pause the program until enter
    call combat round to simulate one combat round.
    '''

    first = Fighter('Death_Mongrel')
    second = Fighter('Hurt_then_Pain')
    i = 1

    
    while first.is_alive() == True and second.is_alive() == True:
        border = '=' * 19
        title = border + ' ROUND '+ str(i)+ ' '+ border + '\n'    
        print(title)
        i += 1
        print(first)
        print(second)
        input('\t' + 'Enter to Fight!')
        combat_round(first, second)
    print('The battle is over!')
    print(first)
    print(second)


if __name__ == '__main__':
    main()
