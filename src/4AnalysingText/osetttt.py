
import pickle
import os

data_frame_name = "ave_top_20"
# data_frame_name = "ave_worst_20"
# data_frame_name = "2021_top_20"
# data_frame_name = "2021_worst_20"


li = [1,2,3,4]
data_dir = os.getcwd()+  f"/{data_frame_name}"
if not os.path.exists(data_dir) :
  os.mkdir(data_dir)

with open(f"{data_dir}/test", "wb") as fp:
  pickle.dump(li, fp)
# import glob

# def call_sample_dir_name(initial_name):
#     if initial_name == "a":
#         return "AfterSample"
#     elif  initial_name == "t":
#         return "TransitionPeriodSample"
#     else:
#         return "BeforeSample"


# def call_csv_files(sample_dir_name="AfterSample", data_frame_spec=None, industry_spec=None):
    
#     if data_frame_spec is None:
        
#         if industry_spec is None:
#             csv_files = glob.glob('/home/jovyan/3FetchingMDandA' + f"/**/{sample_dir_name}/*.csv", recursive=True)
#         else:
#              csv_files = glob.glob(f'/home/jovyan/3FetchingMDandA' + f"/**/{industry_spec}/{sample_dir_name}/*.csv", recursive=True)
#     else:
#         if industry_spec is None:
#             csv_files = glob.glob(f'/home/jovyan/3FetchingMDandA/{data_frame_spec}' + f"/**/{sample_dir_name}/*.csv", recursive=True)
#         else:
#              csv_files = glob.glob(f"/home/jovyan/3FetchingMDandA/{data_frame_spec}/{industry_spec}/{sample_dir_name}/*.csv", recursive=True)
    
#     return  csv_files

