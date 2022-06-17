import sqlite3                                #commande d'importation du module SQlite

def connect():
    conn =sqlite3.connect("parcinfo.db")      #connexion à la base de données (si ce dernier n'existe pas, il est alors créé)
    cur= conn.cursor()                        #récuperation d'un curseur pour pouvoir exécuter des requêtes SQlite sur Python
                                              #exécution de la requête "CREATE" qui créé une table
    cur.execute("CREATE TABLE IF NOT EXISTS parcinfo (id INTEGER PRIMARY KEY, poste text, salle text, os text, brand text, date text, cpu text, ram text, gpu text, screen text, hdd text, ssd text, wifi text, bluetooth text, usbports text, cdplayer text, solidworks text, proteus text ) ")
    conn.commit()                             #validation des modifications car lorsqu'on effectue des modifications, celles-ci ne sont pas automatiquement validées
    conn.close()                              #deconnexion à la base de données


def insert(poste, salle, os, brand, date, cpu, ram, gpu, screen, hdd, ssd, wifi, bluetooth, usbports, cdplayer, solidworks, proteus):
    conn =sqlite3.connect("parcinfo.db")      #connexion à la base de données
    cur= conn.cursor()                        #récuperation d'un curseur pour pouvoir exécuter des requêtes SQlite sur Python
                                              #exécution de la requête "INSERT" qui ajoute les données de la base sur la table
    cur.execute("INSERT INTO parcinfo VALUES(NULL, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (poste, salle, os, brand, date, cpu, ram, gpu, screen, hdd, ssd, wifi, bluetooth, usbports, cdplayer, solidworks, proteus))
    conn.commit()                             #validation des modifications car lorsqu'on effectue des modifications, celles-ci ne sont pas automatiquement validées
    conn.close()                              #deconnexion à la base de données


def view():
    conn =sqlite3.connect("parcinfo.db")      #connexion à la base de données
    cur= conn.cursor()                        #récuperation d'un curseur pour pouvoir exécuter des requêtes SQlite sur Python
                                              #exécution de la requête "SELECT" pour récupérer les données
    cur.execute("SELECT * FROM parcinfo")
    rows =cur.fetchall()                      #récupère toutes les lignes d'un résultat de requête et les renvoie sous forme de liste de tuples
    conn.close()                              #deconnexion à la base de données
    return rows

def search(poste="", salle="", os="", brand="", date="", cpu="", ram="", gpu="", screen="", hdd="", ssd="", wifi="", bluetooth="", usbports="", cdplayer="", solidworks="", proteus=""):
    conn =sqlite3.connect("parcinfo.db")      #connexion à la base de données
    cur= conn.cursor()                        #récuperation d'un curseur pour pouvoir exécuter des requêtes SQlite sur Python
                                              #exécution de la requête "SELECT" pour récupérer les données en faisant une recherche ciblée
    cur.execute("SELECT * FROM parcinfo WHERE poste=? OR salle=? OR os=? OR brand=? OR date=? OR cpu=? OR ram=? OR gpu=? OR screen=? OR hdd=? OR ssd=? OR wifi=? OR bluetooth=? OR usbports=? OR cdplayer=? OR solidworks=? OR proteus=?",(poste, salle, os, brand, date, cpu, ram, gpu, screen, hdd, ssd, wifi, bluetooth, usbports, cdplayer, solidworks, proteus))
    rows =cur.fetchall()                      #récupère toutes les lignes d'un résultat de requête et les renvoie sous forme de liste de tuples
    conn.close()                              #deconnexion à la base de données
    return rows

def delete(id):
    conn =sqlite3.connect("parcinfo.db")      #connexion à la base de données
    cur= conn.cursor()                        #récuperation d'un curseur pour pouvoir exécuter des requêtes SQlite sur Python
                                              #exécution de la requête "DELETE" qui supprime des données
    cur.execute("DELETE FROM parcinfo WHERE id=?",(id,))
    conn.commit()                             #validation des modifications car lorsqu'on effectue des modifications, celles-ci ne sont pas automatiquement validées
    conn.close()                              #deconnexion à la base de données

def update(id, poste, salle, os, brand, date, cpu, ram, gpu, screen, hdd, ssd, wifi, bluetooth, usbports, cdplayer, solidworks, proteus):
    conn =sqlite3.connect("parcinfo.db")      #connexion à la base de données
    cur= conn.cursor()                        #récuperation d'un curseur pour pouvoir exécuter des requêtes SQlite sur Python
                                              #exécution de la requête "UPDATE" qui modifie des données
    cur.execute("UPDATE parcinfo SET poste=?, salle=?, os=?, brand=?, date=?, cpu=?, ram=?, gpu=?, screen=?, hdd=?, ssd=?, wifi=?, bluetooth=?, usbports=?, cdplayer=?, solidworks=?, proteus=? WHERE id=?",(poste, salle, os, brand, date, cpu, ram, gpu, screen, hdd, ssd, wifi, bluetooth, usbports, cdplayer, solidworks, proteus, id))
    conn.commit()                             #validation des modifications car lorsqu'on effectue des modifications, celles-ci ne sont pas automatiquement validées
    conn.close()                              #deconnexion à la base de données

connect()

