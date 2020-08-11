import subprocess
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import ctypes
user32 = ctypes.windll.user32


L = str(int((user32.GetSystemMetrics(0) / 2)-150))
H = str(int((user32.GetSystemMetrics(1) / 2)-37.5))
    

master = tk.Tk()

master.title('Sélection des paramètres')
master.geometry('300x75+'+L+'+'+H)
tk.Label(master, 
         text="Serveur à ping:").grid(row=0)
tk.Label(master, 
         text="Temps de ping (s)").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
 
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


def callbackExit():
    global server
    server = e1.get()
    global n
    n = int(e2.get())*10
    master.destroy()
    return 0
    
    

                                    

tk.Button(master, 
          text='OK', command=callbackExit).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)


tk.mainloop()


f=plt.gcf()
f.canvas.set_window_title("Windows pingtest by WG")
f.set_size_inches(11,8)


plt.ylabel("Ping en ms")
plt.xticks([])
plt.title("Serveur: "+  server)

temps = np.arange(0,n,1)
stock = [0,]*n
nbrCrash = 0


for i in range(0,n):

    if i==0:
        plt.axis([1,n,0,1000])
        line, = plt.plot(temps,stock)
    else:
        try:
        
            data = subprocess.check_output(['ping', server, "-n", '1']).decode('cp850', errors="backslashreplace").split(' ')
            ping = data[15].split('=')
            realPing = ping[1] 
            #print(realPing,"ms")
            stock[i] = int(realPing)
            plt.axis([1,i,0,max(stock)])
        except subprocess.CalledProcessError:
            ping = 0
            nbrCrash=nbrCrash + 1
            plt.annotate('crash!', xy=(temps[i],0), xytext=(temps[i]-(1/temps[i]),(-np.max(stock)) / 10), arrowprops=dict(facecolor='red', shrink=0.05))
        line.set_ydata(stock)
        plt.pause(0.05)

plt.autoscale(enable=True, axis='y', tight=True)

pingMoyen = np.mean(stock)
pingMax = np.max(stock)
pingMin = min(stock[1:n])

if pingMin == 0:
    pingMin = "crash!"
    plt.text(-n/8, pingMax * 0.7,"Ping min: " + pingMin)
else:
    pingMin = pingMin
    plt.text(-n/8, pingMax * 0.7,"Ping min: " + str(pingMin) + " ms")

plt.text(-n/8, pingMax * 0.75,"Ping max: " + str(pingMax) + " ms")
plt.text(-n/8, pingMax * 0.65,"Ping moyen: " + str(pingMoyen) + " ms")
plt.text(-n/8, pingMax * 0.6,"Nbr crash: " + str(nbrCrash))

line, = plt.plot(temps,stock)




plt.show()

