#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 18:59:46 2018
This user-module defines the functions that animate and plot both the ring world and projectile trajectories.
@author: T.Yoo
"""
import math as mp
import numpy as np
from vpython import *
import vpython as vp
import matplotlib.pyplot as py
def ring_animation(radius_z,omega_z):
    c = vp.canvas() #defines canvas
    earth_radius = 6.371e6 #defines radius of earth
    angles = [] #stores angles so the rotating spheres on the ring can update their positions.
    for rads in np.linspace(0,2*mp.pi,11): #appends angles into the angles list.
        angles.append(rads)
    period = (2*mp.pi)/omega_z #defines the period
    #creates the earth sphere
    earth = vp.sphere(pos=vp.vector(0,0,-1.01*earth_radius), radius=earth_radius, canvas=c, color = vp.color.blue)
    #creates the ring
    ring_ani = vp.ring(pos=vp.vector(0,0,0),axis = vp.vector(0,0,1), radius=radius_z, canvas=c, thickness = radius_z*0.01 , color = color.white)
    #The following variables create the 10 spheres that rotate with the ring to represent rotation.
    zero_ani = vp.sphere(pos=vp.vector(radius_z*mp.cos(angles[0]),radius_z*mp.sin(angles[0]),0), radius=radius_z*0.05, canvas=c, color = color.yellow)
    one_ani = vp.sphere(pos=vp.vector(radius_z*mp.cos(angles[1]),radius_z*mp.sin(angles[1]),0), radius=radius_z*0.05, canvas=c, color = color.blue)
    two_ani = vp.sphere(pos=vp.vector(radius_z*mp.cos(angles[2]),radius_z*mp.sin(angles[2]),0), radius=radius_z*0.05, canvas=c, color = color.yellow)    
    three_ani = vp.sphere(pos=vp.vector(radius_z*mp.cos(angles[3]),radius_z*mp.sin(angles[3]),0), radius=radius_z*0.05, canvas=c, color = color.blue)
    four_ani = vp.sphere(pos=vp.vector(radius_z*mp.cos(angles[4]),radius_z*mp.sin(angles[4]),0), radius=radius_z*0.05, canvas=c, color = color.yellow)
    five_ani = vp.sphere(pos=vp.vector(radius_z*mp.cos(angles[5]),radius_z*mp.sin(angles[5]),0), radius=radius_z*0.05, canvas=c, color = color.blue)
    six_ani = vp.sphere(pos=vp.vector(radius_z*mp.cos(angles[6]),radius_z*mp.sin(angles[6]),0), radius=radius_z*0.05, canvas=c, color = color.yellow)
    seven_ani = vp.sphere(pos=vp.vector(radius_z*mp.cos(angles[7]),radius_z*mp.sin(angles[7]),0), radius=radius_z*0.05, canvas=c, color = color.blue)
    eight_ani = vp.sphere(pos=vp.vector(radius_z*mp.cos(angles[8]),radius_z*mp.sin(angles[8]),0), radius=radius_z*0.05, canvas=c, color = color.yellow)
    nine_ani = vp.sphere(pos=vp.vector(radius_z*mp.cos(angles[9]),radius_z*mp.sin(angles[9]),0), radius=radius_z*0.05, canvas=c, color = color.blue)
    #Sets a pointer
    pointer = arrow(pos=vp.vector(0,0,0),axis=vp.vector(radius_z,0,0), shaftwidth=1)
    #Labels Distance
    distance = label(pos=vp.vector(float(radius_z)/2,float(radius_z)*0.2,0), text='Radius = '+str(radius_z)+"m")
    #Labels angular velocity
    ang_vel = label(pos=vp.vector(0,-float(radius_z)*0.5,0), text='Omega = '+str(omega_z)+"rad/s")
    for time in np.arange(0,100000,1): #This for loop updates the positions of the spheres to create "rotation".
        rate(5)
        zero_ani_x = (radius_z)*mp.cos(((2*mp.pi*time)/period)+angles[0])#updates x position
        zero_ani_y = (radius_z)*mp.sin(((2*mp.pi*time)/period)+angles[0])#updates y position
        zero_ani.pos = vp.vector(zero_ani_x,zero_ani_y,0)
        one_ani_x = (radius_z)*mp.cos(((2*mp.pi*time)/period)+angles[1])
        one_ani_y = (radius_z)*mp.sin(((2*mp.pi*time)/period)+angles[1])
        one_ani.pos = vp.vector(one_ani_x,one_ani_y,0)
        two_ani_x = (radius_z)*mp.cos(((2*mp.pi*time)/period)+angles[2])
        two_ani_y = (radius_z)*mp.sin(((2*mp.pi*time)/period)+angles[2])
        two_ani.pos = vp.vector(two_ani_x,two_ani_y,0)
        three_ani_x = (radius_z)*mp.cos(((2*mp.pi*time)/period)+angles[3])
        three_ani_y = (radius_z)*mp.sin(((2*mp.pi*time)/period)+angles[3])
        three_ani.pos = vp.vector(three_ani_x,three_ani_y,0)
        four_ani_x = (radius_z)*mp.cos(((2*mp.pi*time)/period)+angles[4])
        four_ani_y = (radius_z)*mp.sin(((2*mp.pi*time)/period)+angles[4])
        four_ani.pos = vp.vector(four_ani_x,four_ani_y,0)
        five_ani_x = (radius_z)*mp.cos(((2*mp.pi*time)/period)+angles[5])
        five_ani_y = (radius_z)*mp.sin(((2*mp.pi*time)/period)+angles[5])
        five_ani.pos = vp.vector(five_ani_x,five_ani_y,0)
        six_ani_x = (radius_z)*mp.cos(((2*mp.pi*time)/period)+angles[6])
        six_ani_y = (radius_z)*mp.sin(((2*mp.pi*time)/period)+angles[6])
        six_ani.pos = vp.vector(six_ani_x,six_ani_y,0)
        seven_ani_x = (radius_z)*mp.cos(((2*mp.pi*time)/period)+angles[7])
        seven_ani_y = (radius_z)*mp.sin(((2*mp.pi*time)/period)+angles[7])
        seven_ani.pos = vp.vector(seven_ani_x,seven_ani_y,0)
        eight_ani_x = (radius_z)*mp.cos(((2*mp.pi*time)/period)+angles[8])
        eight_ani_y = (radius_z)*mp.sin(((2*mp.pi*time)/period)+angles[8])
        eight_ani.pos = vp.vector(eight_ani_x,eight_ani_y,0)
        nine_ani_x = (radius_z)*mp.cos(((2*mp.pi*time)/period)+angles[9])
        nine_ani_y = (radius_z)*mp.sin(((2*mp.pi*time)/period)+angles[9])
        nine_ani.pos = vp.vector(nine_ani_x,nine_ani_y,0)
def gravity_calc(radius_a, omega_a):#calculates gravity from given radius and omega
    return (float(radius_a)*float(omega_a)**2)/9.8
def radius_calc(gravity_a,omega_a1):#calculates radius from given gravity and omega
    return (float(gravity_a)*9.8)/float(omega_a1)**2
def omega_calc(gravity_a1,radius_a1):#calculates angular velocity from given radius and gravity
    return np.sqrt((float(gravity_a1)*9.8)/float(radius_a1))
def plot_throw(radius,omega,added_v,launch_angle, spin_direction):#plots throw
    r = float(radius)
    w = float(omega)
    height = r*(3/5)
    v_x = w*(height) #tagential velocity of ring
    new_x_ball = []#stores x positions of object
    new_y_ball = []#stores y positions of object
    an = np.linspace(0, 2*np.pi, 100) #sets up circle on plots
    ball_length = 0
    time = 0
    added_v_x = added_v*np.cos(mp.radians(launch_angle))
    added_v_y = added_v*np.sin(mp.radians(launch_angle))
    while ball_length < r:
        #outside frame
        ball_x = v_x*time+(spin_direction)*(added_v_x*time) # "+" spinward, "-" anti
        ball_y = added_v_y*time-height
        #inside frame
        ball_length = mp.sqrt(ball_x**2+ball_y**2)
        new_x_ball.append(ball_x*mp.cos(w*time)+ball_y*mp.sin(w*time))
        new_y_ball.append(-ball_x*mp.sin(w*time)+ball_y*mp.cos(w*time))
        time+=0.1
    py.plot(r*np.cos(an), r*np.sin(an)) #plots circle to represent ring
    #print(new_x_ball)
    #print(new_y_ball)
    py.axis('equal')
    py.title("Projectile Motion in Rotating Reference Frame")
    py.xlabel("Position (x)")
    py.ylabel("Position (y)")
    py.plot(new_x_ball,new_y_ball)
def throw_animation(radius_ring, omega_ring, added_v_throw, angle_throw, spinward): #creates the projectile motion animation
    c = vp.canvas()
    period = (2*mp.pi)/omega_ring
    height = radius_ring*(3/5)
    ball_length = 0
    v_x = omega_ring*(height) 
    time = 0
    ring_ani = vp.ring(pos=vp.vector(0,0,0),axis = vp.vector(0,0,1), radius=radius_ring, canvas=c, thickness = radius_ring*0.01 , color = color.white)
    zero_ani = vp.sphere(pos=vp.vector(0,-height,0), radius=radius_ring*0.05, canvas=c, color = color.yellow, make_trail=True)
    added_v_x = added_v_throw*np.cos(mp.radians(angle_throw))
    added_v_y = added_v_throw*np.sin(mp.radians(angle_throw))
    while ball_length < 1.50*radius_ring: #animates the ball until the distance between ball and center is equal to radius, as lines 129-131 reset the animation.
        #
        ball_x = v_x*time+(spinward)*(added_v_x*time) # "+" spinward, "-" anti
        ball_y = added_v_y*time-height
        rate(20)
        zero_ani_x = ball_x*mp.cos(omega_ring*time)+ball_y*mp.sin(omega_ring*time)
        zero_ani_y = -ball_x*mp.sin(omega_ring*time)+ball_y*mp.cos(omega_ring*time)
        zero_ani.pos = vp.vector(zero_ani_x,zero_ani_y,0)
        ball_length = mp.sqrt(ball_x**2+ball_y**2)
        time += 0.1
        if ball_length > radius_ring:
            zero_ani.make_trail=False
            time = 0