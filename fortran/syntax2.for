      Program syntax2
********************************************
*
* Conversion of Fahrenheit to Celsius and Kelvin
*
* By: Jeremy Corner
*
* I have neither given or recieved nor have I tolerated others' use of unathourized aid.
*
********************************************

      REAL TEMPF

      Print *, 'What is the temperature in Fahrenhiet?'
      READ(*,*) TEMPF

      TEMPC = (5.0/9.0)*(TEMPF-32.0)

      TEMPK = (TEMPF+459.67)*(5.0/9.0)

      PRINT *, 'The temperature is', TEMPC,'degrees Celsius.'
      
      PRINT *, 'The temperature is', TEMPK,'Kelvin.'


      END
