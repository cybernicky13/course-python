from pathlib import Path

# Path(r"C:\Archivos de Programa\Berserk")
# Path(r"/usr/bin")
# Path()
# Path.home()
# Path("one/__init__.py")

path = Path("hola-mundo/mi-archivo.py")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()
)

p = path.with_name("chachito.py")
print(p)
p = path.with_suffix("chachito.bat")
print(p)
p = path.with_stem("feliz")