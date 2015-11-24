Introduction au workflow git/hg-flow
====================================

Introduction
------------

Ce document est une version réactualisée et complétée du document, support de l'`atelier <http://devlog.cnrs.fr/jdev2013/t4.a1>`_ 
"Gérer son workflow de développement avec un DVCS" proposé aux `JDev2013 <http://devlog.cnrs.fr/jdev2013>`_ 
et animé par Fabrice Jammes, Frédéric Magniette et Antoine Pérus.

L'exercice permet de tester l'enchaînement logique du 'workflow' implémenté par **gitflow/hgflow** le plus simplement possible 
pour une première fois. Nous allons successivement :

1. initialiser notre environnement
2. développer de façon parallèle des 'features' 
3. produire une 'release'
4. gérer un 'bugfix'

.. figure:: /_static/images/workflow.png
  :align: center
  :scale: 80%


L'atelier
---------

Deux versions, aux fonctionnalités identiques, sont proposées - l'une sous Mercurial, l'autre sous Git :

Mercurial et hgflow :

.. toctree::
   :maxdepth: 1

   Hg/installation          <hg/installation.rst>
   Initialisation           <hg/initialisation.rst>
   Feature                  <hg/feature.rst>
   Release                  <hg/release.rst>
   Hotfix                   <hg/hotfix.rst>

Git et gitflow :

.. toctree::
   :maxdepth: 1

   Git/installation         <git/installation.rst>
   Initialisation           <git/initialisation.rst>
   Feature                  <git/feature.rst>
   Release                  <git/release.rst>
   Hotfix                   <git/hotfix.rst>

.. toctree::
   :maxdepth: 1

   Références               <references.rst>

