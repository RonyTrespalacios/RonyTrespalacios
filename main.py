import requests
import subprocess
import time

# URL de la API
joke_url = "https://v2.jokeapi.dev/joke/Programming"

def get_joke():
    while True:
        response = requests.get(joke_url)
        joke_data = response.json()
        
        # Verifica si la broma es de tipo "single"
        if joke_data.get("type") == "single":
            return joke_data["joke"]
        
        # Verifica si la broma es de tipo "twopart"
        elif joke_data.get("type") == "twopart":
            return f"{joke_data['setup']}\n{joke_data['delivery']}"
        
        else:
            print("Unexpected joke type. Trying again...")
            time.sleep(1)

def update_readme(joke):
    # Lee el contenido original del README.md
    with open("README.md", "r", encoding="utf-8") as readme_file:
        original_content = readme_file.readlines()

    # Busca la línea donde se agregó la broma anterior
    joke_index = None
    for i, line in enumerate(original_content):
        if line.startswith("## Joke of the Day"):
            joke_index = i
            break

    # Si ya había una broma, elimina la línea
    if joke_index is not None:
        original_content = original_content[:joke_index]

    # Agrega la nueva broma al final del README.md
    new_content = "".join(original_content) + "\n## Joke of the Day\n" + joke + "\n"

    # Escribe el contenido actualizado en el README.md
    with open("README.md", "w", encoding="utf-8") as readme_file:
        readme_file.write(new_content)

def git_commit_push():
    # Comandos de Git que se ejecutarán
    commands = [
        "git add README.md",
        'git commit -m "Update README.md with new joke"',
        "git push origin main"
    ]

    # Ejecutar cada comando
    for command in commands:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            print(f"Error ejecutando el comando: {command}")
            print(stderr.decode("utf-8"))
        else:
            print(stdout.decode("utf-8"))

def main():
    while True:
        joke = get_joke()
        print(f"Joke to add: {joke}")
        user_input = input("Do you want to add this joke to README.md? (Y/N): ").strip().upper()
        
        if user_input == "Y":
            update_readme(joke)
            git_commit_push()
            print("Joke added and changes pushed to GitHub.")
            break
        elif user_input == "N":
            print("Fetching a new joke...")
        else:
            print("Invalid input. Please enter Y or N.")

if __name__ == "__main__":
    main()