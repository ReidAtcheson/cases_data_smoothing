import smooth
import numpy as np
from datetime import datetime
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import scipy.optimize as opt



df=pd.read_csv("global.csv")
cases=np.array(df["Italy"].values,dtype=np.float64)
my=np.amax(np.diff(cases))

plt.plot(np.diff(cases),linewidth=3.0)
plt.legend(["Cases per day"])
plt.title("Cases per day")
plt.xlabel("Days since first case")
plt.ylabel("Cases")
x1,x2,y1,y2 = plt.axis()
plt.axis((x1,x2,0,my))



plt.savefig("italy_raw.svg")
plt.close()




ys=smooth.epi_smooth_dx(np.diff(cases))
plt.plot(ys,linewidth=3)
plt.legend(["Cases per day"])
plt.title("Cases per day")
plt.xlabel("Days since first case")
plt.ylabel("Cases")
x1,x2,y1,y2 = plt.axis()
plt.axis((x1,x2,0,my))


plt.savefig("italy_smoothed.svg")
plt.close()


ys=smooth.moving_average(np.diff(cases))
plt.plot(ys,linewidth=3)
plt.legend(["Cases per day"])
plt.title("Cases per day")
plt.xlabel("Days since first case")
plt.ylabel("Cases")
x1,x2,y1,y2 = plt.axis()
plt.axis((x1,x2,0,my))


plt.savefig("italy_moving_average.svg")
