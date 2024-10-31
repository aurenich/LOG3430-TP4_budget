import os
import sys

# Variables pour les commits (les passer en argument ou définir directement ici)
badhash = sys.argv[1] if len(sys.argv) > 1 else "c1a4be04b972b6c17db242fc37752ad517c29402"
goodhash = sys.argv[2] if len(sys.argv) > 2 else "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"

# Démarrer git bisect
os.system(f"git bisect start {badhash} {goodhash}")

# Exécuter le test avec git bisect
os.system("git bisect run pytest")  # ou votre commande de test, ex: "python manage.py test"

# Terminer git bisect
os.system("git bisect reset")
