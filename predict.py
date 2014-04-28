#average is a list of (time,distance) tuples
#first find the time closest to 'distance'
def closest(average,distance):
	for t,d in average:
		if d > distance:
			return t
	return average[-1][1]

# ---- Gives you the secant line for a given point
#Given an average run and your current distance, 
#Returns your predicted pace to stay on track
#Time is actually not needed
def secant_prediction(average,distance,goal):
	cur_time = closest(average,distance)
	goal_time = closest(average,goal)

	return (goal - distance) / (goal_time - cur_time)
	
# ---- Gives you the tangent line for a given point
#Given an average run and your current distance, 
#Returns your predicted pace based on the current spot in past runs
#Time is actually not needed; nor is goal	
def tangent_prediction(average,distance,goal):
	
	