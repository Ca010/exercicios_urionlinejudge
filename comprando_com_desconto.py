preco = float(input('preco mercadoria: '))
qtd = int(input('quantidade: '))

soma = preco * qtd
desc_uni = soma * (qtd * 0.01)
desc_fixo = (soma * 0.1)
total = float(soma - desc_fixo - desc_uni)

print(f'{soma}')
print(f'{total:.2f}')