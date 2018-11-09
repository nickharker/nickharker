import csv

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
	"""
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 3956 # Use 6371 for km. Use 3956 for miles.
    return c * r
	
with open('csv1', newline='\n') as master:
	reader = csv.reader(master)
	for row in reader:
		with open('csv2', newline='\n') as host:
			readers = csv.reader(host)
			for rows in readers:
				if haversine(row[x], row[y], rows[x], rows[x]) <= z:	#x=index of column with lon, y=index of column with lat, z=distance to be measured in miles or km
					with open('results.csv', 'w', newline='\n') as results:
						writer = csv.writer(results)
						writer.writerows(row + ',' + rows)