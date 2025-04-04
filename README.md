
# Fonction 1
Une fonction générant un mot de passe pour un compte utilisateur spécifié en paramètres de la
 fonction, dont la complexité est fixe (24 caractères, majuscules/minuscules/chiffres/caractères
 spéciaux), et générant un qrcode à partir de ce mot de passe, stockant l'identifiant utilisateur et ce mot
 de passe (en le chiffrant!) dans votre base de données.

# Fonction 2
Une fonction générant un secret 2FA et le qrcode correspondant pour le compte utilisateur demandé
 en paramètres de la fonction, et stockant cette information (en la chiffrant!) en base de données.
 
# Fonction 3
Une fonction authentifiant un utilisateur à partir de son login, son mot de passe, et son code 2FA, après
 avoir vérifié que ces identifiants ont moins de six mois d'ancienneté, sinon elle doit marqué le compte
 comme "expiré" en base de données, et renvoyer une réponse à la frontend relançant le processus de
 création de mot de passe et de 2FA. 