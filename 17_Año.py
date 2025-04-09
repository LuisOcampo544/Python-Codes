from datetime import datetime
fecha = datetime.now()
print(fecha)

import datetime
fecha = datetime.datetime.now() 
print(fecha)

año = datetime.datetime.strftime(fecha, "%Y")
print(año)

# "%d" = "DIA"
# "%m" = "MES"
# "%Y" = "AÑO"
# "%H" = "HORAS"
# "%M" = "MINUTOS"
# "%S" = "SEGUNDOS"                               
