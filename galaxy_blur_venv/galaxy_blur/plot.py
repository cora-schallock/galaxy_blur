import gc
import numpy as np
import matplotlib.pyplot as plt

import galaxy_blur.synthetic_image as synthetic_image

def plot_synthetic_SDSS(filename, savefile='syn_sdss_gri.png', **kwargs):
    #changed to read sdss
    print("in plot")
    rp, img = return_synthetic_SDSS_img(filename, **kwargs)
    
    my_save_image(img, savefile, save_indiv_bands = None)
    del img
    gc.collect()

def return_synthetic_SDSS_img(filename, 
                lupton_alpha=0.5, lupton_Q=0.5, scale_min=1e-4, 
                                b_fac=0.7, g_fac=1.0, r_fac=1.3,
                seed_boost=1.0,
                r_petro_kpc=None,
                **kwargs):
#changed to read SDSS

    fail_flag=True      # looks for "bad" backgrounds, and tells us to try again
    n_iter = 1
    while(fail_flag and (n_iter < 2)):
        fail_flag=False
        """
        try:
            seed=int(filename[filename.index('broadband_')+10:filename.index('.fits')])*(n_iter)*seed_boost
        except:
            try:
                seed=int(filename[filename.index('.fits')-3:filename.index('.fits')])*(n_iter)*seed_boost
            except:
                seed=1234
        """
        seed = 1234
        n_iter+=1

        # b_image, rp, the_used_seed,this_fail_flag    = sunpy__synthetic_image.build_synthetic_SDSS_image(filename, 'g_SDSS.res', 
        #         seed=seed,
        #         r_petro_kpc=r_petro_kpc, 
        #         fix_seed=False,
        #         **kwargs)
        # if(this_fail_flag):
        #     fail_flag=True

        # g_image, dummy, the_used_seed,this_fail_flag = sunpy__synthetic_image.build_synthetic_SDSS_image(filename, 'r_SDSS.res', 
        #         seed=the_used_seed,
        #         r_petro_kpc=rp,
        #         fix_seed=True, 
        #         **kwargs)
        # if(this_fail_flag):
        #     fail_flag=True

        r_image, rp, the_used_seed, this_fail_flag = synthetic_image.build_synthetic_SDSS_image(filename, 'i_SDSS.res', 
                                seed=seed,
                r_petro_kpc=r_petro_kpc,
                fix_seed=True, 
                **kwargs)
        if(this_fail_flag):
            fail_flag=True

    print("changed for SDSS")
    return rp, r_image

def my_save_image(img, savefile, opt_text=None, top_opt_text=None, full_fov=None, cut_bad_pixels=False, zoom=None, save_indiv_bands=None, **kwargs):
    if img.shape[0] >1:
        n_pixels_save = img.shape[0]
        print(n_pixels_save)
        n_pixels_save = 500


    	# if zoom!=None:
     #        n_pixels_current = img.shape[0]
    	#     center = np.floor(img.shape[0]/(2.0))
    	#     n_pixels_from_center  = np.floor(img.shape[0]/(2.0*zoom))
    	#     img = img[center - n_pixels_from_center:center+n_pixels_from_center, center - n_pixels_from_center:center+n_pixels_from_center]
    	#     print "resized image from "+str(n_pixels_current)+" to "+str(img.shape[0])+" pixels"
    	#     if full_fov!=None:
     #            full_fov /= (1.0*zoom)

    	# if cut_bad_pixels:
     #        cut_index=-1
    	#     print np.mean(img[cut_index:, cut_index:])
    	#     while( np.mean(img[cut_index:, cut_index:]) == 0 ):
    	#         print cut_index
    	#         cut_index -= 1
    	#     img = img[:cut_index,:cut_index]

        fig = plt.figure(figsize=(1,1))
        ax = fig.add_subplot(111)
        imgplot = ax.imshow(img,origin='lower', interpolation='nearest')

        plt.axis('off')

     #    if not opt_text==None:
     #        ax.text(img.shape[0]/2.0, img.shape[0]/2.0, opt_text, ha='center',va='center', color='white', fontsize=4)

     #    if not top_opt_text==None:
     #        ax.text(img.shape[0]/2.0, 0.9*img.shape[0], top_opt_text, ha='center',va='center', color='white', fontsize=4)

    	# if not full_fov==None:
     #        bar_size_in_kpc    = np.round(full_fov/5.0)
    	#     pixel_size_in_kpc  = full_fov / (1.0 * img.shape[0])
    	#     bar_size_in_pixels = bar_size_in_kpc / pixel_size_in_kpc
    	#     center = img.shape[0]/2.0
    	    
    	#     ax.text( center, 0.15 * img.shape[0], str(bar_size_in_kpc)+" kpc", color='w', fontsize=4, ha='center', va='center')
    	#     ax.plot( [center-bar_size_in_pixels/2.0, center+bar_size_in_pixels/2.0] , [0.1*img.shape[0], 0.1*img.shape[0]], lw=2,color='w')
    	#     ax.set_xlim([0,img.shape[0]-1])
    	#     ax.set_ylim([0,img.shape[0]-1])

        fig.subplots_adjust(left=0.0, right=1.0, top=1.0, bottom=0.0)
        # n_pixels_save = 10
        print("n_pixels_save" +str(n_pixels_save))
        # fig.set_size_inches(25.6,25.6)
        fig.savefig(savefile, dpi=n_pixels_save)
        fig.clf()
        plt.close()
        
        if save_indiv_bands:
            print ("in my_save_image")
            print(img.shape)
            for iii in np.arange(3):
                fig = plt.figure(figsize=(1,1))
                ax = fig.add_subplot(111)
                print (img[:,:,iii].min(), img[:,:,iii].max())

                imgplot = ax.imshow(img[:,:,iii],origin='lower', interpolation='nearest', cmap = cm.Greys, vmin=0, vmax=1)
                plt.axis('off')
                fig.subplots_adjust(left=0.0, right=1.0, top=1.0, bottom=0.0)
                print("n_pixels_save" +str(n_pixels_save))
                fig.savefig(savefile+"_band_"+str(iii)+'.png', dpi=n_pixels_save)
                fig.clf()
                plt.close()

        del img
        gc.collect()