
import random



lista = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56]', '57', '58', '59', '60']


NumerosSorteados = [random.choice(lista) for i in range(6)]
print('='*55)
print('\n')
print(f'OS NÚMEROS DO SORTEIO SÃO: {lista}.')
print('\n')
print('='*55)
print('***OS NÚMEROS SORTEADOS SÃO:', ', '.join(NumerosSorteados).upper())
print('\n')
print(f'Continuam participando do sorteio: {lista}.' )          
print('='*55)

