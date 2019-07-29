from django.db import models

# Create your models here.
class Address(models.Model):
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    line1 = models.CharField(max_length=50)
    line2 = models.CharField(max_length=30)
    landmark = models.CharField(max_length=30)
    pincode = models.IntegerField()

    class Meta:
        db_table = "Address_Info"

#a1 = Address(city="Pune", state="MH", line1="karwe nagar", line2="canal road", landmark="kothrud", pincode=12345 )

class Company(models.Model):
    companyWebsite = models.CharField(max_length=50)
    companyEmail = models.CharField(max_length=50)
    landline = models.IntegerField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        db_table = "Company_Info"

#c1 = Company(companyWebsite="website", companyEmail="company@gmail.com", landline=249488, address="Pune")

class Employee(models.Model):
    employeeEmail = models.CharField(max_length=50)
    employeename = models.CharField(max_length=50)
    employeecontact = models.IntegerField()
    employeeage = models.IntegerField()
    empaddress = models.ManyToManyField(Address)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        db_table = "Employee_Info"

#e1 = Employee(employeeEmail = "emp1@gmail.com", employeename = "meee", employeecontact = 12345, employeeage = 23, empaddress = "Pusad")
print("good morning")
print('change')
print("change from orig")
print('new start')