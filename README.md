# Rapport des travaux
Ce présent répo présente les playbooks  pour l'automatisation des tâches d'administration systeme au sein d'un entreprise lambda.
  Ses principales tâches sont la création des utilisateurs au sein de  différentes machines  distantes qui elles mêmes sont classées en 2 groupes
      - Le groupe Projet et le groupe test
      
Nous avons aussi la création des utilisateurs selon les groupes de machines (fichier inventaire) et les groupes utilisateurs
les utilisateurs ont des mots de passe que nous avons crypté à l'aide d'ansible-vault
le load balacing grâce au role Haproxy
le partitionnement et la création de disque

Pour finir nous avons aussi paramètrer une tâche qui se lance automatiquement à l'aide de crontab,tâche qui met simplement à jour les paquets du système sur les machines du groupe test (ubuntu) chaque 11h du matin et tous les jours

Une partie du rapport d'activité globale concerne aussi le debogage d'un serveur central via Linux. Voir le Pdf de présentation.


