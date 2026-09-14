## ENTRADAS
Valor_compras = float (input ("\nValor total das compras: R$"))

##Processo
if Valor_compras < 200:  
 desconto = 0.05 * Valor_compras
 Valor_desconto = 5

elif Valor_compras >=200 and Valor_compras <300:
 desconto = 0.10 * Valor_compras
 Valor_desconto = 10

elif Valor_compras >=300:
 desconto = 0.15 * Valor_compras
 Valor_desconto = 15

valor_pago = Valor_compras - desconto


##SAIDAS 
print ("\n------Nota fiscal------")
print (f"Desconto de {Valor_desconto}% aprovado")
print (f"valor a ser pago: R$ {valor_pago:.2f}")
print (f"o Valor total do desconto é: R${desconto:.2f}")
