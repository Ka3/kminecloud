from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#import audit
from reversion import revisions as reversion


# Create your models here.


ContactType_Choices = (
    ('Advisor', 'Advisor'),
    ('Member', 'Member'),
)

Contact_Role = (
    ('Admin Contact', 'Admin Contact'),
    ('Decision Maker' , 'Decision Maker'),
)

Status_Choices = (
                  ('Active','Active'),
                  ('Inactive','Inactive')        
                  )

Gender_Choices = (
                  ('Male','Male'),
                  ('Female','Female'),
                  )

Yes_No_Choices = (
                  ('Yes','Yes'),
                  ('No','No')
                  )

class IRM_Ethinicity(models.Model):
    types = models.CharField(max_length=100, help_text='Ethnicity', verbose_name="Ethnicity")
    def __str__(self):
        return self.types
    
class IRM_Location(models.Model):
    types = models.CharField(max_length=100, help_text='Location', verbose_name="IRM Office Location" )
    def __str__(self):
        return self.types
    
class Marital_Status(models.Model):
    types = models.CharField(max_length=20,verbose_name='Marital Status' )
    def __str__(self):
        return self.types

class Report_Status(models.Model):
    types = models.CharField(max_length=20,verbose_name='Report Status')
    def __str__(self):
        return self.types
    
class Case_Type(models.Model):
    types = models.CharField(max_length=20,verbose_name='Case Type')
    def __str__(self):
        return self.types

class Panel_Role(models.Model):
    types = models.CharField(max_length=50,verbose_name='Panel Role')
    def __str__(self):
        return self.types

class Panel_Recommendations(models.Model):
    types = models.CharField(max_length=200, help_text='Placeholder',verbose_name='Panel Recommendations')
    def __str__(self):
        return self.types

class IRM_Title(models.Model):
    types = models.CharField(max_length=100, help_text='Title',verbose_name='Title')
    def __str__(self):
        return self.types
    
class Agency_Type(models.Model):
    types = models.CharField(max_length=100, help_text='Type of Agency',verbose_name='Agency Type')
    def __str__(self):
        return self.types
    
class Test_Person(models.Model):
    def __str__(self):
        return self.First_Name + ' '  + self.Last_Name
    Title = models.ForeignKey(IRM_Title, help_text='Title', verbose_name='Title' )
    First_Name = models.CharField(max_length=100, help_text='F Name', verbose_name='Sample person first name')
    Last_Name = models.CharField(max_length=100, help_text='L Name')
    Ethnicity = models.ForeignKey(IRM_Ethinicity)
    Location = models.ForeignKey(IRM_Location)
    
