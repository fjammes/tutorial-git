
.. LoOPS DVCS slides file, created by
   hieroglyph-quickstart on Wed Aug 21 10:19:52 2013.

.. role:: red
.. role:: barre


============
Atelier DVCS
============

.. rst-class:: center
  
  Un workflow pour collaborer
  

.. image:: /_static/images/gitflow.png
   :align: center
   :scale: 50%

.. rst-class:: center
  
  gitflow & hgflow

.. rst-class:: small
  
  LoOPS - 19 décembre 2013 - A. Pérus



Préambule
=========

.. rst-class:: small

- Présentation et atelier directement tirés de l'atelier similaire proposé aux JDev2013_
  par *Fabrice Jammes*, *Frédéric Magniette* & *Antoine Pérus* (T4.A1)  
- D'après l'article de Vincent Driessen, `"A successful Git branching model" <http://nvie.com/posts/a-successful-git-branching-model>`_
- Ce n'est pas une introduction aux (D)VCS
- Ce n'est pas une comparaison des mérites respectifs de Hg et Git …

.. _JDev2013 : http://devlog.cnrs.fr/jdev2013


Les branches
============

.. image:: /_static/images/arbre.jpg
   :class: fill
   
- Simple divergence de code
- Permettent d'avoir plusieurs lignes de développement parallèles
- On peut nommer les branches
- Une branche est toujours le fork d'une branche
- Les branches peuvent fusionner (merge)
- La fusion peut créer des conflits qu'il faut arbitrer
- Les branches sont permanentes et globales


Manipulation des branches
=========================

- Créer une branche nommée "experimental"

.. code-block:: bash
   
   $> hg branch experimental && hg commit
   $> git checkout -b experimental
   
.. image:: /_static/images/secateur.png
   :align: right
   :scale: 50%

- Voir les branches existantes

.. code-block:: bash
   
   $> hg branches
   $> git branch
   

- Se positionner sur une branche

.. code-block:: bash
   
   $> hg update experimental
   $> git checkout experimental
 
 
Fusionner les branches
======================

Fusionner la branche "experimental" avec sa branche parent "develop"


.. image:: /_static/images/merge.png
   :align: right
   :scale: 70%

- On se place dans la branche "develop"

  .. code-block:: bash
     
     $> hg update develop
     $> git checkout develop

- On fusionne

  .. code-block:: bash
     
     $> hg merge experimental
     $> git merge experimental
     
- On commit le merge

  .. code-block:: bash
     
     $> hg commit
     $> git commit -a
 
 
Résoudre les conflits
=====================


- Parfois au merge, on a un message de conflit

  .. rst-class:: small

  .. code-block:: bash
  
    warning: conflicts during merge.
    merging test.txt incomplete! (edit conflicts, then use 'hg resolve --mark')
  
  .. image:: /_static/images/conflit.gif
     :align: right
     :scale: 50%
  
- Éditer le fichier pour corriger

  .. rst-class:: small

  .. code-block:: bash
  
    <<<<<<< local
    titi
    =======
    toto
    >>>>>>> other
  

- On anonce la résolution du conflit

  .. code-block:: bash
     
     $> hg resolve test.txt –mark
     $> git add test.txt
  
- On refait le merge (hg) et on commit

.. rst-class:: small

Il existe également des outils graphiques très pratiques pour faire ce travail



Des branches et des workflows
=============================

.. image:: /_static/images/branch2workflow.jpg
   :class: fill
   

- But : organiser les processus de développement

  + Séparer les versions de production des versions de développement
  + Limiter les conflits, les compilations cassées
  + Permettre une gestion efficace des bugs
  + Réduire les problèmes inter-developpeurs

.. rst-class:: build

- Comment ?

  + :red:`En créant des branches spécifiques pour chaque usage`


Le modèle de Vincent Driessen 
==============================


.. image:: /_static/images/driessen.png
   :align: center
   :scale: 70%


