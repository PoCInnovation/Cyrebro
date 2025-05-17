# Dataset

## 🔍 Input de base
Nous avions prévu d’utiliser comme dataset un questionnaire rempli par un patient (sous forme de questions-réponses).

## ⚠️ Problème
Ce type de données ne permet pas d’entraîner efficacement un LLM à tenir une conversation médicale, car :

- le format est trop rigide (Q/R),
- il manque le contexte et les nuances de la discussion,
- aucune logique de dialogue fluide entre patient et clinicien.

## 💡 Solution
Créer de la donnée synthétique en transformant les questions-réponses en une fausse conversation naturelle entre un clinicien et un patient.

## 🧪 Exemple

### 🔸 Format original (Questionnaire Q/R)
- **Q :** Comment vous sentez-vous ces derniers temps ?  
  **R :** Je me sens fatigué et démotivé.
- **Q :** Avez-vous des problèmes de sommeil ?  
  **R :** Oui, je dors trop ou parfois pas du tout.
- **Q :** Avez-vous perdu l'appétit ?  
  **R :** Oui, je saute des repas.
- **Q :** Depuis combien de temps cela dure-t-il ?  
  **R :** Depuis environ 3 semaines.
- **Q :** Ressentez-vous un manque d'intérêt pour les choses que vous aimiez ?  
  **R :** Oui, je ne prends plus plaisir à rien.

### 🔹 Format conversationnel (donnée synthétique pour le LLM)
- **Clinicien :** Bonjour, comment vous vous sentez ces derniers temps ?  
  **Patient :** Honnêtement… je me sens épuisé, sans énergie. Et j’ai de plus en plus de mal à rester motivé.
- **Clinicien :** Je comprends. Est-ce que vous avez remarqué des changements dans votre sommeil ?  
  **Patient :** Oui, totalement… parfois je dors toute la journée, parfois je n’arrive pas à dormir du tout.
- **Clinicien :** Et concernant l’appétit ?  
  **Patient :** Pareil, j’ai pas vraiment faim, je saute souvent les repas.
- **Clinicien :** Cela dure depuis combien de temps environ ?  
  **Patient :** Ça fait trois semaines que ça va pas…
- **Clinicien :** Est-ce que vous ressentez encore du plaisir dans les choses que vous aimiez faire ?  
  **Patient :** Non, plus rien ne me fait envie en ce moment…

# Quantité de données
Il faudrait au moins 100 000 dialogues pour un fine-tuning pertinent.
Il est possible de faire de la data augmentation en demandant à un gros modèle de reformuler un dialogue (X2-3 sur le dataset).

# Pipeline

## Mise en forme du dataset
Transformer les données initiales sous forme de dialogue/conversation.

## Fine-tuning supervisé
Entraîner le modèle sur l’ensemble du dataset.

## Création de nouveaux datasets
- Générer une liste de questions ou de débuts de conversation.
- Pour chaque item, le LLM fine-tuné produit deux réponses différentes.
- Un LLM plus puissant (ou un modèle spécialisé) évalue ces deux réponses et sélectionne la meilleure.

## DPO
Appliquer un DPO sur ce nouveau dataset pour affiner le modèle, améliorer sa précision et réduire les erreurs récurrentes.