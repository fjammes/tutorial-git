Clone, Add, Status, Commit
--------------------------

Robert peut maintenant commencer à coder. Puisque c'est la première fois qu'il utilise Mercurial, il initialise son fichier de configuration **.hgrc** avec son identifiant. C'est ce dernier qui sera utilisé pour indentifier ses commits dans les logs.

.. code-block:: bash

  [ui]
  username = Robert <robert@futilisoft.com>


Il crée son dépôt local en clonant le dépôt central créé par Alice.

.. code-block:: bash

  ~ robert$ hg clone http://server.futilisoft.com:8000/ ./lottery
  no changes found
  updating to branch default
  0 files updated, 0 files merged, 0 files removed, 0 files unresolved

Robert regarde alors si Alice a commencé à travailler sur le nouveau dépôt :

.. code-block:: bash

  ~ robert$ cd lottery

  lottery robert$ ls -al
  total 0
  drwxr-xr-x   3 robert  staff  102 May 17 07:55 .
  drwxr-xr-x  21 robert  staff  714 May 17 07:55 ..
  drwxr-xr-x   8 robert  staff  272 May 17 07:55 .hg

Apparemment non, il n'y a que le répertoire de configuration. Il créé donc un :download:`premier programme <data/lottery_v1.py>` :

.. literalinclude:: data/lottery_v1.py
   :language: python
   :linenos:

Voici un premier jet de qualité. Robert vérifie que le code s'éxecute correctement :

.. code-block:: bash

  lottery robert$ ls -l
  total 32
  -rwxr-xr-x  1 robert  staff  8904 May 17 07:56 lottery.py~
  -rw-r--r--  1 robert  staff  8904 May 17 07:56 lottery.py

  lottery robert$ ./lottery.py
  Usage: ./lottery.py power_ball (5 white balls)

  lottery robert$ ./lottery.py 42 1 2 3 4 5
  0 percent chance of winning

Parfait, il faut maintenant enregistrer ce fichier dans le dépôt Mercurial. Tout d'abord, Robert doit ajouter le fichier au jeu de modifications (changeset) en cours.

.. code-block:: bash

  lottery robert$ hg add lottery.py

Robert vérifie ensuite que l'opération s'est bien déroulée :

.. code-block:: bash

  lottery robert$ hg status
  A lottery.py
  ? lottery.py~

Mercurial ne sait pas comment gérer le fichier lottery.py~. C'est un fichier de sauvegarde emacs, il peut être ignoré [#f1]_.  Robert peut maintenant effectuer un commit.

.. code-block:: bash

  lottery robert$ hg commit -m "initial implementation"

.. rubric:: Notes

.. [#f1] On peut également gérer ce type de fichier dans le `.hgignore <http://www.selenic.com/mercurial/hgignore.5.html>`_
