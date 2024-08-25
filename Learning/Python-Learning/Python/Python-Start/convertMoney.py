print('Choose your money ref with E for Euros and $ for Dollars')


# Taux de change Euro -> Dollar (par exemple, 1 Euro = 1.10 Dollars)
taux_euro_dollar = 1.10

# Montant en Euros
montant_en_euros = 50

# Conversion en Dollars
montant_en_dollars = montant_en_euros * taux_euro_dollar
# Taux de change inverse Dollar -> Euro
taux_dollar_euro = 1 / taux_euro_dollar

print(f"{montant_en_euros} Euros = {montant_en_dollars:.2f} Dollars")
# Conversion en Euros
montant_en_euros = montant_en_dollars * taux_dollar_euro

print(f"{montant_en_dollars} Dollars = {montant_en_euros:.2f} Euros")