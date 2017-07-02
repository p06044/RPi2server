import pandas as pd
import datetime
import matplotlib.pyplot as plt
def get_csv():
 fx = pd.read_csv("fx.csv", header=None)
 fx.columns = ['Date', 'Bid', 'Ask']
 return fx

def generate(data):
 data_frame = data[["Date","Bid","Ask",]]
 dates = []
 hiduke = pd.DataFrame(data_frame["Date"])
 hiduke.columns = ["Hiduke"]
 for day in data_frame["Date"]:
  time = datetime.datetime.strptime(str(day), '%Y%m%d%H%M%S')
  dates.append(time)
 data_frame["Date"] = dates
 tmp = data_frame["Date"].values.astype("datetime64[m]")
 d = tmp
 data_frame["Date"] = tmp.astype(float)
 index = len(data_frame["Date"])
 index_data = []
 for x in range(index):
  index_data.append(x)
 data_frame.index = index_data
 hiduke.index = index_data
 data_frame = pd.concat([data_frame, hiduke], axis=1)
 return data_frame

class Score:
 def __init__(self, data):
  self.data = data

 def sma_addition(self):

  sma5 = pd.Series.rolling(self.data['Bid'], window=5,center=False).mean()
  sma5 = pd.DataFrame(sma5)
  sma5.columns = ["sma5"]
  sma5 = sma5.dropna(subset=["sma5"])
  kago = [go for go in range(len(sma5))]
  sma5.index = kago
  new_data = pd.concat([self.data, sma5], axis=1)

  sma25 = pd.Series.rolling(self.data['Bid'], window=25,center=False).mean()
  sma25 = pd.DataFrame(sma25)
  sma25.columns = ["sma25"]
  sma25 = sma25.dropna(subset=["sma25"])
  kago = [go for go in range(len(sma25))]
  sma25.index = kago
  new_data = pd.concat([new_data, sma25], axis=1)

  sma75 = pd.Series.rolling(self.data['Bid'], window=25,center=False).mean()
  sma75 = pd.DataFrame(sma75)
  sma75.columns = ["sma75"]
  sma75 = sma75.dropna(subset=["sma75"])
  kago = [go for go in range(len(sma75))]
  sma75.index = kago
  new_data = pd.concat([new_data, sma75], axis=1)

  choice_data = new_data.ix[:, ["Date","Bid","Ask","Hiduke","sma5","sma25","sma75"]]
  self.choice_data = choice_data

  return self.choice_data

 def ochl(self):
  ax1 = plt.subplot()
  ax1.plot(self.choice_data["Date"], self.choice_data["Bid"], color="#1e8eff", label = "sma5")


  plt.plot(self.choice_data["Date"], self.choice_data["sma5"], color="#1e8eff", label = "sma5")
  plt.plot(self.choice_data["Date"], self.choice_data["sma25"], color="#ff8e1e", label = "sma25")
  plt.plot(self.choice_data["Date"], self.choice_data["sma75"], color="#ff1e8e", label = "sma75")
#  plt.legend(loc='best')

  #plt.xticks(self.choice_data["Date"][::40], self.choice_data["Hiduke"][::40])
#  plt.grid(color='#f5f5f5')
#  ax1.patch.set_facecolor('#333333')
#  try:
#   x_left = self.choice_data["Date"][120]
#  except KeyError:
#   left = len(self.choice_data["Date"])
#   x_left = left - 1
#  x_right = self.choice_data["Date"][0]
#  plt.xlim(x_left - 5, x_right + 5)
  plt.savefig("fx.png")
  return plt.clf()

if __name__ == "__main__":
 data = get_csv()
# generate_data = generate(get_csv())
# print(generate_data)
 big_fx = Score(data)
 big_fx.sma_addition()
 big_fx.ochl()

