def msg_transform():

    codes = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}

    inputMsg = input('Input: ').lower()
    outputMsg = ''

    for element in inputMsg: 
        for key in codes:
            if element == key:
                element = str(codes[key])
            elif element == str(codes[key]):
                element = key
        outputMsg = outputMsg + element   
    print('Output: ', outputMsg)

msg_transform()