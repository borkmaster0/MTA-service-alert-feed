a = MTA

print(a.pretty_alert(a.all_planned_work_for_line('F')[0]))

'''
Above code prints:

Planned - Part Suspended
-------------------------
In Brooklyn, no [F] between Kings Hwy and Coney Island-Stillwell Av


[F] runs between Jamaica-179 St and Kings Hwy, the last stop.



shuttle bus icon Free shuttle buses run between Kings Hwy and Coney Island-Stillwell Av.

Transfer between trains and shuttle bus icon buses at Kings Hwy.

For direct service between Coney Island-Stillwell Av and Manhattan/Downtown Brooklyn, take the [N] or [Q].



Transfer stations:

34 St-Herald Sq accessibility icon | [F][N][Q]

4 Av-9 St [F][N]

Kings Hwy [F] and shuttle bus icon

Coney Island-Stillwell Av accessibility icon | [N][Q] and shuttle bus icon

What's happening?

We're modernizing signals on the Culver Line



accessibility icon This service change affects one or more ADA accessible stations and these travel alternatives may not be fully accessible. Please contact 511 to plan your trip.

-------------------------
May 18 - 20, Sat 12:15 AM to Mon 5:00 AM
None


'''

print(a.all_planned_work_for_line('A'))

'''
The above command prints:

[
  {'index': 40, 
  'alert_type': 'planned_work', 
   'affected_routes': 'A', 
   'header_text': 'In Manhattan, uptown local [A] skips Spring St, 23 St and 50 St', 
   'description_text': "For service to Spring St and 23 St, take the [A] to W 4 St-Wash Sq or 34 St-Penn Station and transfer to a downtown [A] local or [E].\n\n\n\nFor service to 50 St, take the [E] via transfer at 42 St-Port Authority.\n\n\n\nFor service from these stations, take the [A] or [E] to 42 St-Port Authority, 14 St or Canal St and transfer to an uptown [A].\n\n\n\nWhat's happening?\n\nWe're making electrical improvements", 
   'detailed_alert_type': 'Planned - Stops Skipped', 
   'time_in_effect': 'May 17 - 20, Fri 11 PM to Sat 6:30 AM, Sat 11 PM to Sun 7:45 AM and Sun 11 PM to Mon 5 AM'
  }, 
  {'index': 50, 
   'alert_type': 'planned_work', 
   'affected_routes': 'A', 
   'header_text': 'In Manhattan, downtown local [A] skips 50 St, 23 St and Spring St', 
   'description_text': "For service to these stations, take the [A] to 42 St-Port Authority, 14 St or Canal St and transfer to an uptown [A] or [E].\n\n\n\nFor service from 50 St, take the [E] to 42 St-Port Authority accessibility icon and transfer to the [A].\n\n\n\nFor service from 23 St and Spring St, take the [A] or [E] to 34 St-Penn Station or W 4 St-Wash Sq and transfer to a downtown [A].\n\n\n\nWhat's happening?\n\nWe're making structural improvements\n\n\n\naccessibility icon This service change affects one or more ADA accessible stations and these travel alternatives may not be fully accessible. Please contact 511 to plan your trip.", 
   'detailed_alert_type': 'Planned - Stops Skipped', 
   'time_in_effect': 'May 31 - Jun 3, Fri 10:30 PM to Sat 6:15 AM, Sat 11 PM to Sun 7:45 AM and Sun 11 PM to Mon 5 AM'
  }, 
  {
    'index': 125, 
    'alert_type': 'planned_work', 
    'affected_routes': 'A', 
    'header_text': 'In Manhattan, downtown local [A] skips 50 St, 23 St and Spring St', 
    'description_text': "For service to these stations, take the [A] to 42 St-Port Authority, 14 St or Canal St and transfer to an uptown [A].\n\n\n\nFor service from 50 St, take the [A] to 59 St-Columbus Circle and transfer to a downtown [A].\n\n\n\nFor service from 23 St and Spring St, take the [A] to W 4 St-Wash Sq or 34 St-Penn Station and transfer to a downtown [A].\n\n\n\nWhat's happening?\n\nStructural maintenance\n\n\n\naccessibility icon This service change affects one or more ADA accessible stations and these travel alternatives may not be fully accessible. Please contact 511 to plan your trip.", 
    'detailed_alert_type': 'Planned - Stops Skipped', 
    'time_in_effect': 'May 24 - 28, Fri 10:30 PM to Sat 6:15 AM, Sat to Mon, 11 PM to 7:45 AM and Mon 11 PM to Tue 5 AM'
  }, 
  {'index': 142, 
   'alert_type': 'planned_work', 
   'affected_routes': 'A', 
   'header_text': 'In Lower Manhattan and Brooklyn, no Queens-bound [A] at Spring St, Canal St, Chambers St, Fulton St and High St', 
   'description_text': "Ozone Park/Far Rockaway-bound [A] runs via the [F] from W 4 St-Wash Sq to Jay St-MetroTech.\n\n\n\nTravel Alternatives:\n\nFor Spring St, Canal St and Chambers St/World Trade Center, take the [E] or an uptown [A] via transfer at W 4 St-Wash Sq accessibility icon.\n\n\n\nFor Fulton St, take the [J] via transfer at Delancey St-Essex St [F] station. Or, use the nearby World Trade Center accessibility icon | [E] station via transfer at W 4 St-Wash Sq accessibility icon.\n\n\n\nFor High St, use the nearby York St [F] station instead.\n\n\n\nWhat's happening?\n\nStructural maintenance\n\n\n\naccessibility icon This service change affects one or more ADA accessible stations, and these travel alternatives may not be fully accessible. Please contact 511 to plan your trip.", 
   'detailed_alert_type': 'Planned - Reroute', 
   'time_in_effect': 'May 20 - 24, Mon to Fri, 9:45 PM to 5:00 AM'
  }, 
  {'index': 143, 
   'alert_type': 'planned_work', 
   'affected_routes': 'A', 
   'header_text': 'In Manhattan, downtown [A] stops at 50 St and 23 St', 
   'description_text': "Reminder: Late night local trains also serve these stations.\n\n\n\nWhat's happening?\n\nStructural maintenance", 
   'detailed_alert_type': 'Planned - Express to Local', 
   'time_in_effect': 'May 20 - 23, Mon to Thu, beginning 10 PM'
  }, ...
'''
