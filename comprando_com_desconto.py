preco = float(input('preco mercadoria: '))
qtd = int(input('quantidade: '))

soma = preco * qtd
desc_uni = (preco * 1 / 100)
valor_desc_uni = preco - desc_uni
conta = valor_desc_uni * qtd
desc_fixo = (conta * 10 / 100)
total = conta - desc_fixo

print(f'{soma}')
print(f'{total:.2f}')