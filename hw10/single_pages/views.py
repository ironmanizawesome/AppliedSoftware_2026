import csv
import os

from django.shortcuts import render

def landing(request):
    return render(
        request,
          'single_pages/landing.html')


def about_me(request):
    csv_path = os.path.join(os.path.dirname(__file__), 'profile.csv')
    profile_data = {}

    with open(csv_path, newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            category = row['category']
            if category not in profile_data:
                profile_data[category] = []
            profile_data[category].append(
                {'label': row['label'], 'value': row['value']}
            )

    return render(request, 'single_pages/about_me.html', {'profile_data': profile_data})

def gallery(request):
    return render(request, 'single_pages/gallery.html')
