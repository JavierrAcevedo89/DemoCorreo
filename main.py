import tkinter as tk
from tkinter import messagebox

class EmailApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Bandeja de Correo Electrónico")

        self.messages = []

        self.from_label = tk.Label(master, text="De:")
        self.from_label.grid(row=0, column=0, sticky="w")
        self.from_entry = tk.Entry(master)
        self.from_entry.grid(row=0, column=1, columnspan=2, sticky="we")

        self.to_label = tk.Label(master, text="Para:")
        self.to_label.grid(row=1, column=0, sticky="w")
        self.to_entry = tk.Entry(master)
        self.to_entry.grid(row=1, column=1, columnspan=2, sticky="we")

        self.subject_label = tk.Label(master, text="Asunto:")
        self.subject_label.grid(row=2, column=0, sticky="w")
        self.subject_entry = tk.Entry(master)
        self.subject_entry.grid(row=2, column=1, columnspan=2, sticky="we")

        self.message_label = tk.Label(master, text="Mensaje:")
        self.message_label.grid(row=3, column=0, sticky="nw")
        self.message_text = tk.Text(master, height=10, width=50)
        self.message_text.grid(row=3, column=1, columnspan=2, sticky="we")

        self.send_button = tk.Button(master, text="Enviar", command=self.send_message)
        self.send_button.grid(row=4, column=1)

        self.refresh_button = tk.Button(master, text="Actualizar", command=self.refresh_messages)
        self.refresh_button.grid(row=4, column=2)

        self.message_listbox = tk.Listbox(master, height=15, width=70)
        self.message_listbox.grid(row=5, column=0, columnspan=3, sticky="we")

    def send_message(self):
        sender = self.from_entry.get()
        receiver = self.to_entry.get()
        subject = self.subject_entry.get()
        message = self.message_text.get("1.0", tk.END)

        if sender and receiver and subject and message:
            self.messages.append({"De": sender, "Para": receiver, "Asunto": subject, "Mensaje": message})
            messagebox.showinfo("Mensaje enviado", "El mensaje ha sido enviado correctamente.")
            self.clear_fields()
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    def refresh_messages(self):
        self.message_listbox.delete(0, tk.END)
        for msg in self.messages:
            self.message_listbox.insert(tk.END, f"De: {msg['De']} - Para: {msg['Para']} - Asunto: {msg['Asunto']}")

    def clear_fields(self):
        self.from_entry.delete(0, tk.END)
        self.to_entry.delete(0, tk.END)
        self.subject_entry.delete(0, tk.END)
        self.message_text.delete("1.0", tk.END)

def main():
    root = tk.Tk()
    app = EmailApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
