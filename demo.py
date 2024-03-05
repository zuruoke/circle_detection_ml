import subprocess
import sys

def upgrade_packages():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "Flask-WTF", "WTForms"])
        print("Packages upgraded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to upgrade packages: {e}")

# Call the function at the very start of your app.py
upgrade_packages()
