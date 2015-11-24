.. _hotfix:

.. index:: 
  pair: hgflow; hotfix
  pair: hgflow; maintenance

==================================
Branche de maintenance ou 'hotfix'
==================================


Il arrive qu'on remonte des problèmes dans l'environnement de production ! Une branche 'hotfix' est alors utilisée pour corriger ce qui peut l'être facilement. C'est une branche utilisée uniquement pour de petites interventions simples sur le code de production. C'est la seule branche qui part directement de la branche de production 'default'. Dès que la correction est faite, elle est fusionnée à la fois avec la branche de développement et avec la branche de production et celle-ci est taguée avec un nouveau numéro de version. 

Avoir une telle branche de développement dédiée aux corrections de bug permet de les corriger sans gêner le reste du processus de développement. 
Illustrons cette remarque en créant une nouvelle branche 'feature' avant de nous interrompre pour traiter la remontée d'un gros bug, 
suite à notre dernière 'release' … :

.. code-block:: bash

  $> hg flow feature start feature-005
  $> hg summary
  parent: 22:031a95428dd0 tip
   hg flow, add branch `feature/feature-005`.
  branch: feature/feature-005
  commit: (clean)
  update: (current)
  
  $> cat >> Readme
  Feature 005 in progress
  [CTRL-D]
  $> hg commit -m "Feature 005"
  
Nous sommes donc en train de travailler sur cette nouvelle fonctionnalité que nous espérons intégrer à la prochaine 'release'. Nous sommes dans la branche 'feature/feature-005'. Arrive ce ticket déposé par l'un de nos utilisateurs et qui signale un bug aussi inattendu que majeur … On stoppe tout et on démarre une branche de maintenance !


Démarrer un 'hotfix'
--------------------

.. code-block:: bash

  $> hg flow hotfix start bug-001

On crée une nouvelle branche 'hotfix/bug-001' basée sur la branche de production 'default'. Et on y bascule automatiquement.

.. code-block:: bash

  $> hg summary
  parent: 24:858ce14d6c89 tip
   hg flow, add branch `hotfix/bug-001`.
  branch: hotfix/bug-001
  commit: (clean)
  update: (current)


Correction
----------

Bon, dans notre cas, la correction est plus simple qu'on ne pouvait le craindre ! Alors, corrigeons :

.. code-block:: bash

  $> sed -i -e 's/\.\.\./ - Hotfix needed \.\.\./' Readme
  $> hg commit -m "Bug fixed"



Terminer le 'hotfix'
--------------------

.. code-block:: bash

  $> hg flow hotfix finish bug-001
  
On clôt la branche 'hotfix/bug-001', en fusionnant dans la branche de production 'default' ainsi que dans la branche de développement 'develop' tout en étiquetant également la branche de production.

Vérifications :

.. code-block:: bash
  :emphasize-lines: 4

  $> hg summary
  parent: 29:fef4a6d0b98b tip
   hg flow, merge release `bug-001` to develop branch `develop`
  branch: develop
  commit: (clean)
  update: (current)
  
  $> hg branches -c
  develop                       29:fef4a6d0b98b
  default                       28:6a9f2f22acb6
  feature/feature-005           23:e4273c0d729f
  hotfix/bug-001                27:13755c02b1a6 (closed)
  release/0.1                   19:b5abf7223aff (closed)
  feature/feature-003           14:1168bd9e02e8 (closed)
  feature/feature-002           12:0e44e74c587c (closed)
  feature/feature-001            5:1df13b8c8a91 (closed)
  
  $> hg tags
  tip                               29:fef4a6d0b98b
  bug-001                           25:fd972dacbc89
  0.1                               17:86bbebe8080e
  
  
Illustration graphique :

.. figure:: /_static/images/maintenance-1.png
  :align: center


Reprendre et finir le travail en cours
--------------------------------------

On peut maintenant retourner dans la branche de 'feature' et continuer le développement en cours :

.. code-block:: bash
  :emphasize-lines: 5

  $> hg feature feature-005
  $> hg summary
  parent: 23:e4273c0d729f
   Feature 005
  branch: feature/feature-005
  commit: (clean)
  update: (current)
  
  
On peut également vérifier que la branche de 'feature' a été créée avant le report du 'bug fix' dans la branche de développement :

.. code-block:: bash

   $> more Readme
   This is the Readme file

   Some details there …
   Feature work 002 - more
   Feature work 003
   Feature 005 in progress
   
Pour mémoire, le fichier *Readme*, après correction :

.. code-block:: bash
  :emphasize-lines: 4

  $> hg cat -r default Readme
  This is the Readme file

  Some details there  - Hotfix needed …
  Feature work 002 - more
  Feature work 003
  
On peut vouloir simplement récupérer le 'bug fix', si celui-ci est nécessaire pour le développement de la 'feature' en cours :

.. code-block:: bash
  :emphasize-lines: 5-6,13

  $> hg merge -r develop
  $> hg commit -m "Récupération du bugfix 001"
  $> hg summary
  parent: 30:daa16c5ca6bb tip
   Récupération du bugfix 001
  branch: feature/feature-005
  commit: (clean)
  update: (current)

  $> more Readme
  This is the Readme file
  
  Some details there  - Hotfix needed …
  Feature work 002 - more
  Feature work 003
  Feature 005 in progress

Finir le travail et clore le développement de la 'feature' :

.. code-block:: bash
  :emphasize-lines: 6-7

  $> sed -i -e 's/003/003 - more/' Readme
  $> hg commit -m "Work in progress"
  $> hg flow feature finish feature-005
  $> hg summary
  parent: 33:5898a331f04a tip
   hg flow, merge release `feature-005` to develop branch `develop`
  branch: develop
  commit: (clean)
  update: (current)
  
Visualisons :  

.. code-block:: bash

  $> hg serve
  listening at http://localhost:8000/ (bound to *:8000)
  $> open http://localhost:8000/graph/tip
  
.. figure:: /_static/images/hg-serve-graph.png
  :align: center


