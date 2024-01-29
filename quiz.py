import random
import pandas as pd

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

def lancer_quiz(df):
    score = 0
    for index, row in df.iterrows():
        reussi = poser_question(row["Question"], eval(row["Responses"]), row["Correct Response"])
        if reussi:
            print(Fore.GREEN + "Bonne réponse !")
            print(Style.RESET_ALL)
            score += 1
        else:
            print(Fore.RED + "Mauvaise réponse.")
            print(Style.RESET_ALL)
    print(f"Votre score final : {score}/{len(df)}")

def convert_to_csv(questions,name):
    df=pd.DataFrame(columns=["Question","Responses","Correct Response"])
    for i,v in questions.items():
        df.loc[len(df.index)]=[i,v["reponses"],v["reponse_correcte"]]
    df.to_csv(name,index=False)
if __name__ == "__main__":

    #convert_to_csv(questions,"questions.csv")
    df = pd.read_csv('./questions.csv')
    lancer_quiz(df)

