li = ['Wort', 1, "noch eine Zeichenkette", 23.4]                # Eine Liste


week_day_dict = {1: 'Montag', 2: 'Dienstag', 3: 'Mittwoch', 4: 'Donnerstag', 5: 'Freitag', 6: 'Samstag', 7:'Sonntag'}

print(f"Der 4. Wochentag ist der {week_day_dict[4]}")


import numpy as np

dir_dict = {'left': np.array([-1,0]), 'right':np.array([1,0]), 'up': np.array([0,-1]), 'down': np.array([0,1]) }

pos = np.array([5,12])
pos = pos + 3*dir_dict['up']    # Macht 3 Schritte nach oben
keys = list(dir_dict.keys())     
dir = np.random.choice(keys)    
pos=pos+dir_dict[dir]           # macht einen Schritt in zufälliger Richtung


for (k,v in dir_dict):
    print(k,v)
