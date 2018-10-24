      PROGRAM c_to_f

c converts Celsius to Farhenheit 

      implicit none
      integer c, f

      print*, "Enter a temperature in celsius"
      read(*,*) c

      f = ((1.8 * c) + 32)

      print*, "The temperature", c, "Celsius is", f, "Farhenheit"

      end
