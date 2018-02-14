from flask import Flask, render_template
import sqlite3
import sys
import RPi.GPIO as GPIO


def select():
    c.execute("SELECT * FROM pomiary")
    data = c.fetchall()
    print(data)

app = Flask(__name__)
@app.route('/')
def index():
    #  tu wylaczyc pompke
    Pompka = 16
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(Pompka, GPIO.OUT)   # Set LedPin's mode is output  GPIO.setmode(GPIO.BOARD)
    GPIO.output(Pompka, GPIO.LOW)  # led off
    return render_template('glowna.html')

@app.route('/on')
def on():
    # tu wlaczyc pompke
    Pompka = 16
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(Pompka, GPIO.OUT)   # Set LedPin's mode is output  GPIO.setmode(GPIO.BOARD)
    GPIO.output(Pompka, GPIO.HIGH)  # led off
    
    
    
    return render_template('glowna.html')


@app.route('/off')
def off():
    # tu wylaczyc pompke
    Pompka = 16
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(Pompka, GPIO.OUT)   # Set LedPin's mode is output  GPIO.setmode(GPIO.BOARD)
    GPIO.output(Pompka, GPIO.LOW)  # led off    GPIO.output(Pompka, GPIO.LOW)  # led off
    return render_template('glowna.html')

@app.route('/graph')
def graph(chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
        conn = sqlite3.connect('../pomiary.db')
        c = conn.cursor()
        wynik = ""
        c.execute("SELECT * FROM pomiary ORDER BY Czas_pomiaru DESC LIMIT 12")
        dane = c.fetchall()
        czas = []
        temp = []
        wilg = []
        gleba = []
        opady = []
        for row in dane:
            czas.append(row[0].encode('ascii', 'ignore'))
            temp.append(row[1])
            wilg.append(row[2])
            gleba.append(row[3])
            opady.append(row[4])
        c.close()
        conn.close()
        print(czas)
        
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
	series = [{"name": 'Temperatura', "data": temp}, {"name": 'Wilgotnosc', "data": wilg}]
	title = {"text": 'Ostatnie pomiary temperatury'}
	xAxis = {"categories": czas}
	yAxis = [{"title": {"text": 'Temperatura [*C]'}}, {"title": {"text":'Wilgotnosc'}}]
	return render_template('wykresik.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)

    
@app.route('/wykres2')
def wykres(chartID = 'chartID', chart_type = 'line', chart_height = 500):
    
                                                      
    conn = sqlite3.connect('../pomiary.db')
    c = conn.cursor()
    wynik = ""
    c.execute("SELECT * FROM pomiary ORDER BY Czas_pomiaru DESC LIMIT 5")
    dane = c.fetchall()
    czas = []
    temp = []
    wilg = []
    gleba = []
    opady = []
    for row in dane:
        czas.append(row[0])
        temp.append(row[1])
        wilg.append(row[2])
        gleba.append(row[3])
        opady.append(row[4])
        
    print(czas)
    print(temp)

    #print(row)
    #wynik = wynik + str(row) + '\n' #nie dziala nowa linia i nie wiem za bardzo jak to naprawic, chyba w htmlu trzeba dodawac nowe linie za pomoca <br>
    #print(data)
    c.close()
    conn.close()
    #return render_template('wykres.html', series1 = series1)

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
    
