

import random, string


def associated_words(f):
    words, count, output = str.lower(file.read(f)).replace('\xe2\x80\x94', ''), -1, {}
    for i in  string.punctuation:
        words = words.replace(i, '')
    words = words.split()
    
    for current_item in words:                      # start searching through the txt file
        count += 1                                  # start counting 
        if count + 3 > len(words):                  # abandon ship! the index is too large 
            break
        next_item, next_item2 = words[count+1], words[count+2]   # set vlaues of item      
        if (current_item, next_item) in output:                  # if item is in the dict, add to entry
            output[(current_item, next_item)] = output[(current_item, next_item)] + [next_item2]
        if (current_item, next_item) not in output:              # create new entry if not in dict
            output.update({(current_item, next_item):[next_item2]})
            
    return output


def make_random_story(f, num_words):
    words, output = associated_words(f), []
    current_words = random.choice(words.keys())
    output = [x for x in current_words]
    while len(output) < num_words:
        next_word = random.choice(words[current_words])
        if type(next_word) is str:
            output += [next_word]
        if type(next_word) is list:
            output += next_word
        current_words = (output[-2], output[-1])
    return ' '.join(output)



f = open("/dune-text.txt", 'r')
print make_random_story(f, 1000)






