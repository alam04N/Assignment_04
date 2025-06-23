user1 = input('Enter the text to write to the file: ' )

with open ('output.txt','w') as file:
    writing_text = file.write(user1 +'\n')
    print(writing_text)

user2 = input('Enter the  additional  text to want to append to  the file: ' )
with open ('output.txt','a') as file:
    appending_text = file.write(user2 +'\n')
    print(appending_text)

with open('output.txt') as file:
    reading_txt= file.read()
    print('\n final content of the file')
    print(reading_txt)




