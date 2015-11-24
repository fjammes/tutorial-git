.. _installation:

.. index:: 
  double: git; init
  double: git; download

============
Installation
============

Git
***

Si nécessaire, `télécharger <http://git-scm.com/downloads>`_ le gestionnaire de version Git
et l'installer comme indiqué sur la page de téléchargement. Normalement, l'installation se fait en
double-cliquant sur l'installeur … et ne présente pas de difficultés particulières à traiter ici …

Configurer l'outil en exécutant les commandes suivantes :

.. code-block:: bash

  $> git config --global user.name "Nom prénom"
  $> git config --global user.email "nom.prenom@mon.labo.fr"
  

Script gitflow
**************

Heu … les `instructions d'installation <https://github.com/nvie/gitflow/wiki/Installation>`_ sont détaillées à la page du projet, 
mais on peut récupérer une archive du dépôt `ici <../_static/code/gitflow.tgz>`_, décompresser chez soi et le ranger quelque part, 
par exemple sous ``/usr/local/gitflow.git`` comme dans l'exemple ci-dessous.

Voici un exemple d'installation sous Mac OSX :

.. code-block:: bash
  
  $> cd /usr/local/git-flow.git/contrib
  $> chmod u+x gitflow-installer.sh
  $> INSTALL_PREFIX=~/bin REPO_HOME=/usr/local/gitflow.git ./gitflow-installer.sh
  ### gitflow no-make installer ###
  Installing git-flow to /Users/aperus/bin
  Cloning repo from GitHub to gitflow
  Clonage dans 'gitflow'...
  fait.
  Updating submodules
  Sous-module 'shFlags' (git://github.com/nvie/shFlags.git) enregistr'e pour le chemin 'shFlags'
  Clonage dans 'shFlags'...
  remote: Counting objects: 454, done.
  remote: Compressing objects: 100% (132/132), done.
  remote: Total 454 (delta 337), reused 414 (delta 312)
  Réception d'objets: 100% (454/454), 130.95 KiB | 224.00 KiB/s, done.
  Résolution des deltas: 100% (337/337), done.
  Vérification de la connectivité... fait.
  Chemin de sous-module 'shFlags' : '2fb06af13de884e9680f14a00c82e52a67c867f1' extrait
  << gitflow/git-flow >> -> << /Users/aperus/bin/git-flow >>
  << gitflow/git-flow-init >> -> << /Users/aperus/bin/git-flow-init >>
  << gitflow/git-flow-feature >> -> << /Users/aperus/bin/git-flow-feature >>
  << gitflow/git-flow-hotfix >> -> << /Users/aperus/bin/git-flow-hotfix >>
  << gitflow/git-flow-release >> -> << /Users/aperus/bin/git-flow-release >>
  << gitflow/git-flow-support >> -> << /Users/aperus/bin/git-flow-support >>
  << gitflow/git-flow-version >> -> << /Users/aperus/bin/git-flow-version >>
  << gitflow/gitflow-common >> -> << /Users/aperus/bin/gitflow-common >>
  << gitflow/gitflow-shFlags >> -> << /Users/aperus/bin/gitflow-shFlags >>
  

On peut vérifier que l'extension 'gitflow' est bien installée :

.. code-block:: bash

   $>git flow help
   usage: git flow <subcommand>
   
   Available subcommands are:
      init      Initialize a new git repo with support for the branching model.
      feature   Manage your feature branches.
      release   Manage your release branches.
      hotfix    Manage your hotfix branches.
      support   Manage your support branches.
      version   Shows version information.
   
   Try 'git flow <subcommand> help' for details.



