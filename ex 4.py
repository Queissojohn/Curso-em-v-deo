x = input('Digite algo: ')
print(f'O tipo primitivo de x é : {type(x)}')
print(f'Possui a primeira letra maiúscula: {x.istitle()}')
print(f'É alfabético: {x.isalpha()}')
print(f'É um número? {x.isalnum()}')
print(f'É um número decimal? {x.isdecimal()}')
print(f'{x.isascii()}')
print(f'{x.isidentifier()}')
print(f'É tudo minúsculo? {x.islower()}')
print(f'É tudo maiúsculo? {x.isupper()}')
print(f'{x.isprintable()}')
