# **‘Opportunities ans risks of large language models in psychiatry’ : Résumé et interprétation**

[Lien du papier de recherche](attachment:c8701773-d130-4673-a8bc-e511c3807b65:s44277-024-00010-z-1.pdf)

### Implication des LLM dans la santé mentale

**Accès équitable au LLM :**

- Si le LLM est adapté, il peut proposer une liste de soins thérapeutiques au patient pour un problème tel que les phobies
- Le traitement des informations à grande échelle est très coûteux. Il est difficile pour les différents prestataires et institutions d'affiner leurs modèles comme il le faudrait en raison des coûts liés à l'entraînement de ces modèles.
    - **Problème**: Le traitement des données en santé mentale nécessite énormément de précision pour avoir une compréhension et des nuances optimales, ce qui est nécessaire en santé mentale.

**Considération relative à la gestion et aux processus :**

Cette partie traite plus de l'utilisation d'un LLM dans l'organisation et la gestion des patients au sein d'un hôpital ou d'un service spécifique (voir papier de recherche **[ref 19]**). L'IA permettrait de faire des prédictions (sur la mortalité, la durée d'un séjour, réadmission). Possibilité d'améliorer la prise de décision au sein de cliniques ou d'hôpitaux en reformant leur gestion et leurs processus. - Cette partie serait utile dans le cas où le projet serait déployé dans des hôpitaux. Ils pourraient fournir aux soignants des données sur les patients afin de mieux adapter leur soin.

**Risque pour la population liée au LLM** :

Les réflexions apportées dans cette partie semblent concerner les risques de la généralisation de l'IA en santé mentale et non pas les risques que comporte un modèle en particulier. - Les risques : - Remplacement des soignants par des IA et donc baisse de la qualité de la santé mentale de la population. - Interaction agréable : Le ton chaleureux voire amicale de beaucoup d'IA peut présenter des risques. Le risque est que l'utilisateur remplace la socialisation entre humains par l'interaction homme-machine, avec donc des risques d'isolement et de dépendance au modèle. Une recherche (**[ref 22]**) montre ce phénomène sur le bien-être d'étudiants en déployant Facebook dans le campus. Il semble que l'IA pourrait avoir un impact similaire.

Attention : Réguler la durée que passe l'utilisateur sur le produit afin d'éviter les risques énoncés ci-dessus.

### Cadre pour l’évaluation des risques

(https://doi.org/10.48550/arXiv.2306.05949) = Cadre pour examiner l'impact social, l'intégration de préjugés, de stéréotypes, violation de vie privée dans le LLM.

Le LLM est sujet aux préjugés, il faut donc faire attention aux biais qui peuvent arriver de manière inattendue.

- Réponse absurde/fantaisiste -> Risque de désinformation ou de confusion. Encore plus pour les personnes qui souffrent de trouble de la pensée
- Dans le médical, il existe des cadres/directives pour la conception d'IA. Toutefois, il y a souvent dans ces directives un manque de compréhension claire des paramètres de sécurité à évaluer. Mais aussi un manque de composante de surveillance pour contrôler et identifier les avantages et les risques.

### Les possibilités des LLM pour les soin et la recherche psychiatrique

- Grand potentiel des LLM en santé mentale
- 1er application : Évaluation de l’état de santé mentale d’un personne :
    - Évaluer la gravité d'une maladie mentale, suggérer des diagnostics, élaborer des plans de traitement, contrôler l'effet d'une intervention, donner des indicateurs d'évaluation de risque

Cette étude examine si un LLM sans réglage fin, mais formé aux médicales en général, pouvait projeter le fonctionnement psychiatrique d'un individu sur la base de la documentation clinique du patient.

- Résultat : L'équipe a constaté que le LLM a réussi : Ils n'ont pas rejeté l'hypothèse selon laquelle le LLM était aussi performant que les évaluateurs cliniques humains

Cette étude montre le potentiel prometteur de les LLM pour évaluer la santé mentale en interprétant des informations verbales.
Une étude récente a évalué le modèle "LUMEN" qui est un coach thérapeutique qui utilise Alexa en comparant des participants qui reçoivent 8 sessions avec LUMEN par rapport à un groupe témoin. Les résultats ont montré une augmentation de l'activité du cortex préfrontal dorsolatéral qui est liée à de meilleures capacités de résolution de problème et une diminution des stratégies d'évitement. Il y a aussi une légère réduction des symptômes dépressifs et d'anxiété. Cependant l'étude a été menée sur un petit échantillon, et des recherches supplémentaires sont nécessaires

- Ces résultats montrent la vitesse à laquelle évoluent ces technologies. Au-delà de la vitesse de traitement de l’information, utiliser un LLM a d’autres bénéfices :
    - L'utilisateur peut interagir avec le chatbot plus naturellement.
    - Il peut personnaliser le style et le ton employés par le chatbot.
    - Identification de la condition mentale du patient
    - Identification des causes de cette condition mentale
    - Reconnaître les émotions dans une conversation
    - Comprendre les relations entre un événement et sa réponse émotionnelle
- Il y a aussi des inconvénients :
    - Le chatbot est "associé" à une région ou une culture spécifique.
    - Il y a un manque de contrôle et de contraintes sur la manière dont le chatbot dérive du LLM peut et va répondre.
    - Les modèles actuels sont donc limités par des prédictions instables et des modifications mineures des messages-guide.

Pour le futur, il faudra donc avoir une approche qui permet une saisie plus libre pour l'utilisateur en limant la sortie du chatbot pour des raisons sécuritaires.

### Risque des LLM pour les soins et la recherche psychiatrique

- Sortie imprévisible : Les LLM sont non déterministe et peuvent donc donner des réponses inattendu et/ou inexacte.
- Le manque de compréhension dans un contexte donnée : Les réponse généré par les LLM peuvent être inadapté selon le contexte (ex : idée suicidaire) ce qui peut dans certain cas empirée l’état de santé du patient.
- Risque de dépendance des cliniciens : comme on n’a pu le voir il y a un risque que le patient devienne dépendant mais aussi que le clinicien le devienne aussi. Le risque serait alors qu’il ne puisse plus se passer du LLM pour traiter les patient et donc nécessairement réduire le niveau de compétence.

**Établir des “gardes-fous” :**

- Une approche « Responsible AI » : Supervision humaine, analyse des impacts, contrôle humain pour garantir que le LLM est toujours bien aligné avec les principes thérapeutique et ethnique.
- « Red team » : Réaliser des audits sur l’IA en essayant de chercher des vulnérabilités. Ce processus est essentiel à mettre en place avant la mise sur le marché du produit.
- Diversité des tests : Il faut évidemment réaliser des tests sur le LLM, en veillant à la diversité des patients, que ce soit en termes de pathologie ou de culture afin qu’il soit adapté au plus grand nombre.