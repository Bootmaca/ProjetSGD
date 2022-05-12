<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>

# Table des matières

### [Introduction](#introduction)
### [PARTIE 1 : Conception et mise en œuvre de la base de données MongoDB](#partie1)
### &nbsp; &nbsp;[1. Diagramme de classe](#sub1Partie1)
### &nbsp; &nbsp;[2. Documents JSON](#sub2Partie1)
### &nbsp; &nbsp; &nbsp; &nbsp;[2.1 Jeux](#sub1sub2Partie1)
### [PARTIE 2 : Requêtage de la base de données MongoDB](#partie2)
### &nbsp; &nbsp;[1. Placer les fichiers JSON sur les serveurs de l'université](#sub1Partie2)
### &nbsp; &nbsp;[2. Insérer les documents dans la base de données MongoDB de l'université](#sub2Partie2)
### &nbsp; &nbsp;[3. Se connecter sur la base de données](#sub3Partie2)
### &nbsp; &nbsp;[4. Les requêtes ](#sub4Partie2)

### [PARTIE 3 : Python et pyMongo](#partie3)
### [Conclusion](#laconclusion)


<br/><br/>

# **Introduction** <a name="introduction"></a>
Some introduction text

<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>

# **PARTIE 1 : Conception et mise en œuvre de la base de données MongoDB** <a name="partie1"></a>

## &nbsp; &nbsp; **1. Diagramme de classe** <a name="sub1Partie1"></a>
&nbsp; &nbsp; Pour commencer ce projet, nous avons réalisé un diagramme de classe afin de servir de bonne base pour réaliser les fichiers json grâce à la modélisation des classes, des attributs et des relations entre ses objets.

<br/>

![](image/Diagramme%20de%20classe.png)

<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>

## &nbsp; &nbsp; **2. Documents JSON** <a name="sub2Partie1"></a>
&nbsp; &nbsp; Les documents JSON ont été crée à l'aide du diagramme de classe ci dessus. Ils ont été crée avec un objectif de favoriser l'optimisation et la performance en facilitant les requêtes et évitant les jointures mais pour ce faire il a fallut avoir beaucoup de redondance de données. Ce qui peut poser problème lors de la mise à jour des données cependant ces types d'actions sont beaucoup moin fréquente que les requêtes d'affichage. 
Nous allons donc vous décrire un document par collection crée et justifier l'utilité des redondances 

### &nbsp; &nbsp; &nbsp; &nbsp; **2.1 Jeux** <a name="sub1sub2Partie1"></a>

