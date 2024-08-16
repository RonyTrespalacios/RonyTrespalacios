# main.py

# Texto que deseas agregar al final del README.md
additional_content = """
## Updates

- This is an update added by main.py
"""

# Abre el archivo README.md en modo append ('a'), lo que permite agregar contenido al final del archivo
with open("README.md", "a") as readme_file:
    # Agrega el nuevo contenido al final del archivo
    readme_file.write(additional_content)

print("Contenido añadido al README.md")
