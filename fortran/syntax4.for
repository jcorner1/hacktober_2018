      PROGRAM syntax4

***********************************************************
* A program that will subtract 5 from a given value until 
* it is less than 0. The program will then output the 
* number of times 5 was subtracted from the value.
*
* By: Jeremy Corner
* 
* I have neither given or recieved, nor have I tolerated 
* others' use of unathourized aid.
*
***********************************************************




c Program currently generates a random number between 0 and 1000 

      real rvalue
      integer nvalue,i,evalue,fvalue

c Start random number generator with computer time
      rvalue1 = rand(time())

c Select random number, make integer between 0 and 1000
      nvalue = 1000*rand(0)

c Print random number value
      print *,"the intial value is", nvalue
     
c we can find the amount of times the value is subtracted, by dividing the number by 5

      fvalue = nvalue/5

c Now we need to subtract from the value
      
      do while (nvalue .gt. 0)
          print*, nvalue
        nvalue = nvalue-5
      enddo

c now we print the amount of time the progam subtracted 5.

      print *, 'The program subtracted 5 from the given value' , fvalue, 'times.'

      END
