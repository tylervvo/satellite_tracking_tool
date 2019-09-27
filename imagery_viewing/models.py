from django.db import models

# Create your models here.
class Analysis(models.Model):
	TWO_WEEKS = '2Wks'
	ONE_MONTH = '1mo'
	TWO_MONTHS = '2mo'
	ASYNC = 'async'

	SATELLITE = 'sat'
	NO2 = 'no2'

	TYPE_OPTIONS = [
		(SATELLITE, 'Satellite'),
		(NO2, 'NO2')
	]

	FREQUECY_OPTIONS = [
		(TWO_WEEKS, '2 Weeks'),
		(ONE_MONTH, '1 Month'),
		(TWO_MONTHS, '2 Months'),
		(ASYNC, 'Asynchronously')
	]


	north_east_long = models.DecimalField(max_digits=17, decimal_places=14)
	north_east_lat = models.DecimalField(max_digits=17, decimal_places=14)
	south_west_long = models.DecimalField(max_digits=17, decimal_places=14)
	south_west_lat = models.DecimalField(max_digits=17, decimal_places=14)
	start_date = models.DateField()
	end_date = models.DateField()
	frequency = models.CharField( #subjected to change as I develop this
			max_length=100,
			choices=FREQUECY_OPTIONS,
			default=ASYNC,
		)
	type_analysis = models.CharField(
			max_length=100,
			choices=TYPE_OPTIONS,
			default=SATELLITE,
		)
	case = models.CharField(max_length=100) #this is actually a foreign key, temp value for identification purposes
	#type of analysis: a unique model with name and description
