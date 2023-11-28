# Tokenisation

Tokenisation avec Hugging Face Datasets et SpaCy
Prérequis
Assurez-vous d'avoir Python installé sur votre machine. Vous pouvez télécharger Python sur le site officiel.

Installez les bibliothèques nécessaires en utilisant la commande suivante dans votre terminal :


pip install datasets spacy
Instructions
Clonez ce dépôt sur votre machine locale.

Exécutez le script Python tokenization_script.py en utilisant la commande suivante :

python tokenization_script.py
Assurez-vous d'être connecté à Internet, car le script téléchargera le modèle de données Allociné depuis Hugging Face.

Le script affichera l'avis original ainsi que les tokens obtenus à partir de la tokenisation avec SpaCy.

Remarque
Ce script utilise le jeu de données Allociné fourni par Hugging Face Datasets. Assurez-vous d'avoir une connexion Internet active lors de l'exécution du script pour télécharger le jeu de données.

Le modèle de langue française de SpaCy (fr_core_news_sm) est utilisé pour la tokenisation. Si vous n'avez pas encore installé ce modèle, SpaCy le téléchargera automatiquement lors de la première exécution.
