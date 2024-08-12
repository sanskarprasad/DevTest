import pandas as pd
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import UploadFileForm

from django.shortcuts import render



def home_view(request):
    return render(request, 'fileupload/home.html')

def handle_uploaded_file(f):
    # Save the uploaded file to the media directory
    file_path = f'media/{f.name}'
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path

def generate_summary(file_path):
    # Load the Excel file into a DataFrame
    df = pd.read_excel(file_path)
    
    # Group by 'Cust State' and sum the 'DPD' column
    summary_df = df.groupby('Cust State')['DPD'].sum().reset_index()
    
    # Convert the DataFrame to a string for the email body
    summary = summary_df.to_string(index=False)
    return summary

def file_upload_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_path = handle_uploaded_file(request.FILES['file'])
            summary = generate_summary(file_path)
            
            # Send the email with the summary
            send_mail(
                'Python Assignment - Sanskarkumar Prasad',
                summary,
                'sampraa7@gmail.com',
                ['tech@themedius.ai','yash@themedius.ai'],
                fail_silently=False,
            )
            
            # Render the success page with the summary
            return render(request, 'fileupload/success.html', {'summary': summary})
    else:
        form = UploadFileForm()
    return render(request, 'fileupload/upload.html', {'form': form})
