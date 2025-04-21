# Formating currency lesson
import locale

locale.setlocale(locale.LC_ALL, '')

price = 1234.56
fmt_price = locale.currency(price)

print(fmt_price)
#test change

locale.setlocale(locale.LC_ALL, 'fr_FR')
fmt_price = locale.currency(price)

print(fmt_price)

locale.setlocale(locale.LC_ALL, 'pl_PL')
fmt_price = locale.currency(price)

print(fmt_price)

locale.setlocale(locale.LC_ALL, '')
fmt_price = locale.currency(price, grouping=True)

print(fmt_price)