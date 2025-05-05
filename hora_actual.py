from fastapi import FastAPI , Query
from datetime import datetime
import pytz

app = FastAPI()

@app.get("/")
def obtener_hora_actual(timezone : str = Query(default = "UTC", description = "Zona horaria en Formato 'Content/City', ej: America/Mexico_City")):

    if timezone not in pytz.all_timezones:
        return {
            "Error" : "Zona Horaria no valida. Usa el Formato 'Content/City'. Ejemplo : America/Mexico_City"
        }

    zona = pytz.timezone(timezone)
    hora = datetime.now(zona)
    return {
        "Zona Horaria" : timezone,
        "Fecha": hora.strftime("%Y-%m-%d"),
        "Hora": hora.strftime("%H:%M:%S"),
        #"TimeStamp" : hora.isoformat()
    }
