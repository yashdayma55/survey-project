from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Survey
from datetime import datetime

def survey_form(request):
    if request.method == 'POST':
        # Extract form data
        form_data = {
            'first_name': request.POST.get('first-name'),
            'last_name': request.POST.get('last-name'),
            'address': request.POST.get('address'),
            'city': request.POST.get('city'),
            'state': request.POST.get('state'),
            'zipcode': request.POST.get('zip'),
            'phone': request.POST.get('phone'),
            'raffle': request.POST.get('raffle', ''),
            'email': request.POST.get('email'),
            'url': request.POST.get('url', ''),
            'survey_date': request.POST.get('survey-date'),
            'likes': request.POST.get('likes', ''),
            'interest': request.POST.get('interest', ''),
            'other_text': request.POST.get('other-text', ''),
            'comments': request.POST.get('comments', ''),
            'recommendation': request.POST.get('recommendation'),
        }

        # Server-side validation (in case JavaScript is disabled)
        errors = []
        if not form_data['first_name'].isalpha():
            errors.append("First Name should contain only alphabets.")
        if not form_data['last_name'].isalpha():
            errors.append("Last Name should contain only alphabets.")
        if not all(c.isalnum() or c in " ,' -" for c in form_data['address']):
            errors.append("Address should contain only alphanumeric characters, spaces, commas, or hyphens.")
        if not form_data['email'].count('@') == 1 or not '.' in form_data['email'].split('@')[-1]:
            errors.append("Please enter a valid email address.")
        if not form_data['likes']:
            errors.append('Please select at least one option for "What did you like most about the campus?"')
        if not form_data['interest']:
            errors.append('Please select an option for "How did you become interested in the university?"')

        if form_data['raffle']:
            numbers = form_data['raffle'].split(',')
            if len(numbers) < 10:
                errors.append("Raffle must contain at least 10 numbers separated by commas.")
            else:
                valid_numbers = [num for num in map(lambda x: int(x.strip()) if x.strip().isdigit() else None, numbers) if num and 1 <= num <= 100]
                if len(valid_numbers) < 10:
                    errors.append("Raffle must contain at least 10 numbers between 1 and 100.")

        if errors:
            return render(request, 'survey_form.html', {
                'errors': errors,
                'form_data': form_data,
                'likes': form_data['likes'].split(',') if form_data['likes'] else [],
            })

        # Save to database
        survey = Survey(
            first_name=form_data['first_name'],
            last_name=form_data['last_name'],
            address=form_data['address'],
            city=form_data['city'],
            state=form_data['state'],
            zipcode=form_data['zipcode'],
            phone=form_data['phone'],
            raffle=form_data['raffle'],
            email=form_data['email'],
            url=form_data['url'],
            survey_date=datetime.strptime(form_data['survey_date'], '%Y-%m-%d').date(),
            likes=form_data['likes'],
            interest=form_data['interest'],
            other_text=form_data['other_text'],
            comments=form_data['comments'],
            recommendation=form_data['recommendation'],
        )
        survey.save()

        messages.success(request, "Survey submitted successfully!")
        return redirect('survey_list')

    # For GET requests, render the form
    return render(request, 'survey_form.html', {'form_data': {}})

def survey_list(request):
    surveys = Survey.objects.all().order_by('-created_at')
    return render(request, 'survey_list.html', {'surveys': surveys})