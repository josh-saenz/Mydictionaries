frequency = {}

myfile = open('sometext.txt', 'r')

text = myfile.read()

mylist = text.split(" ")

for word in mylist: 
    if word not in frequency:
        frequency[word] = 1
    else:
        frequency[word] += 1

for key, value in frequency.items():
    print(f'{key} : {value}')