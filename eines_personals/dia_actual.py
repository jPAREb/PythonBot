from datetime import datetime

messos = [
    "Gener",
    "Febrer",
    "Març",
    "Abril",
    "Maig",
    "Juny",
    "Juliol",
    "Agost",
    "Setembre",
    "Octubre",
    "Novembre",
    "Desembre"
]

def data_actual_tweet():
    mes = ''
    if (datetime.today().strftime('%m')[0] == '0'):
        mes = datetime.today().strftime('%m')[0]
    else:
        mes = datetime.today().strftime('%m')

    missatge = ''
    if (mes == '4' or mes == '8' or mes == '10'):
        missatge = 'Avui és ',datetime.today().strftime('%d'), " d'", messos[int(mes)-1], " de l'any ", datetime.today().strftime('%Y')
    else:
        missatge = 'Avui és ',datetime.today().strftime('%d'), ' de ', messos[int(mes)-1], " de l'any ", datetime.today().strftime('%Y')
    
    string_missatge = ''
    for blocs in missatge:
        string_missatge += blocs
    return string_missatge