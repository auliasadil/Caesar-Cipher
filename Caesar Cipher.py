#Created by Muhammad Aulia Adil

#Caesar Cipher is a way of encoding a sentece by shifting the character(alphabet) to character next to the right of it
#EXAMPLE: 'ADIL' will be encoded as 'BEJM' if the shifted number is one

print('CAESAR CIPHER')

#This program will always running unless you press enter(you give the the input: 'blank')
while True:
    #You can encode a sentence or decode an encoded sentence
    code=input('encode or decode?(press enter to stop) ')
    if code=='':
        break
    if code == 'encode':
        word = input('Your message: ')
        #Whether the alphabet in capital or not, it will be returned in lowercase by this method
        word = word.lower()
        #You can choose the shifted number with this line 
        shift = eval(input('The word got shifted by: '))
        for m in word:
            if m>='a' and m<='z':
                letter=ord(m)-ord('a')
                letter=(letter+shift)%26
                letter= letter+ord('A')
                print(chr(letter), end='')
            #if a 'space' is 
            elif m==(' '):
                print(' ', end='')
            #This mean that except alphabet, the character will be returned the same
            else:
                print(m,end='')
        print('')
        #Decode is the reverse of encode, it will shift the character to the left
    if code=='decode':
        word=input('Enter the code: ')
        word=word.lower()
        shift=eval(input('The word got shifted by: '))
        for m in word:
            if m>='a' and m<='z':
                letter=ord(m)-ord('a')
                letter=(letter-shift)%26
                letter= letter+ord('A')
                print(chr(letter), end='')
            elif m==(' '):
                print(' ', end='')
            else:
                print(m,end='')
        print('')
        
        
                
        
