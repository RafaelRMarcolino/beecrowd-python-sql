#Read an integer value corresponding to a person's age (in days) and print it in years,
# months and days, followed by its respective message “ano(s)”, “mes(es)”, “dia(s)”.

#Note: only to facilitate the calculation, consider the whole year with 365 days 
# and 30 days every month. In the cases of test there will never be a situation that allows 12 months and some days, like 360, 363 or 364. This is just an exercise for the purpose of testing simple mathematical reasoning.

#Input
#The input file contains 1 integer value.

#Output
#Print the output, like the following example.


idade = int(input('Digite a quantidade de dias de idade '))
years = 365
mounth = 30

anos = idade / years
anosRestoMes = idade % years

meses = anosRestoMes / 30
diasResto = anosRestoMes % 30
dias = diasResto 

print("{} ano ".format(int(anos)))
print("{} mes ".format(int(meses)))
print("{} dia ".format(int(dias)))