@reversion.register()
class IRM_Agency(models.Model):
    def __str__(self):
        return self.Agency_Name
    #AgencyID = models.IntegerField(auto_increment=True) 
    Location = models.ForeignKey(IRM_Location) 
    Agency_Type = models.ForeignKey(Agency_Type) 
    Agency_Name = models.CharField(max_length=100, help_text='Agency Name') 
    Agency_FullName = models.CharField(max_length=100,blank=True, null=True, help_text='Agency Full Name')
    Notes = models.TextField(max_length=2000,blank=True, null=True, help_text='Notes')
    To_Delete = models.BooleanField(default=False)
    Modified_by =  models.CharField(max_length=100,blank=True,null=True)
    Created_by = models.CharField(max_length=100,blank=True,null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    
    def save(self, *args, **kwargs):
            if not self.id:
                self.created = timezone.now()
                self.Created_by = self.Modified_by
            self.modified = timezone.now()
            return super(IRM_Agency, self).save(*args, **kwargs)


class IRM_Agency_Admin_Contact(models.Model):
    def __str__(self):
        return self.Firstname + ' ' + self.Surname 
    AgencyID_FK = models.ForeignKey(IRM_Agency,verbose_name='Agency')  #
    Title = models.ForeignKey(IRM_Title) #
    Firstname =  models.CharField(max_length=100, help_text='First name of Agency Admin') 
    Surname = models.CharField(max_length=100, help_text='Surname of Agency Admin')
    Position = models.CharField(max_length=100, help_text='Position(Designation) in the Agency')
    Address_Line_1 = models.CharField(max_length=200, help_text='Placeholder')
    Address_Line_2 = models.CharField(max_length=200, blank=True, null=True,  help_text='Placeholder')
    Address_Line_3 = models.CharField(max_length=200, blank=True, null=True,  help_text='Placeholder')
    Address_Line_4 = models.CharField(max_length=200, blank=True, null=True,  help_text='Placeholder')
    Town = models.CharField(max_length=200, blank=True, null=True,  help_text='Town')
    County = models.CharField(max_length=200, blank=True, null=True,  help_text='County')
    Postcode = models.CharField(max_length=200,  help_text='UK Postcode')
    Phone = models.CharField(max_length=200, blank=True, null=True,  help_text='Phone Number')
    Mobile = models.CharField(max_length=200, blank=True, null=True, help_text='Mobile Number')
    Email = models.EmailField(blank=True, null=True)
    Fax = models.IntegerField(blank=True, null=True, help_text='Fax Number')
    Role = models.CharField(max_length=50, choices=Contact_Role,help_text='Role Type')
    Notes = models.TextField(max_length=1000, blank=True, null=True,help_text='Short Notes about Agency')
    Modified_by =  models.CharField(max_length=100,blank=True,null=True)
    Created_by = models.CharField(max_length=100,blank=True,null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    
    def save(self, *args, **kwargs):
            if not self.id:
                self.created = timezone.now()
                self.Created_by = self.Modified_by
            self.modified = timezone.now()
            return super(IRM_Agency_Admin_Contact, self).save(*args, **kwargs)


class IRM_PanelContactRole(models.Model):
    def __str__(self):
        return self.Role
    Role = models.CharField(max_length=100, help_text='Role')
    ContactType = models.CharField(max_length=20, choices=ContactType_Choices  ,help_text='Contact Type')


class IRM_PanelContact(models.Model):   
    
 

    Principal_IRMLocationID_FK = models.ForeignKey(IRM_Location,related_name='%(class)s_Principal_Location',verbose_name='Principal IRM Location')
    Two_IRMLocationID_FK =  models.ForeignKey(IRM_Location,related_name='%(class)s_Secondary_Location', verbose_name='Secondary IRM Location' )
    Three_IRMLocationID_FK =  models.ForeignKey(IRM_Location,blank=True, null=True, related_name='%(class)s_Third_Location', verbose_name='IRM Location 3(optional)' )
    Four_IRMLocationID_FK =  models.ForeignKey(IRM_Location,blank=True, null=True ,related_name='%(class)s_Fourth_Location', verbose_name='IRM Location 4(optional)')
    Title = models.ForeignKey(IRM_Title)
    Firstname = models.CharField(max_length=100)
    Surname = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100,choices=Gender_Choices)
    Ethnicity = models.ForeignKey(IRM_Ethinicity)
    Participant_Type = models.CharField(max_length=100,blank=True,null=True)
    Panel_Role = models.ForeignKey(IRM_PanelContactRole)
    Position = models.CharField(max_length=50,blank=True,null=True)
    
    
    Home_Address_Line_1 = models.CharField(max_length=100)
    Home_Address_Line_2 = models.CharField(max_length=100,blank=True,null=True)
    Home_Address_Line_3 = models.CharField(max_length=100,blank=True,null=True)
    Home_Address_Line_4 = models.CharField(max_length=100,blank=True,null=True)
    Home_Town = models.CharField(max_length=100)
    Home_County = models.CharField(max_length=100,blank=True,null=True)
    Home_Postcode = models.CharField(max_length=100,blank=True,null=True)  
    Home_Phone = models.CharField(max_length=40,blank=True,null=True)
    ##
    Work_Address_Line_1 = models.CharField(max_length=100)
    Work_Address_Line_2 = models.CharField(max_length=100,blank=True,null=True)
    Work_Address_Line_3 = models.CharField(max_length=100,blank=True,null=True)
    Work_Address_Line_4 = models.CharField(max_length=100,blank=True,null=True)
    Work_Town = models.CharField(max_length=100)
    Work_County = models.CharField(max_length=100,blank=True,null=True)
    Work_Postcode = models.CharField(max_length=100)
    Work_Phone = models.CharField(max_length=40,blank=True,null=True)
    
    Mobile = models.CharField(max_length=40,blank=True,null=True)
    Email = models.EmailField(max_length=40,blank=True,null=True)
    Fax = models.CharField(max_length=40,blank=True,null=True)
    Appointment_Date = models.DateField()
    ###  
    To_Delete = models.BooleanField(default=False)
    Availability = models.CharField(max_length=100,blank=True,null=True)
    Status = models.CharField(default='Active',max_length=50,choices=Status_Choices)
    Notes = models.TextField(max_length=200,blank=True,null=True)
    
    Modified_by =  models.CharField(max_length=100,blank=True,null=True)
    Created_by = models.CharField(max_length=100,blank=True,null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    
    #history = audit.AuditTrail()
    
    def __str__(self):
        return self.Firstname + ' ' + self.Surname
    
    def save(self, *args, **kwargs):
            if not self.id:
                self.created = timezone.now()
                self.Created_by = self.Modified_by
            self.modified = timezone.now()
            return super(IRM_PanelContact, self).save(*args, **kwargs)

    

    
class Case_Type(models.Model):
    types = models.CharField(max_length=100, help_text='Type of Case',verbose_name='Case_Type')
    def __str__(self):
        return self.types
        
class Report_Status(models.Model):
    types = models.CharField(max_length=100, help_text='Report Status',verbose_name='Report_Status')
    def __str__(self):
        return self.types

class Agency_Decision(models.Model):
    types = models.CharField(max_length=100, help_text='Agency Decision',verbose_name='Agency Decision')
    def __str__(self):
        return self.types

class Panel_Recommendations(models.Model):
    types = models.CharField(max_length=100, help_text='Panel Recommendations',verbose_name='Panel_Recommendations')
    def __str__(self):
        return self.types


class IRM_Case_dup(models.Model):
    abc = models.CharField(max_length=20,blank=True, null=True)
    lef = models.CharField(max_length=20,blank=True, null=True)
    sar = models.CharField(max_length=20,blank=True, null=True)
        
class IRM_Case(models.Model):
    #CaseID =  models.IntegerField(auto_increment=True,startswith=1000)
    Agency = models.ForeignKey(IRM_Agency) #
    Legal_Advisor = models.ForeignKey(IRM_PanelContact) #
    IRM_Reference = models.CharField(max_length=20,blank=True, null=True)
    IRM_Location = models.ForeignKey(IRM_Location)
    Type = models.ForeignKey(Case_Type) #
    Date_Appliction_Received = models.DateField()  #Created_Date
    Report_Status = models.ForeignKey(Report_Status,blank=True, null=True)
    Inter_Country = models.CharField(max_length=10,choices=Yes_No_Choices)
    Major_Recommendation = models.CharField(max_length=10,choices=Yes_No_Choices)
    Agency_Decision = models.ForeignKey(Agency_Decision, blank=True, null=True)
    Case_Notes = models.TextField(max_length=2000, blank=True, null=True)
    
    #########Applicatant Information#####################
    Salutation = models.CharField(max_length=100, blank=True, null=True)
    Person_1_Title = models.ForeignKey(IRM_Title, related_name='%(class)s_Person1_Title')
    Person_1_FirstName = models.CharField(max_length=100)
    Person_1_Surname = models.CharField(max_length=100)
    Person_1_Gender = models.CharField(max_length=20,choices=Gender_Choices)
    Person_1_DateOfBirth = models.DateField(blank=True, null=True)
    Person_1_Ethnicity = models.ForeignKey(IRM_Ethinicity,related_name='%(class)s_Person1_Ethnicity')
    Person_2_Title = models.ForeignKey(IRM_Title, related_name='%(class)s_Person2_Title')
    Person_2_FirstName = models.CharField(max_length=100, blank=True, null=True)
    Person_2_Surname =  models.CharField(max_length=100, blank=True, null=True)
    Person_2_Gender = models.CharField(max_length=20,choices=Gender_Choices)
    Person_2_DateOfBirth = models.DateField(blank=True, null=True)
    Person_2_Ethnicity = models.ForeignKey(IRM_Ethinicity, related_name='%(class)s_Person2_Ethnicity')
    Marital_Status = models.ForeignKey(Marital_Status)
    
    ##### Applicant Contact Information############
    Address_Line_1 =models.CharField(max_length=100)
    Address_Line_2 = models.CharField(max_length=100, blank=True, null=True)
    Address_Line_3 = models.CharField(max_length=100, blank=True, null=True)
    Address_Line_4 = models.CharField(max_length=100, blank=True, null=True)
    Town = models.CharField(max_length=100)
    County = models.CharField(max_length=100, blank=True, null=True)
    Postcode = models.CharField(max_length=20)
    Phone = models.CharField(max_length=50, blank=True, null=True)
    Mobile = models.CharField(max_length=50, blank=True, null=True)
    Email = models.EmailField(max_length=50, blank=True, null=True)
    Fax = models.CharField(max_length=50, blank=True, null=True)
    ContactNotes =  models.TextField(max_length=2000, blank=True, null=True)
    

""" 
class IRM_Case_TimeLine(models.Model):
    ########### Case Time Line ####################
    Case_ID = models.ForeignKey(IRM_Case)
    Date_Acknwldge_Applictn_To_Applicant = models.DateField(blank=True, null=True)
    Date_Notifictn_Of_Applictn_To_Agency = models.DateField(blank=True, null=True)
    Date_Receipt_Paperwk_From_Agency = models.DateField(blank=True, null=True)
    Date_Agency_Papers_Sent_To_Legal_Advisor = models.DateField(blank=True, null=True)
    Date_Applicant_Notified_Of_Hearing = models.DateField(blank=True, null=True)
    Date_Paperwk_Sent_To_Panel_Mems =  models.DateField(blank=True, null=True)
    Date_Papers_From_Hearing_Received_By_IRM = models.DateField(blank=True, null=True)
    Date_Agency_Papers_marked_Complete = models.DateField(blank=True, null=True)
    Panel_Recommendtn = models.Forignkey(Panel_Recommendations, blank=True, null=True)
    Date_Recommdtn_Plus_Mins_Signed_By_Chair = models.DateField(blank=True, null=True)
    Date_Applicant_Notifd_Of_Recommdtn = models.DateField(blank=True, null=True)
    Date_Agency_Notifd_Of_Recommdtn = models.DateField(blank=True, null=True)
    
    
    Date_Shredded = models.DateField(blank=True, null=True)
    Date_Received_Agency_Decision = models.DateField(blank=True, null=True)
    Date_Any_Follow_Up_To_Agency = models.DateField(blank=True, null=True)
         
    Date_Questionnaires_From_Panel =  models.DateField(blank=True, null=True)
    Date_Questionnaires_From_Applicants = models.DateField(blank=True, null=True)
    Date_Questionnaires_From_Agency = models.DateField(blank=True, null=True)
    Date_Agency_Papers_Sent_To_Medical_Advisor = models.DateField(blank=True, null=True)
    Date_Confirmation_PanelDate_to_PanelMembers = models.DateField(blank=True, null=True)
    Date_Agency_Notified_Of_Hearing = models.DateField(blank=True, null=True)
    Date_Paperwk_Sent_To_Applicant = models.DateField(blank=True, null=True)
    Date_Paperwk_Sent_To_Agency = models.DateField(blank=True, null=True)
    Date_Alert_Proposed_Hearing_To_Panel = models.DateField(blank=True, null=True)
    Date_Feedback_On_Mins_Received_From_Agency = models.DateField(blank=True, null=True)
    Date_Agency_Decision_Mins_And_Recs_Sent_To_Panel = models.DateField(blank=True, null=True)
    Date_Feedback_Received_From_Panel = models.DateField(blank=True, null=True)
    Date_Original_Papers_Returned_To_Agency  = models.DateField(blank=True, null=True)
    
    ReceivedPapersFromAgency  = models.ChoiceField(max_length=10,choices=Yes_No_Choices)
    IdentifiedPanelToHearReview = models.ChoiceField(max_length=10,choices=Yes_No_Choices)
    SentPanelLocationAndDatetoBothParties = models.ChoiceField(max_length=10,choices=Yes_No_Choices)
    SentPapersToApplicant = models.ChoiceField(max_length=10,choices=Yes_No_Choices)
    SentPapersToPanelMembersAndAgency = models.ChoiceField(max_length=10,choices=Yes_No_Choices)
    SelectedPanelAndAlerted = models.ChoiceField(max_length=10,choices=Yes_No_Choices)
    ConfirmedPanelDateToMems = models.ChoiceField(max_length=10,choices=Yes_No_Choices)
    ChasedUpDecisionWithAgency = models.ChoiceField(max_length=10,choices=Yes_No_Choices)
    
    
    Orig_Papers_Rtnd_To_Agency_Or_Shredded =  models.BooleanField()
    Who_Shredded_Orig_Papers = models.CharField(max_length=100, blank=True, null=True)
    QualifyingDetermination = models.DateField(blank=True, null=True)
    To_Delete = models.BooleanField(default=False)

    Panel_Cancelled = models.DateField(blank=True, null=True)
    Panel_Deferred_To = models.DateField(blank=True, null=True)

class IRM_PanelVenue(models.Model):
    PanelVenueID = models.IntegerField(auto_increment=True,startswith=1000)
    Address_Line_1 = models.CharField(max_length=100)
    Address_Line_2 = models.CharField(max_length=100,blank=True,null=True)
    Town = models.CharField(max_length=100)
    County = models.CharField(max_length=50,blank=True,null=True)
    Postcode = models.CharField(max_length=100)
    Phone = models.CharField(max_length=100)

class IRM_PanelDay(models.Model):
    PanelDayID = models.IntegerField(auto_increment=True,startswith=1000)
    PanelVenueID_FK = models.ForeignKey(IRM_PanelVenue)
    IRMLocationID_FK = models.ForeignKey(IRM_Location)
    Date = models.DateField()
    Notes = models.CharField(max_lenth=1000,blank=True,null=True)
    To_Delete = models.Choicefield(max_length=10,choices=Yes_No_Choices)
    
class IRM_PanelDayBooking(models.Model):
    PanelDayBookingID = models.IntegerField(auto_increment=True,startswith=1000)
    PanelDayID_Fk = models.ForeignKey(IRM_PanelDay)
    PanelContactID_FK = models.ForeignKey(IRM_PanelContact)
    Can_Attend = models.Choicefield(max_length=10,choices=Yes_No_Choices)
    Attended = models.Choicefield(max_length=10,choices=Yes_No_Choices)
    ReasonIfAbsent =  models.CharField(max_lenth=200,blank=True,null=True)
    Role_For_Day =  ''
    Notes =  models.CharField(max_lenth=1000,blank=True,null=True)


class IRM_PanelHearing(models.Model):
    pass
    PanelHearingID = models.IntegerField(auto_increment=True,startswith=1000)
    CaseID_FK = models.ForeignKey(IRM_Case)
    PanelDayID_FK = models.ForeignKey(IRM_PanelDay)
    Start_Time = models.TimeField()
    Applicant_Attended = models.Choicefield(max_length=10,choices=Yes_No_Choices)
    Notes = models.CharField(max_lenth=1000,blank=True,null=True)
    Agency_Attendee_Name =  models.CharField(max_lenth=200)
    Agency_Attendee_Position = models.CharField(max_lenth=200)
    FirstApplicantAttended = models.Choicefield(max_length=10,choices=Yes_No_Choices)
    SecondApplicantAttended = models.Choicefield(max_length=10,choices=Yes_No_Choices)
    SupporterAttended =  models.Choicefield(max_length=10,choices=Yes_No_Choices)
    InterpreterAttended = models.Choicefield(max_length=10,choices=Yes_No_Choices)

    
class IRM_Agency_Interest(models.Model):
    '''
    AgencyInterestID = models.IntegerField(auto_increment=True)
    AgencyID_FK = models.ForeignKey(IRM_Agency)
    PanelContactID_FK = models.ForeignKey(IRM_Agency_Admin_Contact)
    '''
    pass


"""
    

    
    

    
    
    
    
    
    