# Les LLM des entreprises

## **Woebot Health :**

Woebot a été créer en 2017. Elle propose un produit appelé Woebot qui est un « compagnon conversationnel basé sur l’IA ». Il a été conçu pour offrir un soutien psychologique accessible en permanence sans toute fois remplacé le travail des soignants.

**Médical :**

D’un point de vue médicale Woebot se base principalement sur trois types de thérapies :
- La thérapie cognitivo-comportemental (TCC)
- La thérapie interpersonnelle (TIP)
- La thérapie comportementale dialectique (TCD)

**Technique :**

Woebot est basé sur un NLP (Natural Language Processing) afin de rendre la discussion plus naturelle et donc plus chaleureuse/amicale.

- Interprété l’intention derrière le message
- Détecte les émotions et les schémas cognitif
- Choisit une réponse parmi une base de contenus psychothérapeutique qui ont été validé cliniquement, tout en tenant compte du contexte.

**Woebot n’est pas une IA générative mais un moteur de dialogue contrôlé. Ce choix est volontaire afin de prioriser la sécurité dans les réponses apportées.**

Woebot repose sur un arbre de décision dynamiques, qui a été enrichie en utilisant du machine learning.

- Chaque échange suit un flux thérapeutique selon le module (module de gestion du stress ou de gestion des pensées négatives).
- Les scénarios ont été conçu par des psychologues cliniciens.
- L’IA sélectionne le prochain noeud en fonction des réponses de l’utilisateur

Les réponses sont donc basées sur des règles et un arbre de décision :

- Comme Woebot n’est pas une IA générative « pur », il repose en partie sur des arbres de décision pour gérer les dialogues de manière dirigé. Ces arbres ont été conçu pour suivre des parcours thérapeutiques spécifique en fonction de ce que choisi l’utilisateur.

**Ce système permet d’avoir une expérience personnalisée tout en restant dans un cadre sur et en cohérence avec les principes thérapeutique.**

Pour gérer les dépendances temporelles, il semblerait que Woebot utilise le « Long Short-Term Memory » (LSTM) couplé avec un « Recurent Neuronal Networks » (RNN).
Le LSTM est un type de réseau de neurones récurent (RNN) qui est conçu pour « apprendre les dépendances à long terme dans les séquences de données » grâce à une architecture qui régule le flux d’information via des portes (entrée, oublie, sortie). Ce qui permet donc d’éviter d’oublier d’ancienne information.

## **Wysa :**

**Médical :**

But : Apporté un soutien psychologique pour des troubles telle que :

- Le stress
- L’anxiété
- La dépression légère à modéré
- Rumination mentale
- Trouble du sommeil

Wysa n’est pas là pour remplacer les thérapeutes mais plutôt comme un complément qui est disponible tout le temps. Il est aussi anonyme, ce qui permet de mieux s’ouvrir.

Les approches thérapeutiques utilisé :

- TCC (Thérapie Cognitivo-Comportemental)
- ACT (Acceptance and Commitment Therapy)
- Méditation guider et “Mindfulness”
- Exercice de respiration et d’ancrage corporel

Limite :

- Ne donne pas de diagnostique
- Pas adapté aux situations de crise (pensée suicidaire)
- Plus utile comme traitement de prévention/accompagnement qu’en intensif

### Technique

**NLP rules based / Machine learning :**

- Le modèle détecte l’intention de l’utilisateur et permet de rediriger vers la bonne réponse pré-écrite, ou le bon exercice;

Tout comme Woebot, wysa n’est pas une IA générative :

- IA restreinte, entraîné pour comprendre les intentions et les émotions de l’utilisateur
- Choisi des réponses prédéfinis, enrichis avec de tout petite variations pour éviter d’être répétitif.

