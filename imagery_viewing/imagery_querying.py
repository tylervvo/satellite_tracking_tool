
# currently using EE locally, still need to figure out how to run on servers
# Successfully goes through all of the images but it doesn't export it (?????) very confused.

from imagery_viewing.models import Analysis
import ee

ee.Initialize()

#Constant to use when referencing different attributes of a filter
FILTER_CHOICE = {
				'Satellite':{'collection': 'LANDSAT/LE07/C01/T1_RT', 'bands':['B3','B2','B1']},
				#add more in the same format
				}


def queryAll():
	all_analysis = Analysis.objects.all()
	for analysis in all_analysis:

		type_analysis = analysis.type_analysis
		start_date = analysis.start_date
		end_date = analysis.end_date
		case = analysis.case
		NE_long, NE_lat, SW_long, SW_lat = analysis.north_east_long, analysis.north_east_lat, analysis.south_west_long, analysis.south_west_lat

		geometry = ee.Geometry.Rectangle([float(NE_lat), float(NE_long), float(SW_lat), float(SW_long)])
		
		if type_analysis == 'sat': #would add different if branches to query different filters
			filter_choice = FILTER_CHOICE['Satellite']
			#this needs to be editted to include the most relevant images (some images are covered in clouds or complete black)
			collection = ee.ImageCollection(filter_choice['collection']).filterDate(str(start_date), str(end_date)) \
																			.filterBounds(geometry) \
																			.select(filter_choice['bands']) \
																			.filter(ee.Filter.lt('CLOUD_COVER',25))

		size = collection.size().getInfo()
		images = collection.toList(size)
		print("{} {} filter from {} to {} has {} images".format(case, type_analysis, start_date, end_date, size))

		for i in range(size):
			curr = ee.Image(images.get(i))
			export = ee.batch.Export.image.toCloudStorage(image=curr,
		                                     	region= geometry.getInfo()['coordinates'],
		                                     	bucket='satellite-mapping-standalone.appspot.com',
		                                     	maxPixels=10000000, #arbitrary this can be changed
			                                    description="{}.{}.{}".format(case, type_analysis, str(curr.get('DATE_ACQUIRED').getInfo())),
		                                    	scale=30)
			export.start()
			#to check if the export is completed, use command line: earthengine task list 
			print(export.status())



#to query an individual area, to input in command line (shell)
#note type = 'sat' or ... , dates must be in format '2018-01-01'
def getIndividualQuery(NE_long, NE_lat, SW_long, SW_lat, type_analysis, start_date, end_date, case):
	geometry = ee.Geometry.Rectangle([float(NE_lat), float(NE_long), float(SW_lat), float(SW_long)])

	filter_choice = FILTER_CHOICE[type_analysis]
	collection = ee.ImageCollection(filter_choice['collection']).filterDate(str(start_date), str(end_date)) \
																	.filterBounds(geometry) \
																	.select(filter_choice['bands']) \
																	.filter(ee.Filter.lt('CLOUD_COVER',25))
	size = collection.size().getInfo()
	images = collection.toList(size)

	for i in range(size):
		curr = ee.Image(images.get(i))
		export = ee.batch.Export.image.toCloudStorage(image=curr,
	                                     	region= geometry.getInfo()['coordinates'],
	                                     	bucket='satellite-mapping-standalone.appspot.com',
	                                     	maxPixels=1000000,
	                                     	description="test.{}.{}".format(type, str(curr.get('DATE_ACQUIRED').getInfo())),
	                                    	scale=30)
		export.start()
		#to check if its completed, use commend line: earthengine task list
		print(export.status())
