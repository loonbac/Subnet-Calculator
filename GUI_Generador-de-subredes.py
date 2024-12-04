import tkinter as tk
from tkinter import messagebox
import ipaddress

class SubredApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Subredes")
        
        self.label_ip = tk.Label(root, text="Ingresa una dirección IP:")
        self.label_ip.grid(row=0, column=0, padx=10, pady=10)
        self.entry_ip = tk.Entry(root)
        self.entry_ip.grid(row=0, column=1, padx=10, pady=10)

        self.label_mascara = tk.Label(root, text="Ingresa una máscara en formato CIDR (0-31):")
        self.label_mascara.grid(row=1, column=0, padx=10, pady=10)
        self.entry_mascara = tk.Entry(root)
        self.entry_mascara.grid(row=1, column=1, padx=10, pady=10)

        self.boton_generar = tk.Button(root, text="Generar Subredes", command=self.generar_subredes)
        self.boton_generar.grid(row=2, column=0, columnspan=2, pady=10)

        self.label_subredes = tk.Label(root, text="Selecciona una máscara para ver las subredes:")
        self.label_subredes.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.combo_subredes = tk.StringVar()
        self.lista_subredes = tk.OptionMenu(root, self.combo_subredes, [])
        self.lista_subredes.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.boton_mostrar = tk.Button(root, text="Mostrar Subredes", command=self.mostrar_subredes)
        self.boton_mostrar.grid(row=5, column=0, columnspan=2, pady=10)

        self.texto_resultados = tk.Text(root, height=15, width=50)
        self.texto_resultados.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def obtener_ip_y_mascara(self):
        try:
            ip = self.entry_ip.get()
            mascara = int(self.entry_mascara.get())

            if mascara < 0 or mascara > 31:
                messagebox.showerror("Error", "La máscara debe estar entre 0 y 31.")
                return None, None

            red = ipaddress.ip_network(f"{ip}/{mascara}", strict=False)
            return red, mascara
        except ValueError as e:
            messagebox.showerror("Error", f"Error: {e}. Ingresa una dirección IP y una máscara válidas.")
            return None, None

    def generar_subredes(self):
        red, mascara = self.obtener_ip_y_mascara()
        
        if red and mascara:
            self.texto_resultados.delete(1.0, tk.END)
            self.lista_subredes['menu'].delete(0, 'end')
            subredes = []

            for nueva_mascara in range(mascara + 1, 32):
                bits_para_subredes = nueva_mascara - mascara
                num_subredes = 2 ** bits_para_subredes
                subredes.append(nueva_mascara)

            for subred in subredes:
                self.lista_subredes['menu'].add_command(label=f"/{subred}", command=tk._setit(self.combo_subredes, f"/{subred}"))

    def mostrar_subredes(self):
        try:
            seleccion = self.combo_subredes.get()
            if not seleccion:
                messagebox.showerror("Error", "Selecciona una máscara.")
                return

            mascara = int(seleccion[1:])
            red, _ = self.obtener_ip_y_mascara()
            if red:
                subredes_generadas = list(red.subnets(new_prefix=mascara))

                self.texto_resultados.delete(1.0, tk.END)  # Limpiar resultados previos

                for i, subred_actual in enumerate(subredes_generadas):
                    primera_ip = subred_actual.network_address + 1
                    ultima_ip = subred_actual.broadcast_address - 1
                    broadcast = subred_actual.broadcast_address

                    self.texto_resultados.insert(tk.END, f"Subred {i + 1}:\n")
                    self.texto_resultados.insert(tk.END, f"  ID de red: {subred_actual.network_address}\n")
                    self.texto_resultados.insert(tk.END, f"  Primera IP usable: {primera_ip}\n")
                    self.texto_resultados.insert(tk.END, f"  Última IP usable: {ultima_ip}\n")
                    self.texto_resultados.insert(tk.END, f"  Broadcast: {broadcast}\n\n")
        except ValueError:
            messagebox.showerror("Error", "Hubo un problema al procesar las subredes.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SubredApp(root)
    root.mainloop()
