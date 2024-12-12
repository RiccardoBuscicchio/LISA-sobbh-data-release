import numpy as np
import copy
import astropy.units as u
from astropy.cosmology import Planck18
from astropy import constants as const

T = 4 * (1*u.year).to(u.s).value
def replace_numpy_float64(obj):
    obj = copy.deepcopy(obj)
    if isinstance(obj, dict):
        return {key: replace_numpy_float64(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        # If the object is a list, process its elements
        return [replace_numpy_float64(element) for element in obj]
    elif isinstance(obj, np.float64):
        # Replace numpy.float64 with native float
        return float(obj)
    else:
        # For other types, return the object unchanged
        return obj
    
def luminosity_distance_from_redshift(redshift):
    # Define a cosmology with specified parameters
    cosmo = Planck18
    # Calculate the luminosity distance in parsec
    d_L = cosmo.luminosity_distance(redshift)
    return d_L.to(u.pc).value

def fmax_of_fmin(f0, MCf, T):
    # We work in geometrized units, so c=G=1
    # Inputs are:
    # f0: value of the starting frequency of the signal in Hz
    # MCf: value of the chirp mass
    # T: mission duration in seconds
    fSI = f0*u.Hz
    TSI = T*u.s
    MCfSI = MCf*const.M_sun
    fGU = (fSI/const.c).decompose()
    TGU = TSI*const.c
    MCfGU = const.G*MCfSI/const.c**2
    K = 256 * np.pi**(8/3)/5
    ffinalGU = (fGU**(-8/3) - K*MCfGU**(5/3)*TGU)**(-3/8)
    ffinalSI = ffinalGU*const.c
    return ffinalSI.to("Hz").value

def fmin_of_tm(tm, MCf):
    # Inputs are not dimensionful astropy quantities. They are
    # tm: value of the time to coalescence in seconds
    # MCf: value of the chirp mass of the sources in solar masses
    tmSI = tm*u.s
    tmGU = tmSI*const.c
    MCfSI = MCf*const.M_sun
    MCfGU = const.G*MCfSI/const.c**2
    # Compute the frequency of the signal given its merger time
    fminGU = 5**(3/8)/(8*np.pi)*MCfGU**(-5/8)*tmGU**(-3/8)
    # Returns the value of f in Hz
    return (const.c*fminGU).value

def tm_of_fmin(fmin, MCf):
    # Inputs are not dimensionful astropy quantities. They are
    # f0: value of the starting frequency of the signal in Hz
    # MCf: value of the chirp mass of the sources in solar masses
    fminSI = fmin*u.Hz
    fminGU = fminSI/const.c
    MCfSI = MCf*const.M_sun
    MCfGU = const.G*MCfSI/const.c**2
    # Compute the frequency of the signal given its merger time
    tmGU = (5/256)*(fminGU**(-8/3))*(MCfGU**(-5/3))*(np.pi**(-8/3))
    # Returns the value of f in Hz
    return (tmGU/const.c).to("s").value