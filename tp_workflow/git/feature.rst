.. _feature:

.. index:: 
  double: gitflow; feature

========================
Développer une 'feature'
========================

Nous sommes prêts pour développer notre première 'feature'. Et nous le faisons dans une branche spécifique, pour bien isoler le développement sans rien casser ni dans la branche de développement, ni surtout dans la branche de production ('master'). Cette encapsulation facilite également le travail à plusieurs : il permet par exemple de proposer à la discussion ou à l'évaluation un développement particulier; il est aussi plus facile de suivre l'évolution d'un développement dans une branche spécifique.

En phase de développement, chacun peut se concentrer sur sa partie et minimiser les risques de conflits.


Démarrer une 'feature'
----------------------

.. code-block:: bash
  :emphasize-lines: 5-6

  $> git flow feature start feature-001
  Basculement sur la nouvelle branche 'feature/feature-001'
  
  Summary of actions:
  - A new branch 'feature/feature-001' was created, based on 'develop'
  - You are now on branch 'feature/feature-001'
  
  Now, start committing on your feature. When done, use:
  
       git flow feature finish feature-001

Cette commande crée une nouvelle branche de développement, nommée 'feature/feature-001', basée sur la branche de développement. Et y bascule automatiquement. Bon, dans la vraie vie, on aurait donné un nom beaucoup plus explicite à notre branche …

Vérifions que la branche a bien été créée et que nous y sommes installés :

.. code-block:: bash
  :emphasize-lines: 2

  $> git status
  Sur la branche feature/feature-001
  rien à valider, la copie de travail est propre
  

Travailler
----------

Développons notre 'feature' …

.. code-block:: bash

  $> cat >> Readme
  
  Some details there …
  [CTRL-D]

.. Et vérifions (on débute …) :
.. 
.. .. code-block:: bash
..   :emphasize-lines: 4-5
.. 
..   $> hg summary
..   parent: 3:38f08ad380e3 tip
..    hg flow, add branch `feature/feature-001`.
..   branch: feature/feature-001
..   commit: 1 modified
..   update: (current)
.. 
.. 

On commit chaque fois que nécessaire; allons-y :

.. code-block:: bash

  $> git commit -a -m "Why I did this 2nd ci"
  [feature/feature-001 17706ee] Why I did this 2nd ci
   1 file changed, 2 insertions(+)


Graphiquement, voici la situation, normalement :

.. figure:: /_static/images/feature-branches-0.png
  :align: center




Terminer la 'feature'
---------------------

Maintenant que notre fonctionnalité est développée, nous pouvons l'intégrer dans la branche de développement. On fusionne le contenu de la branche 'feature/feature-001' avec la branche de développement et la branche 'feature/feature-001' est fermée :

.. code-block:: bash

  $> git flow feature finish feature-001
  Basculement sur la branche 'develop'
  Mise à jour 7c1b223..17706ee
  Fast-forward
   Readme | 2 ++
   1 file changed, 2 insertions(+)
  Branche feature/feature-001 supprimée (précédemment 17706ee).
  
  Summary of actions:
  - The feature branch 'feature/feature-001' was merged into 'develop'
  - Feature branch 'feature/feature-001' has been removed
  - You are now on branch 'develop'


.. figure:: /_static/images/feature-branches-1.png
  :align: center

Vérifions que nous avons bien réintégré la branche de développement :

.. code-block:: bash
  :emphasize-lines: 2

  $> git status
  Sur la branche develop
  rien à valider, la copie de travail est propre
  

Jetons un coup d'oeil aux branches :

.. code-block:: bash
  :emphasize-lines: 2

  $> git branch -a
  * develop
    master
  


Développer plusieurs 'features' en parallèle
--------------------------------------------

Pour mieux apprécier encore (!) l'utilisation de ce 'workflow', développons en parallèle deux 'features'; chacune dans sa branche, sans se marcher sur les pieds.

Commençons par développer une nouvelle fonctionnalité :

