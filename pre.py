

def process(raw):

	cooked = []

	for line in raw:
		entry = {}
		entry['name'], entry['lat'], entry['lon'] = line.split(',').strip()
		cooked.append(entry)

	return cooked
