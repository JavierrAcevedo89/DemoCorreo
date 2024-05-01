import tkinter as tk
from tkinter import messagebox

class EmailApp:
    def __init__(self, master, username, other_app):
        self.master = master
        self.username = username
        self.other_app = other_app
        self.master.title(f"Bandeja de Correo Electrónico - {self.username}")

        self.received_messages = []
        self.sent_messages = []

        self.from_label = tk.Label(master, text="De:")
        self.from_label.grid(row=0, column=0, sticky="w")
        self.from_entry = tk.Entry(master)
        self.from_entry.grid(row=0, column=1, columnspan=2, sticky="we")
        self.from_entry.insert(0, self.username)
        self.from_entry.config(state="readonly")

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

        self.received_listbox_label = tk.Label(master, text="Correos Recibidos:")
        self.received_listbox_label.grid(row=6, column=0, sticky="w")
        self.received_message_listbox = tk.Listbox(master, height=10, width=70)
        self.received_message_listbox.grid(row=7, column=0, columnspan=3, sticky="we")
        self.received_message_listbox.bind('<Double-Button-1>', self.show_message_details)

        self.sent_listbox_label = tk.Label(master, text="Correos Enviados:")
        self.sent_listbox_label.grid(row=8, column=0, sticky="w")
        self.sent_message_listbox = tk.Listbox(master, height=10, width=70)
        self.sent_message_listbox.grid(row=9, column=0, columnspan=3, sticky="we")
        self.sent_message_listbox.bind('<Double-Button-1>', self.show_message_details)

    def send_message(self):
        sender = self.username
        receiver = self.to_entry.get()
        subject = self.subject_entry.get()
        message = self.message_text.get("1.0", tk.END)

        if sender and receiver and subject and message:
            self.other_app.receive_message({"De": sender, "Para": receiver, "Asunto": subject, "Mensaje": message})
            self.sent_messages.append({"De": sender, "Para": receiver, "Asunto": subject, "Mensaje": message})
            messagebox.showinfo("Mensaje enviado", "El mensaje ha sido enviado correctamente.")
            self.clear_fields()
            self.refresh_messages()
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    def receive_message(self, message):
        self.received_messages.append(message)
        self.refresh_messages()

    def refresh_messages(self):
        self.received_message_listbox.delete(0, tk.END)
        self.sent_message_listbox.delete(0, tk.END)

        for msg in self.received_messages:
            self.received_message_listbox.insert(tk.END, f"De: {msg['De']} - Para: {msg['Para']} - Asunto: {msg['Asunto']}")

        for msg in self.sent_messages:
            self.sent_message_listbox.insert(tk.END, f"De: {msg['De']} - Para: {msg['Para']} - Asunto: {msg['Asunto']}")

    def show_message_details(self, event):
        index_received = self.received_message_listbox.curselection()
        index_sent = self.sent_message_listbox.curselection()

        if index_received:
            index = index_received[0]
            msg = self.received_messages[index]
        elif index_sent:
            index = index_sent[0]
            msg = self.sent_messages[index]

        details = f"De: {msg['De']}\nPara: {msg['Para']}\nAsunto: {msg['Asunto']}\nMensaje:\n{msg['Mensaje']}"
        messagebox.showinfo("Detalles del Mensaje", details)

    def clear_fields(self):
        self.to_entry.delete(0, tk.END)
        self.subject_entry.delete(0, tk.END)
        self.message_text.delete("1.0", tk.END)

def main():
    root1 = tk.Tk()
    app1 = EmailApp(root1, "Usuario1", None)

    root2 = tk.Tk()
    app2 = EmailApp(root2, "Usuario2", app1)

    app1.other_app = app2

    root1.mainloop()
    root2.mainloop()

if __name__ == "__main__":
    main()
