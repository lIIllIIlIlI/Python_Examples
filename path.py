# 1. verhindern : hardcoded path user/data/text.txt
# 2. verhindern : relative Pfade, read(/logfiles/error.log), da Module in Unterordnern jeweils einen angepassten Pfad brauchen
# Besser ist es, die Pfade zur Lautzeit absolut zu bestimmen. 
# Wird ein Skript aus der ferne aufgerufen bzw innerhalb einer Ide über eine Ordnerstruktur hinweg, ist nicht klar welches library
# welchen Pfad als root bezeichnet, den Pfad der Aufrufers oder den Pfad des Skriptes. Daher sollte der Skriptpfad absolut zur 
# Lautzeit eingeholt werden und alle weiteren Pfade von dort aus absolut bestimmt werden. 

import pathlib
