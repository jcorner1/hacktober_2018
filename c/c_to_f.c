#include <stdio.h>

int main()
{
	float C, F;

	printf("Enter a temperature in Celsius");
	scanf("%f", &C);

	F = (1.8 * C) + 32; 

	//printf("\n %.2f Celcius = %.2f Fahrenheit", C, F);
	printf("The temperature %.2f Celsius is the temperature %.2f Fahrenheit", C, F); 

	return 0;
}
