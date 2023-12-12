from django.shortcuts import render, redirect, HttpResponse
from .forms import CSVUploadForm
from .models import Employee
import csv


def handle_uploaded_csv(csv_file):
    decode_file = csv_file.read().decode('utf-8').splitlines()
    csv_reader = csv.reader(decode_file)
    headers = next(csv_reader)
    # print(headers)               # for print header
    for row in csv_reader:
            employee_data = dict(zip(headers, row))
            # print("employee_data:-", employee_data)             # print all the data in terminal
            Employee.objects.create(**employee_data)



def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_csv(request.FILES['csv_file'])
            return HttpResponse("file uploaded succesfully...!")
    else:
        form = CSVUploadForm()
    return render(request, 'upload_csv.html', {'form': form})
            

                        #OR#
# ---------------------------------------------------------------



# def handle_uploaded_csv(csv_file):
#     with csv_file.open() as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             Employee.objects.create(
#                 name=row['name'],
#                 email=row['email'],
#                 department=row['department'],
# )


# -----------------------------------------------------------------


def download_csv(request):
     # Query the Employee model to get all records
    employees = Employee.objects.all()

    # Create the HttpResponse object with CSV content
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employee_data.csv"'

    # Create the CSV writer and write the header
    csv_writer = csv.writer(response)
    csv_writer.writerow(['first_name', 'last_name', 'email'])  # CSV header

    # Write data rows
    for employee in employees:
        csv_writer.writerow([employee.first_name, employee.last_name, employee.email])

    return response 