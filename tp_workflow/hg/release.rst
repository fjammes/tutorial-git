.. _release:

.. index:: 
  double: hgflow; release

==========
'Releaser'
==========


Une fois terminé le développement des fonctionnalités, corrigé les bugs, on produit une release en environnement de production. Peut-être également devons-nous fournir cette 'release' à une date fixée (avant la fin de l'atelier ;-) !). 

La branche de release a pour objet de séparer la préparation de la release des nouveaux développements en cours ou prévus (et qui ne figureront pas dans cette release).
Le code est, à ce moment-là, contrôlé soigneusement. C'est la phase de test.


Démarrer une 'release'
----------------------

.. code-block:: bash

  $> hg flow release start 0.1

On crée ici une nouvelle branche nommée 'release/0.1', basée sur la branche de développement, et on y bascule automatiquement.

Lorsqu'on démarre une branche de 'release', cela signifie qu'on passe en phase de test. Tous les bugs trouvés doivent être corrigés là, dans la branche 'release/<release_name>'. Il ne devrait pas y avoir de nouvelles fonctionnalités développées pour cette release.

Vérifions que la branche a bien été créée et que nous y sommes installés :

.. code-block:: bash
  :emphasize-lines: 4

  $> hg summary
  parent: 16:ab9c2ef3bde1 tip
   hg flow, add branch `release/0.1`.
  branch: release/0.1
  commit: (clean)
  update: (current)


Préparer la 'release'
---------------------

Ici, nous nous contentons de rajouter un fichier :

.. code-block:: bash

  $> cat > Release
  Release 0.1
    - proof of concept
  [CTRL-D]
  $> hg commit -A -m "Release notes"


Terminer la 'release'
---------------------

C'est très simple :

.. code-block:: bash

  $> hg flow release finish 0.1

On clôt la branche 'release/0.1', en fusionnant dans la branche de production 'default' ainsi que dans la branche de développement 'develop' et on étiquette également la branche de production.

Vérifications :

.. code-block:: bash
  :emphasize-lines: 4

  $> hg summary
  parent: 21:953b460ec9f5 tip
   hg flow, merge release `0.1` to develop branch `develop`
  branch: develop
  commit: (clean)
  update: (current)
  
  $> hg branches -c
  develop                       21:953b460ec9f5
  default                       20:40d06e99260a
  release/0.1                   19:b5abf7223aff (closed)
  feature/feature-003           14:1168bd9e02e8 (closed)
  feature/feature-002           12:0e44e74c587c (closed)
  feature/feature-001            5:1df13b8c8a91 (closed)
  
  $> hg tags
  tip                               21:953b460ec9f5
  0.1                               17:86bbebe8080e
  
  
Illustration graphique :

.. figure:: /_static/images/release-branches-1.png
  :align: center

