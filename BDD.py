#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector 
from agent import Psutil

connection = mysql.connector.connect(host="localhost",user="root",password="root", database="python")
cursor = connection.cursor()


#creation BDD
cursor.execute("""
CREATE TABLE IF NOT EXISTS infosPC (
    id int(5) NOT NULL AUTO_INCREMENT,
    nomHost varchar(255) DEFAULT NULL,
    disk varchar(255) DEFAULT NULL,
    OS varchar(255) DEFAULT NULL,
    CPU_STAT varchar(255) DEFAULT NULL,
    PRIMARY KEY(id)
);
""")

# insérer des données
# info = {"nomHost": "PC1", "disk": "3564879", "OS": "windows"}
# cursor.execute("""INSERT INTO infosPC (nomHost, disk, OS) VALUES(%(nomHost)s, %(disk)s, %(OS)s)""", info)

info = Psutil()
infoPC = info.getInfo()
print infoPC
cursor.execute("""INSERT INTO infosPC (nomHost, disk, OS, CPU_STAT) VALUES(%(nomHost)s, %(disk)s, %(OS)s, %(CPU_STAT)s)""", infoPC)

#affichage des données
cursor.execute("""SELECT * FROM infosPC""")
rows = cursor.fetchall()
for row in rows:
    print('{0} : {1} - {2} - {3} - {4}'.format(row[0], row[1], row[2], row[3], row[4]))

connection.commit()

connection.close()