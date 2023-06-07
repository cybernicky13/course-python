import json
from pathlib import Path

# escribir JSON
# productos = [
#     {"id": 1, "name": "Guitarra"},
#     {"id": 2, "name": "Bateria"},
#     {"id": 3, "name": "Bajo"}
# ]

# data = json.dumps(productos)
# Path("archivos/productos.json").write_text(data)

# leer JSON
data = Path("archivos/productos.json").read_text(encoding=("utf-8"))
productos = json.loads(data)
print(productos)

# modificar JSON
productos[0]["name"] = "Chanchito Feliz"
Path("archivos/productos.json").write_text(json.dumps(productos))