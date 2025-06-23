import Requisições

def cambio_real():
    cr = (Requisições.cambio() * Requisições.inflacao_eua()) / Requisições.ipca()
    while True:
        try:
            valor_desejado = float(input('\33[mValor em reais: ')) 
        except (ValueError, TypeError):
            print('\33[31mDigite um valor válido')
        else:
            valor_f = valor_desejado * cr   
            print(f'Câmbio real: \33[32mR${cr:.2f}') 
            return valor_f
        
valor = cambio_real()
print(f'\33[mO valor da conversão foi \33[32mR$ {valor:.2f}')