```JSON
{
  "_id" : 1, // Identifiant du jeu
  "nom" : "GRAAAAAAAL !", // Nom du jeu
  "description" : "Battez-vous et que le meilleur graaal", // Description du jeu
  "prix" : 22.90, // Prix du jeu
  "nbJoueurMin" : 3, // Nombre de joueur minimum pouvant jouer au jeu
  "nbJoueurMax" : 8, // Nombre de joueur maximum pouvant jouer au jeu
  "duree" : 30, // Temps moyen que dure une partie de ce jeu
  "ageMin" : 6, // Age minimum pour jouer à ce jeu
  "noteComplexite" : 1, // Complexité de ce jeu allant de 1 à 5
  "noteConcentration" : 2, // Concentration nécéssaire pour ce jeu allant de 1 à 5
  "noteAmbiance" : 5, // Ambiance que procure ce jeu allant de 1 à 5
  "langue" : [ //Tableau des ou de la langue(s) du jeu
    {
      "idLangue" : 1, // Référence à l'id de la langue du fichier langues.json
      "libelle" : "Français" // Intitulé de la langue
    }
  ],
  "categorie" : { //Information sur la catégorie
    "idCategorie" : 1, // l'id de la catégorie venant du fichier categories.json
    "libelle" : "Jeux d'ambiance" // Intitulé de la catégorie
  },
  "editeur" : [ //Tableau des ou de l'editeur(s) du jeu
    {
      "idEditeur" : 1,// l'id de l'éditeur venant du fichier editeurs.json
      "intitule" : "Celtic Tales" // Nomination de l'éditeur
    }
  ],
  "auteur" : [ // Tableau des ou de l'auteur(s) du jeu
    {
      "idAuteur" : 1, // l'id de l'auteur venant du fichier auteurs.json
      "nom" : "BERNARD", // nom de l'auteur
      "prenom": "Pascal" // prénom de l'auteur
    }
  ],
  ```
  <br/><br/>

  ```JSON
    "avis" : [ // Tableau des ou de l'avis du jeu
        {
            "idAvis" : 8, // l'id de l'avis venant du fichier auteurs.json
            "note" : 5, //note donné par l'utilisateur sur le jeu
            "commentaire" : "AWESOMEEEEEE", //commentaire donné par l'utilisateur
            "date" : ISODate("2020-05-28T01:47:20.202Z"), //date de l'avis
                "utilisateur" : {
                    "idUtil" : 6, // Id utilisateur venant de utilisateurs.json
                    "pseudo" : "maroux", // Pseudo de l'utilisateur
                    "age" : 37 //Age de l'utilisateur
                }
        },
        {
            "idAvis" : 31,
            "note" : 5,
            "commentaire" : "Super",
            "date" : ISODate("2022-04-09T00:28:20.202Z"),
            "utilisateur" : {
                "idUtil" : 17,
                "pseudo" : "greg",
                "age" : 35
            }
        }
    ]
}
```
Comme vous avez pu le constater ce document présente beaucoup d'information qui sont déjà présente dans d'autres fichier json comme le nom et prenom de l'auteur, les informations sur les avis, le libellé de la catégorie etc... Mais comme dis précedement cela va permettre de simplifier les requêtes et éviter les jointures.
La redondance des libellés pour les langues, les catégories, les auteurs et les éditeurs permettent d'éviter de faire des jointures par exemple lorsque qu'on veut afficher les informations complète d'un jeux. Ou alors quand un client souhaitent appliquer des filtres lors d'une recherche pour trouver un jeu qui lui convient par exemple les jeux d'une catégorie spéciale qui est en anglais, cela ne demandera pas de jointure avec une autre collection.


# **PARTIE 2 : Requêtage de la base de données MongoDB** <a name="partie2"></a>

Tout d'abord pour réaliser les requêtes sur votre environnement de travail veuillez réaliser les instructions qui suivent

## &nbsp; &nbsp; **1. Placer les fichiers JSON sur les serveurs de l'université** <a name="sub1Partie2"></a>

**Si vous êtes sur un ordinateur de l'université et que les fichiers sont dessus veuillez passer directement à l'étape 2.**

