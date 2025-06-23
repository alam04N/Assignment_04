

try:
    with open('sample.txt', 'r') as file:
        reading_file= file.read()
        print(reading_file)
except FileNotFoundError:
    print('Error: the file sample.txt was not found')


'''
output:-
this is my first notebook
i will read it tomorrow
'''


