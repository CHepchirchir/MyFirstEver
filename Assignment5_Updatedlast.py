# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 13:23:30 2021

@author: chepchir
"""

options = '' #Declaring an empty string

while options != 'Q':
    options = input('Enter the options [P,C,NM,M,CM,Y,In,Q]?')
    print()
      
    if options == 'P':
        print('[P] Print Options')
        print('[C] Convert from Celsius')
        print('[NM] Convert from Nautical Miles')
        print('[M] Convert from Kilometer')
        print('[CM] Convert from Centimeters')
        print('[Y] Convert from Yards')
        print('[In] Convert from Inches')
        print('[Q] Quit')
          
        print ()
    elif options == 'C':       
        #1. Temperature from Fahrenheit to Celsius and back
        celsius = 37.5
        fahrenheit = celsius * 1.8 + 32
        print('%0.3f farenheit equal to %0.1f Celsius' %(fahrenheit,celsius))
          
    elif options == 'NM':
        #2. Convert Nautical Miles to KMS and back,
        KMS = float(input('Enter distance in KMS: '))
        Nautical= float(input('Enter distance in Nautical miles: '))
          # conversion factor
        NMconv_factor = 1.852
        Nautical_Mile = KMS * NMconv_factor
        KILOMETERS = Nautical / NMconv_factor
        print('%0.3fNautical_Miles equal to %0.3f Kilometers' % (KMS,Nautical_Mile))
        print('%0.3fKilometers equal to %0.3f Nautical Miles' % (Nautical,KILOMETERS))
          
    elif options == 'M':
          #3. Convert Kilometer to Miles and back,
          kilo_meter = float(input('Enter distance in Kilometers: '))
          Miles =float(input('Enter distance in Miles: '))
          # conversion factor
          KMconv_fac = 0.621371
          miles = kilo_meter * KMconv_fac
          Kilometer = Miles / KMconv_fac
          print('%0.3f kilometers is equal to %0.3f miles' % (Miles,Kilometer))
          print('%0.3f miles is equal to %0.3f Kilometers' % (kilo_meter,miles))
          
    elif options == 'CM':      
          ## 4.Convert Centimeters to meters and back
          centimeter = float(input("Enter the length in Centimeters: "))
          meter = float(input("Enter the length in Meters: "))
          meters = float(centimeter/ 100)
          Centimeters =float(meter* 100)
          print('%0.3f Centimeters is equal to %0.3f Meters' % (meter ,Centimeters))
          print('%0.3f Centimeters is equal to %0.3f meters' % (centimeter,meters))
          
    elif options == 'Y':
          ## 5Convert Yard to Meters and back,
          meter = float(input("Enter the length in Meters: "))
          yard =float(input('Enter lenght in yards:'))
          # converting Meter to Yard
          meter_to_yard = meter * 1.09361
          # converting Yard to meter
          yard_to_meter = yard / 1.09361
          print("%d Meter is equal to %.4f Yard" % (meter, meter_to_yard))
          print("%d Yard is equalto %.4f Meter" % (yard, yard_to_meter))

    elif options == 'In':
          #6. Convert Inches to Centimeters and back
          inches= float(input("Enter length in Inches: "))
          centimeter = float(input("Enter the length in Centimeters: "))
          # conversion factor
          conv_fac = 0.39370
          Inches = centimeter * conv_fac
          Centimeters =inches / conv_fac
          print("%d Inches is equal to %.4f Centimeters" % (inches, Inches))
          print("%d Centimeters is equalto %.4f inches" % (centimeter, Centimeters))
        
    elif options =='Q':
          print ('Quit')
    else:
          print("invalid option")
    
    print('Thank you')
       
