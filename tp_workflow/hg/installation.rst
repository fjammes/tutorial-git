.. _installation:

.. index:: 
  double: hg; .hgrc
  double: hg; download

============
Installation
============

Mercurial
*********

Si nécessaire, `télécharger <http://mercurial.selenic.com/downloads/>`_ le gestionnaire de version Mercurial
et l'installer comme indiqué sur la page de téléchargement. Il faut avoir sur sa machine, un Python de version 
comprise entre 2.4 et 2.7

Configurer l'outil en rajoutant les 2 lignes suivantes dans son fichier de configuration, ``~/.hgrc`` 
(ou ``mercurial.ini`` dans son 'home directory' sous Windows) :

.. code-block:: bash

  $> touch ~/.hgrc && cat >> ~/.hgrc
  [ui]
  username = Nom prénom <nom.prenom@mon.labo.fr>
  [CTRL-D]
  

.. index::
  single: extension

Script hgflow
*************

Récupérer le script Python qui implémente le workflow *hgflow* [#]_ :download:`ici <../_static/code/hgflow.py>`

Éditer le fichier de configuration de mercurial ``~/.hgrc`` et ajouter la ligne suivante, dans la section ``[extensions]``; 
s'il s'agit d'une première utilisation de Mercurial, cette section n'existe pas encore; on la crée alors :

.. code-block:: bash
  
  $> cat >> ~/.hgrc
  [extensions]
  hgflow = /PATH/TO/hgflow.py
  [CTRL-D]

*/PATH/TO* correspond, bien sûr, à l'endroit où vous avez rangé le script ``hgflow.py``, par exemple dans ``~/.hgext/``.


On peut vérifier que l'extension 'hgflow' est bien reconnue :

.. code-block:: bash

  $> hg help hgflow
  hgflow extension - no help text available
  
  list of commands:
  
   feature       (no help text available)
   flow          (no help text available)
   hotfix        (no help text available)
   release       (no help text available)
  
  use "hg -v help hgflow" to show builtin aliases and global options

Pour voir quelles sont les extensions activées, on peut également demander ``$> hg help extensions`` …


.. [#] Le script est également disponible là : https://bitbucket.org/yinwm/hgflow/downloads/ (hgflow-v0.4.pyhgflow-v0.4.py) 

