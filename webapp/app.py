from flask import Flask, render_template
import sqlite3


def select():
    c.execute("SELECT * FROM pomiary")
    data = c.fetchall()
    print(data)

app = Flask(__name__)
@app.route('/')
def index():
    #  tu wylaczyc pompke
    return render_template('glowna.html')

@app.route('/on')
def on():
    # tu wlaczyc pompke
    return render_template('glowna.html')


@app.route('/off')
def off():
    # tu wylaczyc pompke
    return render_template('glowna.html')


    
@app.route('/wykres')
def wykres():
    return render_template('wykresik.html')

@app.route('/aktualne')
def aktualne():
    conn = sqlite3.connect('../pomiary.db')
    c = conn.cursor()
    wynik = ""
    c.execute("SELECT * FROM pomiary ORDER BY Czas_pomiaru DESC LIMIT 1")
    dane = c.fetchall()
    czas = dane[0][0]
    temp = dane[0][1]
    wilg = dane[0][2]
    gleba = dane[0][3]
    opady = dane[0][4]
    if gleba == 1:
        gleba = "Tak"
    else:
        gleba = "Nie"
        
    if opady == 1:
        opady = "Tak"
    else:
        opady = "Nie"

    #print(row)
    #wynik = wynik + str(row) + '\n' #nie dziala nowa linia i nie wiem za bardzo jak to naprawic, chyba w htmlu trzeba dodawac nowe linie za pomoca <br>
    #print(data)
    c.close()
    conn.close()
    
    return render_template('aktualne.html', czas = czas, temp = temp, wilg = wilg, opady = opady, gleba = gleba)
    
@app.route('/halo')
def halo():
    conn = sqlite3.connect('../pomiary.db')
    c = conn.cursor()
    wynik = ""
    c.execute("SELECT * FROM pomiary ORDER BY Czas_pomiaru DESC LIMIT 10")
    data = c.fetchall()
    for row in data:
        print(row)
        wynik = wynik + str(row) + '\n' #nie dziala nowa linia i nie wiem za bardzo jak to naprawic, chyba w htmlu trzeba dodawac nowe linie za pomoca <br>
    #print(data)
    c.close()
    conn.close()
    
    return wynik
    
    #return str(data)

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name= name)


if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')
    
