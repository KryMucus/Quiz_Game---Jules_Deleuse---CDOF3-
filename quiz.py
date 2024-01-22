import random

def poser_question(question, reponses, reponse_correcte):
    print(question)
    for lettre, reponse in reponses.items():
        print(f"{lettre}) {reponse}")

    choix_utilisateur = input("Votre réponse (lettre) : ").lower()
    return choix_utilisateur == reponse_correcte

def lancer_quiz(questions):
    score = 0
    for question, infos in questions.items():
        reussi = poser_question(question, infos["reponses"], infos["reponse_correcte"])
        if reussi:
            print("Bonne réponse !")
            score += 1
        else:
            print("Mauvaise réponse.")
    print(f"Votre score final : {score}/{len(questions)}")

if __name__ == "__main__":
    questions = {
        "Quelle est la capitale de la France ?": {
            "reponses": {"a": "Lyon", "b": "Marseille", "c": "Paris"},
            "reponse_correcte": "c"
        },
        "Quel est le plus grand océan du monde ?": {
            "reponses": {"a": "Océan Atlantique", "b": "Océan Pacifique", "c": "Océan Indien"},
            "reponse_correcte": "b"
        },
        "Qu'est-ce qu'une attaque de phishing en cybersécurité ?": {
            "reponses": {"a": "Une attaque visant à perturber un site web", "b": "Une attaque visant à voler des informations sensibles en se faisant passer pour légitime", "c": "Une attaque visant à bloquer l'accès à un réseau"},
            "reponse_correcte": "b"
        },
        "Quelle est la principale fonction d'un pare-feu (firewall) dans un réseau informatique ?": {
            "reponses": {"a": "Protéger contre les incendies", "b": "Filtrer le trafic réseau pour bloquer les menaces potentielles", "c": "Améliorer la vitesse de la connexion Internet"},
            "reponse_correcte": "b"
        },
        "Que signifie l'acronyme VPN en cybersécurité ?": {
            "reponses": {"a": "Vraiment Pas Nécessaire", "b": "Virtual Private Network", "c": "Vraiment Pas Sûr"},
            "reponse_correcte": "b"
        },
        "Quelle est la méthode la plus courante pour protéger un mot de passe en ligne ?": {
            "reponses": {"a": "Partager le mot de passe avec des amis", "b": "Utiliser un mot de passe simple et facile à retenir", "c": "Utiliser un gestionnaire de mots de passe et créer des mots de passe forts"},
            "reponse_correcte": "c"
        },
        "Qu'est-ce qu'une vulnérabilité 'zero-day' en sécurité informatique ?": {
            "reponses": {"a": "Une vulnérabilité qui n'existe pas", "b": "Une vulnérabilité qui est déjà connue et corrigée", "c": "Une vulnérabilité fraîchement découverte qui n'a pas encore de correctif disponible"},
            "reponse_correcte": "c"
        }
            # Ajoutez d'autres questions ici
        }

    lancer_quiz(questions)

