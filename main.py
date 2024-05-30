import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import Tk, Label, Entry, Text, Button, END, messagebox

def send_email():
    sender_email = sender_entry.get()
    sender_password = password_entry.get()  # Aquí ingresarás la contraseña de aplicación
    recipient_email = recipient_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", END)

    if not sender_email or not sender_password or not recipient_email or not subject or not message.strip():
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return

    try:
        # Configurar el servidor SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Construir el correo electrónico
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Enviar el correo electrónico
        server.send_message(msg)
        server.quit()

        messagebox.showinfo("Éxito", "Correo enviado exitosamente")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo enviar el correo: {e}")

# Crear la interfaz gráfica
root = Tk()
root.title("Enviar correo por Gmail")

Label(root, text="Correo remitente:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
sender_entry = Entry(root, width=50)
sender_entry.grid(row=0, column=1, padx=10, pady=5)

Label(root, text="Contraseña remitente:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
password_entry = Entry(root, width=50, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

Label(root, text="Correo destinatario:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
recipient_entry = Entry(root, width=50)
recipient_entry.grid(row=2, column=1, padx=10, pady=5)

Label(root, text="Asunto:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
subject_entry = Entry(root, width=50)
subject_entry.grid(row=3, column=1, padx=10, pady=5)

Label(root, text="Mensaje:").grid(row=4, column=0, padx=10, pady=5, sticky="ne")
message_text = Text(root, width=50, height=10)
message_text.grid(row=4, column=1, padx=10, pady=5)

Button(root, text="Enviar correo", command=send_email).grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
