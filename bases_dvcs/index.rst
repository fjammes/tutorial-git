
.. DVCS : principe et bonnes pratiques slides file, created by
   hieroglyph-quickstart on Wed Aug 21 10:19:52 2013.


=================================================
DVCS : introduction, principe et bonnes pratiques
=================================================

.. figure:: /_static/img/code-tree.jpg
   :class: fill

Historique
==========

Trois générations de systèmes de contrôle de version.

+-----------+----------------------+------------------------+-----------------+
| Réseau    | Opérations           | Concurrence            | Exemples        |
+===========+======================+========================+=================+  
| Aucun     | Mono-fichier         | Verrous                | RCS, SCCS       |
+-----------+----------------------+------------------------+-----------------+
| Centralisé| Multi-fichiers       | Branch/Merge complexe  | CVS, Subversion |
+-----------+----------------------+------------------------+-----------------+
| Distribué | Jeu de modifications | Branch/Merge généralisé| Git, Mercurial  |
+-----------+----------------------+------------------------+-----------------+

|

.. image:: /_static/img/computerhistory.jpg
   :scale: 50 %
   :align: center

Les bases des DVCS
==================

Assez semblables aux outils de deuxième génération. 

4 concepts en plus :

* **clone** : créer un nouveau dépôt en dupliquant un dépôt d'origine
* **push** : copier les changements du dépôt local vers un dépôt distant.
* **pull** : copier les changements d'un dépôt distant vers le dépôt local.
* **les DAG** : des arbres orientés acycliques pour gérer son flux de développement

Clone : créer un nouveau dépôt en dupliquant un dépôt d'origine
===============================================================

Deuxième génération (centralisé) :

.. image:: /_static/img/cvcs_topology.jpg
   :align: center

|

Troisième génération (décentralisé) :

.. image:: /_static/img/dvcs_topology.jpg
   :align: center

Push
====

|

Envoyer un jeu de modifications du dépôt local vers un dépôt distant 

.. image:: /_static/img/op_push.jpg
   :align: center

Les deux dépôts ne sont pas forcément identiques après cette opération.

Pull
====

|

Récupérer un jeu de modifications d'un dépôt distant vers le dépôt local 

.. image:: /_static/img/op_pull.jpg
   :align: center

Synchro complète de deux instance => pull complet du dépôt distant + push complet du dépôt local

Les DAG
=======

Deuxième génération (centralisé) :

.. image:: /_static/img/repo_history_dag_merged.jpg
   :align: center

Troisième génération (décentralisé) :

.. image:: /_static/img/repo_history_dag_chaos.jpg
   :align: center

Avantages : copie privée du dépôt
=================================

**Objectif :** limiter le nombre d'opérations de synchronisation (comme pour le multi-thread)

+-----------------+--------------------------------------------------+-------------------------------------------------+--------------------------------------------------+
| Développeurs    | 1                                                | 4                                               | 10                                               |
+=================+==================================================+=================================================+==================================================+  
|                 |  .. figure:: /_static/img/team_complexity_1.jpg  | .. figure:: /_static/img/team_complexity_5.jpg  | .. figure:: /_static/img/team_complexity_10.jpg  |
+-----------------+--------------------------------------------------+-------------------------------------------------+--------------------------------------------------+
| Connections     | 0                                                | 6                                               | 45                                               |
+-----------------+--------------------------------------------------+-------------------------------------------------+--------------------------------------------------+


Avantages : rapidité
====================

|

Temps d'un commit sur l'arbre entier de Valgrind [#]_ 

+-----------------+-----------------+---------------+----------------+---------+
|   Operation     | Subversion [#]_ |   Bazaar      |    Mercurial   |  Git    |                                                                                 
+=================+=================+===============+================+=========+                 
|    Commit (s)   |    21.9         |    5.2        |       4.6      |  3.2    +                                                                                 
+-----------------+-----------------+---------------+----------------+---------+

|
|


.. [#] Valgrind : 3,143 fichiers; 42 MB
.. [#] svnserve sur 127.0.0.1

Avantages : multi-sites
=======================

|

Plus grande flexibilité dans la gestion des synchronisation entre plusieurs sites.

.. image:: /_static/img/dvcs_geography.jpg
   :align: center

Avantages : répartition de charge
=================================

|

Permet d'alléger la criticité du dépôt central.

|

.. image:: /_static/img/dvcs_scale_out.jpg
   :align: center

Autres avantages
================

|

* Mode non connecté
* Organisation flexible des processus de développement
* Fusion du code plus simple
* Sauvegarde implicite

Inconvénients
=============

* Verrous
* Gestion des très grands dépôt
* Intégration aux autres outils des forges
* Suppressions définitives
* Administration (ACL, utilisateurs)
* Contrôle d'accès par répertoire
* Facilité d'utilisation
* IHM

.. image:: /_static/img/great-developers-slightly-autistic.jpg
   :align: center
   :width: 150 pt

Bonnes pratiques collectives
============================

* Définir le processus de développement dès le début du projet
* Assurer la traçabilité des branches via un outil de gestion de tickets
* Compiler et tester le code automatiquement après chaque commit
* Utiliser des tags pour faciliter la navigation dans les versions

Bonnes pratiques individuelles
==============================

* Revue rapide (diff) avant chaque commit
* Revue rapide des travaux de l'équipe (chaque matin)
* Veiller à la logique des commits
* Commenter l'intérêt de chaque commit
* Conserver les branches de travail fonctionnelles
* Revue des opérations de merge automatique, avant le commit
* Eviter les suppressions définitives
* Ne pas commenter le code lui-même
* Eviter les verrous

Autres bonnes pratiques
=======================

* Garder le dépôt aussi petit que possible (plusieurs dépôts/projet)
* Ne stocker que les objets créés manuellement

.. image:: /_static/img/gitmerge.jpg
   :align: center

Références
==========

| Version Control by Example, Eric Sink 
| http://www.ericsink.com/vcbe/html/

| Comparaison des commandes Git/Mercurial, Eric Sink
| http://www.ericsink.com/vcbe/html/apa.html

| Utilisation de git pour LSST, Mario Juric
| https://dev.lsstcorp.org/trac/wiki/GitDemoAndTutorial

| Documentation de référence de git
| http://git-scm.com/docs/gittutorial

| Tutorial Mercurial
| http://mercurial.selenic.com/wiki/Tutorial
