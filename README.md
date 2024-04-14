# 📇 **Application de Parcours d'Annuaire MVC** 🖥️

Ce projet correspond au développement d'une application permettant de parcourir un annuaire en respectant la séparation entre la vue et le modèle, utilisant le motif Modèle-Vue-Contrôleur (**MVC**). L'application a été conçue dans le cadre des travaux pratiques du cours "R2.02 : développement d'application avec IHM".

📝 **Description**<br>
L'application se présente avec une interface utilisateur permettant d'afficher les détails d'une personne de l'annuaire, ainsi que des boutons de navigation pour passer d'une personne à une autre, créer une nouvelle personne, charger un annuaire et sauvegarder un annuaire. Les données de l'annuaire sont stockées dans un fichier au format JSON.

🛠️ **Étapes de développement**<br>
**Étape 1 :** Personne et Vue Personne<br>
Dans cette première étape, la classe VuePersonne a été développée pour afficher les détails d'une personne. Cette classe contient des composants graphiques tels que des zones de texte pour le prénom, le nom et la biographie, ainsi que des menus déroulants pour la civilité et des sélecteurs de date pour la naissance et le décès.

**Étape 2 :** Annuaire et Vue Annuaire<br>
La deuxième étape a consisté à développer le modèle et la vue de l'annuaire. Le modèle, représenté par la classe Annuaire, gère les opérations sur l'annuaire telles que l'ajout, la suppression et la récupération de personnes. La vue Annuaire affiche les boutons de navigation et émet des signaux pour communiquer avec le contrôleur.

**Étape 3 :** Contrôleur et Main<br>
La dernière étape a implémenté le contrôleur, qui relie la vue et le modèle. Le contrôleur intercepte les signaux émis par la vue, effectue les opérations nécessaires sur le modèle et met à jour la vue en conséquence.

🚀 **Gestion des cas spéciaux**<br>
L'application prend en charge plusieurs cas spéciaux lors de l'ajout ou de la lecture des personnes dans l'annuaire :

**Date de mort antérieure à la date de naissance :**<br>
Lorsqu'une personne est ajoutée avec une date de mort antérieure à sa date de naissance, un message d'erreur est affiché dans la console et la personne n'est pas ajoutée à l'annuaire.

**Ajout d'une même personne :** <br>
Il n'est pas possible d'ajouter deux fois la même personne dans l'annuaire. Si une tentative d'ajout est détectée, un message d'erreur est affiché dans la console et la personne n'est pas ajoutée.

**Gestion de la mort :** <br>
Lors de la création ou de la modification d'une personne, l'utilisateur peut spécifier si la personne est décédée ou non. Si elle est décédée, un choix est proposé pour spécifier la date de décès. Si la personne est en vie, la date de décès est définie comme nulle.

**Sauvegardes :** <br>
Lors de la sauvegarde de l'annuaire, les informations ne sont pas écrites sur le fichier de sauvegarde actuel. Au lieu de cela, l'utilisateur doit choisir de créer un nouveau fichier ou d'écraser le fichier de sauvegarde précédent. Des informations sur les types d'erreurs rencontrées sont affichées dans la console pour informer l'utilisateur sur les problèmes éventuels lors de la sauvegarde.

▶️ **Utilisation**<br>
Pour exécuter l'application, exécutez le fichier principal Controller.py. Assurez-vous d'avoir PyQt installé sur votre système.

🔗 **Références**<br>
PyQt Documentation v6.2.1
[AnnuaireMVC sur GitHub](https://github.com/xMegumi/AnnuaireMVC)
