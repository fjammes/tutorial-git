Atelier DVCS
============

:Contacts: 

  Antoine Perus perus@lal.in2p3.fr 0164468443
  
  Frédéric Magniette magniette@llr.in2p3.fr 0169335619

  Fabrice Jammes fabrice.jammes@clermont.in2p3.fr 0473407299	

Proposition de programme
************************

La base : 1h
------------

- Introduction au DVCS : présentation 20mn
- Problématique de migration de svn : présentation 10mn
- Fonctionalités de base : init / clone / commit / merge / status : TP 30mn
- Différences/similitudes Svn, Git, Mercurial 

Spécificités de git/mercurial : 45m 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Avantages par rapport à SVN/CVS.

- Spécifités de git :
    1. stashing : la possibilité de 'cacher' son travail courant pour entreprendre une autre action rapidement
    2. cherry-picking : recopier seulement un patch (commit) entre deux branches
    3. history rewriting : changer l'histoire
    4. rebase : différence avec le commit classique
    5. octopus merge : pouvoir merger plusieurs branches en une fois dans la branche de travail

- Spécifité de mercurial :
   1. simplicité d'utilisation
   2. TODO

Topo sur la différence entre les concepts de branches des deux outils ? 


DVCS et gestion de projet : 1h15m 
---------------------------------

Cette partie n'est pas particulière au DVCS, elle s'applique également avec un système non distribué.

- Utilisation en relation avec un gestionnaire de ticket/BT (id branche = id ticket)
- Traçabilité (travail effectué sur le ticket accessible bia le BT)
- Cycle de travail (exemple s'appuyant sur le flow LSST, mais on pourra prendre un autre exemple): 
	1. création/affectation d'un ticket, 
	2. création de la branche idoine (feature), 
	3. développement et tests, 
	4. relecture/validation du code, 
	5. merge avec la branche parente et tests,
	6. commit dans la branche parente,
	7. création de release
- Intérêt d'un DVCS pour l'intégration continue

- Branching / git/hg-flow : présentation 20mn
- Manipulation des branches feature, release, master, hotfix: TP 30mn
	1. les branches personnelles : présentation et intérêt
- Retour d'expérience sur ce schéma et ses modifications éventuelles : Discussion 10mn

Le travail à plusieurs : 30m
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Resolution de conflits : présentation 10mn
- Resolution de conflits : TP 10mn
    1. merge simple
    2. merge avec conflit
    3. merge avec nécessité de faire un patch correctif sur la branche parente

Les serveurs : 1h
-----------------

- fonctionalité de serveur : présentation 10mn
- Manipulation d'un serveur, migration d'un serveur : TP 20mn
- Gestion des droits d'accès (git)
- hooks : présentation 10mn 
- hooks fabrication d'archive tar / test automatique : TP 20mn


Les serveurs collaboratifs : 30mn
---------------------------------

- Github et Bitbucket : présentation 10mn
- Creation d'un projet dans Github : TP 20mn

Les Tps pourront être dédoublés sous Mercurial ou sous Git en fonction des souhaits des participants. 
