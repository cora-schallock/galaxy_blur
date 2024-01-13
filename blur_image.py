import sys
import os
sys.path.append('/galaxy_blur')


import galaxy_blur.plot


common_args = { 
                'add_background':       False,          # default option = False, turn on one-by-one
                'add_noise':            False,
                'add_psf':              False,
                'rebin_phys':           False,
                'resize_rp':            False,
                'rebin_gz':             False,           # always true, all pngs 424x424
                'scale_min':            1e-10,          # was 1e-4  #1e-10
                'lupton_alpha':         2e-12,          # was 1e-4
                'lupton_Q':             10,             # was ~100
                'pixelsize_arcsec':     0.24,
                'psf_fwhm_arcsec':      0.5,
                'sn_limit':             1000,           # super low noise value, dominated by background
                'sky_sig':              None,           #
                'redshift':             0.01,           # the distance k=0...10 no 0
                'b_fac':                1.1, 
                'g_fac':                1.0, 
                'r_fac':                0.9,
                'camera':               1,              #4 camera
                'seed_boost':           1.0,
                'save_fits':            True,
                'verbose':              False,           # 'r_petro_kpc':          7,
                # 'psf_pixsize_arcsec':   2
                # 'r_petro_kpc':          10
                }

sn_list = [8, 16, 32, 64, 128, 256] #64, 32
pixelsize_arcsec = [5, 10, 20, 40] # 80
psf_list = [4.0,4.7,5.6, 6.7, 8.0, 9.5, 11.3, 13.4, 16.0, 19.0, 22.6, 26.9, 32.0, 38.0, 45.2, 53.8, 64.0, 76.1, 90.5, 107.6, 128.0]

def sdss_get_64_image(input_fits_path,output_path):
    for psf in psf_list:
        for sn in sn_list:
            print("in loop")
            common_args['rebin_phys'] = True
            common_args['add_psf'] = True
            common_args['add_noise'] = True
            common_args['psf_fwhm_arcsec'] = psf
            common_args['sn_limit'] = sn
            common_args['pixelsize_arcsec'] = float(psf/3.2)
            print(input_fits_path)
            output_path_full = os.path.join(output_path, 'IC1683_i_psf_'+ str(psf) + 'background_' + str(sn) +'.png')
            galaxy_blur.plot.plot_synthetic_SDSS(input_fits_path, savefile= output_path_full, **common_args)

input_fits_path='C:\\Users\\school\\Desktop\\cross_id\\sdss_mosaic_construction\\table2\\IC1683\\IC1683_i.fits'
output_path='C:\\Users\\school\\Desktop\\IC1683_i'
sdss_get_64_image(input_fits_path,output_path)