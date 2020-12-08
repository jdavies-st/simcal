
import os
from jwst.pipeline import Detector1Pipeline
os.environ["MIRAGE_DATA"] = "/ifs/jwst/wit/mirage_data/"
os.environ["CRDS_DATA"] = "/Users/snweke/mirage/crds_cache"
os.environ["CRDS_SERVER_URL"] = "https://jwst-crds.stsci.edu"



catalogs = {'GOODS-S-FIELD': {'point_source':'imaging_example_data/ptsrc_catalog.cat'}}
cosmic_rays = {'library': 'SUNMAX', 'scale':  1.0}
background = 'medium'
roll_angle = pav3
dates = '2022-10-31'
reffile_defaults = 'crds'
verbose = True
output_dir = './imaging_example_data/'
#simdata_output_dir=simdata_output_dir
simulation_dir --> simdata_output_dir
datatype = 'raw'


def test_nircam_imaging():
      # - define a specifc xml_file, pointing_file
     xml_file = 'imaging_example_data/example_imaging_program.xml'
     pointing_file = 'imaging_example_data/example_imaging_program.pointing'
     #call run_yaml_generator() (see function below)
     yfiles = run_yaml_generator(xml_file, pointing_file, catalogs=None, cosmic_rays=None,
                                         background=None, roll_angle=None,
                                         dates='2022-10-31', reffile_defaults = 'crds',
                                         verbose=True, output_dir= './imaging_example_data/',
                                         simulation_dir --> simdata_output_dir,
                                         datatype='raw')

      #1- call create_simulations() (see function below)
      uncal_files = create_simulations(yfiles)
      # run the calwebb_detector1 pipeline
      rate_files = [ ]
      for fname in uncal_files:
          result = Detector1Pipeline.call(fname)
          rate_files.append(result)
          result.save(result.meta.filename +".fits")

      # - run the calwebb_image2 pipeline
      #- compare the rate files to truth files
     #- compare the cal files to truth files

#dates = '2022-10-31'
#reffile_defaults = 'crds'





def run_yaml_generator(xml_file, pointing_file, catalogs=None, cosmic_rays=None,
                                         background=None, roll_angle=None,
                                         dates=None, reffile_defaults = 'crds',
                                         verbose=True, ,
                                         simdata_output_dir=None,
                                         datatype='raw'):
    yam = yaml_generator.SimInput(input_xml=xml_file, pointing_file=pointing_file,
                              catalogs=catalogs, cosmic_rays=cosmic_rays,
                              background=background, roll_angle=pav3,
                              dates=dates, reffile_defaults = 'crds',
                              verbose=True, output_dir= './imaging_example_data/',
                              simulation_dir --> simdata_output_dir




                              datatype=datatype)
    yam.create_inputs()
    yfiles = glob(os.path.join(output_dir,'jw*.yaml'))
    return yfiles






def create_simulations(input_yaml_files):

     for fname in input_yaml_files:
           img_sim = imaging_simulator.ImgSim()
           #img_sim.paramfile = yamlfile
           img_sim.paramfile = fname
           img_sim.create()
    # runs `ImgSim` on the input YAML files
    # return all `_uncal.fits` file
     uncal_files = glob("*_uncal.fits")
    return uncal_files




    # We want try out the test functions

def run_yaml_generator(xml_file):
	"""" This is to Generate Mirage XML files from APT XML files """
	print(f"DEBUG: my file is {xml_file}")



def create_simulations(input_yaml_files):
	""" Create simulations using Mirage """

	pass

def test_nircam_mirage_pipeline():

	file_xml = os.path.join(
		os.path.dirname(__file__), "data/file.xml"
		)

	assert os.path.exists(file_xml)
	create_simulations(["foo", "bar"])
	run_yaml_generator(file_xml)


def test_mirage_pipeline():
	pass
