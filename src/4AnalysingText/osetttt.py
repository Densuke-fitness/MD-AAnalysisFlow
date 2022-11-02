import glob
import pandas as pd
import os 
import oseti
import pickle


data_frame_spec = "ave_top_20"
# data_frame_spec = "ave_worst_20"
# data_frame_spec = "2021_top_20"
# data_frame_spec = "2021_worst_20"


def call_sample_dir_name(initial_name):
    if initial_name == "a":
        return "AfterSample"
    elif  initial_name == "t":
        return "TransitionPeriodSample"
    else:
        return "BeforeSample"


def call_csv_files(sample_dir_name="AfterSample", data_frame_spec=None, industry_spec=None):
    
    if data_frame_spec is None:
        
        if industry_spec is None:
            csv_files = glob.glob('/src/3FetchingMDandA' + f"/**/{sample_dir_name}/*.csv", recursive=True)
        else:
             csv_files = glob.glob(f'/src/3FetchingMDandA' + f"/**/{industry_spec}/{sample_dir_name}/*.csv", recursive=True)
    else:
        if industry_spec is None:
            csv_files = glob.glob(f"/src/3FetchingMDandA/{data_frame_spec}/**/{sample_dir_name}/*.csv", recursive=True)
        else:
             csv_files = glob.glob(f"/src/3FetchingMDandA/{data_frame_spec}/{industry_spec}/{sample_dir_name}/*.csv", recursive=True)
    
    return  csv_files
  

analyzer = oseti.Analyzer()
def make_atb_li(atb_file, analyzer):

    atb_df = pd.read_csv(atb_file, index_col=0)
    if len(atb_df) < 1:
        return 0
    texts_joined = "".join(list(atb_df["Text"].values))
    #parse error対策
    texts_joined = texts_joined.replace("\n", "")
    
    scores = analyzer.count_polarity(texts_joined)
    sum_plus = 0
    sum_minus = 0
    for score in scores:
        sum_plus += score["positive"]
        sum_minus += score["negative"]

    ret_val =  (sum_plus - sum_minus)/(sum_plus + sum_minus)
    return ret_val


data_dir = f'/src/4AnalysingText/{data_frame_spec}'
if os.path.isfile(f"{data_dir}/before") and os.path.isfile(f"{data_dir}/transition") and os.path.isfile(f"{data_dir}/after"):
  print("already done.")
else:
  industry_spec=None
  #before
  dir_name_b = call_sample_dir_name("b")
  before_csv_files  = call_csv_files(dir_name_b, data_frame_spec, industry_spec)
  #transition
  dir_name_t = call_sample_dir_name("t")
  transition_period_csv_files = call_csv_files(dir_name_t, data_frame_spec, industry_spec)
  #after
  dir_name_a = call_sample_dir_name("a")
  after_csv_files = call_csv_files(dir_name_a, data_frame_spec, industry_spec)

  print(before_csv_files)
  print(transition_period_csv_files)
  print(after_csv_files)
  print("--------ここまで終わりました1------")


  #cache化して速度向上
  before_li = []
  f = before_li.append

  for b_file in  before_csv_files :
      tmp = make_atb_li(b_file, analyzer) 
      f(tmp)
  print("-------ここまで終わりました2-------")


  transition_period_li = []
  f = transition_period_li.append

  for t_file in  transition_period_csv_files  :
      tmp = make_atb_li(t_file, analyzer) 
      f(tmp)
  print("-------ここまで終わりました3-------")

  after_li = []
  f = after_li.append

  for a_file in  after_csv_files :
      tmp = make_atb_li(a_file, analyzer) 
      f(tmp)
  print("-------ここまで終わりました4-------")



  with open(f"{data_dir}/before", "wb") as fp:
    pickle.dump(before_li, fp)

  with open(f"{data_dir}/transition", "wb") as fp:
    pickle.dump(transition_period_li, fp)

  with open(f"{data_dir}/after", "wb") as fp:
    pickle.dump(after_li, fp)

  print("caluculation finished")