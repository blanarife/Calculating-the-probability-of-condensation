import tkinter as tk
from tkinter import filedialog, messagebox
from pgmpy.readwrite import BIFReader
from pgmpy.inference import VariableElimination
from modelH import create

def selecteaza_fisier():
    nume_fisier = filedialog.askopenfilename(filetypes=[("BIF Files", "*.bif")])
    if nume_fisier:
        return nume_fisier
    else:
        return None

def citeste_retea(nume_fisier):
    reader = BIFReader(nume_fisier)
    return reader.get_model()

def seteaza_si_interogheaza(retea, inferenta, evidenta):
    def adauga_evidenta():
        nod = nod_entry.get()
        valoare = valoare_entry.get()
        if (nod in retea.nodes()) and (valoare in retea.get_cpds(nod).state_names[nod]): #Verifica daca nodul/valoare exista in retea
            if nod and valoare: #Verifica daca utilizatorul a introdus un nod si o valoare
                evidenta[nod] = valoare
                nod_entry.delete(0, tk.END)
                valoare_entry.delete(0, tk.END)
                afiseaza_evidenta()
        else:
            messagebox.showwarning("Avertisment", f"Nodul '{nod}' nu există în rețea sau nodul nu are valoarea '{valoare}'.")


    def afiseaza_evidenta(): #Afiseaza evidentele adaugate in interfață
        info_evidenta.config(text=f"Evidența curentă: {', '.join([f'{k}={v}' for k, v in evidenta.items()])}")

    def interogare():
        nod_interogat = nod_interogare_entry.get()
        if nod_interogat in retea.nodes(): #Verifica daca nodul exista in retea
            rezultat = inferenta.query(variables=[nod_interogat], evidence=evidenta) #obtinem rezultatele inferentei
            messagebox.showinfo("Rezultat Interogare", f"Probabilitatea pentru nodul '{nod_interogat}':\n{rezultat}")
        else:
            messagebox.showwarning("Avertisment", f"Nodul '{nod_interogat}' nu există în rețea.")

    def scoate_evidente():
        evidenta.clear()
        afiseaza_evidenta()
    
    root = tk.Tk()
    root.title("Interogare și Setare Evidență")

    tk.Label(root, text="Nume nod de evidență:").grid(row=0, column=0)
    nod_entry = tk.Entry(root)
    nod_entry.grid(row=0, column=1)

    tk.Label(root, text="Valoare nod de evidență:").grid(row=1, column=0)
    valoare_entry = tk.Entry(root)
    valoare_entry.grid(row=1, column=1)

    adauga_button = tk.Button(root, text="Adaugă Evidență", command=adauga_evidenta)
    adauga_button.grid(row=2, columnspan=2)

    tk.Label(root, text="Nume nod de interogat:").grid(row=3, column=0)
    nod_interogare_entry = tk.Entry(root)
    nod_interogare_entry.grid(row=3, column=1)

    interogare_button = tk.Button(root, text="Interogare Nod", command=interogare)
    interogare_button.grid(row=4, columnspan=2)

    scoate_button = tk.Button(root, text="Scoate Evidențe", command=scoate_evidente)
    scoate_button.grid(row=5, columnspan=2)

    info_evidenta = tk.Label(root, text="")
    info_evidenta.grid(row=6, columnspan=2)

    root.mainloop()

create()
if __name__ == "__main__":
    nume_fisier_retea = selecteaza_fisier()
    if nume_fisier_retea:
        retea = citeste_retea(nume_fisier_retea)
        inferenta = VariableElimination(retea)
        #VariableElimination permite efectuarea de inferențe asupra rețelei bayesiene, 
        #precum calcularea probabilităților pentru anumite variabile în funcție de anumite evidențe.
        #Apoi putem interoga un nod utilizand metoda query pentru a obține rezultatele inferenței.
        evidenta = {} #La inceput nu avem nicio evidenta

        seteaza_si_interogheaza(retea, inferenta, evidenta)
