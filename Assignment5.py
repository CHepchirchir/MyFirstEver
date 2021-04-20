# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 13:23:30 2021

@author: chepchir
"""

#1. convert Metric to SI Units

celsius =(37.5)
fahrenheit =((celsius * 1.8) + 32)
print("%0.3f farenheit equal to %0.1f Celsius" %(fahrenheit,Celsius)
      
#2. Nautical Miles conversion factor
print("Enter the distance in KMS: ")
KMS = float(input())
# conversion factor
NMconv_factor = 1.852

Nautical_Mile = float(KMS * NMconv_factor)
print("%0.3fNauticalMiles equal to %0.3f Kilometers" %(Nautical_Mile,kms)

#3. convert kilometers into miles
kilo_meter = float(input("Enter distance in kilometers: "))

KMconv_fac = 0.621371
 
miles = kilo_meter * KMconv_fac
print('%0.3f kilometers is equal to %0.3f miles' %(km,miles))

###convert miles into kilometers
miles = float(input("Enter distance in miles: "))
 
# conversion factor
Mileconv_fac = 1.60934
 
# calculate miles
km = miles * Mileconv_fac
print('%0.3f miles is equal to %0.3f Kilometers' %(miles,km))




## CM-M 
print("Enter the length in centimeter::")
centimeter = float(input())
meters = float(centimeter/100)
print("Length in Meter      = ", meters, " m")
print("Length in Centimeter    = ", centimeter, " cm")
##
meter =float(input()) # Length in Meter
yard =float(input())  # Length in Yard
  
# converting Meter to Yard
meter_to_yard = meter * 1.09361
  
# converting Yard to meter
yard_to_meter = yard / 1.09361
  
# printing the output
print("%d Meter in Yard = %.4f " % (meter, meter_to_yard))
print("%d Yard in Meter = %.4f " % (yard, yard_to_meter))