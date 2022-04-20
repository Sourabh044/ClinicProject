from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Appointment, Patient
from .forms import PatientForm , AppointmentForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
# def HomePage(request):
    # return HttpResponse('this is homepage.')

def HomePage(request):
        # form = AppointmentForm()
        # context = {'form': form }
        return render(request, 'Main.html')
        

def Dashboard(request):
        return render(request, 'UI.html')



# Reading a particular Appointment
def appointment(request, pk):
    Appointmentsobj = Appointment.objects.get(id_number=pk)
    prescription = Appointmentsobj.prescription_set.all()
    # We can also access prescription in the template directly just by adding {% for i in Appointment.prescription_set.all %}
    context = {'Appointment': Appointmentsobj, 'prescription' : prescription}
    # return HttpResponse('project page: ' + str(pk))
    return render (request, 'SingleAppointment.html', context)

# Reading appointments and rendering in the templates
def appointments(request):
    Appointments = Appointment.objects.all()
    context = {'Appointments' : Appointments}
    return render (request, 'Appointments.html', context)
    # return HttpResponse('This is projects page.')

def addappointment(request):
    form = AppointmentForm() #passed the appointment Form.
    # patients =  Patient.objects.filter(user=request.user)
    # print(patients)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        userobj = request.user
        patients =  Patient.objects.get(user=request.user)
        print(patients)
        if form.is_valid():
            obj = form.save(commit=False) # Return an object without saving to the DB
            obj.name = str(obj.patient) 
            obj.save() 
            form.save()
            return redirect('/Appointments/')
        else:
            form = AppointmentForm()
            # patients =  Patient.objects.filter(user=request.user)
            # print(patients)
    context = {'form': form ,}
    return render(request, 'Add-Appointment.html', context)



# CRUD EXAMPLE HERE
# Creating the Patient
def addpatient(request):
    form = PatientForm() #Here we passed the PatientForm so that it ony show the main

    if request.method == 'POST':
        form = PatientForm(request.POST)
        # current_user = request.user
        # form.fields['user'] = current_user.id
        if form.is_valid():
            obj = form.save(commit=False) # Return an object without saving to the DB
            obj.user = User.objects.get(pk=request.user.id) # Add an author field which will contain current user's id
            obj.save() # Save the final "real form" to the DB
            form.save()
            return redirect('Patients')

    context = {'form': form }
    return render(request, 'Add-Patient.html', context)

# Reading the Patients on the template
def patients(request):
    Patients = Patient.objects.all()
    context = {'Patients' : Patients}
    return render (request, 'Patients.html', context)

# Updating the Patient Details
def updatepatient(request, pk):
    patient = Patient.objects.get(id=pk) #That id into field is bcos i was calling it id, but real name of
    # the PK was id_number
    form = PatientForm(instance=patient) #Here we passed the instance=patient so that it show the Pre-filled data
    
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('Patients')

    context = {'form': form }
    return render(request, 'Update-Patient.html', context)


# Deleting the Patient
def DeleteAppointment(request, pk):
    appointment = Appointment.objects.get(id_number=pk)

    if request.method == 'POST':
        appointment.delete()
        return redirect("Appointments")
    return render(request, 'Delete-Appointment.html', {'Appointment': appointment})



    # Reading Patients of a single user
def viewpatients(request):
    userobj = request.user #making the instance of the current user
    Patients = userobj.patient_set.all()  #then accessing all the patients created by the user
    context = {'Patients' : Patients}
    return render (request, 'Patients.html', context)

    #Signup a user 
def signup(request):
    # new_user = User.

    if request.method == 'POST':

        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        # password = request.POST['phone']
        password = request.POST['password']
        newuser = User.objects.create_user(username = username , password = password, email=email,first_name= first_name, last_name= last_name) # 
        newuser.save()
        messages.success(request, 'Profile Created. Login Please.')

        return redirect('/')
    else:
        # return HttpResponse('Error')
        return render(request, 'SignUp.html')

# Creating a new view for the Login
def Login(request):
    if 'Login' in request.POST:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['psw']
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request,'username or password not correct. Please login Again')
                return render(request, 'Main.html')
                # return HttpResponse("Invalid Username or password")
    
    # if 'Appointment' in request.POST:
    #     form = AppointmentForm() #passed the appointment Form.
    # # So now to fix the name issue we will use the trick from the Patient
      
    #     if request.method == 'POST':
    #         form = AppointmentForm(request.POST)
    #         if form.is_valid():
    #             obj = form.save(commit=False) # Return an object without saving to the DB
    #             obj.name = str(obj.patient) 
    #             obj.save()
    #             form.save()
    #             return redirect('Appointments')
    #         else:
    #             return HttpResponse('Not added')
    #     context = {'form': form }
    #     return render(request, 'Appointments.html', context)