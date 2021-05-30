import pandas as pd
import os
import glob
import random

current_path = os.getcwd()
csv_files = glob.glob(os.path.join(current_path, "*.csv"))

for f in csv_files:
    file_name, _ = os.path.splitext(f)
    dict_from_csv = pd.read_csv(f, header=None, index_col=0,
                                squeeze=True).to_dict()
    # print(dict_from_csv)
    create_path = os.path.join(current_path, file_name)
    os.mkdir(create_path)
    for id, name in dict_from_csv.items():
        full_filename = os.path.join(create_path,
                                     str(id) + name + "练习作业" + ".mp3")
        file = open(full_filename, "wb")
        file_size = random.randrange(1, 6) * random.randrange(
            1000, 2000) * random.randrange(1000, 2000)
        file.write(os.urandom(file_size))
        file.close()
