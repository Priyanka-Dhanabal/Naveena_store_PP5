from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage
from .forms import ContactForm
import os


def contact_view(request):
    """
    Handles creation of contact submissions.
    Saves the submission to the database and sends an email to the admin.
    """
    # Retrieve admin email from environment variables
    admin_email = os.environ.get("EMAIL_ADMIN_ADDRESS")

    if not admin_email:
        messages.error(request, "Admin email is not configured. Please try again later.")
        return redirect(reverse("home"))

    # Meta description for the contact page
    meta_description = (
        "Get in touch with Naveena's Store. Reach out for inquiries, support, "
        "or feedback. We aim to respond within two working days."
    )

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            # Save the form instance and retrieve cleaned data
            try:
                contact_message = form.save(commit=False)
                contact_message.save()
            except Exception as e:
                print(f"Form errors: {form.errors}")
                print(f"Error saving message: {e}")
                messages.error(request, "There was an issue saving your message. Please try again later.")
                return redirect(reverse("home"))

            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            # Send an email notification to the admin
            try:
                send_mail(
                    "New Contact Form Submission",
                    f"You have received a new message from {name} ({email}):\n\n"
                    f"Subject: {subject}\n\n{message}",
                    settings.DEFAULT_FROM_EMAIL,
                    [admin_email],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Error sending email: {e}")
                messages.error(request, "There was an issue sending the notification email. Please try again later.")
                return redirect(reverse("home"))

            # Send confirmation email to user (optional)
            try:
                send_mail(
                    "Thank you for contacting us",
                    "Thank you for reaching out to us. We have received your message and will get back to you shortly.",
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Error sending confirmation email: {e}")
                # Continue processing even if this fails, but you can add feedback if needed.

            # Provide user feedback and redirect
            messages.success(
                request,
                "Your message has been sent successfully. We will contact you "
                "within 2 working days.",
            )
            return redirect(reverse("home"))
        else:
            # Handle form errors
            print(form.errors)  # For debugging purposes
            messages.error(request, "There were errors in your form submission. Please correct them and try again.")
            return render(request, "contact/contact.html", {"form": form, "meta_description": meta_description})

    else:
        # Pre-fill the form for authenticated users
        if request.user.is_authenticated:
            initial_data = {
                "name": f"{request.user.first_name} {request.user.last_name}",
                "email": request.user.email,
            }
            form = ContactForm(initial=initial_data)
        else:
            form = ContactForm()

    # Render the contact page
    template = "contact/contact.html"
    context = {
        "form": form,
        "meta_description": meta_description,  # Pass meta description
    }
    return render(request, template, context)
