import numpy as np
import matplotlib.pyplot as plt

# En funktion som returnerar planets z-koordinat för given x- och y-koordinat.
# Kräver en normal (n) till planet eftersom formeln använder planets normalform.
def planeZ(n, x, y):
    return (-n[0]*x - n[1]*y) / n[2] # Planet på normalform, men med z utlöst
        # z = (-Ax - Bx) / C   (för plan genom origo)

# En funktion som tar en punkt och en normal till planet, 
# och returnerar punkten projicerad på planet (eller vektorn från origo till projicerad punkt). 
def projectionOfPoint(p, n):
    # p kan betraktas som en vektor från origo till punkten p.
    # Projektionen av vektorn p på normalen till planet bli alltså:
    projectionOnNormal = (np.dot(p, n) / np.dot(n, n)) * n 

    # p = p projicerad på planet + p projicerad på normalen till planet
    # => p projicerad på planet = p - p projicerad på normalen till planet
    return p - projectionOnNormal

# --- Förbered figuren ---
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
x = np.linspace(-10, 10, 10)
y = np.linspace(-10, 10, 10)
X, Y = np.meshgrid(x, y) # X- och Y-värden som används med planeZ för att beskriva planet.
# ------------------------

# Hjälpfunktion för att slippa skriva ut alla komponenter för att rita en punkt.
def plotPoint(p, c):
    ax.plot(p[0], p[1], p[2], color=c, marker="o")

def deluppgiftb():
    # --- Variabler ---
    point = [np.pi, np.e, 1]
    u = [1, 1, 0]  # Riktningsvektor 1 för planet
    v = [0, -1, 0] # Riktningsvektor 2 för planet
    minusv = [0, 1, 0]
    # Planen beräknas på normalform så en normal per plan krävs.
    normal1 = np.cross(u, v)
    normal2 = np.cross(u, minusv)
    # -----------------

    ax.plot_surface(X, Y, planeZ(normal1, X, Y), color='red', alpha=0.5) #Rita ut planet
    ax.plot_surface(X, Y, planeZ(normal2, X, Y), color='red', alpha=0.5) #Rita ut planet med -v
    plotPoint(point, "blue")              # Rita ut den (oprojicerade) punkten.
    t = projectionOfPoint(point, normal1) # Beräkna projektionen av punkten på första planet.
    plotPoint(t, "green")                 # Rita ut den första projicerade punkten.
    t = projectionOfPoint(point, normal2) # Beräkna projektionen av punkten på andra planet.
    plotPoint(t, "red")                   # Rita ut den andra projicerade punkten.

    # Den gröna punkten visas inte eftersom den röda ritas över den.
    # Kryssprodukten resulterar bara i samma normal med motsatt riktning när -v används ...
    # som också beskriver samma plan. Båda projicerade punkter är likadana.

def deluppgiftc():
    # --- Variabler ---
    point = [np.pi, np.e, 1]
    normal1 = np.array([1, 1, 1]) # Gör "listorna" till vektorer
    normal2 = np.array([3, 3, 3])
    np.vectorize(normal1, normal2)
    # -----------------

    ax.plot_surface(X, Y, planeZ(normal1, X, Y), color='red', alpha=0.5) #Rita ut första planet
    ax.plot_surface(X, Y, planeZ(normal1, X, Y), color='blue', alpha=0.5) #Rita ut andra planet
    plotPoint(point, "blue")              # Rita ut den (oprojicerade) punkten.
    t = projectionOfPoint(point, normal1) # Beräkna projektionen av punkten på första planet.
    plotPoint(t, "green")                 # Rita ut den första projicerade punkten.
    t = projectionOfPoint(point, normal2) # Beräkna projektionen av punkten på andra planet.
    plotPoint(t, "red")                   # Rita ut den andra projicerade punkten.

#deluppgiftb() # 2b) avkommentera för att köra
deluppgiftc()
plt.show() # Visa rummet
