import random
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def wichteln(personen):
    zu_beschenken = personen.copy()
    wichtel_dict = {}
    
    for person in personen.keys():
        auswahl = [p for p in zu_beschenken.keys() if p != person]
        if len(auswahl) == 0:
            return None
            
        beschenkter = random.choice(auswahl)
        wichtel_dict[person] = beschenkter
        zu_beschenken.pop(beschenkter)
        
    return wichtel_dict

teilnehmer = {'Person1': 'email1@example.com', 'Person2': 'email2@example.com', 
              'Person3': 'email3@example.com', 'Person4': 'email4@example.com', 
              'Person5': 'email5@example.com'}

ergebnis = wichteln(teilnehmer)
while ergebnis is None:
    ergebnis = wichteln(teilnehmer)

print("\n🎉🎉🎉 Willkommen zum Wichteln! 🎉🎉🎉\n")
time.sleep(2)

# E-Mail-Einstellungen
smtp_server = 'smtp.example.com'
smtp_port = 587  # oder 465 für SSL
smtp_username = 'your_email@example.com'
smtp_password = 'your_password'

# Verbindung zum SMTP-Server herstellen
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_username, smtp_password)

for person, beschenkter in ergebnis.items():
    print(f"🌟 {person}, du ziehst jetzt...")
    time.sleep(2)
    print("📧 ... und die E-Mail ist unterwegs! 📧\n")
    time.sleep(1)

    subject = "Dein Wichtel-Partner!"
    html_message = f"""<html>
    <body>
        <h1>Hallo {person},</h1>
        <p>Du bist der Wichtel für <strong>{beschenkter}</strong>!</p>
        <p>Frohe Feiertage! 🎉🎁</p>
    </body>
    </html>"""

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = smtp_username
    msg['To'] = teilnehmer[person]

    msg.attach(MIMEText(html_message, 'html'))

    server.sendmail(smtp_username, teilnehmer[person], msg.as_string())
    time.sleep(1)

# Verbindung zum SMTP-Server beenden
server.quit()

print("🎉🎉🎉 E-Mails wurden gesendet. Das Wichteln ist abgeschlossen! Frohe Feiertage! 🎉🎉🎉")

