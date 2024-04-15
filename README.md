# Sakai_Aufgabe_1
Leistungskurve

## Klonen Sie das GitHub-Repository auf Ihren PC:
- Öffnen Sie dazu Git Bash und navigieren Sie zu dem gewünschten Ordner: cd "<gewünschter Ordner>"
- Geben Sie den folgenden Befehl ein, um das Repository in den Ordner zu klonen: git clone <Link des Repositorys>

## Öffnen Sie den Ordner in VS Code.

## Virtuellen Bereich erstellen:
- Öffnen Sie ein neues Terminal --> Windows PowerShell.
- Geben Sie folgenden Befehl ein, um einen virtuellen Bereich zu erstellen: python -m venv .venv
- Geben Sie folgenden Befehl ein, um einen virtuellen Bereich zu aktivieren: .\.venv\Scripts\Activate
- Falls dieser nicht funktioniert, geben Sie vorher folgenden Befehl ein, um den Zugriff zu erlauben: Set-ExecutionPolicy RemoteSigned -Scope CurrentUser.
- Der virtuelle Bereich ist nun erstellt und aktiviert.

## Notwendige Pakete installieren:
- Die notwendigen Pakete sind in der Textdatei requirements.txt aufgeführt.
- Für die nächsten Schritte müssen Sie sich bereits in der Umgebung befinden und diese muss aktiviert sein.
- Sie können sie einzeln installieren, indem Sie folgenden Befehl in die Kommandozeile von Windows PowerShell eingeben: pip install <gewünschtes Paket>
- Sie können auch alle Pakete gleichzeitig installieren, indem Sie folgenden Befehl in die Kommandozeile von Windows PowerShell eingeben: pip install -r requirements.txt
- Erstellen der Textdatei requirements.txt: pip freeze > requirements.txt

## Der Code kann nun ausgeführt werden.

## Wird der Code ausgeführt, wird eine Bilddatei namens "Leistungskurve.png" gespeichert.