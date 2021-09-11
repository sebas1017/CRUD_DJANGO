
from datetime import datetime, time

def quitar_espacios(valor):
    valor = valor.rstrip()
    valor = valor.lstrip()
    valor = valor.upper()
    return valor
def valida_tiempo(time_attention,final_attention_time,date_of_request):
    time_attention =  datetime.strptime(time_attention , '%H:%M') 
    final_attention_time = datetime.strptime(final_attention_time , '%H:%M') 
    if final_attention_time < time_attention:
        error = 'La hora final de atencion no puede ser menor a la hora inicial de atencion...'
        return error 
    try:
        date_time_obj = datetime. strptime(date_of_request , '%Y-%m-%d')
        if date_time_obj > datetime.now():
            error = 'La fecha de solicitud no puede ser mayor a la fecha actual , gracias...'
            return error
    except:
        error = 'El formato de fecha del campo Date of request no es el adecuado recuerde yyyy-mm-dd...'
        return error
    
    return None