.. code-block:: bash

  $> git flow feature start feature-002
  Basculement sur la nouvelle branche 'feature/feature-002'
  
  Summary of actions:
  - A new branch 'feature/feature-002' was created, based on 'develop'
  - You are now on branch 'feature/feature-002'
  
  Now, start committing on your feature. When done, use:
  
       git flow feature finish feature-002
  $> cat >> Readme
  Feature work 002
  [CTRL-D]
  $> git commit -a -m "Feature"
  $> sed -i -e 's/002/002 - more/' Readme
  $> git commit -a -m "Feature"
  

Vérifions :

.. code-block:: bash
  :emphasize-lines: 2,6-9

  $> git status
  Sur la branche feature/feature-002
  rien à valider, la copie de travail est propre
  
  $> more Readme
  This is the Readme file
  
  Some details there …
  Feature work 002 - more


Bon, l'algorithme se corse, faisons une pause pour laisser murir et passons au développement de notre autre 'feature' avant d'avoir perdu le fil … :

.. code-block:: bash

  $> git flow feature start feature-003
  

Examinons les choses :

.. code-block:: bash
  :emphasize-lines: 2,6-8

  $> git status
  Sur la branche feature/feature-003
  rien à valider, la copie de travail est propre

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
  $> git commit -a -m "More changes for feature 003"
  

Au passage, remarquons que nous sommes capables de passer simplement d'une branche de 'feature' à l'autre :

.. code-block:: bash

  $> git flow feature list
    feature-002
  * feature-003
  $> git branch -a
    develop
    feature/feature-002
  * feature/feature-003
    master

.. code-block:: bash
  :emphasize-lines: 2,5

  $> git checkout feature/feature-002
  Basculement sur la branche 'feature/feature-002'
  $> more Readme
  $> git checkout feature/feature-003
  Basculement sur la branche 'feature/feature-003'
  $> more Readme
  


Maintenant, après avoir longuement discuté avec les collègues (et pour les besoins du tp …), on décide d'arrêter là les développements de nos nouvelles fonctionnalités; et on décide donc d'intégrer celles-ci dans la branche de développement ('develop'). Terminons donc la première :

.. code-block:: bash
  :emphasize-lines: 3

  $> git flow feature finish feature-002
  $> git status
  Sur la branche develop
  rien à valider, la copie de travail est propre
  


Et terminons la seconde :

.. code-block:: bash

  $> git flow feature finish feature-003 -m "Feature-003 implemented"
  Déjà sur 'develop'
  Fusion automatique de Readme
  CONFLIT (contenu) : Conflit de fusion dans Readme
  La fusion automatique a échoué ; réglez les conflits et validez le résultat.
  
  There were merge conflicts. To resolve the merge conflict manually, use:
      git mergetool
      git commit
  
  You can then complete the finish by running it again:
      git flow feature finish feature-003

Cette fois-ci, les choses se compliquent : il y a conflit puisque, bien que travaillant dans des espaces séparés, nous avons modifié le même fichier et aux mêmes endroits de surcroît ! Il nous faut résoudre le conflit à la main; ici, on peut le faire simplement en éditant le fichier *Readme*, dans la vraie vie, on aura intérêt à utiliser un outil de fusion graphique et à dire à M. DVCS de nous le proposer à ces occasions.

.. code-block:: bash

  $> vi Readme
  $> > git commit -a -m "Added feature-003"
  [develop a170eb2] Added feature-003
  $> git flow feature finish feature-003 -m "Feature-003 implemented"
  
Vérifions :

.. code-block:: bash

  $> git status
  Sur la branche develop
  rien à valider, la copie de travail est propre

  $> more Readme
  This is the Readme file

  Some details there …
  Feature work 002 - more
  Feature work 003
  
  
  
.. figure:: /_static/images/feature-branches-3.png
  :align: center

.. code-block:: bash

  $> git branch -a
  * develop
    master
  


