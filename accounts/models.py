from django.db import models

# Create your models here.
class Classroom(models.Model):
    name=models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.name
    
GENDER_CHOICES=  (
    ("M","MALE"),
    ("F","FEMALE")
)
STATUS_CHOICES=(
    ("Active","Active"),
    ("InActive","InActive")
)

class Student(models.Model):
    current_class=models.ForeignKey(Classroom,on_delete=models.CASCADE,related_name='students')
    registration_number=models.CharField(max_length=50,unique=True)
    name=models.CharField(max_length=100)
    roll_no=models.IntegerField(unique=True)
    email=models.EmailField(max_length=50,unique=True)
    password=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES)
    dob=models.DateField()
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pin_code=models.CharField(max_length=30)
    admission_date=models.DateField()
    parent_mobile_number=models.CharField(max_length=20)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES)

    def __str__(self):
        return self.current_class.name

class Subject(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    subjects=models.ManyToManyField(Subject,related_name='teachers')
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    qualification=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    address=models.TextField()
    joining_date=models.DateField()
    aadhar_number=models.CharField(max_length=100)
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES)
    image=models.ImageField(upload_to='images',blank=True,null=True)

    def __str__(self):
        return self.name

class Leave(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='leaves')
    email=models.EmailField(max_length=50)
    available_leave_days=models.IntegerField()
    leave_type=models.CharField(max_length=100)
    reason_for_leave=models.TextField()
    start_date=models.DateField()
    end_date=models.DateField()
    def __str__(self):
        return self.email
    

class Attendance(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    date=models.DateField()
    is_present=models.BooleanField()
    is_absent=models.BooleanField()

    


    
    
