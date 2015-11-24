.. _release:

.. index:: 
  double: gitflow; release

==========
'Releaser'
==========


Une fois terminé le développement des fonctionnalités, corrigé les bugs, on produit une release en environnement de production. Peut-être également devons-nous fournir cette 'release' à une date fixée (avant la fin de l'atelier ;-) !). 

La branche de release a pour objet de séparer la préparation de la release des nouveaux développements en cours ou prévus (et qui ne figureront pas dans cette release).
Le code est, à ce moment-là, contrôlé soigneusement. C'est la phase de test.


Démarrer une 'release'
----------------------

.. code-block:: bash

  $> git flow release start 0.1
  Basculement sur la nouvelle branche 'release/0.1'
  
  Summary of actions:
  - A new branch 'release/0.1' was created, based on 'develop'
  - You are now on branch 'release/0.1'
  
  Follow-up actions:
  - Bump the version number now!
  - Start committing last-minute fixes in preparing your release
  - When done, run:
  
       git flow release finish '0.1'

On crée ici une nouvelle branche nommée 'release/0.1', basée sur la branche de développement, et on y bascule automatiquement.

Lorsqu'on démarre une branche de 'release', cela signifie qu'on passe en phase de test. Tous les bugs trouvés doivent être corrigés là, dans la branche 'release/<release_name>'. Il ne devrait pas y avoir de nouvelles fonctionnalités développées pour cette release.

Vérifions que la branche a bien été créée et que nous y sommes installés :

.. code-block:: bash
  :emphasize-lines: 2, 7

  $> git status
  Sur la branche release/0.1
  rien à valider, la copie de travail est propre
  $> git branch -a
    develop
    master
  * release/0.1


Préparer la 'release'
---------------------

Ici, nous nous contentons de rajouter un fichier :

.. code-block:: bash

  $> cat > Release
  Release 0.1
    - proof of concept
  [CTRL-D]
  $> git add Release
  $> git commit -m "Release notes"


Terminer la 'release'
---------------------

C'est très simple :

.. code-block:: bash

  $> git flow release finish 0.1
  Basculement sur la branche 'master'
  Merge made by the 'recursive' strategy.
   Readme  | 5 +++++
   Release | 2 ++
   2 files changed, 7 insertions(+)
   create mode 100644 Readme
   create mode 100644 Release
  Basculement sur la branche 'develop'
  Merge made by the 'recursive' strategy.
   Release | 2 ++
   1 file changed, 2 insertions(+)
   create mode 100644 Release
  Branche release/0.1 supprimée (précédemment 6f8f6e3).
  
  Summary of actions:
  - Latest objects have been fetched from 'origin'
  - Release branch has been merged into 'master'
  - The release was tagged '0.1'
  - Release branch has been back-merged into 'develop'
  - Release branch 'release/0.1' has been deleted

On clôt la branche 'release/0.1', en fusionnant dans la branche de production 'master' ainsi que dans la branche de développement 'develop' et on étiquette également la branche de production.

Vérifications :

.. code-block:: bash
  :emphasize-lines: 1

  $> git tag --list
  0.1
  
  
Illustration graphique :

.. figure:: /_static/images/release-branches-1.png
  :align: center

