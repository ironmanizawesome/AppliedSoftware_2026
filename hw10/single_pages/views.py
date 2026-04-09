from django.shortcuts import render
import os
import pandas as pd

def landing(request):
    return render(
        request,
          'single_pages/landing.html')


def about_me(request):
    csv_path = os.path.join(os.path.dirname(__file__), 'profile.csv')
    df = pd.read_csv(csv_path)
    profile_data = {}
    for _, row in df.iterrows():
        category = row['category']
        if category not in profile_data:
            profile_data[category] = []
        profile_data[category].append({'label': row['label'], 'value': row['value']})
    return render(request, 'single_pages/about_me.html', {'profile_data': profile_data})

def gallery(request):
    return render(request, 'single_pages/gallery.html')