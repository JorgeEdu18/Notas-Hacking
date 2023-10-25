text = '                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                '

firstType = ' '
secondType =  ' '
binaryString = ''

for char in text:
    if char == firstType :
        binaryString += '0'
    else:
        binaryString += '1'
print(binaryString)