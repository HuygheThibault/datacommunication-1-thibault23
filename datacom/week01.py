from RPi import GPIO
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# HOUD JE STRIKT AAN DE NAAMGEVING EN GEBRUIKTE PINNUMMERS UIT DE OPGAVE
# DE EXPRESSIE ... DIENT ALS PLAATSHOUDER EN MOET JE VERVANGEN DOOR EIGEN CODE
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# 1) Maak een klasse LED
class LED:
    # a) De init-methode heeft 1 parameter 'pin' waarmee je het pinnummer meegeeft.
    # Dit nummer wordt bijgehouden in een klassevariabele met dezelfde naam.
    # De overeenkomstige pin moet worden ingesteld als output.
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    # b) De methode 'on' laat de LED branden
    def on(self):
        GPIO.output(self, GPIO.HIGH)

        # c) De methode 'off' dooft de LED
    def off(self):
        GPIO.output(self, GPIO.LOW)
    # d) De methode 'toggle' leest eerst de huidige status van de pin.
    # Vervolgens wordt de tegenovergestelde waarde naar de pin geschreven.
    def toggle(self):
        value = GPIO.input(self)
        if value == "HIGH":
            GPIO.output(self, GPIO.LOW)
        else:
            GPIO.output(self, GPIO.HIGH)


# 2) Maak een klasse Button
class Button:
    # a) De init-methode heeft 1 parameter, pin, waarmee je het pinnummer meegeeft.
    # Dit nummer wordt bijgehouden in een klassevariabele met dezelfde naam.
    # De overeenkomstige pin moet worden ingesteld als input met pull-up weerstand.
    ...

    # b) De klasse heeft een (read-only) property 'pressed', die de status van de knop teruggeeft (ingedrukt = True)
    ...

    # c) Maak een methode wait_for_press
    # Deze methode test in een oneindige lus of de knop is ingedrukt.
    # Indien niet, wacht ze 100ms. Indien wel, returnt ze.
    ...

    # CHALLENGE: Maak een methode on_press, waarmee je een functienaam kan meegeven.
    # Wanneer op de knop gedrukt wordt, wordt deze functie uitgevoerd
    ...


def main():
    # Hier kan je code schrijven die wordt uitgevoerd wanneer je het bestand rechtsreeks uitvoert
    # (i.p.v. er klassen uit te importeren). Schrijf hier de code om je klassen te testen.

    # Stel de pinnummering van de GPIO library in (!)
    ...

    # Initialiseer een LED op pin 28:
    led = ...

    # Laat de LED branden, wacht 1 sec., en doof ze weer:
    ...

    # Initialiseer een knop op pin 29:
    btn = ...

    # Print de status van de knop:
    print(...)

    # Wacht tot op de knop gedrukt wordt, laat dan de LED 5x knipperen met een interval van 250ms:
    ...
    for i in ...:
        ...

    # Initialiseer een list van LEDs op volgende pins:
    led_pins = (28, 29, 34, 25)
    led_objects = ...

    # Laat de leds 1 voor 1 branden voor een halve seconde:
    ...


# Deze vreemde constructie zorgt ervoor dat de functie main enkel wordt opgeroepen
# wanneer het script rechtstreeks wordt gestart.
if __name__ == '__main__':
    main()
