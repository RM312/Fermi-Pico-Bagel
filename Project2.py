import random
original_number = str(random.randint(1,999))  #Choose any random number between 1 to 999
while True :
    output = []
    guess_number = input('\nGuess The Number: ')

    if len((guess_number)) != len(original_number):
        print(f'Enter {len(original_number)} digit number')
        continue
        
    if len(guess_number)  != len(set(guess_number)):
        print('Duplicate number')
        continue
    
    if (int(guess_number) - int(original_number)) == 0 :
        print(' Fermi '*len(original_number))
        print('\nYou won !!')
        break
    
    for i in range(len(original_number)): 
        for j in range(len(guess_number)):     
            if original_number[i] == guess_number[j]: 
                if i == j:               
                    output.append('Fermi')
                else:
                    output.append('Pico')
                    
    output_string = ''
    for item in output :
        output_string = output_string + ' ' + item 
        
    if len(output) == 0:           
        print(' Bagels')
    else:
        print(output_string)
        
