num = input('Digite algum numero diferente de 0 e maior que 2: ')

valor = int(num)

if valor >= 2:

        if valor % 2 == 0:
            par_post = valor + 2
            impar_anterior = valor - 1
            print(impar_anterior, par_post)
        else:
            par_post_impar = valor + 1
            impar_anterior_impar = valor - 2
            print(impar_anterior_impar, par_post_impar)