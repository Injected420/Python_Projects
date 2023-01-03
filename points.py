import random
import asyncio
import 
import math
TEAM_ONE_POINTS = 10000
TEAM_TWO_POINTS = 10000

def team_points():
    
    menu = input(f"[*] If you would like to add points, Press A\r\n[*] If you would like to remove points, Press R\r\n[*] Press Q if you would like to quit: ")

    if menu.lower == "A" or menu.lower == "a":
        print(f"Points for Team One:\r\n {team_one_points}")
        print(f"Points for Team Two:\r\n {team_two_points}")
        team_to_add = input("[*] Enter the team you would like to add points to (1 or 2 ): ")
        if team_to_add == 1:
            add_points = input("[*] Enter the number of points to add: ")
            if add_points:
                team_one_points += add_points
                print(f"[*] The points for Team One are now {team_one_points}")
            else:
                print(ValueError)
        elif team_to_add == 2:
            add_points = input("[*] Enter the number of points to add: ")
            if add_points:
                team_two_points += add_points
                print(f"[*] The points for Team Two are now {team_two_points}")
            else:
                print(ValueError)
                
                
                
def add_points():
    team = input("[*] Enter the Team you would like to add points to (1 or 2): ")
    if team != 1 or team != 2:
        return ValueError
    else:
        points = input(f"[*] Enter the number of points you would like to add for Team {team}: ")
        pass
add_points()