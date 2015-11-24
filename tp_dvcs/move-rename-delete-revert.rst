Autres commandes très utiles
----------------------------

Ces commandes sont à effectuer précédemment à un commit.

Indiquer qu'un conflit suite à un *merge* a été résolu manuellement : resolve
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: bash

  hg resolve -m lottery.py

Renommer/déplacer des fichiers de la branche courante du dépôt lors du prochain commit : rename
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: bash

  hg mv lottery.py

Supprimer des fichiers de la branche courante du dépôt lors du prochain commit : remove
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: bash

  hg rm lottery.py

Annuler une ou plusieurs modifications apportées à des fichiers : revert
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: bash

 lottery robert$ hg revert

