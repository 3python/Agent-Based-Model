# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 12:48:38 2017

@author: kate
"""
import random

#Making the agents.
#Making the Agent class.
class Agent():
    #Initialising the agent class.
    def __init__(self, environment, agents, td_xs=None, td_ys=None):
        """Initialise the environment."""           
        self.environment = environment
        self.agents = agents
        self.store = 0
        self.h = len(environment)
        self.w = len(environment[0])
        
        if (td_xs == None):
            self._x = random.randint(0,self.w)        
        else:
            self._x = td_xs
    

        if (td_ys == None):
            self._y = random.randint(0,self.h)
        else:
            self._y = td_ys
    
        
    def eat(self):
        """
        Agents eat the environment.
        
        Returns:
        The z values of the coordinates with the amount the sheep have eaten removed.
        """
        if self.environment[self.y][self.x]>10:
            self.environment[self.y][self.x] -=10
            self.store += 10
    
    #Moving the agents.
    def move(self):
        """
        Move the agents to generate new random positions.
        
        Returns:
        New coordinate positions of the x and y values.
        """
        if random.random() < 0.5:
            self._x = (self._x + 1) % self.w
        else:
            self._x = (self._x - 1) % self.w

        if random.random() < 0.5:
            self._y = (self._y + 1) % self.h
        else:
            self._y = (self._y - 1) % self.h
           
            
    def share_with_neighbours(self, neighbourhood):
        """
        Share stores between agents.
        
        neighbourhood -- the maximum distance between agents where they will still share thier values with oneanother (no default)
        
        Returns:
        Average value eaten between agent and agents within a certain distance of that agent.
        """
        for agent in self.agents:
            dist = self.distance_between(agent) 
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave))

    def distance_between(self, agent):
        """
        Calculate the distance between two agents using pythagoras theorum.
        
        Positional Arguements:
        agent -- an integer value (no default)
        
        Returns:
        The distance between two agents.
        """
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5  
            
        
    #Prints the values created by the agents within programs.
    def __str__(self):
        """
        Take values from the agent class and print them when called.
        
        Returns:
        Values that have been called to print.
        """
        return str(self.x) + " " + str(self.y)   
    
    #Sets up the variable (x) so access can only occur by accessor/mutator methods.
    #Makes the variable read only.
    @property
    def x(self):
        """Make the x coordinate read only."""
        return self._x
    
    #Sets an attribute value for (x).
    @x.setter
    def x(self, value):
        """Set an attribute for the x coordinate."""
        self._x = value
    
    #Gets the attribute value for (x).
    @x.getter
    def x(self):
        """Get the value for the x coordinate."""
        return self._x
    
    #Sets up the variable (y) so access can only occur by accessor/mutator methods.
    #Makes the variable read only.
    @property
    def y(self):
        """Make the y coordinate read only."""
        return self._y
    
    #Sets an attribute value for (y).
    @y.setter
    def y(self, value):
        """Set an attribute for the y coordinate."""
        return self._y
    
    #Gets the attribute value for (y).
    @y.getter
    def y(self):
        """Get the value for the y coordinate."""
        return self._y




        