Le modèle de Vincent Driessen 
==============================

- Deux branches 'historiques'

  + "master" / "default"
  + "develop"

- Des branches de 'features'
- Des branches de 'releases'
- Des branches de maintenance ('hotfix')


.. rst-class:: appear

La branche principale de développement
======================================

.. image:: /_static/images/driessen-develop.png
   :align: center
   :scale: 70%


.. rst-class:: appear

La branche principale de développement
======================================

.. image:: /_static/images/trunk.jpg
   :class: fill
   
- Nommée "develop"
- C'est la branche principale (le tronc)
- Intégration des nouvelles fonctionnalités à partir des développements locaux
- Les commits sont normalemment des intégrations ou des bugfixes
- Dans un VCS centralisé (par ex. SVN), c'est la seule branche



Les branches de features
========================

.. image:: /_static/images/driessen-feature.png
   :align: center
   :scale: 70%


.. rst-class:: appear

Les branches de features
========================

- Nommées "feature/feature-explicit-name"
- Utilisée pour développer une nouvelle fonctionnalité
- Disjointe de la branche principale de développement ("develop")
- Permet de sauvegarder un développement en cours

.. image:: /_static/images/feature.png
   :align: right
   :scale: 45%

- Fusionnée avec "develop" lorsque la fonctionnalité est implémentée et testée
- Avantage : minimise les conflits à la seule fusion 


Les branches de releases-candidates
===================================

.. image:: /_static/images/driessen-release.png
   :align: center
   :scale: 70%


.. rst-class:: appear

Les branches de releases-candidates
===================================

.. image:: /_static/images/release.png
   :align: right
   :scale: 80%

- Une fois que la branche "develop" contient les fonctionalités requises pour la nouvelle release, 
  on ouvre une nouvelle branche "release"
- Mauvais nommage : release pour rc
- Nommées "release/num-release"
- Branche de test pour validation
- Lorsqu'il n'y a plus de bug, on ferme la branche 

  + Les modifications sont fusionnées dans "develop"
  + Une nouvelle version de production est créée



La chaîne de production
=======================

- Tous les commit sont issus de la fermeture d'une branche de release

.. image:: /_static/images/chaine.jpg
   :align: right
   :scale: 25%

- Les commits sont tagués par le nom de la release (ex v1.0)
- La branche est nommée "default" ou "master" pour permettre un chargement de la version de production au clone 

Les hotfixes
============

.. image:: /_static/images/driessen-hotfix.png
   :align: center
   :scale: 70%


.. rst-class:: appear

Les hotfixes
============

- Si un bug est trouvé dans la branche de production, on crée un "hotfix"
- Branche nommée "hotfix/ref-to-bug"
- On corrige le(s) bug(s) dans la branche "hotfix" puis on le ferme

  + Les modifs sont propagées dans "develop"
  + Une nouvelle release est créée dans la branche de production ("tag")

.. image:: /_static/images/hotfix.jpg
   :align: center
   :scale: 60%


Hgflow et Gitflow
=================

.. image:: /_static/images/hg.png
   :align: right
   :scale: 30%

- Implémentation du concept de V. Driessen sous Mercurial et Git
- Simples fonctions pour automatiser les (quelques) commandes correspondant à chaque action
- Permet d'acquérir une culture et une pratique commune
- Garantit une cohérence du workflow dans une équipe

.. image:: /_static/images/git.png
   :align: left
   :scale: 25%


L'atelier
=========


L’exercice permet de tester l’enchaînement logique du ‘workflow’ implémenté par gitflow/hgflow le plus simplement possible pour une première fois. 


.. image:: /_static/images/maintenance.png
   :scale: 60%
   :align: right

.. rst-class:: small

#. initialisation de l'environnement
#. développement de façon parallèle des ‘features’
#. production d'une ‘release’
#. gestion d'un ‘bugfix’
   
