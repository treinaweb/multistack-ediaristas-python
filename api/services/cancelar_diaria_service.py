import datetime

def verificar_diferenca_data_atual(data_diaria):
    data_atual = datetime.datetime.now()
    data_diaria_cancelar = data_diaria.replace(tzinfo=None)
    return abs(data_diaria_cancelar - data_atual)
