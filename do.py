from datasets import load_dataset

# Charger le jeu de données Allociné
allocine_dataset = load_dataset("allocine")

# Accéder aux avis
reviews = allocine_dataset["train"]["review"]

# Afficher le premier avis
print("Premier avis Allociné :")
print(reviews[0])
