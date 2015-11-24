.. _hotfix:

.. index:: 
  pair: gitflow; hotfix
  pair: gitflow; maintenance

==================================
Branche de maintenance ou 'hotfix'
==================================


Il arrive qu'on remonte des problèmes dans l'environnement de production ! Une branche 'hotfix' est alors utilisée pour corriger ce qui peut l'être facilement. C'est une branche utilisée uniquement pour de petites interventions simples sur le code de production. C'est la seule branche qui part directement de la branche de production 'master'. Dès que la correction est faite, elle est fusionnée à la fois avec la branche de développement et avec la branche de production et celle-ci est taguée avec un nouveau numéro de version. 

Avoir une telle branche de développement dédiée aux corrections de bug permet de les corriger sans gêner le reste du processus de développement. Illustrons cette remarque en créant une nouvelle branche 'feature' avant de traiter la remontée d'un gros bug, suite à notre dernière 'release' … :

.. code-block:: bash

  $> git flow feature start feature-005
  $> git branch
    develop
  * feature/feature-005
    master
  
  $> cat >> Readme
  Feature 005 in progress
  [CTRL-D]
  $> git commit -a -m "Feature 005"
  
Nous sommes donc en train de travailler sur cette nouvelle fonctionnalité que nous espérons intégrer à la prochaine 'release'. Nous sommes dans la branche 'feature/feature-005'. Arrive ce ticket déposé par l'un de nos utilisateurs et qui signale un bug aussi inattendu que majeur … On stoppe tout et on démarre une branche de maintenance !


Démarrer un 'hotfix'
--------------------

.. code-block:: bash

  $> git flow hotfix start bug-001
  Basculement sur la nouvelle branche 'hotfix/bug-001'
  
  Summary of actions:
  - A new branch 'hotfix/bug-001' was created, based on 'master'
  - You are now on branch 'hotfix/bug-001'
  
  Follow-up actions:
  - Bump the version number now!
  - Start committing your hot fixes
  - When done, run:
  
       git flow hotfix finish 'bug-001'

On crée une nouvelle branche 'hotfix/bug-001' basée sur la branche de production 'default'. Et on y bascule automatiquement.

.. code-block:: bash
  :emphasize-lines: 2,7

  $> git status
  Sur la branche hotfix/bug-001
  rien à valider, la copie de travail est propre
  $> git branch
    develop
    feature/feature-005
  * hotfix/bug-001
    master


Correction
----------

Bon, dans notre cas, la correction est plus simple qu'on ne pouvait le craindre ! Alors, corrigeons :

.. code-block:: bash

  $> sed -i -e 's/…/ - Hotfix needed …/' Readme
  $> git commit -a -m "Bug fixed"



Terminer le 'hotfix'
--------------------

.. code-block:: bash

  $> > git flow hotfix finish bug-001
  Basculement sur la branche 'master'
  Merge made by the 'recursive' strategy.
   Readme | 2 +-
   1 file changed, 1 insertion(+), 1 deletion(-)
  Basculement sur la branche 'develop'
  Merge made by the 'recursive' strategy.
   Readme | 2 +-
   1 file changed, 1 insertion(+), 1 deletion(-)
  Branche hotfix/bug-001 supprimée (précédemment 62e2f6d).
  
  Summary of actions:
  - Latest objects have been fetched from 'origin'
  - Hotfix branch has been merged into 'master'
  - The hotfix was tagged 'bug-001'
  - Hotfix branch has been back-merged into 'develop'
  - Hotfix branch 'hotfix/bug-001' has been deleted
  
On clôt la branche 'hotfix/bug-001', en fusionnant dans la branche de production 'master' ainsi que dans la branche de développement 'develop' tout en étiquetant également la branche de production.

Vérifications :

.. code-block:: bash
  :emphasize-lines: 4

  $> hg summary
  $> hg tags
  tip                               29:fef4a6d0b98b
  bug-001                           25:fd972dacbc89
  0.1                               17:86bbebe8080e
  
.. code-block:: bash
  :emphasize-lines: 2,7

  $> git status
  Sur la branche develop
  rien à valider, la copie de travail est propre
  $> git branch
  * develop
    feature/feature-005
    master
  
Illustration graphique :

.. figure:: /_static/images/maintenance-1.png
  :align: center


Reprendre et finir le travail en cours
--------------------------------------

On peut maintenant retourner dans la branche de 'feature' et continuer le développement en cours :

.. code-block:: bash
  :emphasize-lines: 5

  $> git checkout feature/feature-005
  Basculement sur la branche 'feature/feature-005'
  $> git branch
    develop
  * feature/feature-005
    master
  
  
On peut également vérifier que la branche de 'feature' a été créée avant le report du 'bugfix' dans la branche de développement :

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

  $> git show master:Readme
  This is the Readme file
  
  Some details there  - Hotfix needed …
  Feature work 002 - more
  Feature work 003 - done
  
On peut vouloir simplement récupérer le 'bugfix', si celui-ci est nécessaire pour le développement de la 'feature' en cours :

.. code-block:: bash

  $> git merge develop
  Fusion automatique de Readme
  Merge made by the 'recursive' strategy.
   Readme | 2 +-
   1 file changed, 1 insertion(+), 1 deletion(-)
   
  $> more Readme
  This is the Readme file

  Some details there  - Hotfix needed …
  Feature work 002 - more
  Feature work 003 - done
  Feature 005 in progress

Finir le travail et clore le développement de la 'feature' :

.. code-block:: bash
  :emphasize-lines: 4,8

  $> sed -i -e 's/003/003 - more/' Readme
  $> git commit -a -m "Work in progress"
  $> git flow feature finish feature-005
  Basculement sur la branche 'develop'
  Merge made by the 'recursive' strategy.
   Readme | 3 ++-
   1 file changed, 2 insertions(+), 1 deletion(-)
  Branche feature/feature-005 supprimée (précédemment 21f5bf2).
  
  Summary of actions:
  - The feature branch 'feature/feature-005' was merged into 'develop'
  - Feature branch 'feature/feature-005' has been removed
  - You are now on branch 'develop'
  



