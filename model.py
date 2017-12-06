# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 11:39:16 2017

@author: kate
"""

#Imports.
import random
import operator
import matplotlib
import matplotlib.pyplot
import matplotlib.animation 
matplotlib.use('TkAgg')
import matplotlib.backends.backend_tkagg
import csv
import tkinter
import requests
import bs4

import agentframework


#Setting up global variables.
#Making a list called environment to store my x,y values in.
environment = []
#The number of agents used in this model.
num_of_agents = 10
#The number of times each agent is moved.
num_of_iterations = 100
#Blank list of the agents.
agents = []
#Cretating the neighbourhood value.
neighbourhood = 20
#Distance between agents.
length = []


#Reading in data.

#Getting initial x and y coordinates from a website.
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})

#Testing that x and y coordinates have imported from the website.
print("x and y from website")
print(td_ys)
print(td_xs)

#Code to read in the topography data from the CSV reader.
f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    #Making a list to store rows, i.e. the y values.
    row_list = []
    #Looping through the data to store values as rows of data.
    #This is going to be used to create a nested list within the list of environments.
    for value in row:
        row_list.append(value)
    #Adds the lists of the row data to a list of all the data arranged by rows.
    environment.append(row_list)
#        print(value)
f.close()

#Checking that the topography data has loaded properly. Thas has been coded out.
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

#Printing the environment. This has been coded out.
print ("This prints the environment")
print (environment)

carry_on = True


#Initialising the agents using the inital agent values from the website.
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))


#Calculates the distance between agents.
for i in range(num_of_agents):
    length.append(agents[i].distance_between(agent))
    
#Prints the list of distances between agents.
print("distance between agents")
print(length)


#Prints the distance between agents and tells you if they are occupying the same point.
print ("Distance between agents")
for i in range(num_of_agents-1):
    print (length[i])       
    if length[i] == 0:
        print ("Oh no, two agents have crashed")

#Printing a list of the coordinates of the agents.
print ("Coordinate pairs of the agents") 
for agent in agents:
    print (agent)


#Setting up the graph so that it can be animated.
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_autoscale_on(False)

#Updating the graph with the new positions that the agents are moving into.
def update(frame_number):
    """Update the frame everytime an interation is run.
    
    Positional arguements:
    frame_number -- an interger number (no default)
    
    Returns:
    The new position of the variables.
    """
    #Clearing anything that is already displayed in the graph.
    fig.clear()
    #Getting the agents to do things a certain number of times.
    random.shuffle(agents)
    for i in range(num_of_agents):
        #Getting the agents to move.
        agents[i].move()
        #Getting the agents to eat.
        agents[i].eat()
        #Seeing if the agensts are within 20 units of thier neighbours.
        agents[i].share_with_neighbours(neighbourhood)
    
    #Getting the graph to print the new locations of the agents.
    #Getting the graph to print the new topography as the agents have eaten into it.
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
        #Setting up the x and y scales.
        #If I change the x and y scales to 100, it will only plot the axes up to 100.
        #However, this is not a good idea as the agents can move up to x and y coordinates of 300.
        matplotlib.pyplot.ylim(0,300)
        matplotlib.pyplot.xlim(0,300)     
    matplotlib.pyplot.imshow(environment)  

#Function to get an intruction, conduct a task and then wait for it's next call.
def gen_function (b = [0]):
    """Wais to be called, then run.
    
    Positional arguements:
    b -- an interger number (default = 0)
    
    Returns:
    The function.
    """
    a = 0
    global carry_on 
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        

#Making the GUI.
def run():
    """Run the GUI.
    
    Returns:
    The GUI.
    """
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.show()

#Setting up the GUI.
root = tkinter.Tk()
root.wm_title("Model")
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 

#Getting the GUI to show the animation the model is run.
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
c = tkinter.Canvas(root, width=200, height=200)
c.pack()
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
canvas.show()


#Gets the model to run.
tkinter.mainloop()

#Writing the amount the sheep have eaten to a list in a file.
#Making a list of what the sheep have eaten
eaten = []
for i in range(num_of_agents):
    a = agents[i].store
    eaten.append(a)
print("This is a list of what the agents have eaten")
print(eaten)

#Writing the list of what the agents have eaten to a file
f = open("stomach.txt", 'w')
string_eaten = str(eaten)
f.write(string_eaten)
f.close()


#Agent 5 telling us what agent 0 has eaten.
print("Agent 5, what has agent 0 eaten?")
print("Hello user, I am agent 5, I have just spoken to agent 0, and it told me that it has eaten " + str(agents[5].agents[0].store) + " units" )
