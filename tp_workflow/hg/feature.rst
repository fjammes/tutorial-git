.. _feature:

.. index:: 
  double: hgflow; feature

========================
Développer une 'feature'
========================

Nous sommes prêts pour développer notre première 'feature' ou fonctionnalité. Et nous le faisons dans une branche spécifique, pour bien isoler le développement sans rien casser ni dans la branche de développement, ni surtout dans la branche de production ('default'). Cette encapsulation facilite également le travail à plusieurs : il permet par exemple de proposer à la discussion ou à l'évaluation un développement particulier; il est aussi plus facile de suivre l'évolution d'un développement dans une branche spécifique.

En phase de développement, chacun peut se concentrer sur sa partie et minimiser les risques de conflits.


Démarrer une 'feature'
----------------------

.. code-block:: bash

  $> hg flow feature start feature-001

Cette commande crée une nouvelle branche de développement, nommée 'feature/feature-001', basée sur la branche de développement. Et y bascule automatiquement. Bon, dans la vraie vie, on aurait donné un nom beaucoup plus explicite à notre branche …

Vérifions que la branche a bien été créée et que nous y sommes installés :

.. code-block:: bash
  :emphasize-lines: 4

  $> hg summary
  parent: 3:38f08ad380e3 tip
   hg flow, add branch `feature/feature-001`.
  branch: feature/feature-001
  commit: (clean)
  update: (current)
  

Travailler
----------

Développons notre 'feature' …

.. code-block:: bash

  $> cat >> Readme
  
  Some details there …
  [CTRL-D]

Et vérifions (on débute …) :

.. code-block:: bash
  :emphasize-lines: 4-5

  $> hg summary
  parent: 3:38f08ad380e3 tip
   hg flow, add branch `feature/feature-001`.
  branch: feature/feature-001
  commit: 1 modified
  update: (current)


On commit chaque fois que nécessaire; allons-y :

.. code-block:: bash

  $> hg status .
  $> hg commit -m "Why did I do this 2nd ci"


Graphiquement, voici la situation, normalement :

.. figure:: /_static/images/feature-branches-0.png
  :align: center




Terminer la 'feature'
---------------------

Maintenant que notre fonctionnalité est développée, nous pouvons l'intégrer dans la branche de développement. On fusionne le contenu de la branche 'feature/feature-001' avec la branche de développement et la branche 'feature/feature-001' est fermée :

.. code-block:: bash

  $> hg flow feature finish feature-001



.. figure:: /_static/images/feature-branches-1.png
  :align: center

Vérifions que nous avons bien réintégré la branche de développement :

.. code-block:: bash
  :emphasize-lines: 3

  $> hg summary
   hg flow, merge release `feature-001` to develop branch `develop`
  branch: develop
  commit: (clean)
  update: (current)
  

Jetons un coup d'oeil aux branches (option ``-c`` pour avoir les branches closes dans la liste) :

.. code-block:: bash
  :emphasize-lines: 3

  $> hg branches -c
  develop                        6:6a672ed605f8
  feature/feature-001            5:1df13b8c8a91 (closed)
  default                        0:3ad540ced546 (inactive)
  


Développer plusieurs 'features' en parallèle
--------------------------------------------

Pour mieux apprécier encore (!) l'utilisation de ce 'workflow', développons en parallèle deux 'features'; chacune dans sa branche, sans se marcher sur les pieds.

Commençons par développer une nouvelle fonctionnalité :

.. code-block:: bash

  $> hg flow feature start feature-002
  $> cat >> Readme
  Feature work 002
  [CTRL-D]
  $> hg commit -m "Feature"
  $> sed -i -e 's/002/002 - more/' Readme
  $> hg commit -m "Feature"
  

Vérifions :

.. code-block:: bash
  :emphasize-lines: 4,9-12

  $> hg summary
  parent: 9:d4819a6f453f tip
   Feature
  branch: feature/feature-002
  commit: (clean)
  update: (current)
  
  $> more Readme
  This is the Readme file
  
  Some details there …
  Feature work 002 - more


Bon, l'algorithme se corse, faisons une pause pour laisser murir et passons au développement de notre autre 'feature' avant d'avoir perdu le fil … :

.. code-block:: bash

  $> hg flow feature start feature-003
  

Examinons les choses :

.. code-block:: bash
  :emphasize-lines: 4,9-11

  $> hg summary
  parent: 10:f7f85802040f tip
   hg flow, add branch `feature/feature-003`.
  branch: feature/feature-003
  commit: (clean)
  update: (current)

  $> more Readme
  This is the Readme file
  
  Some details there …
  

Ah ah ! Nous sommes bien dans notre nouvelle branche 'feature-003' et nous sommes bien reparti de la branche 'develop', en ignorant tout de ce qui a pu être fait dans d'autres branches de 'features', du moins tant que celles-ci n'ont pas fusionné avec la branche de développement; on peut faire le parallèle avec les transactions du monde des bases de données, une fusion réussie correspondant à un *commit* :

.. figure:: /_static/images/feature-branches-2.png
  :align: center


Bon, implémentons notre nouvelle fonctionnalité :

.. code-block:: bash

  $> cat >> Readme
  Feature work 003
  [CTRL-D]
  $> hg commit -m "More changes for feature 003"
  

Au passage, remarquons que nous sommes capables de passer simplement d'une branche de 'feature' à l'autre - pour autant que nous avons bien tout commité … :

.. code-block:: bash

  $> hg feature feature-002
  $> hg summary
  $> hg feature feature-003
  $> hg summary
  


Maintenant, après avoir longuement discuté avec les collègues (et pour les besoins du tp …), on décide d'arrêter là les développements de nos nouvelles fonctionnalités; et on décide donc d'intégrer celles-ci dans la branche de développement ('develop'). Terminons donc la première :

.. code-block:: bash
  :emphasize-lines: 4-5

  $> hg flow feature finish feature-002
  $> hg summary
  parent: 13:bbb53a7cbf43 tip
   hg flow, merge release `feature-002` to develop branch `develop`
  branch: develop
  commit: (clean)
  update: (current)
  


Et terminons la seconde :

.. code-block:: bash
  :emphasize-lines: 4-5

  $> hg flow feature finish feature-003

Cette fois-ci, les choses se compliquent : il y a conflit puisque, bien que travaillant dans des espaces séparés, nous avons modifié le même fichier et aux mêmes endroits de surcroît ! Il nous faut résoudre le conflit à la main; ici, on peut le faire simplement en éditant le fichier *Readme*, dans la vraie vie, on aura intérêt à utiliser un outil de fusion graphique et à dire à M. DVCS de nous le proposer à ces occasions.

.. code-block:: bash

  $> vi Readme
  $> hg resolve -m Readme
  $> hg commit -m "Merge from feature-003"
  
Vérifions :

.. code-block:: bash

  $> hg summary
  parent: 15:2c4ca008edda tip
   Merge from feature-003
  branch: develop
  commit: (clean)
  update: (current)
  $> more Readme
  This is the Readme file

  Some details there …
  Feature work 002 - more
  Feature work 003
  
  
  
.. figure:: /_static/images/feature-branches-3.png
  :align: center

.. code-block:: bash

  $> hg branches -c
  develop                       15:2c4ca008edda
  feature/feature-003           14:1168bd9e02e8 (closed)
  feature/feature-002           12:0e44e74c587c (closed)
  feature/feature-001            5:1df13b8c8a91 (closed)
  default                        0:3ad540ced546 (inactive)
  


