from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.ensemble import RandomForestClassifier
import joblib
# Create your models here.
Gender=(
    (1,'Female'),
    (0,'Male')
)
addrs=(
    (1,'Urban'),
    (0,'Rural')
)
fmsz=(
     (1,'less than 3'),
    (0,'Greater than 3')
)
psts=(
    (1,'Together'),
    (0,'Apart')
)
pedu=(
     (0,'None'),
     (1,'Primary(4th grade)'),
     (2,'5th to 9th Grade'),
     (3,'Secondary'),
     (4,'Higher')
)
pjob=(
     (0,'teacher'),
     (1,'health'),
     (2,'services'),
     (3,'at_home'),
     (4,'other')
)
t_time=(
    (1, 'less than 15 min'),
    (2, '15 to 30 min'),
    (3, '30 min to 1 hour'),
    (4, 'more than 1 hour'),
)
st_time=(
    (1, 'less than 2 hours'),
    (2, '2 to 5 hours'),
    (3, '5 to 10 hours'),
    (4, 'more than 10 hours'),
)
quality=(
    (1,'very bad'),
    (2,'bad'),
    (3,'better'),
    (4,'good'),
    (5,'excellent')
)
addict1=(
(1,'never'),
(2,'sometimes'),
(3,'ocassionaly'),
(4,'weekly'),
(5,'Daily'),
)
addict2=(
(1,'never'),
(2,'ocassional'),
(3,'sometimes'),
(4,'often'),
(5,'Always'),
)
#resn=(
#     (0,'home'),
#     (1,'reputation'),
#     (2,'course'),
#     (3,'other')
#)
guard=(
    (0,'mother'),
     (1,'father'),
     (2,'other'),
)
chose=(
    (1,'Yes'),
    (0,'No')
)
class Data(models.Model):
    name=models.CharField(max_length=100,null=True)
    sex=models.PositiveIntegerField(choices=Gender,null=True)
    address=models.PositiveIntegerField(choices=addrs,null=True)
    famsize=models.PositiveIntegerField(choices=fmsz,null=True)
    Pstatus=models.PositiveIntegerField(choices=psts,null=True)
    Medu=models.PositiveIntegerField(choices=pedu,null=True)
    Fedu=models.PositiveIntegerField(choices=pedu,null=True)
    Mjob=models.PositiveIntegerField(choices=pjob,null=True)
    Fjob=models.PositiveIntegerField(choices=pjob,null=True)
 #   reason=models.PositiveIntegerField(choices=resn,null=True)
    guardian=models.PositiveIntegerField(choices=guard,null=True)
    traveltime=models.PositiveIntegerField(
        #   validators=[MinValueValidator(1), MaxValueValidator(4)],
        choices=t_time,
        null=True)
    studytime=models.PositiveIntegerField(
        #   validators=[MinValueValidator(1), MaxValueValidator(4)],
        choices=st_time,
        null=True)
    failures=models.PositiveIntegerField(
          validators=[MinValueValidator(0), MaxValueValidator(3)],
        null=True)
    schoolsup=models.PositiveIntegerField(choices=chose,null=True)
    famsup=models.PositiveIntegerField(choices=chose,null=True)
    paid=models.PositiveIntegerField(choices=chose,null=True)
    activities=models.PositiveIntegerField(choices=chose,null=True)
    nursery=models.PositiveIntegerField(choices=chose,null=True)
    higher=models.PositiveIntegerField(choices=chose,null=True)
    internet=models.PositiveIntegerField(choices=chose,null=True)
    romantic=models.PositiveIntegerField(choices=chose,null=True)
    famrel=models.PositiveIntegerField(
        #   validators=[MinValueValidator(1), MaxValueValidator(5)],
        choices=quality,
        null=True)
    freetime=models.PositiveIntegerField(
        #  validators=[MinValueValidator(1), MaxValueValidator(5)],
        choices=quality,
        null=True)
    goout=models.PositiveIntegerField(
        #  validators=[MinValueValidator(1), MaxValueValidator(5)],
          choices=quality,
        null=True)
    Dalc=models.PositiveIntegerField(
        #  validators=[MinValueValidator(1), MaxValueValidator(5)],
        choices=addict1,
        null=True)
    Walc=models.PositiveIntegerField(
        #  validators=[MinValueValidator(1), MaxValueValidator(5)],
        choices=addict2,
        null=True)
    health=models.PositiveIntegerField(
        #  validators=[MinValueValidator(1), MaxValueValidator(5)],
          choices=quality,
        null=True)
    absences=models.PositiveIntegerField(
         validators=[MinValueValidator(0), MaxValueValidator(75)],
        null=True)
    # G1=models.PositiveIntegerField(
    #       validators=[MinValueValidator(0), MaxValueValidator(20)],
    #     null=True)
    # G2=models.PositiveIntegerField(
    #       validators=[MinValueValidator(0), MaxValueValidator(20)],
    #     null=True)
    G1 = models.PositiveIntegerField(choices=[(0, '0-25%'), (1, '25-50%'), (2, '50-75%'), (3, '75-90%'), (4, '90-100%')], null=True)
    G2 = models.PositiveIntegerField(choices=[(0, '0-25%'), (1, '25-50%'), (2, '50-75%'), (3, '75-90%'), (4, '90-100%')], null=True)
    Grades= models.CharField(max_length=100, blank=True)
    # date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/student_grade_model2.joblib')
        self.G1 = self.map_percentage_to_value(self.G1)
        self.G2 = self.map_percentage_to_value(self.G2)
        self.Grades = ml_model.predict(
            [[self.sex,self.address,self.famsize,self.Pstatus,self.Medu,self.Fedu,self.Mjob,self.Fjob,
            #self.reason,
            self.guardian,
            self.traveltime,self.studytime,self.failures,self.schoolsup,self.famsup,self.paid,self.activities,self.nursery,self.higher,self.internet,
            self.romantic,self.famrel,self.freetime,self.goout,self.Dalc,self.Walc,self.health,self.absences,self.G1,self.G2]])
        return super().save(*args, *kwargs)
    def map_percentage_to_value(self, percentage):
        percentage_mapping = {
            0: 0,
            1: 5,
            2: 10,
            3: 15,
            4: 20,
        }
        return percentage_mapping.get(percentage, 0)
    # class Meta:
        # ordering = ['-date']

    def __str__(self):
        return self.name   
