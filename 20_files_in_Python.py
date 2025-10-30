# Öffnen oder erstellen der Datei zum Schreiben ("w" = write)
import os

with open("python123.txt", "w") as file:
    file.write("Hallo, das ist meine erste Datei mit Python!\n")
    file.write("Ich lerne gerade, wie man Dateien liest und schreibt.\n")

print("Datei erfolgreich erstellt und Text gespeichert!")

with open("python123.txt", "r") as file:
    content = file.read()  # Lies den ganzen Inhalt
    print("📄 Dateiinhalt:")
    print(content)

with open("python123.txt", "a") as file:
  file.write("Diese Zeile wurde später hinzugefügt.\n")

print("Neuer Text wurde an die Datei angehängt!")

with open("python123.txt", "r") as file:
    for line in file:
        print("Zeile:", line.strip())

    

if os.path.exists("python123.txt"):
    print("✅ Datei existiert!")
else:
    print("❌ Datei nicht gefunden.")