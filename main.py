import locale
locale.setlocale(locale.LC_MONETARY, 'es_US')

from helpers import juros_compostos

if __name__ == '__main__':
    quantia_a_emprestar = float(input("Qual o valor a emprestar: "))
    taxa_juros_anual = float(input("Qual a taxa de juros anual:"))
    prazo = int(input("Qual o prazo: "))

    valor_final_a_pagar = juros_compostos(quantia_a_emprestar, taxa_juros_anual, prazo)
    print(f"O montante total calculado é de {locale.currency(valor_final_a_pagar, grouping=True)}.")