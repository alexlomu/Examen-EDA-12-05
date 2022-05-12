import pandas as pd
import mathplotlib as plt

conversion = pd.read.csv("conversiones.csv")
navegacion = pd.read.csv("navegacion.csv")


def user_repetido():
  navegacion["id_user"] = navegacion.drop_duplicates("id_user")
  navegacion["gclid"] = navegacion.drop_duplicates("gclid")
  navegacion["cookie"] = navegacion.drop_duplicates("cookie")
  navegacion.dropna()
  

def recurrente():
  num = 0
  for i in navegacion["user_recurrent"]:
    if navegacion["user_recurrent"] == "true":
      num += 1
  porcentaje = num/len(navegacion["user_recurrent"])
  print("Hay un {}% de usuarios recurrentes".format(porcentaje))

def tipo_conversion():
  call = 0
  form = 0
  for i in conversion["lead_type"]:
    if conversion["lead_type"] == "CALL":
      call +=1
    else:
      form +=1
  print("Hay {} CALLS y {} FORMS".format(call, form))

user_repetido()
recurrente()
tipo_conversion()

def date():
  fecha = []
  fecha = navegacion["ts"]
  

def grafica_conversion():
  fig, ax = plt.subplots()
  conversion["lead_type"].plot(kind = "bar", ax = ax)
  ax.set_tittle("Tipos de conversion", loc = "center", fontdict = {"fontsize": 14, "fontweight":"bold", "color":"tab:blue"})
  ax.set_ylabel("")
  plt.savefig("graficos/grafico.png", bbox_inches = "tight")

grafica_conversion()