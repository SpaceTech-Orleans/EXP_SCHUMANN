########################################################
# This file contain functions to be used # in the simulation 
# notebook: schumann_board_simu.ipynb 
# The goal is to gathers here usefull function to make the notebook more readable. 
########################################################
#################### Importations ######################

from xml.sax.handler import feature_external_ges
import numpy as np
########################################################
########################################################



########################################################
#           Signal generation functions
########################################################

#################### sine_generator ####################
'''
@brief: Generate a sine wave with given paramaters
@param: - f,[float]: Frequency of the sine wave in Hz
        - Amp,[float]: Amplitude of the sine wave in V
        - sim_time,[float]: Simulation time in s
        - time_step,[float]: Time between two samples in s
@output: - Signal and time values in a numpy array of shape [len, 2] [[time][signal value]], 
                len is given by int(sim_time/time_step)
'''
def sine_generator(f,Amp,sim_time, time_step):
    # Number of samples
    nb_samples = int(sim_time/time_step)              
    # Signal generation
    signal1 = np.zeros((nb_samples,2))                # Create empty signal
    signal1[:,0] = np.linspace(0,sim_time,nb_samples) # Create time vector                      
    signal1[:,1] = Amp*np.sin(2*np.pi*f*signal1[:,0]) # Generate sine wave

    return signal1


################# Multi_sine_generator #################
'''
@brief: Generate a sum of sine wave with given paramaters.
@param: - sim_time,[float]: Simulation time in s
        - time_step,[float]: Time between two samples in s 
        - freq,[list of float]: Frequencies of the sines wave in Hz
        - Amp,[list of float]: Amplitudes of the sines wave in V
        
@output: - Signal and time values in a numpy array of shape [len, 2] [[time][signal value]], 
                len is given by int(sim_time/time_step)
'''
def multi_sine_generator(freq,Amps,sim_time, time_step):
    # Number of samples
    nb_samples = int(sim_time/time_step)              
    # Signal generation
    signal = np.zeros((nb_samples,2))                # Create empty signal
    signal[:,0] = np.linspace(0,sim_time,nb_samples) # Create time vector                      
    # Sum sines waves
    for i in range(0,len(freq)):
        temp_sine = Amps[i]*np.sin(2*np.pi*freq[i]*signal[:,0]) # Generate sine wave
        signal[:,1]+= temp_sine
    return signal


########################################################
#             Signal processing functions
########################################################

########################################################
'''
@brief: 
@param:         
@output: 
'''
