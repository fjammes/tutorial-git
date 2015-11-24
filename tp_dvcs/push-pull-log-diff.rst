Push, Pull, Log, Diff
---------------------

Puisque c'est la première fois qu'Alice utilise Mercurial, elle initialise son fichier de configuration **.hgrc**.

.. code-block:: bash

  [ui]
  username = Alice <alice@futilisoft.com>


Elle crée son dépôt local en clonant le dépôt central.

.. code-block:: bash

  ~ alice$ hg clone http://server.futilisoft.com:8000/ ./lottery
  no changes found
  updating to branch default
  0 files updated, 0 files merged, 0 files removed, 0 files unresolved

  ~ alice$ cd lottery

  lottery alice$ ls -al
  total 0
  drwxr-xr-x   3 alice  staff  102 May 17 08:00 .
  drwxr-xr-x  19 alice  staff  646 May 17 08:00 ..
  drwxr-xr-x   8 alice  staff  272 May 17 08:00 .hg

Hmm, le code écrit par Robert n'est pas présent dans le dépôt. Pourquoi ? Pourtant Robert a bien effectué le commit, mais il a oublié de faire un *push* sur le serveur central. Alice le lui signale donc.

.. code-block:: bash

  lottery robert$ hg push
  pushing to http://server.futilisoft.com:8000/
  searching for changes
  remote: adding changesets
  remote: adding manifests
  remote: adding file changes
  remote: added 1 changesets with 1 changes to 1 files

Alice peut maintenant effectuer un *pull*.

.. code-block:: bash
  :emphasize-lines: 8

  lottery alice$ hg pull
  pulling from http://server.futilisoft.com:8000/
  requesting all changes
  adding changesets
  adding manifests
  adding file changes
  added 1 changesets with 1 changes to 1 files
  (run 'hg update' to get a working copy)

.. note::

 Les développeurs de Mercurial ont beaucoup travaillé sur la simplicité d'utilisation, comme en atteste la dernière ligne affichée dans le message ci-dessus. Mercurial est le DVCS le plus simple à utiliser.

Maintenant qu'elle a effectué le *pull*, Alice devrait disposer du code, n'est-ce pas :

.. code-block:: bash

  lottery alice$ ls -al
  total 0
  drwxr-xr-x   3 alice  staff  102 May 17 08:00 .
  drwxr-xr-x  20 alice  staff  680 May 17 08:06 ..
  drwxr-xr-x  12 alice  staff  408 May 17 08:06 .hg

Hmmm, il n'est toujours pas là. Ah, peut-être devrait-elle effectuer un *hg update* sur la copie de travail.

.. note::

  Par défaut, Mercurial ne met pas à jour le répertoire de travail après un pull. Cela signifie que bien que le dépôt contient maintenant le ChangeSet, mais le répertoire de travail a encore son contenu d'avant le pull. 


.. code-block:: bash

  lottery alice$ hg update
  1 files updated, 0 files merged, 0 files removed, 0 files unresolved

  lottery alice$ ls -al
  total 8
  drwxr-xr-x   4 alice  staff  136 May 17 08:07 .
  drwxr-xr-x  20 alice  staff  680 May 17 08:06 ..
  drwxr-xr-x  12 alice  staff  408 May 17 08:07 .hg
  -rw-r--r--   1 alice  staff  555 May 17 08:07 lottery.py


Le code est bien là, Alice regarde alors les logs pour en savoir plus.

.. code-block:: bash

  lottery alice$ hg log
  changeset:   0:1f8baa59f5a4
  tag:         tip
  user:        Robert <robert@futilisoft.com>
  date:        Tue May 17 07:58:36 2011 -0500
  summary:     initial implementation


.. note::

  Notez bien la manière dont Mercurial décrit le commit: **0:1f8baa59f5a4**. Un identifiant de version pour Mercurial est un hash SHA-1, affiché sur les 12 premiers caractères en hexadécimal. C'est cet identifiant qui est présent après le symbole *:*. Avant ce symbole  figure le numéro de la révision, ce dernier commence à zéro et s'incrémente de 1 après chaque nouvelle version. Il est plus intuitif à comprendre mais est valide seulement pour une instance de dépôt.

Lorsque Alice analyse le code, elle remarque immédiatement un détail qui cloche. En effet, le programme attend le numéro "chance" comme premier argument, suivi des cinq autres. Mais, à la loterie, les cinq premiers numéros sont toujours tirés et affichés en premier. Elle pense que cela pourrait être source de confusion chez les utilisateurs et décide de résoudre ce problème. Par chance, il est seulement nécessaire de modifier quelques lignes du main().

.. literalinclude:: data/lottery_v2.py
   :language: python
   :lines: 14-24
   :emphasize-lines: 1,9,11
   :linenos:

Elle utilise alors l'opération *status* pour visualiser les changements locaux en cours.

.. code-block:: bash

  lottery alice$ hg status
  M lottery.py


Pas de surprise, Mercurial sait que lottery.py a été modifié. Alice veut effectuer une double vérification en regardant les changement eux-mêmes.

.. code-block:: bash

  lottery alice$ hg diff
  diff -r 1f8baa59f5a4 lottery.py
  --- a/lottery.py Tue May 17 07:58:36 2011 -0500
  +++ b/lottery.py Tue May 17 08:09:58 2011 -0500
  @@ -11,7 +11,7 @@
     of winning at the lottery.
     Five white balls and a power ball are drawn"""
     
  -    usage = "Usage: %prog power_ball (5 white balls)"
  +    usage = "Usage: %prog (5 white balls) power_ball"
     parser = OptionParser(usage)
 
     (_, args) = parser.parse_args()
  @@ -19,9 +19,9 @@
     if len(args) != 6:
         parser.error("incorrect number of arguments")
 
  -    power_ball = int(args[0])
  +    power_ball = int(args[5])
 
  -    white_balls = [int(arg) for arg in args[1:]]
  +    white_balls = [int(arg) for arg in args[:5]]
 
     result = calculate_result(white_balls, power_ball)

Cela semble parfait!
