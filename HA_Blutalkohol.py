# Masse in kg

m = input("Geben sie die Masse der Person in kg ein: ")
while not m.isnumeric():
    m = input("Antwort muss eine Zahl sein.\nGeben sie die Masse der Person in kg ein: ")
m = float(m)

# Verteilungsfaktor im Körper (Frauen: 0.6, Männer: 0.7)

g = input("Geben sie den Geschlecht (m/f) der Person ein: ")
while g != 'm' and g !='f':
    g = input("Antwort muss entweder 'f' oder 'm' sein.\nGeben sie den Geschlecht (m/f) der Person ein: ")
if g == 'm':
    r = 0.6
elif g == 'f':
    r = 0.7

# Volumen des Getränks in ml

V = input("Geben sie das Volumen des Getränks in ml ein: ")
while not V.isnumeric():
    V = input("Antwort muss eine Zahl sein.\nGeben sie das Volumen des Getränks in ml ein: ")
V = float(V)

# Alkoholvolumenanteil in Prozent

e = input("Geben sie den Alkoholvolumenanteil in Prozent ein: ")
while not e.replace(".", "").isnumeric():
        e = input("Antwort muss eine Zahl sein.\nGeben sie den Alkoholvolumenanteil in Prozent ein: ")

e = float(e)

# Führe Berechnung durch

A = V * e * 0.8

c = A / (m * r)

print (round(c,2))

