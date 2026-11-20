from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm
from .models import Contact


def contact_list(request):
    query = request.GET.get("q", "").strip()
    contacts = Contact.objects.all()

    if query:
        contacts = contacts.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )

    return render(
        request,
        "main/contact_list.html",
        {
            "contacts": contacts,
            "query": query,
        },
    )


def contact_add(request):
    form = ContactForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("contact_list")

    return render(request, "main/contact_form.html", {"form": form})


def contact_edit(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    form = ContactForm(request.POST or None, instance=contact)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("contact_list")

    return render(
        request,
        "main/contact_form.html",
        {
            "form": form,
            "contact": contact,
        },
    )


def contact_delete(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)

    if request.method == "POST":
        contact.delete()
        return redirect("contact_list")

    return render(
        request,
        "main/contact_confirm_delete.html",
        {"contact": contact},
    )
