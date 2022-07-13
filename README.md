# craftworkChallenge
 
- Die Daten beinhalten Ausschnitte in unterschiedlichen Sprachen, ev. auch in ungültigem CSV Format. Welche Probleme können dabei auftreten, wie könnte diesen vorgebeugt werden?
  - Bei unterschiedlichen Sprachen kann es dazu kommen, dass manche Symbole (z.B Russisch) nicht richtig angezeigt werden können. Hier im challenge.csv sind auch arabische Zeichen vorhanden, dadurch man in diesen Länder alles von rechts nach links liest ist hier auch der Index des Arrays falsch. Am besten wäre es, dass das File nur eine Sprache beinhaltet damit man nicht viele Randcases beachten muss. 
  - Bevor man mit dem File überhaupt beginnt zu arbeiten, sollte man immer checken ob das CSV Format zu den vorrausetzungen passt. Wenn nicht, sollte man zuerst das File reinigen, damit man später nicht auf Fehler stößt.
  
- Es kann vorkommen, dass Daten mehrmals gesendet werden (nicht notwendigerweise als identisches CSV, möglicherweise auch neue Daten gemischt mit bereits empfangenen Daten). Es soll jeder Eintrag aber nur einmalig gespeichert werden. Wie kann das gewährleistet werden?
  - In der jetzigen Implementation ist das nicht gewährleistet. Um es gewährleisten wären Timestamps, also der Zeitpunkt wann der Eintrag aufgenommen wurde, die perfekte Lösung. Somit könnte man mehrere Daten der gleichen Stadt oder immer die neuesten Datein immer speichern.
  
- Es sollen zusätzlich noch die Daten von weiteren Kontinenten gespeichert werden. Welche Änderungen wären dafür notwendig? Was muss unternommen werden, falls auch die historischen Daten (d. h. bereits empfangene Daten) in diese Tabellen geladen werden sollen?
  - Es müsste eine neue Tabelle, in der Datenbank, des Kontinents erstellt werden. Dann müsste eine neue Variable erstellt werden, die die Boundary Box erstellt. Danach müsste nur mehr auf die Boundary box überprüft werden wie in Zeile 48 und später in die Datenbank eingefügt werden. 
  
- Könnten mit der gegebenen Implementierung 10 Mio Zeilen am Tag bearbeitetwerden? Falls nein, welche Änderungen (am Code, an den verwendeten Technologien, ...) können unternommen werden um diese Performance zu gewährleisten?
  - Von meinem Gefühl aus sollte es möglich sein, eine hohe Anzahl von Zeilen am Tag zu bearbeiten. 
  
  
