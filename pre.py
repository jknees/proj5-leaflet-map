

def process(raw):

	cooked = []

	for line in raw:
		entry = {}
		entry['name'], entry['lat'], entry['lon'] = line.strip().split(',')
		cooked.append(entry)

	return cooked
