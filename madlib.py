'''
Author: <Nikki Diguardi>
Date: 04.07.2022
Class: ISTA 130
Section Leader: <Sara Cielaszyk>

Description:
Do not use tab character for indentation. Ensure you are using all of the coding tips you have
learned thus far or it will cost points. A Mad lib is a story template that has various
words missing. The goal is to associate fucntions to the different word adjectives and 
create a unique stroy from the results. This program will read a Mad lib story tempalte
from a file. The mad lib will have speech labels all uppercase the program will  ask the
user to supply the speech labels.'''



def print_report(filename):
    '''Write a function that takes a single string for the name of the file. The function
    will read the given file and print a report giving the information listed. Total number
    of vowels (not y) total number of consonants in the file. The total number of white
    spaces. Total number of punctionations, and characters. The percent of of the file
    composed of vowels, consonants, white space and punctuations. Print this in a pretty
    table.
    Parameter: a string of file name
    return: none'''
    vowel_count = 0 
    cons_count = 0
    white_count = 0
    punct_count = 0
    # above is to keep count of total number
    vowels = ('aeiou')
    vowels += vowels.upper()

    file = open(filename, 'r')
    for line in file:
        for ch in line:
            if ch in vowels:
                vowel_count += 1
            elif ch.isalpha():
                cons_count += 1
            elif ch.isspace():
                white_count += 1
            else:
                punct_count += 1
    file.close()
    total_count = vowel_count+cons_count+white_count+punct_count
    #find percents
    per_v = round((vowel_count/total_count)*100, 1)
    per_c = round((cons_count/total_count)*100, 1)
    per_s = round((white_count/total_count)*100, 1)
    per_p = round((punct_count/total_count)*100, 1)
    # for table formatting
    count = ['', '', vowel_count, cons_count, white_count, punct_count, '', total_count,'',
    per_v, per_c, per_s, per_p, '', '']
    title = ['', '','Vowels:', 'Consonants:', 'Whitespace:', 'Punctuation:', '', 'Total:','',
    'Percent vowels:', 'Percent consonants:', 'Percent spaces:', 'Percent punctuation:', '', '']

    # creating table
    for i in range(15):
        if i == 0 or i == 8 or i == 14:
            # for spacing
            print()
        elif i == 1:
            # banner of the table
            print( filename.center(25, '-' ))
        elif i == 6:
            print('-' * 25)
        elif i == 13:
            print('=' * 25)
        else:
            # wording in table
            print(title[i].ljust(20, ' ') + str(count[i]).rjust(5, ' '))

def replace_parts_of_speech(phrase, types):
    '''Write a function that takes two parameters. The first a string rep. a line from a file
    it may contain part of speech labels that need to be replaced by words. The second is
    the type of speech label that needs replacing. Use a prompt to ask for the type to replace.
    parameter: two strings. one the line of a file, the second a type of speech label need
    replacing.
    return: new line with type of speech replaced'''

    count = phrase.count(types)
    for i in range(count):      
        entry = input('Enter '+ types.lower() + ': ')
        phrase = phrase.replace(types, entry, 1)
    return phrase


def complete_mad_lib(name):
    '''Write a fucntion that takes the name of the madlib template file to read. This funciton
    will read the indicated template file line by line, replace all part of speech labels with
    words entered by the user. This will be done in order: Plural noun, verb past, verb, noun
    adjective. Write a new file with the story and begin with Mad_
    parameter: a string name of the template file
    return: a new mad file'''

    original = open(name, 'r')
    new_file = 'MAD_' + name[:-4] + name[len(name)-4:]
    mad_file = open(new_file, 'w')
    new_line = ''
    for line in original:
        line = replace_parts_of_speech(line, 'PLURAL NOUN')
        line = replace_parts_of_speech(line, 'VERB PAST')
        line = replace_parts_of_speech(line, 'VERB')
        line = replace_parts_of_speech(line, 'NOUN')
        line = replace_parts_of_speech(line, 'ADJECTIVE')
        new_line += line
    mad_file.write(new_line)
    original.close()
    mad_file.close()
    

#==========================================================
def main():
    '''
    Ask the user to enter the Mad-lib template file name with a prompt. 
    call your functions to print the character report on that file. Call the fuction
    to have the user complete the mad lib story.
    '''
    file_name = input('Enter file name: ')
    print_report(file_name)
    complete_mad_lib(file_name)




if __name__ == '__main__':
    main()
