import json
from colorama import Fore,Style

def poser_question(question, reponses, reponse_correcte):
    print(question)
    for lettre, reponse in reponses.items():
        print(f"{lettre}) {reponse}")

    choix_utilisateur = input("Votre réponse (lettre) : ").lower().strip()
    while choix_utilisateur not in reponses.keys():
        print(Fore.YELLOW + "Invalid Response, enter again!")
        choix_utilisateur = input("Votre réponse (lettre) : ").lower().strip()
    return choix_utilisateur == reponse_correcte

def lancer_quiz(questions):
    score = 0
    for question, infos in questions.items():
        reussi = poser_question(question, infos["reponses"], infos["reponse_correcte"])
        if reussi:
            print(Fore.GREEN + "Bonne réponse !")
            print(Style.RESET_ALL)
            score += 1
        else:
            print(Fore.RED + "Mauvaise réponse.")
            print(Style.RESET_ALL)
    print(f"Votre score final : {score}/{len(questions)}")

def load_questions_from_file(filename):
    with open(filename, 'r') as file:
        questions = json.load(file)
    return questions

if __name__ == "__main__":
    lancer_quiz(load_questions_from_file("questions.txt"))