
# Alignment free - TP 1

L'objectif du TP est de comparer 5 especes de bactéries entre elles.
Vous trouverez les données en suivant [ce lien](https://we.tl/t-ACiDxJko7s)

## Composer le TP

Vous devez forker ce projet puis compléter ses fonctions.
Le rendu sera le dépot git dans lequel vous aurrez forké.

Le but est d'obtenir toutes les distances paire à paire des différentes bactéries.
Vous devez compléter le README pour y afficher la matrice des distances des bactéries.
Vous devez également y indiquer le temps d'exécution qu'il a fallu pour calculer cette matrice ainsi que l'espace mémoire maximale. Pour cela vous pouvez utiliser la commande ```/usr/bin/time -v```.



En observant les distances obtenues, que pouvez-vous dire des espèces présentes dans cet échantillon ?

On precise que ici on mesure une similarité avec l'indice de jaccard, la notion de distance n'est pas vraiment existante (il suffit juste de faire 1 - similarité pour retrouver la distance de Jaccard).

            Seq1        Seq2       Seq3      Seq4        Seq5
Seq1  [[0.         0.01360741 0.01580614 0.00967742 0.01246676]
Seq2   [0.         0.         0.67850894 0.02501316 0.02772614]
Seq3  [0.         0.         0.         0.02432211 0.02700035]
Seq4  [0.         0.         0.         0.         0.96858637]
Seq5  [0.         0.         0.         0.         0.        ]]


A partir de la matrice de distance ci-dessus on remarque une tres grande similarité entre les especes 4 et 5, et une similarité moyenne entre les especes 2 et 3. Les similarité des combinaisons restantes sont faibles. 

Temps d'execution :  119.84506011009216
Espace disque utilisé par le programme : 4493312 octets
