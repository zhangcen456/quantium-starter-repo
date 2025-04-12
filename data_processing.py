import pandas as pd
import os

def read_all_data(data_dir):
    datas=list()
    for file in os.listdir(data_dir):
        if(file.endswith(".csv")):
            with open(os.path.join(data_dir,file),'r') as f:
                datas.append(pd.read_csv(f))
    return pd.concat(datas)

if __name__=="__main__":
    datas=read_all_data("./data")
    #product: Pink Morsels
    datas=datas[datas['product']=='pink morsel']
    #multiply quantity with price
    datas['price']=datas['price'].str.replace('$', '', regex=False)
    datas['price']=pd.to_numeric(datas['price'])
    datas['quantity']=pd.to_numeric(datas['quantity'])
    datas['sales']=datas['price']*datas['quantity']
    datas['sales']="$"+datas['sales'].astype(str)
    #save
    datas_selected=datas[['sales','date','region']]
    datas_selected.to_csv("./data/processed.csv",index=False)