import os

from blur_image import sdss_get_64_image

#dirs = ['table2','table4']
dirs = ['table2','table4'] #done 3 and 5
sdss_bands =  ['u','g','r','i','z']
input_folder = "C:\\Users\\school\\Desktop\\cross_id\\sdss_mosaic_construction\\"

for table_name in dirs:
    for gal_name in os.listdir(os.path.join(input_folder,table_name)):
        for file_name in os.listdir(os.path.join(input_folder,table_name,gal_name)):
            if not file_name.endswith(".fits"): continue

            full_fits_path = os.path.join(os.path.join(input_folder,table_name,gal_name,file_name))
            band_label = file_name.replace(".","_").split("_")[1]
            try:
                sdss_get_64_image(input_fits_path=full_fits_path,output_path='',band_label=band_label, dir_name=table_name)
            except Exception as e:
                print(e)
            #break
        #break
    #break