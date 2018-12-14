#thoughts: for word in dictionary that is so long and contains anll these letters: add to list
import itertools
import enchant
from itertools import permutations

run = True

while run is True:
    #number of item in  list
    g = -1
    trues = "trues"

    #how long should the word be? - set x = _
    print "#### Begin ####"
    x = raw_input("Length of word / Number of characters: ")
    x = int(x)
    print "(Enter 'done' when all letters are entered)"
    print ""

    returned = "True"
    false = "true"

    list_of_letters = []
    empty_list = []
    one_list = []
    final_list = []
    list_letters = []


    #Enter Letters
    while trues == "trues":
        ask = raw_input("Enter a letter: ")
        if ask == "done":
            trues = "not true"
        list_of_letters.insert(0, ask)
    list_of_letters.remove("done")
    
    #############################################################################################

    d = enchant.Dict("en_US")
    
    for p in permutations(list_of_letters, x):
        item = "".join(p)
        
        check = d.check(str(item))
        if check == True:
            final_list.insert(0, item)
        
    #alphabetically organize list here
    final_list.sort()
    final_list2 = list(set(final_list))
    final_list2.sort()
    print ""
    print "Possible word combinations:"
    for item in final_list2:
        print item

    print "\n"
