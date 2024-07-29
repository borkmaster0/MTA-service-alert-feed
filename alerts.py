import urllib.request
import json
import time

# Initialize MTA class
class MTA:
    
    class MTAError(Exception):
        pass
    
    class Subway: # Subway class
    
        @staticmethod
        def fetch_data() -> list[dict]:
            '''
            Fetch and repackage data.
            '''
            # Get the data
            try:
                response = urllib.request.urlopen(
            r"https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/camsys%2Fsubway-alerts.json"
            ).read()
            except:
                raise MTA.MTAError("Failed to retrieve subway data.")
            
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
                
                data.append({'index': selected_alert_index, 
                 'alert_type': alert_type, 
                 'affected_routes': affected_routes, 
                 'header_text': header_text, 
                 'description_text': description_text, 
                 'detailed_alert_type': alert_type_detailed, 
                 'time_in_effect': alert_time_in_effect})
            return data

        @staticmethod
        def get_alert_at_index(index: int) -> list:
            '''
            Gets an alert at a selected index.
            '''
            all_alerts = MTA.Subway.fetch_data()
            
            for alert in all_alerts:
                if alert['index'] == index:
                    return alert
            return []
    
        @staticmethod
        def alerts() -> list:
            '''
            Fetch all current alerts.
            '''
            all_data = MTA.Subway.fetch_data()
            
            alerts = []
            for alert in all_data:
                if alert['alert_type'] == 'alert':
                    alerts.append(alert)
            
            return alerts

        @staticmethod
        def planned_work() -> list:
            '''
            Fetch all planned work.
            '''
            all_data = MTA.Subway.fetch_data()
            
            planned_work = []
            for alert in all_data:
                if alert['alert_type'] == 'planned_work':
                    planned_work.append(alert)
            
            return planned_work

        @staticmethod
        def alerts_for_line(line: str) -> list:
            '''
            Get all active alerts for a line.
            '''
            all_data = MTA.Subway.fetch_data()
            
            alerts = []
            for alert in all_data:
                if alert['affected_routes'] == line and alert['alert_type'] == 'alert':
                    alerts.append(alert)
            return alerts

        @staticmethod
        def planned_work_for_line(line: str) -> list:
            '''
            Get all planned work for a line.
            '''
            all_data = MTA.Subway.fetch_data()
            
            alerts = []
            for alert in all_data:
                if alert['affected_routes'] == line and alert['alert_type'] == 'planned_work':
                    alerts.append(alert)
            return alerts

        @staticmethod
        def pretty_alert(alert: dict) -> None:
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
                raise MTA.MTAError("Value is not an alert.")

    class Bus: # Bus class
        
        @staticmethod
        def fetch_data() -> list[dict]:
            """
            Fetch and repackage data
            """
            try:
                response = urllib.request.urlopen(
            r"https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/camsys%2Fbus-alerts.json"
            ).read()
            except:
                raise MTA.MTAError("Failed to retrieve bus data.")
            
            # Parse raw JSON into a dictionary
            jsonified_data = json.loads(response)['entity']
            
            data = []
            
            for i in range(0, len(jsonified_data)):
                alert_type_internal = jsonified_data[i]['id'].split(":")[1]
                alert_selection = jsonified_data[i]['alert']
                lines_affected = []
                for item in alert_selection['informed_entity']:
                    lines_affected.append(item['route_id'])
                
                header_text = alert_selection['header_text']['translation'][0]['text']
                
                try:
                    description_text = alert_selection['description_text']['translation'][0]['text']
                except:
                    description_text = 'None'
                
                display_alert_type = alert_selection['transit_realtime.mercury_alert']['alert_type']
                created_at = time.localtime(alert_selection['transit_realtime.mercury_alert']['created_at'])
                updated_at = time.localtime(alert_selection['transit_realtime.mercury_alert']['updated_at'])
                
                if alert_type_internal == 'planned_work':
                    planned_work_time = alert_selection['transit_realtime.mercury_alert']['human_readable_active_period']['translation'][0]['text']
                else:
                    planned_work_time = 'None'
                
                data.append({
                    'index': i,
                    'alert_type_internal': alert_type_internal,
                    'lines_affected': lines_affected,
                    'header_text': header_text,
                    'description_text': description_text,
                    'display_alert_type': display_alert_type,
                    'created_at': created_at,
                    'updated_at': updated_at, 
                    'planned_work_time': planned_work_time
                })
            
            return data

        @staticmethod
        def get_alert_at_index(index: int=0) -> list:
            """
            Get an alert at a index.
            """
            data = MTA.Bus.fetch_data()
            return data[index]

        @staticmethod
        def alerts() -> list:
            """
            Get all current alerts.
            """
            data = MTA.Bus.fetch_data()
            temp = []
            for item in data:
                if item['alert_type_internal'] == 'alert':
                    temp.append(item)
            return temp

        @staticmethod
        def planned_work() -> list:
            """Get all planned work for buses."""
            data = MTA.Bus.fetch_data()
            temp = []
            for item in data:
                if item['alert_type_internal'] == 'planned_work':
                    temp.append(item)
            return temp
        
        @staticmethod
        def alerts_for_line(line: str) -> list:
            """Get all alerts for a bus line."""
            data = MTA.Bus.fetch_data()
            temp = []
            for item in data:
                if line in item['lines_affected'] and item['alert_type_internal'] == 'alert':
                    temp.append(item)
            return temp

        @staticmethod
        def planned_work_for_line(line: str) -> list: 
            """Get all planned work for a bus line."""
            data = MTA.Bus.fetch_data()
            temp = []
            for item in data:
                if line in item['lines_affected'] and item['alert_type_internal'] == 'planned_work':
                    temp.append(item)
            return temp

        @staticmethod
        def pretty_alert(alert: dict) -> None:
            """Attempt to display the alert in a human readable format"""
            try:
                print(alert['display_alert_type'])
                print('-'*25)
                print(alert['header_text'])
                print('\n')
                if alert['description_text'] != 'None':
                    print('\n')
                    print(alert['description_text'])
                
                print('\n' + '-'*25)
                if alert['planned_work_time'] != 'None':
                    print(alert['planned_work_time'])
            except:
                raise ValueError("Value is not an alert.")

    class Equipment:
        @staticmethod
        def fetch_data() -> list[dict]:
            """Fetch data for equipment outages.

            Returns:
                list[dict]: List containing dictionaries of the equipment information.
            """
            try:
                response = urllib.request.urlopen(
            r"https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fnyct_ene.json"
            ).read()
            except:
                raise MTA.MTAError("Failed to retrieve equipment data.")
            
            # Parse raw JSON into a dictionary
            jsonified_data = json.loads(response)
            
            return jsonified_data

        @staticmethod
        def outage(station_name: str = None, **kwargs) -> list[dict]: ## Main outage function
            '''
            Gets outages for a station or all outages.
            Station Name is required.\n
            Optional Args:
            - Equipment ID
            - Equipment Type
            - Reason
            - Outage date & time (MM/DD/YYYY HH:MM:SS AM/PM)
            \n\tTypes:
            - ES (Escalators)
            - EL (Elevators)
            '''
            equipment_id = kwargs.get("id", None)
            equipment_type = kwargs.get("type", None)
            reason = kwargs.get('reason', None)
            date = kwargs.get("date", None)
            
            if equipment_type != "ES" and equipment_type != "EL" and equipment_type != None:
                raise ValueError("Invalid equipment type. Can only be 'ES' or 'EL' or None.")
            
            data = MTA.Equipment.fetch_data()
            items = []
            
            for item in data:
                if all([True if station_name == None else item['station'] == station_name,
                    True if equipment_id == None else item['equipment'] == equipment_id,
                    True if equipment_type == None else item['equipmenttype'] == equipment_type,
                    True if reason == None else item['reason'] == reason,
                    True if date == None else item['outagedate']]):
                        items.append(item)
            return items

        @staticmethod
        def upcoming(station_name: str = None, **kwargs) -> list[dict]: 
            """
            Get upcoming outages.
            Station Name is required.\n
            Optional Args:
            - Equipment ID
            - Equipment Type
            - Reason
            \n\tTypes:
            - ES (Escalators)
            - EL (Elevators)
            """
            if station_name != None:
                eq_id = kwargs.get('id', None)
                eq_type = kwargs.get('type', None)
                r = kwargs.get('reason', None)
                data = MTA.Equipment.outage(station_name=station_name, id=eq_id, type=eq_type, reason=r)
                
                items = []
                for item in data:
                    if item['isupcomingoutage'] == "Y":
                        items.append(item)
                return items
            else:
                data = MTA.Equipment.fetch_data()
                items = []
                for item in data:
                    if item['isupcomingoutage'] == "Y":
                        items.append(item)
                return items

        @staticmethod
        def maintenance(station_name: str =None, **kwargs) -> list[dict]:
            """
            Get whether or not a outage is maintenance related.
            Station Name is required.\n
            Optional Args:
            - Equipment ID
            - Equipment Type
            - Reason
            \n\tTypes:
            - ES (Escalators)
            - EL (Elevators)
            """
            if station_name != None:
                eq_id = kwargs.get('id', None)
                eq_type = kwargs.get('type', None)
                r = kwargs.get('reason', None)
                data = MTA.Equipment.outage(station_name=station_name, id=eq_id, type=eq_type, reason=r)
                
                items = []
                for item in data:
                    if item['ismaintenanceoutage'] == "Y":
                        items.append[item]
                return items
            else:
                data = MTA.Equipment.fetch_data()
                items = []
                for item in data:
                    if item['ismaintenanceoutage'] == "Y":
                        items.append[item]
                return items

        def all_equipment_info(**kwargs) -> list[dict]:
            """Gets all equipment information. User needs to parse through this data if optional filter args are not filled.
            
            Optional Filter Args:
                station: str = Station Name
                line: str = Train Line
                bus_connections: str = Bus Line
                active: bool = If the equipment is active
                private: bool = If the equipment is privately maintained
                equipment_type: str = The type of equipment (ES) or (EL)

            Returns:
                list[dict]: A list containing dictionaries of all equipment.
            
            Dictionary keys:
                station: Station name\n
                borough: Empty\n
                trainno: Trains served\n
                equipmentno: Equipment id\n
                equipmenttype: if escalator or elevator\n
                serving: Lines served\n
                ADA: Is ADA compliant?\n
                isactive: is being used and active\n
                nonNYCT: is privately maintained?\n
                shortdescription: A short description of its position\n
                linesservedbyelevator: Lines served\n
                elevatorsgtfsstopid: GTFS stop id\n
                elevatormrn: Unknown\n
                stationcomplexid: GTFS Station complex id\n
                nextadanorth: Next ADA compliant equipment north of the station\n
                nextadasouth: Next ADA compliant equipment south of the station\n
                redundant: If the equipment is a redundant\n
                busconnections: All bus connections\n
                alternativeroute: Alternatives if equipment is down.
            """
            
            station = kwargs.get("station", None)
            line = kwargs.get("line", None)
            bus_connections = kwargs.get("bus", None)
            active = kwargs.get("active", None)
            
            try:
                response = urllib.request.urlopen(
                r"https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fnyct_ene_equipments.json"
                ).read()
            except:
                raise MTA.MTAError("Failed to retrieve equipment information")
            
            jsonified_data = json.loads(response)
            
            for item in jsonified_data:
                item['trainno'] = item['trainno'].split('/')
                item['busconnections'] = item['busconnections'].split(',')
                item['linesservedbyelevator'] = item['linesservedbyelevator'].split('/')
            
            ## Filters
            if station != None:
                jsonified_data = [item for item in jsonified_data if item['station'] == station]
            
            elif line != None:
                jsonified_data = [item for item in jsonified_data if line in ['trainno']]
            
            elif bus_connections != None:
                jsonified_data = [item for item in jsonified_data if bus_connections in item['busconnections']]
            
            elif active != None: 
                jsonified_data = [item for item in jsonified_data if ("Y" if active else "N") == ("Y" if active else "N")]
            
            return jsonified_data

        @staticmethod
        def is_accessible(station: str, type: str, **kwargs) -> bool:
            """Gets whether or not a station is accessible.

            Args:
                station (str): Station name e.g. 'Grand Central-42 St'
                type (str): Escalator (ES) or elevator (EL)
            
            Optional:
                available (bool): Get all available equipment
                unavalable (bool): Get all unavailable equipment

            Returns:
                bool: If station is accessible
                
            """
            get_available = kwargs.get("available", False)
            get_unavailable = kwargs.get("unavailable", False)
            
            outages = []
            all_equipment = []
            temp = []
            
            ## Parse through and only get the equipment at the station
            for item in MTA.Equipment.all_equipment_info():
                if item['station'] == station:
                    all_equipment.append(item['equipmentno'])
            
            ## Get all equipment IDs for out equipment
            for item in MTA.Equipment.outage(station, type=type):
                outages.append(item['equipment'])
            
            ## Remove the equipment IDs that are out
            for item in outages:
                all_equipment.pop(all_equipment.index(item))
            
            ## Return the equipment data if args provided
            if get_available:
                for item in MTA.Equipment.all_equipment_info():
                    for i in range(len(all_equipment)):
                        if item['equipmentno'] == all_equipment[i]:
                            temp.append(item)
                return temp
            elif get_unavailable:
                for item in MTA.Equipment.all_equipment_info():
                    for i in range(len(outages)):
                        if item['equipmentno'] == outages[i]:
                            temp.append(item)
                return temp
            
            ## return Boolean
            return True if len(all_equipment) != 0 else False
            
if __name__ == "__main__":
    a = MTA.Equipment
    print(a.upcoming())
