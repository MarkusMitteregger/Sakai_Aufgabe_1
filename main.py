import numpy as np
from sort import insertion_sort, bubble_sort    
import matplotlib.pyplot as plt
from load_data import load_data

if __name__ == "__main__":
    #Laden der Daten
    data = load_data('activity.csv')
    power_W = data['PowerOriginal']
    
    
    #Speichern der sortierten Daten
    sorted_power_W = insertion_sort(power_W)

    #Berechnen des Zeit-Vektors
    #time_array = np.linspace(0, 1805, np.size(sorted_power_W))
    time = data['Duration']
    indices = list(range(len(time)))
    x_values_scaled = [x/60 for x in indices]
    
    #Plotten der Leistungskurve
    plt.plot(x_values_scaled, sorted_power_W[::-1])
    ax = plt.subplot()
    ax.plot(x_values_scaled, sorted_power_W[::-1])
    ax.set_xlabel("$t/min$")
    ax.set_ylabel("$P/W$")
    plt.title("Leistungskurve")
    ax.grid(True, linestyle = '-')
    ax.set_yticks(np.arange(0, 450, 50))
    #Bild speichern:
    datapath = r'figures\my_power_curve.png'
    plt.savefig(datapath)
    plt.show()

 #Kommt bei Insertion_sort und Bubble_sort der gleiche Vektor heraus?
if bubble_sort(power_W).all() == sorted_power_W.all():
     bool_same = True
else:
    bool_same = False
print(bool_same)