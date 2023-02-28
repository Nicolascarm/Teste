string = input('Digite uma frase: ')

nova_string = ''

for i in range(len(string) - 1, -1, -1):
    nova_string += string[i]

print(f'Frase original: {string}')
print(f'Frase invertida: {nova_string}')
