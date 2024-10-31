import os
import sys
import django
import re

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'budgetproject.settings')
django.setup()

badhash = sys.argv[1] if len(sys.argv) > 1 else "c1a4be04b972b6c17db242fc37752ad517c29402"
goodhash = sys.argv[2] if len(sys.argv) > 2 else "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"

def replace_assert_equals():
    test_directory = 'budget/tests'  # Update this to your test directory
    for dirpath, _, filenames in os.walk(test_directory):
        for filename in filenames:
            if filename.endswith('.py'):  # Only process Python files
                filepath = os.path.join(dirpath, filename)
                with open(filepath, 'r') as file:
                    content = file.read()
                
                # Replace assertEquals with assertEqual
                updated_content = re.sub(r'\bassertEquals\b', 'assertEqual', content)
                
                # Write changes back to the file if changes were made
                if content != updated_content:
                    with open(filepath, 'w') as file:
                        file.write(updated_content)
                    print(f"Updated {filepath}: replaced assertEquals with assertEqual")


# Démarrer git bisect
os.system(f"git bisect start {badhash} {goodhash}")

# Exécuter le test avec git bisect
result = os.system("git bisect run pytest")  # ou votre commande de test
if result != 0:
    print("Tests failed.")
    os.system("git bisect reset")
    sys.exit(result)
# Terminer git bisect
os.system("git bisect reset")
