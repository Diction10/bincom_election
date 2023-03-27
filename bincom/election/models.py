from django.db import models
from datetime import datetime

    

# table Agent Name
class AgentName(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    pollingunit_uniqueid = models.IntegerField()

    def __str__(self):
        return f'{self.first_name}'
    

# table Party Name
class PartyName(models.Model):
    party_id = models.CharField(max_length=50)
    party_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.party_name}'
    
    

# table Announced ward result
class WardResult(models.Model):
    ward_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_IPaddress = models.CharField(max_length=50)
    
    

    def __str__(self):
        return f'{self.party_abbreviation} --> {self.party_score}'
    

# table Announced LGA result
class LGAResult(models.Model):
    lga_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_IPaddress = models.CharField(max_length=50)
    

    def __str__(self):
        return f'{self.lga_name} -> {self.party_abbreviation} -> {self.party_score}'
    

# table Announced State result
class StateResult(models.Model):
    state_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_IPaddress = models.CharField(max_length=50)
    

    def __str__(self):
        return f'{self.party_abbreviation} --> {self.party_score}'
    

# table Polling Unit Name
class PollingUnitName(models.Model):
    polling_unit_id = models.IntegerField()
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    uique_ward_id = models.IntegerField()
    polling_unit_number = models.CharField(max_length=50)
    polling_unit_name = models.CharField(max_length=50)
    polling_unit_description = models.CharField(blank=True, null=True, max_length=500)
    latitude = models.CharField(max_length=255, null=True)
    longitude = models.CharField(max_length=255, null=True)
    entered_by_user = models.CharField(blank=True,null=True, max_length=50)
    date_entered = models.DateTimeField(blank=True,null=True)
    user_IPaddress = models.CharField(blank=True, null=True, max_length=50)

    def __str__(self):
        return f'{self.lga_id}->{self.polling_unit_id}->{self.polling_unit_name}'
    

# table Ward
class WardName(models.Model):
    ward_id = models.IntegerField()
    ward_name = models.CharField(max_length=50)
    lga_id = models.IntegerField()
    ward_description = models.CharField(blank=True, max_length=500)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_IPaddress = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.ward_name}'


    

LG_CHOICES = (
    ('default','Select LLocal Government'),
    (1, 'Aniocha North'),
    (2, 'Aniocha - South'),
    (5, 'Ethiope East'),
    (6, 'Ethiope West'),
    (7, 'Ika North - East'),
    (8, 'Ika - South'),
    (9, 'Isoko North'),
    (10, 'Isoko South'),
    (11, 'Ndokwa East'),
    (12, 'Ndokwa West'),
    (13, 'Okpe'),
    (14, 'Oshimili - North'),
    (15, 'Oshimili - South'),
    (16, 'Patani'),
    (17, 'Sapele'),
    (18, 'Udu'),
    (19, 'Ughelli North'),
    (20, 'Ughelli South'),
    (21, 'Ukwuani'),
    (22, 'Uvwie'),
    (31, 'Bomadi'),
    (32, 'Burutu'),
    (33, 'Warri North'),
    (34, 'Warri South'),
    (35, 'Warri South West'),
)

# table LGA Name
class LGAName(models.Model):
    lga_id = models.IntegerField()
    lga_name = models.CharField(max_length=50, choices=LG_CHOICES,)
    state_id = models.IntegerField()
    lga_description = models.CharField(blank=True, max_length=500)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_IPaddress = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.lga_name}'
    

# table Announced Polling Unit result
class PUResult(models.Model):
    pollingunit_uniqueid = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_IPaddress = models.CharField(max_length=50)
    

    def __str__(self):
        return f'{self.party_abbreviation} --> {self.party_score}'
    


# table State Name
class StateName(models.Model):
    state_id = models.IntegerField()
    state_name = models.CharField(max_length=50)
    

    def __str__(self):
        return f'{self.state_name}'
    
    




