import sys
import numpy
import scipy
import sklearn
import pandas
import matplotlib
print(f"numpy verdsion={numpy.__version__}")
print("scipy version={}, sklearn={}".format(scipy.__version__,sklearn.__version__))

print(f"pandas version ={pandas.__version__}" )
print("it works at",sys.executable)


import pandas as pd
url1 = 'https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data'
df1 = pd.read_csv(url1, header=None,prefix='X')
