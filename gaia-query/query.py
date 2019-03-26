#!usr/#!/usr/bin/env python

from astroquery.gaia import Gaia
from astropy.coordinates import SkyCoord
import astropy.units as u
import k2plr
client = k2plr.API()

def get_ra_dec_mag(epicnum,verbose=False):
    '''
    get ra, dec, and mag using `k2plr`
    '''
    if verbose:
        print('\nquerying RA and DEC...\n')
    epic = client.k2_star(int(epicnum))
    ra  = float(epic.k2_ra)
    dec = float(epic.k2_dec)
    mag = float(epic.kp)
    return ra, dec, mag

def query_gaia(ra, dec, rad):
    coord = SkyCoord(ra=ra, dec=dec, unit=(u.degree, u.degree), frame='icrs')
#     width = u.Quantity(20, u.arcsec)
#     height = u.Quantity(20, u.arcsec)
#     tab = Gaia.query_object_async(coordinate=coord, width=width, height=height)
    radius = u.Quantity(rad, u.arcsec)
    tab = Gaia.query_object_async(coordinate=coord, radius=radius)
    return tab.to_pandas()