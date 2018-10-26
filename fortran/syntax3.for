      PROGRAM syntax3

*************************************************
*
* By: Jeremy Corner Date: August 30 2018
*
* I have neither given or recieved nor I tolerated
* others' use of unathourized aid. 
* 
*************************************************


* The first thing to do is to find the current time.

      REAL HOUR, MINS

      PRINT *, 'What is the current hour in UTC?'
      READ (*,*) HOUR

      PRINT *, 'What is the current minute in UTC?'
      READ (*,*) MINS

* Now we know the current time, we can setup IFTHEN statements to determine the model.


       IF ((3 .LE. HOUR) .AND. (HOUR .LE. 8) .AND. (MINS .LE. 59)) THEN
       PRINT *, 'The approiate model to use is the 00 UTC run.'

      ELSEIF ((9 .LE. HOUR) .AND. (HOUR .LE. 14) .AND. (MINS .LE. 59)) THEN
      PRINT *, 'The approiate model to use is the 06 UTC run.'

      ELSEIF ((15 .LE. HOUR) .AND. (HOUR .LE. 20) .AND. (MINS .LE. 59)) THEN
      PRINT *, 'The approiate model to use is the 12 UTC run.'

      ELSEIF (((21 .LE. HOUR) .AND. (HOUR .LE. 23) .OR. ((0 .LE. HOUR) .AND. (HOUR .LE. 2))) .AND. (MINS .LE. 59)) THEN
      PRINT *, 'The approiate model to use is the 18 UTC run.'

      ELSE
      PRINT *, 'The previous numbers entered do not correspond to an actual time.'

      ENDIF

      END 

