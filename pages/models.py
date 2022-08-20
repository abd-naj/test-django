from django.db import models

# Create your models here.
class Login(models.Model):
    email = models.CharField(max_length=50 ,null=False ,verbose_name='البريد الإلكتروني')
    password = models.CharField(max_length=50 ,null=False ,verbose_name='كلمة السر')
    def __str__(self):
        return self.email
    class Meta:
        verbose_name='login'

class Personal(models.Model):
    status = [
        ('single','single'),
        ('married','married'),
    ]
    gender = [
        ('male','male'),
        ('female','female'),
    ]
    name = models.CharField(max_length=50, null=True ,verbose_name='اسم الطالب')
    ratio = models.CharField(max_length=50 ,verbose_name='النسبة')
    placeofpirth = models.CharField(max_length=50, null=True ,verbose_name='مكان الولادة')
    dataofbirth = models.DateField(null=True ,verbose_name='تاريخ الولادة ')
    namefather = models.CharField(max_length=50, null=True ,verbose_name='اسم الأب')
    mothername = models.CharField(max_length=50, null=True ,verbose_name='اسم الأم')
    gender = models.CharField(max_length=50, null=True , choices=gender ,verbose_name='الجنس')
    status = models.CharField(max_length=50, null=True , choices=status ,verbose_name='الحالة الإجتماعية')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='personal information'
        ordering =['name']
class Contact(models.Model):
    phone = models.CharField(max_length=50, null=True ,verbose_name='رقم الهاتف') 
    email = models.CharField(max_length=50, null=True ,verbose_name='البريد الإلكتروني')
    name = models.CharField(max_length=50, null=True ,verbose_name='اسم الدولة') 
    website = models.CharField(max_length=50, null=True ,verbose_name='اسم المدينة')
    message = models.TextField(null=True ,blank=True ,verbose_name='العنوان')
    def __str__(self):
        return self.email
    class Meta:
        verbose_name='contact information'
 
class Academy(models.Model):

    elementaryschool = models.CharField(max_length=50, null=True,verbose_name='اسم المدرسة الإبتدائية')
    preparatoryschool = models.CharField(max_length=50, null=True ,verbose_name='اسم المدرسة الإعدادية')
    highschool = models.CharField(max_length=50, null=True ,verbose_name='اسم المدرسة الثانوية')
    certificatedate = models.CharField(max_length=50 , null=True ,verbose_name='تاريخ الشهادة')
    modified = models.DecimalField(max_digits=5,decimal_places=2, null=True ,verbose_name='المعدل')
    certificatesource = models.CharField(max_length=50, null=False ,verbose_name='مصدر الشهادة') 
    def __str__(self):
        return str(self.modified)
    class Meta:
        verbose_name='academic information'

class Wishlist(models.Model):
    wishs = [
        ('medicine','medicine'),
        ('dentistry','dentistry'),
        ('pharmacy','pharmacy'),
        ('informatics engineering','informatics engineering'),
        ('architecture','architecture'),
        ('mechetronics engineering','mechetronics engineering'),
        ('trade and economy','trade and economy')
    ]
    gender = [
        ('male','male'),
        ('female','female'),
    ]

    name = models.CharField(max_length=50, null=True ,verbose_name='اسم الطالب')
    ratio = models.CharField(max_length=50, null=True ,verbose_name='النسبة')
    placeofbirth = models.CharField(max_length=50, null=True ,verbose_name='مكان الولادة')
    dateofbirth = models.DateField(null=True ,verbose_name='تاريخ الولادة')
    gender = models.CharField(max_length=50, null=True ,choices=gender ,verbose_name='الجنس')
    fathersnameandlineage = models.CharField(max_length=50, null=True ,verbose_name='اسم الأب و نسبته')
    mothersnameandlineage = models.CharField(max_length=50, null=True ,verbose_name='اسم الأم و نسبتها')
    status = models.CharField(max_length=50, null=True ,verbose_name='الحالة الإجتماعية')
    firstwish = models.CharField(max_length=50, null=True ,choices=wishs ,verbose_name='الرغبة الأولى')
    secondwish = models.CharField(max_length=50, null=True ,choices=wishs ,verbose_name='الرغبة الثانية')
    thirdwish = models.CharField(max_length=50, null=True ,choices=wishs ,verbose_name='الرغبة الثالثة')
    fourthwish = models.CharField(max_length=50, null=True ,choices=wishs ,verbose_name='الرغبة الرابعة') 
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='determine desire'
    
class Document(models.Model):
    imgper = models.ImageField(upload_to='personalPhoto/%y/%m/%d' ,verbose_name='صورة شخصية' ,null=False)
    imgid = models.ImageField(upload_to='idPhotos/%y/%m/%d' ,verbose_name='صورة الهوية' ,null=False)
    imgcer = models.ImageField(upload_to='certificatePhotos/%y/%m/%d' ,verbose_name='صورة الشهادة' ,null=False)
    
    class Meta:
        verbose_name='select document'


class UploadImage(models.Model):
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.caption