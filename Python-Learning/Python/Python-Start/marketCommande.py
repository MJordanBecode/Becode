# Définition du stock dans le magasin à l'unité
milk_bottle = 0.225
raw_cider = 1.283333333
flour = 0.9
butter = 0.77
jar_nutella = 1.875

# Demander à l'utilisateur de saisir la quantité pour chaque produit
client_order_milk = float(input("Select your milk quantity: "))  
client_order_raw_cider = float(input("Select your raw cider quantity: "))  
client_order_flour = float(input("Select your flour quantity: "))  
client_order_butter = float(input("Select your butter quantity: "))  
client_order_jar_nutella = float(input("Select your jar nutella quantity: "))  # Convertir en float

# Calcul du prix total de la commande
orderPrice = (milk_bottle * client_order_milk) + (raw_cider * client_order_raw_cider) + (flour * client_order_flour) + (butter * client_order_butter) + (jar_nutella * client_order_jar_nutella)

# Affichage du prix total de la commande
print(f"Total order price: ${orderPrice:.2f}")  # Formatage pour afficher deux décimales


#AllowanceMoney 
rest = None
allowanceMoney = 20

rest = allowanceMoney - orderPrice
if(orderPrice <= 20):
    print('you have money ${:.2f} left'.format(rest))
elif(orderPrice >20):
    print('you are missing ${:.2f} money'.format(abs(rest)))