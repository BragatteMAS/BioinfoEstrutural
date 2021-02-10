#ref.:(https://medium.com/free-code-camp/how-to-combine-multiple-csv-files-with-8-lines-of-code-265183e0854)

import os
import glob
import pandas as pd
os.chdir("/mydir")


extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')

