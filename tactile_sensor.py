import cv2
import sys
import numpy as np
import math
import matplotlib.pyplot as plt
import time
import sys,os
import threading
from constants import *
from f2gripper import F2Gripper,Preassure
from usbcamera import UsbCamera
from finger import Finger
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image 
from matplotlib.figure import Figure
import io
#from sensor_msgs.msg import Image
#from cv_bridge import CvBridge
#import rospy

PATH=os.path.dirname(os.path.abspath('__file__'))
            
class mainTactileWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        ##Finger initialization
        self.run_threads=True
        self.place_object=False
        self.red=ImageTk.PhotoImage(Image.open('imgs/indicator/red.png').resize((400, 250), Image.Resampling.LANCZOS))
        self.green=ImageTk.PhotoImage(Image.open('imgs/indicator/green.png').resize((400, 250), Image.Resampling.LANCZOS))
        self.orange=ImageTk.PhotoImage(Image.open('imgs/indicator/orange.png').resize((400, 250), Image.Resampling.LANCZOS))
        PAPER_IMG=ImageTk.PhotoImage(Image.open('imgs/instruction/Paper.jpg').resize((500, 250) ,Image.Resampling.LANCZOS))
        FABRICS_IMG=ImageTk.PhotoImage(Image.open('imgs/instruction/Fabrics.jpg').resize((500, 250), Image.Resampling.LANCZOS))
        CUP_IMG=ImageTk.PhotoImage(Image.open('imgs/instruction/Cup.jpg').resize((500, 250), Image.Resampling.LANCZOS))
        DOUGH_IMG=ImageTk.PhotoImage(Image.open('imgs/instruction/Dough.jpg').resize((500, 250), Image.Resampling.LANCZOS))
        STRAWBERRY_IMG=ImageTk.PhotoImage(Image.open('imgs/instruction/Strawberry.jpg').resize((500, 250), Image.Resampling.LANCZOS))
        RASPBERRY_IMG=ImageTk.PhotoImage(Image.open('imgs/instruction/Raspberry.jpg').resize((500, 250), Image.Resampling.LANCZOS))
        USB_IMG=ImageTk.PhotoImage(Image.open('imgs/instruction/USB_cable.jpg').resize((500, 250), Image.Resampling.LANCZOS))
        PRISM_IMG=ImageTk.PhotoImage(Image.open('imgs/instruction/Prism.jpg').resize((500, 250), Image.Resampling.LANCZOS))
        self.PICTURES_OBJECTS= {
        'Paper':PAPER_IMG,
        'Fabrics':FABRICS_IMG,
        'Cup':CUP_IMG,
        'Dough':DOUGH_IMG,
        'Strawberry':STRAWBERRY_IMG,
        'Raspberry':RASPBERRY_IMG,
        'USB_cable':USB_IMG,
        'Prism':PRISM_IMG,
        }
        self.gripper=F2Gripper(GRIPPER_PORT)
        self.preassure=Preassure(ARDUINO_PORT)
        self.sensor = Finger(self.gripper)
        self.current_index=0
        self.current_object_index=0
        self.pump_preassure=0.8
        self.sensor.sensibility_alpha=0.01
        self.gripper_pos=100
        self.indicator="STOP"
        self.OPTIONS_PARAMETERS=parameters_list(OPTIONS[0])
        self.OPTIONS_OBJECTS=object_list(OPTIONS[0], self.current_index)
        self.user_cam= UsbCamera()
        self.wm_title("Tactile sensor framework")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        ######MAIN PANEL
        self.experiment_frame = tk.Frame(self, bd=2)
        ####EXPERIMENT SELECTION PANEL
        self.experiment_frame_select = tk.Frame(self.experiment_frame, bd=2)
        self.experiment_frame_select.grid(row=0, column=0,sticky='w')
        self.experiment_frame_next_before = tk.Frame(self.experiment_frame, bd=2)
        self.experiment_frame_next_before.grid(row=1, column=0,sticky='w')
        self.experiment_setup_label=tk.Label(self.experiment_frame_select,text="Setup panel", font='Helvetica 16 bold')
        self.experiment_setup_label.grid(row=0,column=0,sticky='w')
        self.experiment_name_label=tk.Label(self.experiment_frame_select,text="Select experiment: ")
        self.experiment_name_label.grid(row=1,column=0,sticky='w')
        self.object_name_label=tk.Label(self.experiment_frame_select,text="Set object: ")
        self.object_name_label.grid(row=2,column=0,sticky='w')
        self.object_parameters_label=tk.Label(self.experiment_frame_select,text="Set parameters: ")
        self.object_parameters_label.grid(row=3,column=0,sticky='w')
        self.experiment = tk.StringVar(self)
        self.experiment.set(OPTIONS[0]) # default value
        self.experiment_menu = tk.OptionMenu(self.experiment_frame_select, self.experiment, *OPTIONS,command =self.select_experiment)
        self.experiment_menu.grid(row=1, column=2,sticky='w')
        self.exp_objects = tk.StringVar(self)
        self.exp_objects.set(self.OPTIONS_OBJECTS[self.current_index]) # default value
        self.exp_objects_menu = tk.OptionMenu(self.experiment_frame_select, self.exp_objects, *self.OPTIONS_OBJECTS)
        self.exp_objects_menu.grid(row=2, column=2,sticky='w')
        
        self.exp_params = tk.StringVar(self)
        self.exp_params.set(self.OPTIONS_PARAMETERS[self.current_index]) # default value
        self.exp_objects_menu = tk.OptionMenu(self.experiment_frame_select, self.exp_params, *self.OPTIONS_PARAMETERS)
        self.exp_objects_menu.grid(row=3, column=2,sticky='w')
        
        self.next_button=tk.Button(self.experiment_frame_next_before,  width=22,text="Next config", command=self.next_param)
        self.befor_button=tk.Button(self.experiment_frame_next_before,  width=22, text="Prev config", command=self.prev_param)
        self.next_button.grid(row=1, column=1)
        self.befor_button.grid(row=1, column=0)
        
        self.next_obj_button=tk.Button(self.experiment_frame_next_before,  width=22,text="Next obj", command=self.next_object)
        self.befor_obj_button=tk.Button(self.experiment_frame_next_before,  width=22, text="Prev obj", command=self.prev_object)
        self.next_obj_button.grid(row=0, column=1)
        self.befor_obj_button.grid(row=0, column=0)
        
        ######PUMP CONTROL PANEL###########
        self.control_sensor_frame = tk.Frame(self, bd=2)
        self.pump_setup_label=tk.Label(self.control_sensor_frame,text="Pump control", font='Helvetica 16 bold')
        self.pump_setup_label.grid(row=0, column=0,sticky='w')
        self.info_sensor_frame = tk.Frame(self, bd=2)
        self.pump_info_label=tk.Label(self.info_sensor_frame,text="Info: Device connected on port "+ ARDUINO_PORT)
        self.pump_info_label.grid(row=0, column=0,sticky='w')
        self.on_pump_button=tk.Button(self.control_sensor_frame,  width=12,text="On", command=self.pump_on)
        self.off_pump_button=tk.Button(self.control_sensor_frame,  width=12,text="Off", command=self.pump_off)
        self.set_pump_button=tk.Button(self.control_sensor_frame, width=10, text="Set", command=self.pump_set)
        self.on_pump_button.grid(row=1, column=0,sticky='w')
        self.off_pump_button.grid(row=1, column=1 ,sticky='w')
        self.set_pump_button.grid(row=1, column=2, sticky='w')
        self.pump_preasure_entry = tk.Entry(self.control_sensor_frame, width=5)
        self.pump_preasure_entry.grid(row=1, column=3,sticky='w')
        self.pump_preasure_entry.insert(0,str(self.pump_preassure))
        #######GRIPPER CONTROL PANEL#########
        self.control_gripper_frame = tk.Frame(self, bd=2)
        self.gripper_setup_label=tk.Label(self.control_gripper_frame,text="Gripper control", font='Helvetica 16 bold')
        self.gripper_setup_label.grid(row=0, column=0,sticky='w')
        self.open_gripper_button=tk.Button(self.control_gripper_frame, width=10,text="Open", command=self.open_gripper)
        self.close_gripper_button=tk.Button(self.control_gripper_frame, width=10, text="Close", command=self.close_gripper)
        self.set_gripper_button=tk.Button(self.control_gripper_frame, width=10, text="Set", command=self.set_gripper)
        self.init_gripper_button=tk.Button(self.control_gripper_frame, width=26 ,text="Init", command=self.init_gripper)
        self.reset_gripper_button=tk.Button(self.control_gripper_frame, width=26,text="Reset", command=self.reset_gripper)
        self.init_gripper_button.grid(row=1, column=0, sticky='w')
        self.reset_gripper_button.grid(row=2, column=0,sticky='w')
        self.open_gripper_button.grid(row=1, column=1,sticky='w')
        self.close_gripper_button.grid(row=1, column=2,sticky='w')
        self.set_gripper_button.grid(row=2, column=1,sticky='w')
        self.gripper_pos_entry = tk.Entry(self.control_gripper_frame, width=12, text=str(self.gripper_pos))
        self.gripper_pos_entry.grid(row=2, column=2,sticky='w')
        ######CAMERA VIEW PANEL##############
        self.camera_view_frame = tk.Frame(self, bd=2)
        self.camera_view_rgb = ImageTk.PhotoImage(Image.fromarray(self.sensor.rgb_image))
        self.camera_view_rgb_label = tk.Label(self.camera_view_frame, image=self.camera_view_rgb)
        self.camera_view_rgb_label.image = self.camera_view_rgb
        self.camera_view_rgb_label.grid(row=0, column=0)
        self.camera_view_dot = ImageTk.PhotoImage(Image.fromarray(self.sensor.dot_tracking_img))
        self.camera_view_dot_label = tk.Label(self.camera_view_frame, image=self.camera_view_rgb)
        self.camera_view_dot_label.image = self.camera_view_dot
        self.camera_view_dot_label.grid(row=1, column=0)
        self.camera_view_user = ImageTk.PhotoImage(Image.fromarray(self.user_cam.rgb_image))
        self.camera_view_user_label = tk.Label(self.camera_view_frame, image=self.camera_view_rgb)
        self.camera_view_user_label.image = self.camera_view_user
        self.camera_view_user_label.grid(row=0, column=1)
        ###Experiment control panel
        self.control_experiment_frame = tk.Frame(self.camera_view_frame, bd=2)
        self.start_exp_button=tk.Button(self.control_experiment_frame , width=25, text="Start", command=self.start_experiment)
        self.stop_exp_button=tk.Button(self.control_experiment_frame, width= 25, text="Stop", command=self.stop_experiment)
        self.place_exp_button=tk.Button(self.control_experiment_frame, width= 25, text="Place object indicator", command=self.place_experiment)
        self.start_exp_button.grid(row=0, column=1,sticky='w')
        self.stop_exp_button.grid(row=1, column=1,sticky='w')
        self.place_exp_button.grid(row=2, column=1,sticky='w')
        self.control_experiment_frame.grid(row=1, column=1,sticky='w')
        #####USER INSTRRUCTIONS PANEL PANEL#######################
        self.instructions_frame=tk.Frame(self, relief=tk.RAISED, bd=2)
        self.instructions_indicator_img=self.red
        self.instructions_indicator_label = tk.Label(self.instructions_frame, image=self.instructions_indicator_img)
        self.instructions_indicator_label.image=self.instructions_indicator_img
        self.instructions_indicator_label.grid(row=0, column=1)
        
        self.name_indicator_label = tk.Label(self.instructions_frame, text="Raspberry", font='Helvetica 26 bold')
        self.name_indicator_label.grid(row=1, column=0)

        self.ins_indicator_img=self.PICTURES_OBJECTS['Paper']
        self.ins_indicator_label = tk.Label(self.instructions_frame, image=self.ins_indicator_img)
        self.ins_indicator_label.image=self.ins_indicator_img
        self.ins_indicator_label.grid(row=0, column=0)
        #####PLOT PANEL#######################
        self.plot_frame=tk.Frame(self, relief=tk.RAISED, bd=2)
        self.plot_view_rgb = ImageTk.PhotoImage(Image.fromarray(self.sensor.plot_image))
        self.plot_view_rgb_label = tk.Label(self.plot_frame, image=self.plot_view_rgb)
        self.plot_view_rgb_label.image = self.camera_view_rgb
        self.plot_view_rgb_label.grid(row=0, column=0)
        ######MAIN PANEL ARRENGING############
        self.experiment_frame.grid(row=0, column=0, sticky='w')
        self.control_sensor_frame.grid(row=1, column=0, sticky='w')
        self.control_gripper_frame.grid(row=2, column=0, sticky='w')
        self.camera_view_frame.grid(row=3, column=0, sticky='w')
        self.plot_frame.grid(row=3, column=1, sticky='w')
        self.instructions_frame.grid(row=0, column=1, sticky='w')
        self.info_sensor_frame.grid(row=4, column=0,sticky='w')
        ##VIEW CAMERAS THREADS################
        self.cam_1 = threading.Thread(target=self.cam_view_rgb)
        self.cam_1.start()
        self.cam_2 = threading.Thread(target=self.cam_view_dot)
        self.cam_2.start()
        self.cam_3 = threading.Thread(target=self.cam_view_user)
        self.cam_3.start()
        self.plot = threading.Thread(target=self.plot_data)
        self.plot.start()
        ###NOT STARTED THREADS PHOTOS####
        self.photo_hadingover = threading.Thread(target=self.save_img_hadingover)
        self.photo_shaking = threading.Thread(target=self.save_img_shaking)
        #################################
        self.user_light = threading.Thread(target=self.user_indicator_gui)
        self.user_light.start()
        self.set_exp_object()
    def save_img_pre_holding(self):
        
        ID=str(self.current_index)+"_"+str(self.current_object_index)+"_"+str(self.exp_params.get())+"_"+str(self.exp_objects.get())
        PATH_MAIN=self.experiment.get()
        filename=PATH+"/RESULTS/"+ PATH_MAIN +"/placing_object/pre_holding_"+ID+".jpg"
        #print("Saving image to "+ filename)
        cv2.imwrite(filename, self.user_cam.rgb_image)
        ###
        time.sleep(2)
        filename=PATH+"/RESULTS/"+ PATH_MAIN +"/filtered_img/filtered_holding_"+ID+".jpg"
        #print("Saving image to "+ filename)
        cv2.imwrite(filename, self.sensor.dot_tracking_img)
        
        filename=PATH+"/RESULTS/"+ PATH_MAIN +"/real_img/cam_img_holding_"+ID+".jpg"
        #print("Saving image to "+ filename)
        cv2.imwrite(filename, self.sensor.rgb_image)
    def save_img_shaking(self):
        while self.run_threads:
            if self.sensor.gripper_state==1:
                #print("Saving shaking image")
                ID=str(self.current_index)+"_"+str(self.current_object_index)+"_"+str(self.exp_params.get())+"_"+str(self.exp_objects.get())
                PATH_MAIN=self.experiment.get()
                filename=PATH+"/RESULTS/"+ PATH_MAIN +"/gripper_holding_img/shaking_"+ID+".jpg"
                cv2.imwrite(filename, self.user_cam.rgb_image)
                return
            time.sleep(0.3)
        
    def save_img_hadingover(self):
        while self.run_threads:
            if self.sensor.gripper_open:
                time.sleep(0.4)
                ID=str(self.current_index)+"_"+str(self.current_object_index)+"_"+str(self.exp_params.get())+"_"+str(self.exp_objects.get())
                PATH_MAIN=self.experiment.get()
                filename=PATH+"/RESULTS/"+ PATH_MAIN +"/gripper_hading_over_img/releasing_"+ID+".jpg"
                cv2.imwrite(filename, self.user_cam.rgb_image)
                return
            time.sleep(0.3)
        
    def save_plot(self):
        ID=str(self.current_index)+"_"+str(self.current_object_index)+"_"+str(self.exp_params.get())+"_"+str(self.exp_objects.get())
        PATH_MAIN=self.experiment.get()
        filename=PATH+"/RESULTS/"+ PATH_MAIN +"/plot/plot_"+ID+".jpg"
        print("Saving image to "+ filename)
        plot_img=cv2.cvtColor(self.sensor.plot_image.copy(), cv2.COLOR_RGB2BGR)
        cv2.imwrite(filename, plot_img)
        
        ##save plot
        background_img=np.zeros([420,920,3],dtype=np.uint8)
        background_img.fill(255)
        start_img=resize(cv2.imread(PATH+"/RESULTS/"+ PATH_MAIN +"/placing_object/pre_holding_"+ID+".jpg"),50)
        texture_img=resize(cv2.imread(PATH+"/RESULTS/"+ PATH_MAIN +"/real_img/cam_img_holding_"+ID+".jpg"),50)
        shaking_img=resize(cv2.imread(PATH+"/RESULTS/"+ PATH_MAIN +"/gripper_holding_img/shaking_"+ID+".jpg"),50)
        end_img=resize(cv2.imread(PATH+"/RESULTS/"+ PATH_MAIN +"/gripper_hading_over_img/releasing_"+ID+".jpg"),50)
        
        x_offset=0
        y_offset=0
        background_img[y_offset:y_offset+plot_img.shape[0], x_offset:x_offset+plot_img.shape[1]] = plot_img.copy()
        x_offset=135
        y_offset=220
        background_img[y_offset:y_offset+end_img.shape[0], x_offset:x_offset+end_img.shape[1]] = start_img.copy()
        
        x_offset=315
        y_offset=220
        background_img[y_offset:y_offset+texture_img.shape[0], x_offset:x_offset+texture_img.shape[1]] = texture_img.copy()
        x_offset=485
        y_offset=220
        background_img[y_offset:y_offset+shaking_img.shape[0], x_offset:x_offset+shaking_img.shape[1]] = shaking_img.copy()
        x_offset=655
        y_offset=220
        background_img[y_offset:y_offset+end_img.shape[0], x_offset:x_offset+end_img.shape[1]] = end_img.copy()
        #background_img[y_offset:y_offset+start_img.shape[0], x_offset:x_offset+start_img.shape[1]] = start_img.copy()
        ## add pictures to plot
        filename=PATH+"/RESULTS/"+ PATH_MAIN +"/plot/fullplot_"+ID+".jpg"
        cv2.imwrite(filename,  background_img)
        #cv2.imshow('Blended Image',background_img)
        del start_img
        del texture_img
        del shaking_img
        del end_img
        del background_img
        return
    def start_experiment(self):
        self.sensor.start=True
        self.sensor.gripper_open=False
        self.place_object=False
        self.set_gripper()
        self.save_img_pre_holding()
        self.photo_hadingover.start()
        self.photo_shaking.start()
        #set red screen
        self.pump_info_label.config(text = "Info: Starting experiment")
    def stop_experiment(self):
        self.pump_info_label.config(text = "Info: Stoping experiment")
        self.photo_shaking.join()
        self.photo_hadingover.join()
        self.sensor.start=False
        self.sensor.ready_to_handover=False
        self.pump_off()
        self.instructions_indicator_label.configure(image=self.red)
        del self.photo_shaking
        del self.photo_hadingover
        self.photo_hadingover = threading.Thread(target=self.save_img_hadingover)
        self.photo_shaking = threading.Thread(target=self.save_img_shaking)
        self.save_plot()
        
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.stop_threads()
            time.sleep(3)
            self.cam_1.join()
            self.cam_2.join()
            self.cam_3.join()
            self.plot.join()
            self.user_light.join()
            self.close_ports()
            self.destroy()
    def select_obects(self,event):#TODO fix bug about selecting and object differing from its index
        self.set_exp_object()
    def select_parameters(self,event):#TODO fix bug about selecting a set of parameters differing from their index
        self.set_exp_object()
    def select_experiment(self,event):
        self.current_object_index=0
        self.current_index=0
        self.OPTIONS_PARAMETERS=parameters_list(self.experiment.get())
        self.OPTIONS_OBJECTS=object_list(self.experiment.get(), self.current_index)
        self.exp_objects.set(self.OPTIONS_OBJECTS[self.current_index]) # default value
        self.exp_objects_menu = tk.OptionMenu(self.experiment_frame_select, self.exp_objects, *self.OPTIONS_OBJECTS)
        self.exp_params.set(self.OPTIONS_PARAMETERS[self.current_index]) # default value
        self.exp_objects_menu = tk.OptionMenu(self.experiment_frame_select, self.exp_params, *self.OPTIONS_PARAMETERS)
        #self.exp_objects_menu.grid(row=3, column=2,sticky='w')
        self.set_exp_object()
    def user_indicator_gui(self):
        while self.run_threads:
            if self.sensor.ready_to_handover and not self.sensor.gripper_open:
                time.sleep(5)
                self.instructions_indicator_label.configure(image=self.green)
            elif not self.place_object:
                self.instructions_indicator_label.configure(image=self.red)
            else:
                self.instructions_indicator_label.configure(image=self.orange)
            time.sleep(0.5)
    def stop_threads(self):
        self.run_threads=False
        self.sensor.run_threads=False
        self.sensor.run_threads=False
        self.user_cam.run_threads=False
    def close_ports(self):
        self.preassure.close()
    def place_experiment(self):
        self.place_object=True
        time.sleep(0.5)
        self.open_gripper()
        self.pump_set()
        time.sleep(1.2)
        self.pump_on()
        time.sleep(1.2)

    def next_param(self):
        self.current_object_index=0
        self.current_index=(self.current_index + 1)%9
        self.exp_params.set(self.OPTIONS_PARAMETERS[self.current_index])
        self.OPTIONS_OBJECTS=object_list(self.experiment.get(), self.current_index)
        self.exp_objects.set(self.OPTIONS_OBJECTS[self.current_object_index]) # default value
        self.exp_objects_menu = tk.OptionMenu(self.experiment_frame_select, self.exp_objects, *self.OPTIONS_OBJECTS)
        self.set_exp_object()
    def prev_param(self):
        self.current_object_index=0
        self.current_index=(self.current_index - 1)%9
        self.exp_params.set(self.OPTIONS_PARAMETERS[self.current_index])
        self.OPTIONS_OBJECTS=object_list(self.experiment.get(), self.current_index)
        self.exp_objects.set(self.OPTIONS_OBJECTS[self.current_object_index]) # default value
        self.exp_objects_menu = tk.OptionMenu(self.experiment_frame_select, self.exp_objects, *self.OPTIONS_OBJECTS)
        self.set_exp_object()
    def next_object(self):
        self.current_object_index=(self.current_object_index + 1)%8
        #self.OPTIONS_OBJECTS=object_list(self.experiment.get(), self.current_object_index)
        self.exp_objects.set(self.OPTIONS_OBJECTS[ self.current_object_index]) # default value
        self.set_exp_object()
    def prev_object(self):
        self.current_object_index=(self.current_object_index - 1)%8
        #self.OPTIONS_OBJECTS=object_list(self.experiment.get(), self.current_object_index)
        self.exp_objects.set(self.OPTIONS_OBJECTS[ self.current_object_index]) # default value
        self.set_exp_object()
    def set_exp_object(self):
        self.sensor.gripper_open=True
        self.name_indicator_label.config(text = self.exp_objects.get(), font='Helvetica 26 bold')
        self.sensor.sensibility_alpha=EXPERIMENTAL_SETUPS[self.exp_params.get()][0]
        self.pump_preassure=EXPERIMENTAL_SETUPS[self.exp_params.get()][1]
        self.gripper_pos=OPENING_OBJECTS[self.exp_objects.get()]
        self.pump_preasure_entry.delete(0, END)
        self.pump_preasure_entry.insert(0,str(self.pump_preassure))
        self.gripper_pos_entry.delete(0, END)
        self.gripper_pos_entry.insert(0,str(self.gripper_pos))
        self.ins_indicator_label.configure(image=self.PICTURES_OBJECTS[self.exp_objects.get()])
        self.pump_info_label.config(text = "Info: ||" +self.experiment.get()+"|| ID="+str(self.current_index)+"_"+str(self.current_object_index)+"_"+str(self.exp_params.get())+"_"+str(self.exp_objects.get())+" || P = "+str(self.pump_preassure)+" || S = "+str(self.sensor.sensibility_alpha)+ "|| "+str(self.sensor.avg_time)+ " ms")
    def plot_data(self):
        while self.run_threads:
            img=ImageTk.PhotoImage(Image.fromarray(self.sensor.plot_image))
            self.plot_view_rgb_label.configure(image=img)
            self.plot_view_rgb_label.image = img
            time.sleep(0.2)
        return
    def cam_view_user(self):
        while self.run_threads:
            img=ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(resize(self.user_cam.rgb_image,50), cv2.COLOR_BGR2RGB)))
            self.camera_view_user_label.configure(image=img)
            self.camera_view_user_label.image = img
            time.sleep(0.2)
        return
    def cam_view_dot(self):
        while self.run_threads:
            img=ImageTk.PhotoImage(Image.fromarray(resize(self.sensor.dot_tracking_img,50)))
            self.camera_view_dot_label.configure(image=img)
            self.camera_view_dot_label.image = img
            time.sleep(0.2)
        return
    def cam_view_rgb(self):
        while self.run_threads:
            img=ImageTk.PhotoImage(Image.fromarray(resize(self.sensor.rgb_image,50)))
            self.camera_view_rgb_label.configure(image=img)
            self.camera_view_rgb_label.image = img
            time.sleep(0.1)
        return
    def pump_on(self):
        self.preassure.write("ON")
        self.pump_info_label.config(text = "Info: Pump on")
    def pump_off(self):
        self.preassure.write("OFF")
        self.pump_info_label.config(text = "Info: Pump off")
    def pump_set(self):
        try:
            data=self.pump_preasure_entry.get()
            if float(data)<MIN_PREASSURE:
                data=0.0
            if float(data)>MAX_PREASSURE:
                data=1.5
            self.preassure.set_preasure(round(float(data),1))
            answer="Info: Preassure set to "+str(data)+ " psi"
        except Exception as e:
            print(e)
            answer="Error: not valid input"
        self.pump_info_label.config(text = answer)
    def reset_gripper(self):
        self.gripper.reset_gripper()
        self.pump_info_label.config(text = "Info: Reseting gripper")
    def init_gripper(self):
        self.gripper.activate_gripper()
        self.pump_info_label.config(text = "Info: Initilizing gripper")
    def open_gripper(self):
        self.sensor.gripper_open=True
        self.gripper.move(20)
        self.indicator="PUT"
        self.pump_info_label.config(text = "Info: Gripper open")
    def close_gripper(self):
        self.sensor.gripper_open=False
        self.gripper.move(120)
        self.pump_info_label.config(text = "Info: Gripper closed")
    def set_gripper(self):
        try:
            data=self.gripper_pos_entry.get()
            if float(data)<MAX_GRIPPER:
                data=MAX_GRIPPER
            if float(data)>MIN_GRIPPER:
                data=MIN_GRIPPER
            self.gripper.move(int(data))
            answer="Info: Instruction sent to gripper"
            self.sensor.gripper_open=False
        except:
            answer="Error: not valid input"
        self.pump_info_label.config(text = answer)

if __name__ == '__main__':
    TactileGUI = mainTactileWindow()
    TactileGUI.mainloop()
