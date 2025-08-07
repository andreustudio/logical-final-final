from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.

def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']

            # Configuración del email
            email_message = EmailMessage(
                subject=f"Logical arguments: Nuevo mensaje de {nombre}",
                body=f"De: {nombre} <{email}>\n\n"
                     f"Del formulario contacto Logical Arguments\n\n"
                     f"Escribió:\n\n"
                     f"Nombre: {nombre}\n"
                     f"Asunto: {asunto}\n"
                     f"Teléfono: {telefono}\n"
                     f"Mensaje:\n{mensaje}",
                from_email=email,
                to=["logicalargumentsdev@gmail.com"],
                reply_to=[email],
            )

            try:
                email_message.send()
                messages.success(request, '¡Mensaje enviado con éxito. En breve nos pondremos en contacto contigo!')
            except Exception as e:
                messages.error(request, f"Error al enviar el mensaje: {str(e)}")

            return redirect('contacto:contacto')
        else:
            # Si el formulario no es válido, renderiza con los errores
            return render(request, 'contacto/contacto.html', {'form': form})
    else:
        # Si es GET, muestra el formulario vacío
        form = ContactForm()
    return render(request, 'contacto/contacto.html', {'form': form})