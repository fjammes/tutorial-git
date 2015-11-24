.. _initialisation:

.. index:: 
  double: hgflow; init

==========================
Initialiser son 'workflow'
==========================


Création du dépôt
*****************

.. code-block:: bash

  $> cd /MES/PROJETS
  $> hg init tst-hgflow && cd tst-hgflow

On vérifie :

.. code-block:: bash
  :emphasize-lines: 3
  
  $> hg summary
  parent: -1:000000000000 tip (empty repository)
  branch: default
  commit: (clean)
  update: (current)


Initialisation de hgflow
************************

.. code-block:: bash
  
  $> hg flow init


On répond aux différentes questions, mais les valeurs par défaut conviennent très bien :

.. code-block:: bash

  Branch name for production release : [default] 
  Branch name for "next release" development : [develop] 
  
  How to name your supporting branch prefixes?
  Feature branches? [feature/] 
  Release branches? [release/] 
  Hotfix branches? [hotfix/] 
  Version tag prefix? [] 


On vérifie qu'on est bien d'ores et déjà dans la branche de développement :

.. code-block:: bash
  :emphasize-lines: 4

  $> hg summary
  parent: 1:11852b8a4960 tip
   hg flow init, add branch develop
  branch: develop
  commit: (clean)
  update: (current)
  

Si on représente graphiquement la situation :

.. figure:: /_static/images/historical-branches-0.png
  :align: center


Premier commit
**************

Finissons de mettre en place notre travail en créant un premier fichier - nous sommes bien dans la branche de développement :

.. code-block:: bash
  :emphasize-lines: 9-10

  $> cat > Readme
  This is the Readme file
  [CTRL-D]
  
  $> hg status 
  $> hg commit -A -m "Added Readme"
  $> hg summary
  parent: 2:df8f192486fd tip
   Added Readme
  branch: develop
  commit: (clean)
  update: (current)
  

.. figure:: /_static/images/historical-branches-1.png
  :align: center


Bon, voilà : nous avons mis les choses en place. Pour le moment tout va bien … !
  