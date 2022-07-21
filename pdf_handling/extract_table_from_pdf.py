import tabula     # module tabula-py

table = tabula.read_pdf('weather.pdf', pages=1)
print(table)
print(table[0])

table[0].to_csv('weather.csv')
table[0].to_excel('weather.xlsx')     # need module named 'openpyxl'

