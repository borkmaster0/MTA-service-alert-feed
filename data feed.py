import urllib.request
import json

# Initialize MTA class
class MTA():
	@staticmethod
	def fetch_data():
		'''
		Fetch and repackage data.
		'''
		# Get the data
		response = urllib.request.urlopen(
		 r"https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/camsys%2Fsubway-alerts.json"
		).read()
		
		# Parse raw JSON into a dictionary
		jsonified_data = json.loads(response)['entity']
		
		data = []
		
		# Start for loop here
		for k in range(0, len(jsonified_data)):
			selected_alert_index = k
			alert = jsonified_data[selected_alert_index]
			alert_type = alert['id'].split(':')[1]
			alert_data = alert['alert']
			
			# Get all affected routes
			temp = [alert_data['informed_entity']]
			affected_routes = []
			if len(temp) == 1:
				affected_routes = temp[0][0]['route_id']
			else:
				for i in range(0, len(temp)-1):
					affected_routes.append(temp[i]['route_id'])
			
			# Get text
			header_text = alert_data['header_text']['translation'][0]['text']
			try:
				# Try to get the description, if it fails, then set it to nothing
				description_text = '\n\n'.join(alert_data['description_text']['translation'][0]['text'].split('\n'))
			except:
				description_text = 'none'
			
			alert_type_detailed = alert_data['transit_realtime.mercury_alert']['alert_type']
			
			try:
				alert_time_in_effect = alert_data['transit_realtime.mercury_alert']['human_readable_active_period']['translation'][0]['text']
			except:
				alert_time_in_effect = 'none'
			
			data.append({'index': selected_alert_index, 'alert_type': alert_type, 'affected_routes': affected_routes, 'header_text': header_text, 'description_text': description_text, 'detailed_alert_type': alert_type_detailed, 'time_in_effect': alert_time_in_effect})
		return data
	
	@staticmethod
	def get_alert_at_index(index):
		'''
		Gets an alert at a selected index.
		'''
		all_alerts = MTA.fetch_data()
		
		for alert in all_alerts:
			if alert['index'] == index:
				return alert
		return []
	
	@staticmethod
	def all_alerts():
		'''
		Fetch all current alerts.
		'''
		all_data = MTA.fetch_data()
		
		alerts = []
		for alert in all_data:
			if alert['alert_type'] == 'alert':
				alerts.append(alert)
		
		return alerts
	
	@staticmethod
	def all_planned_work():
		'''
		Fetch all planned work.
		'''
		all_data = MTA.fetch_data()
		
		planned_work = []
		for alert in all_data:
			if alert['alert_type'] == 'planned_work':
				planned_work.append(alert)
		
		return planned_work
	
	@staticmethod
	def all_alerts_for_line(line):
		'''
		Get all active alerts for a line.
		'''
		all_data = MTA.fetch_data()
		
		alerts = []
		for alert in all_data:
			if alert['affected_routes'] == line and alert['alert_type'] == 'alert':
				alerts.append(alert)
		return alerts
	
	@staticmethod
	def all_planned_work_for_line(line):
		'''
		Get all planned work for a line.
		'''
		all_data = MTA.fetch_data()
		
		alerts = []
		for alert in all_data:
			if alert['affected_routes'] == line and alert['alert_type'] == 'planned_work':
				alerts.append(alert)
		return alerts
	
	@staticmethod
	def pretty_alert(alert):
		'''
		Attempts to show the alert in a human readable format.
		'''
		try:
			print(alert['detailed_alert_type'])
			print('-'*25)
			print(alert['header_text'])
			if alert['description_text'] != 'none':
				print('\n')
				print(alert['description_text'])
			print('\n' + '-'*25)
			if alert['time_in_effect'] != 'none':
				print(alert['time_in_effect'])
		except:
			raise Exception("Value is not an alert.")

## Testing area
a = MTA()


print(a.pretty_alert(a.all_planned_work_for_line('F')[0]))
