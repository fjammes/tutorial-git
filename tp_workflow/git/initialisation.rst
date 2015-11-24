.. _initialisation:

.. index:: 
  double: gitflow; init

==========================
Initialiser son 'workflow'
==========================


Création du dépôt
*****************

.. code-block:: bash

  $> cd /MES/PROJETS/gitflowtest
  $> git init
  Dépôt Git vide initialisé dans /Users/aperus/Projets/LoOPS/Atelier-DVCS/gitflow/gitflowtest/.git/



Initialisation de gitflow
*************************

On répond aux différentes questions, mais les valeurs par défaut conviennent très bien :

.. code-block:: bash
  
  $> git flow init
  No branches exist yet. Base branches must be created now.
  Branch name for production releases: [master]
  Branch name for "next release" development: [develop]
  
  How to name your supporting branch prefixes?
  Feature branches? [feature/]
  Release branches? [release/]
  Hotfix branches? [hotfix/]
  Support branches? [support/]
  Version tag prefix? []


On vérifie qu'on est bien d'ores et déjà dans la branche de développement :

.. code-block:: bash
  :emphasize-lines: 2

  $> git status
  Sur la branche develop
  rien à valider, la copie de travail est propre
  

Si on représente graphiquement la situation (sauf que notre branche principale s'appelle '*master*' sous Git …) :

.. figure:: /_static/images/historical-branches-0.png
  :align: center


Premier commit
**************

Finissons de mettre en place notre travail en créant un premier fichier - nous sommes bien dans la branche de développement :

.. code-block:: bash
  :emphasize-lines: 7

  $> cat > Readme
  This is the Readme file
  [CTRL-D]
  
  $> git add Readme
  $> git commit -m "Added Readme"
  [develop 7c1b223] Added Readme
   1 file changed, 1 insertion(+)
   create mode 100644 Readme
  $> git status
  Sur la branche develop
  rien à valider, la copie de travail est propre
  

.. figure:: /_static/images/historical-branches-1.png
  :align: center


Bon, voilà : nous avons mis les choses en place. Pour le moment tout va bien … !
  