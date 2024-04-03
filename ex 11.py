largura = float(input('Qual a largura da parede em metros? '))
altura = float(input('Qual a altura da parede em metros? '))
area = largura * altura
tinta = area / 2
print(f'A área da parede é {area:.2f}m² e serão necessários {tinta:.0f} litros de tinta para pintá-la.')