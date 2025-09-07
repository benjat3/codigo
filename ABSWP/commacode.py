def comma(list):
    string = ''
    for index, item in enumerate(list):
        if index != len(list)-1:
            string += str(item) + ', '
        else:
            string += 'and ' + str(item)
    return(string)

spam = ['a', 'b', 'c', 'd', 'e']
print(comma(spam))