**Sinon il va falloir suivre les indications suivantes (au préalable se connecter au VPN de l'université)**

- Ouvrir un invité de commande et se déplacer à l'emplacement des fichiers JSON (que vous trouverez joint avec ce rapport) à l'aide de la commande cd


- Se connecter en sftp avec la commande suivante :
    ```sh
    sftp nomUtilisateur@aragon.iem
    ```
 
- Se déplacer à l'emplacement où l'on veut à l'aide de la commande cd

- Déposer les fichiers JSON à l'aide de la commande suivante :
    ```sh
    put *.json
    ```

- Quitter sftp avec la commande suivante :
    ```sh
    exit
    ```

## &nbsp; &nbsp; **2. Insérer les documents dans la base de données de l'université** <a name="sub2Partie2"></a>

**Se connecter au serveur mongo2**

- Connexion au serveur mongoDB de l'université
    ```sh
    ssh nomUtilisateur@mongo2
    ``` 
   
- Se déplacer là où on a placé les fichiers json à l'aide de la commande cd

- Importer le fichier auteur.json dans la collection Auteurs de votre base
    ```sh
    mongoimport -u nomUtilisateur -p nomUtilisateur --db nomUtilisateur --collection Auteurs --file auteurs.json --host mongo2.iem
    ```

- Importer le fichier categories.json dans la collection Categories de votre base
    ```sh
    mongoimport -u nomUtilisateur -p nomUtilisateur --db nomUtilisateur --collection Categories --file categories.json --host mongo2.iem
    ```

- Importer le fichier jeux.json dans la collection Jeux de votre base
    ```sh
    mongoimport -u nomUtilisateur -p nomUtilisateur --db nomUtilisateur --collection Jeux --file jeux.json --host mongo2.iem --legacy
    ```

- Importer le fichier utilisateurs.json dans la collection Utilisateurs de votre base
    ```sh
    mongoimport -u nomUtilisateur -p nomUtilisateur --db nomUtilisateur --collection Utilisateurs --file utilisateurs.json --host mongo2.iem --legacy
    ```

- Importer le fichier avis.json dans la collection Avis de votre base
    ```sh
    mongoimport -u nomUtilisateur -p nomUtilisateur --db nomUtilisateur --collection Avis --file avis.json --host mongo2.iem --legacy
    ```

- Importer le fichier editeurs.json dans la collection Editeurs de votre base
   ```sh
   mongoimport -u nomUtilisateur -p nomUtilisateur --db nomUtilisateur --collection Editeurs --file editeurs.json --host mongo2.iem --legacy
   ```

- Importer le fichier langues.json dans la collection Langues de votre base
   ```sh
   mongoimport -u nomUtilisateur -p nomUtilisateur --db nomUtilisateur --collection Langues --file langues.json --host mongo2.iem --legacy
   ```

## &nbsp; &nbsp; **3. Se connecter sur la base de données** <a name="sub3Partie2"></a>

- Se connecter sous mongoDB
    ```sh
    mongo -u n -p nomUtilisateur -authenticationDatabase nomUtilisateur -host mongo2.iem
    ```
 
- Fixer la base de travail
    ```sh
    use nomUtilisateur
    ```

## &nbsp; &nbsp; **4. Les requetes** <a name="sub4Partie2"></a>

Vous trouverez ci-dessous un large panel de requêtes pouvant être nécessaires pour le catalogue du site, mais également pour certains aspects plus analytiques sur les jeux. Pour éviter de surcharger le rapport, les requêtes presque identique n'ont pas été ajouté, par exemple l'ajout d'un editeur est presque identique à l'ajout d'une langue il faut juste changer les noms des attributs de la collection editeur par ceux de la collection langue.

1. Afficher tous les jeux, dans le cas d'un site de jeux cette commande pourrait être utilisé pour  
    ```JSON
    db.Jeux.find({})
    ```

2. Afficher un jeu en fonction de son id. Lors d'un clic sur un jeux pour obtenir toutes les informations par exemple
    ```JSON
    db.Jeux.find({"_id" : 1})
    ```



3. Changer le prix d'un jeux. Si par exemple ce jeu ne se vend pas
    ```JSON
    db.Jeux.updateOne(
        { "_id" : 1},
        {$set :
            {"prix" : 25.50}
        }
    )

    //Il faudra ensuite faire la mise à jour de ce prix dans chaque collection pour ce jeu par exemple pour avis. Les modifications du jeu dans les autres collections sont semblable à celui ci.
    db.Avis.updateMany(
        { "jeu.idJeu" : 1},
        {$set :
            {"jeu.prix" : 25.50}
        }
    )
    ```

4. Supprimer un jeu. Si l'éditeur à arreter d'en produire par exemple.
    ```JSON
    db.Jeux.delete({ "_id" : 1})

    //Il faudra ensuite faire la mise à jour de ce prix dans chaque collection pour ce jeu par exemple pour avis supprimer tous les avis de ce jeu
    db.Avis.deleteMany({"jeu.idJeu":1})

    //Ou pour catégorie le supprimer du tableau des jeux de sa catégorie. Les autres suppression du jeu dans les collection ressemble à celui ci.
    db.Categories.updateMany(
        {"jeux.idJeu" : 1},
        {$pull : 
           {"jeux" : {"idJeu" : 1,}} 
        }
    )
    ```


5. Ajouter un jeu. Si un editeur souhaite ajouter un jeux sur le site
    ```JSON
        db.Jeux.insert({
            "_id" : 22,
            "nom" : "DIXIT (NOUVELLE ÉDITION 2021)",
            "description" : "Laissez-vous inspirer par ses illustrations poétiques..!",
            "prix" : 27.00,
            "nbJoueurMin" : 3,
            "nbJoueurMax" : 8,
            "duree" : 30,
            "ageMin" : 8,
            "noteComplexite" : 2,
            "noteConcentration" : 2,
            "noteAmbiance" : 3,
            "langue" : [ 
                {
                    "idLangue" : 1,
                    "libelle" : "Français"
                }
            ],
            "categorie" : {
                "idCategorie" : 1,
                "libelle" : "Jeux d'ambiance"
            },
            "editeur" : [ 
                {
                    "idEditeur" : 1,
                    "intitule" : "Celtic Tales"
                }
            ],
            "auteur" : [ 
                {
                    "idAuteur" : 1,
                    "nom" : "BERNARD",
                    "prenom" : "Pascal"
                }
            ]
        })


    //Il faudra ensuite ajouter ce jeu dans chaque collection par exemple dans auteur. puis on fait pareil pour toutes les autres collections (Langues, Editeurs, Categories)
    db.Auteurs.updateMany(
        {"_id_" : 19},
        {$push : 
            {"jeux" : 
                {
                    "_id" : 22,
                    "nom" : "DIXIT (NOUVELLE ÉDITION 2021)",
                    "prix" : 27.00
                }
            }
        }
    )
    ```

6. Afficher tous les jeux d'une catégorie. Par exemple si l'utilisateur veut voir tous les jeux d'une seule catégorie. Dans ce cas pour faciliter la requête et la rendre plus rapide on va éviter de parcourir tous les jeux qui avec beaucoup plus de jeux prendrait plus de temps on va réaliser directement la requête sur la collection catégorie qui nous permet d'avoir la réponse sans jointure grâce aux redondances crée auparavant
    ```JSON
    db.Categories.find({"libelle":"Jeux d'ambiance"},{"jeux":1})
    ``` 

7. Afficher tous les jeux d'une catégorie. Si l'utilisateur veut voir tous les jeux en anglais car il veut apprendre cette langue tout en jouant. Même raison que auparavant on peu aller chercher directement dans la collection Langues
    ```JSON
    db.Langues.find({"libelle":"Anglais"},{"jeux":1})
    ``` 

8. Afficher tous les avis d'un utilisateur. Par exemple si son avis semble suspect sur un jeu vérification de tous ses avis. Ici on peut aussi pour faciliter la requête chercher dans la collection utilisateur
    ```JSON
    db.Utilisateurs.find({"_id":5},{"avis":1})
    ```

9. Afficher les jeux d'une catégorie donné et d'une langue donné. Si il souhaite réaliser plusieurs filtre lors de la recherche d'un jeu. Dans ce cas la on sera obligé d'utiliser la relation Jeu mais sans faire de jointure. 
    ```JSON
    db.Jeux.find({"idCategorie":1, "idLangue" : 1 })
    ```

10. Voir les avis qui ont les moyennes de note les plus haute. Afin de voir les jeux qui sont les plus apprécié. 
    ```JSON
    db.Jeux.aggregate([
        {
            $unwind : "$avis"
        },
        {
            $group :
            {
                _id : "$nom",
                "Moyenne des avis" : {$avg : "$avis.note"}
            }
        },
        {
            $sort : {"Moyenne des avis": -1}
        }
    ])
    ```

11. Même chose mais ceux qui ont les moyennes les plus basses. Afin de voir les jeux les moins aimé.
    ```JSON
    db.Jeux.aggregate([
        {
            $unwind : "$avis"
        },
        {
            $group :
            {
                _id : "$nom",
                "Moyenne des avis" : {$avg : "$avis.note"}
            }
        },
        {
            $sort : {"Moyenne des avis": -1}
        }
    ])
    ```

12. 10 jeux les mieux noté avec le plus d'avis. Afin de faire une section des jeux les plus aimé sur le site.
    ```JSON
    db.Jeux.aggregate([
        {
            $unwind : "$avis"
        },
        {
            $group :
            {
                _id : {"nom":"$nom", "note":"$avis.note"},
                "Nombre d'avis" : {$sum : 1}
            }
        },
        {
            $sort : {"_id.note":-1,"Nombre d'avis": -1}
        },
        {
            $limit : 10
        }
    ])
    ``` 

13. Voir les jeux les mieux noté avec le plus d'avis cette année. Afin de rajouter une section les jeux les plus aimé cette année.
```JSON
    db.Jeux.aggregate([
        {
            $unwind : "$avis"
        },
        {
            $match : {
                "$expr": { "$eq": [{ "$year": "$avis.date" }, 2022] }
            }
        },
        {
            $group :
            {
                _id : {"nom":"$nom", "note":"$avis.note"},
                "nbAvis" : {$sum : 1}
            }
        },
        {
            $sort : {"_id.note":-1,"Nombre d'avis": -1}
        },
        {
            $limit : 10
        },
        {
            $project : {
                "_id" : 0,
                "nom" : "$_id.nom",
                "note" : "$_id.note",
                "nbAvis" : "$nbAvis"
            }
        }
    ])
``` 

14. Voir les jeux sans avis. Afin de voir pourquoi ils ont pas été commenté 
    ```JSON
    db.Jeux.find({"avis" : {$exists : 0}})
    ```


15. Afficher le nombre d'utilisateur qui ont plus de 80 ans. Afin de voir si il y a des personnes agé qui mettent des avis
    ```JSON
    db.Avis.find(
        {
            "utilisateur.age" : { $gte : 80}
        }
    ).count()
    ```

16. La moyenne d'age de toutes les personnes qui ont commenté 
```JSON
    db.Utilisateurs.aggregate([
        {
            $match : 
            {
                "avis" : {$exists : 1}
            }
        },
        {
            $group :
            {
                _id : 1,
                "Moyenne d'age" : { "$avg" : "$age"}
            }
        }
    ])
```

17. Montrez les noms et prenom des utilisateurs qui ont le plus commenté. Peut servir a leurs envoyer un mail de remerciement qui les encouragera a mettre plus de commentaire
```JSON
    db.Utilisateurs.aggregate([
        {
            $unwind : "$avis"
        },
        {
            $group :
            {
                _id : {"_id":"$_id", "nom":"$nom", "prenom":"$prenom"},
                "NbCommentaires" : { "$sum" : 1}
            }
        },
        {
            $sort : {"NbCommentaires":-1}
        },
        {
            $limit : 5
        },
        {
            $project : {
                "_id" : { $concat: [ "$_id.nom", " ", "$_id.prenom" ] },
                "NbCommentaires" : "$NbCommentaires"
            }
        }
    ])
```


18. Montrez les noms et prenom des utilisateurs qui ont le plus commenté. Peut servir a leurs envoyer un mail de remerciement qui les encouragera a mettre plus de commentaire
```JSON
    db.Utilisateurs.aggregate([
        {
            $unwind : "$avis"
        },
        {
            $group :
            {
                _id : {"_id":"$_id", "nom":"$nom", "prenom":"$prenom"},
                "NbCommentaires" : { "$sum" : 1}
            }
        },
        {
            $sort : {"NbCommentaires":-1}
        },
        {
            $limit : 5
        },
        {
            $project : {
                "_id" : { $concat: [ "$_id.nom", " ", "$_id.prenom" ] },
                "NbCommentaires" : "$NbCommentaires"
            }
        }
    ])
```

19. Nombre de jeux par catégorie. Afin d'équilibrer un peu le nombre de jeux par catégories
    ```JSON
    db.Categories.aggregate([
        {
            $unwind : "$jeux"
        },
        {
            $group :
            {
                _id : {"_id":"$_id", "libelle": "$libelle"},
                "nbJeux" : { "$sum" : 1}
            }
        },
        {
               $project :
               {
                   "_id" : "$_id.libelle",
                   "nbJeux" : "$nbJeux"
               }
        }
    ])
    ```

20. Nombre de requêtes par sexe. A des fins analytique
    ```JSON
    db.Utilisateurs.aggregate([
        {
            $unwind : "$avis"
        },
        {
            $group :
            {
                _id : "$sexe",
                "nbAvis" : { "$sum" : 1}
            }
        }
    ])
    ```
    21. Requête map reduce pour la moyenne des prix par catégorie :
    ```JSON
    var map = function(){
        emit(this.categorie.libelle, this.prix);
    }

    var reduce = function(libelleCat, prix){
        return Array.avg(prix);
    }

    db.Jeux.mapReduce(map, reduce, {out: {inline: 1}});
    ```


# **PARTIE 3 : Python et pyMongo** <a name="partie3"></a>

1. Nombre d'avis par tranche d'age
    ```JSON
    
    ```


Insérer un jeu (python avec fonction)
Grosse requête nombre d'avis pas rapport à des tranches d'age classé par nombre d'avis
Jeu groupé par note et par prix pour savoir si on baisse ou augmente le prix du jeu
Voir le nombre d'avis par tranche de note
max min et moyenne d'un avis




# **Conclusion** <a name="laconclusion"></a>
