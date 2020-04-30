import smooth
import numpy as np
from datetime import datetime
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import scipy.optimize as opt



df=pd.read_excel("Texas COVID-19 Case Count Data by County.xlsx",header=2)
df=df.set_index("County Name")
cases=np.array(df.loc["Dallas"].values[1:],dtype=np.float64)
my=np.amax(np.diff(cases))

dates=[pd.to_datetime(df.loc["Dallas"].index[i].split("\n")[1]+"-2020") for i in range(1,len(df.loc["Dallas"]))]
dates=list(map(datetime.date,dates))
cases=df.loc["Dallas"].values[1:]
dates=dates[1:]
shelter_in_place=np.where(np.array(dates)==datetime(2020,3,23).date())[0][0]
plt.plot(np.diff(cases),linewidth=3.0)
plt.scatter(shelter_in_place,np.diff(cases)[shelter_in_place],color="orange",s=64)
plt.legend(["Cases per day","Shelter-in-place order"])
plt.title("Cases per day")
plt.xlabel("Days since first case")
plt.ylabel("Cases")
x1,x2,y1,y2 = plt.axis()
plt.axis((x1,x2,0,my))



plt.savefig("dallas_raw.svg")
plt.close()




ys=smooth.epi_smooth_dx(np.diff(cases))
plt.plot(ys,linewidth=3)
plt.scatter(shelter_in_place,ys[shelter_in_place],color="orange",s=64)
plt.legend(["Cases per day","Shelter-in-place order"])
plt.title("Cases per day")
plt.xlabel("Days since first case")
plt.ylabel("Cases")
x1,x2,y1,y2 = plt.axis()
plt.axis((x1,x2,0,my))


plt.savefig("dallas_smoothed.svg")
plt.close()


ys=smooth.moving_average(np.diff(cases))
plt.plot(ys,linewidth=3)
plt.scatter(shelter_in_place,ys[shelter_in_place],color="orange",s=64)
plt.legend(["Cases per day","Shelter-in-place order"])
plt.title("Cases per day")
plt.xlabel("Days since first case")
plt.ylabel("Cases")
x1,x2,y1,y2 = plt.axis()
plt.axis((x1,x2,0,my))


plt.savefig("dallas_moving_average.svg")
