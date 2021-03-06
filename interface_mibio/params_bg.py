import pathlib

mibio_path =                        pathlib.Path('/path/to/mibio/executable')
mibio_helper_files_dir_path =       pathlib.Path('/usually__~/.mibio')           

data_path =                         pathlib.Path('/path/to/data')
xml_path =                          data_path.joinpath('slide.xml')
panel_path =                        data_path.joinpath('panel.csv')     
fovs =                              [1,2,3,5,8,13] 

fov_size =                          500                         
remove_slide_bg =                   True 
recalibrate_mass =                  False                       

config_file_path =                  mibio_helper_files_dir_path.joinpath('mibio_config.json')                                   
log_file_path =                     mibio_helper_files_dir_path.joinpath('mibio.log')                                       

# best to set output_file_name to last FOV in array
output_file_name =                  f'Point{fovs[-1]}_RowNumber0_Depth_Profile0.tiff'            
output_tiff_path =                  xml_path.parent.joinpath(xml_path.stem).joinpath(str(xml_path.stem) + '_TIFF')  
output_file_path =                  output_tiff_path.joinpath(output_file_name)                                     

# good parameter set: {ev: 1000000, au: 50, ta: 20}
use_default_slide_bg_removal_pars = False                                                           
bg_thresholds_ev =                  [0,20,50,70,1000000] if not use_default_slide_bg_removal_pars else [0.2]   
bg_thresholds_au =                  [0,25,50,75,100] if not use_default_slide_bg_removal_pars else [50]         
bg_thresholds_ta =                  [0,10,20,30,40] if not use_default_slide_bg_removal_pars else [20]         
bg_removal_types =                  ['events', 'Au', 'Ta']                                                    

# safe timeouts around 180 times the number of fovs
timeout_sec =                       180*len(fovs)
n_trials =                          3                           
