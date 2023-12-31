import time
from array import array

# Creación de un array de un millón de enteros
arr_size = 2_000_000
arr = array("l", [i for i in range(arr_size)])

# Medición del tiempo de acceso
start_time = time.time()
for i in range(arr_size):
    _ = arr[i]

# Convertir a milisegundos
elapsed_time = (time.time() - start_time) * 1000

print("         /^\\/^\\")
print("       _|__|  O|")
print("\\/    /~     \\_/ \\")
print(" \\____|__________/  \\")
print("        \\_______      \\")
print("                `\\     \\                 \\")
print("                  |     |                  \\")
print("                 /      /                    \\")
print("                /     /                       \\\\")
print("              /      /                         \\ \\")
print("             /     /                            \\  \\")
print("           /     /             _----_            \\   \\")
print("          /     /           _-~      ~-_         |   |")
print("         (      (        _-~    _--_    ~-_     _/   |")
print(f"          \\      ~-____-~    _-~    ~-_    ~-_-~    /")
print(f"            ~-_           _-~          ~-_       _-~")
print(f"               ~--______-~                ~-___-~")
print("             ╔═════════════════════════════╗")
print("             ║    Arreglos en Python 󰌠     ║")
print("             ║-----------------------------║")
print(f"             ║ Tiempo de acceso: {elapsed_time:.2f} ms ║")
print("             ╚═════════════════════════════╝")
