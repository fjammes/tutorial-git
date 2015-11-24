Update, Commit (avec un merge)
------------------------------

Pendant ce temps Robert a codé lui aussi. Il a entendu dire que pylint [#f2]_ était un outil fiable pour analyser la qualité de son code et a décidé d'utiliser celui-ci.

.. code-block:: bash

 lottery robert$ pylint lottery.py
 No config file found, using default configuration
  ************* Module lottery
  W:  5:calculate_result: Unused argument 'power_ball'
  W:  5:calculate_result: Unused argument 'white_balls'
  ...


Robert analyse le message et s'aperçoit que la fonction calculate_result() ne contrôle pas ses paramètres d'entrée.
Le numéro de chance est compris entre 1 et 39, alors que les balles blanches sont entre 1 et 59.
Robert implémente alors la gestion d'erreur.

.. literalinclude:: data/lottery_v3.py
   :language: python
   :lines: 5-15
   :emphasize-lines: 4-9
   :linenos:

Robert teste alors le code.

.. code-block:: bash

  lottery robert$ pylint lottery.py
  ...
  Global evaluation
  -----------------
  Your code has been rated at 10.00/10 (previous run: 8.95/10)

  lottery robert$ ./lottery.py  1 2 3 4 5 6
  White balls : [2, 3, 4, 5, 6]
  Chance ball : 1
  0 percent chance of winning

  lottery robert$ ls -l
  total 32
  -rwxr-xr-x  1 robert  staff  8904 May 17 08:16 lottery.py
  -rw-r--r--  1 robert  staff   843 May 17 08:16 lottery.py~

C'est bon, Robert, qui connait les bonnes pratiques, décide de vérifier de nouveau son code, avec *hg diff*.

.. code-block:: bash

  lottery robert$ hg diff
  diff -r 1f8baa59f5a4 lottery.py
  --- a/lottery.py Tue May 17 07:58:36 2011 -0500
  +++ b/lottery.py Tue May 17 08:17:53 2011 -0500
  @@ -4,6 +4,14 @@
 
   def calculate_result(white_balls, power_ball):
       """ Computation is lauched here """
  +
  +    for ball in white_balls:
  +        if ball < 1 or ball > 59:
  +            return -1
  +
  +    if power_ball < 1 or power_ball > 39:
  +        return -1
  +
       return 0
 
   def main():

Parfait, il est temps d'effectuer le commit.

.. code-block:: bash
  
  lottery robert$ hg commit -m "fix some warnings"

Tout se passe, bien. De plus, il ne reste plus à Robert qu'à effectuer un *push* sur le serveur.

Cependant, Alice a également travaillé durant la même période et a effectué son commit puis son push avant Robert.

.. code-block:: bash

  lottery sally$ hg commit -m "change order of the command line args to be \
                              more like what the user will expect"

  lottery sally$ hg push
  pushing to http://server.futilisoft.com:8000/
  searching for changes
  remote: adding changesets
  remote: adding manifests
  remote: adding file changes
  remote: added 1 changesets with 1 changes to 1 files

C'est au tour de Robert de faire un *push* sur le serveur.

.. code-block:: bash

  lottery robert$ hg push
  pushing to http://server.futilisoft.com:8000/
  searching for changes
  abort: push creates new remote heads on branch 'default'!
  (you should pull and merge or use push -f to force)

Que se passe-t-il ? En fait, Mercurial interdit à Robert de faire un *push* sur son jeu de modifications car cela entrainerait la creation de deux feuilles (ou head) dans la branche par défaut de l'arbre de développement (ou DAG).
Ce blocage est analogue à la manière dont les outils de seconde génération interdisaient un commit s'il n'était pas basé sur la plus récente version du dépôt. Mercurial permet de contourner cette restriction, mais il est souvent préférable d'effectuer un *pull* et un *merge* avant de faire un *push*. Cette méthode assure notamment une meilleure entente entre les membres de l'équipe de développement.

Robert télécharge donc les derniers changements avec la commande *hg pull*.

.. code-block:: bash

  lottery robert$ hg pull
  pulling from http://server.futilisoft.com:8000/
  searching for changes
  adding changesets
  adding manifests
  adding file changes
  added 1 changesets with 1 changes to 1 files (+1 heads)
  (run 'hg heads' to see heads, 'hg merge' to merge)

Robert suis alors tout simplement les instructions données par Mercurial.

.. code-block:: bash

  lottery robert$ hg heads
  changeset:   2:7dd1d2434f80
  tag:         tip
  parent:      0:1f8baa59f5a4
  user:        Alice <sally@futilisoft.com>
  date:        Tue May 17 08:25:22 2011 -0500
  summary:     change order of the command line args to be \
               more like what the user will expect

  changeset:   1:efcd0b05ec2c
  user:        Robert <robert@futilisoft.com>
  date:        Tue May 17 08:24:01 2011 -0500
  summary:     fix some warnings

Robert tente alors d'utiliser la commande *hg update* pour mettre à jour son dépôt avec les modifications qu'il vient de télécharger.

.. code-block:: bash

  lottery robert$ hg update
  abort: crosses branches (merge branches or use --check to force update)

Cela ne fonctionne pas, il tente donc un merge :

.. code-block:: bash

  lottery robert$ hg merge
  merging lottery.py
  0 files updated, 1 files merged, 0 files removed, 0 files unresolved
  (branch merge, don't forget to commit)

Superbe, maintenant la fusion des deux feuilles est dans la copie de travail.

.. code-block:: bash

  lottery robert$ hg status
  M lottery.py
  ? lottery.py~


Tout semble avoir fonctionné, Robert veut maintenant comprendre ce qui s'est passé.

.. code-block:: bash

  lottery robert$ hg diff
  diff -r efcd0b05ec2c lottery.py
  --- a/lottery.py Tue May 17 08:24:01 2011 -0500
  +++ b/lottery.py Tue May 17 08:30:00 2011 -0500
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


Intéressant. la commande *diff* montre les changements effectués par Alice. C'est parce que le différentiel a été effectué avec le changeset efcd0b05ec2c. 
Robert utilise alors *hg parents* pour connaître la version de l'arbre sur laquelle ses changement en cours s'appuient.

.. code-block:: bash

  lottery robert$ hg parents
  changeset:   1:efcd0b05ec2c
  user:        Robert <robert@futilisoft.com>
  date:        Tue May 17 08:24:01 2011 -0500
  summary:     fix some warnings

  changeset:   2:7dd1d2434f80
  tag:         tip
  parent:      0:1f8baa59f5a4
  user:        Alice <sally@futilisoft.com>
  date:        Tue May 17 08:25:22 2011 -0500
  summary:     change order of the command line args to be \
             more like what the user will expect

Parce ce qu'une opération de *merge* est en cours, la copie de travail de Robert a deux parents. Le noeud du DAG résultant du *merge* aura également deux parents. 
De plus, Mercurial a été ici capable de fusionner les modification d'Alice et de Robert dans la copie de travail de Robert sans aucun conflit. C'est parfait. Robert teste alors le code.

.. code-block:: bash

  lottery robert$ ./lottery.py  1 2 3 4 5 6
  White balls : [2, 3, 4, 5, 6]
  Chance ball : 1
  0 percent chance of winning

  lottery robert$ ls -l
  total 32
  -rwxr-xr-x  1 robert  staff  8904 May 17 08:28 lottery.py
  -rw-r--r--  1 robert  staff   843 May 17 08:28 lottery.py~

Impeccable, Robert est maintenat prêt à faire le commit.

.. code-block:: bash

  lottery robert$ hg commit -m "merge"

La sortie de *hg parents* ne contient qu'un seul noeud, mais celui-ci a bien deux parents.

.. code-block:: bash

  lottery robert$ hg parents
  changeset:   3:edbf336fe3fa
  tag:         tip
  parent:      1:efcd0b05ec2c
  parent:      2:7dd1d2434f80
  user:        Robert <robert@futilisoft.com>
  date:        Tue May 17 08:35:28 2011 -0500
  summary:     merge

Robert envoie alors son code sur le serveur.

.. code-block:: bash

  lottery robert$ hg push
  pushing to http://server.futilisoft.com:8000/
  searching for changes
  remote: adding changesets
  remote: adding manifests
  remote: adding file changes
  remote: added 2 changesets with 2 changes to 1 files


.. [#f2] : Pylint est un logiciel de vérification de code source et de la qualité du code pour le langage de programmation Python. Il utilise les recommandations officielles de style de la `PEP 8 <http://www.python.org/dev/peps/pep-0008/>`_. Pour le récupérer et, éventuellement, l'installer : http://download.logilab.org/pub/pylint/pylint-1.0.0.tar.gz

