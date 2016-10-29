"""
Nose tests for acp_times.py
"""
import pre

def test_location():
	raw = open("poi.txt")
	places = pre.process(raw)
	assert places[0]['name'] == 'Student Tennis Center'
	assert places[0]['lat'] == '44.04157'
	assert places[0]['lon'] == -123.0732

	assert places[1]['name'] == 'Student Tennis Courts'
	assert places[1]['lat'] == '44.04044'
	assert places[1]['lon'] == '-123.07312'

	assert places[2]['name'] == 'The Y Tennis Courts'
	assert places[2]['lat'] == '44.03612'
	assert places[2]['lon'] == '-123.0833'
