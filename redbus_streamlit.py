'''
%pip install streamlit
%pip install pandas
%pip install numpy
%pip install sqlalchemy
%pip install matplotlib seaborn
%pip install plotly
%pip install streamlit-option-menu'''

#importing libraries
import streamlit as slt 
import pandas as pd
import mysql.connector
from streamlit_option_menu import option_menu

#streamlit application
#kerala_bus
list_k=[]
df_k=pd.read_csv("kerala_routes.csv")
for i,r in df_k.iterrows():
    list_k.append(r["Route_name"])

#TS_BUS
list_TS=[]
df_TS=pd.read_csv("df_TS.csv")
for i,r in df_TS.iterrows():
    list_TS.append(r["TSRTC_ROUTES"])

##KTCL-3
list_KT=[]
df_KT=pd.read_csv("df_KTCL.csv")
for i,r in df_KT.iterrows():
    list_KT.append(r["KTCL_ROUTES"])

#ASTC-4
list_A=[]
df_A=pd.read_csv("df_ASTC.csv")
for i,r in df_A.iterrows():
    list_A.append(r["ASTC_ROUTES"])


#WEST BENGAL(WBTC (CTC))-5
list_W=[]
df_W=pd.read_csv("df_WBTC.csv")
for i,r in df_W.iterrows():
    list_W.append(r["WBTC_ROUTES"])


#Chandigarh Transport Undertaking (CTU)-6
list_C=[]
df_C=pd.read_csv("df_CTU.csv")
for i,r in df_C.iterrows():
    list_C.append(r["ROUTES_CTU"])

#PEPSU (Punjab)-7
list_P=[]
df_P=pd.read_csv("df_PEPSU.csv")
for i,r in df_P.iterrows():
    list_P.append(r["ROUTES_PEPSU"])

#NORTH BENGAL STATE TRANSPORT CORPORATION-8
list_N=[]
df_N=pd.read_csv("df_NBSTC.csv")
for i,r in df_N.iterrows():
    list_N.append(r["ROUTES_NBSTC"])

#Bihar state road transport corporation (BSRTC)-9
list_B=[]
df_B=pd.read_csv("df_BSRTC.csv")
for i,r in df_B.iterrows():
    list_B.append(r["ROUTES_BSRTC"])

#JKSRTC-10
list_J=[]
df_J=pd.read_csv("df_JKSRTC.csv")
for i,r in df_J.iterrows():
    list_J.append(r["ROUTES_JKSRTC"])

    #SETTING UP STREAMLIT PAGE

slt.set_page_config(layout="wide")
web=option_menu(menu_title="Online_Bus_details",
                options=["Home","States and Buses_info"],
                icons=["house","info-circle"],
                orientation="horizontal")

#homepage 

if web=="Home":
        slt.image(r'C:\Users\USER\OneDrive\Desktop\redbus image.jpg',caption="Red_Bus")
        slt.title("Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit")
        slt.header("Home Page")
        slt.subheader("Domain")
        slt.write("Transportation")
        slt.subheader("Objective")
        slt.write('''The Redbus Data Scraping and Filtering with Streamlit Application" aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data''')
        slt.subheader("Skills Used")
        slt.markdown("Web Scraping using Selenium, Python, Streamlit , SQL")
        slt.header("Objective")
        slt.markdown('''The main objective is improve operational efficiency and strategic planning in the transportation industry.''')
        slt.header("Developed by : Sowndharya Jagadeeswaran")
if web=="States and Buses_info":
        s=slt.selectbox("List of states",["Kerala","Telengana","Kadamba","Assam","West Bengal",
                                        "Chandigarh","Punjab","North Bengal","Bihar","Jammu & Kashmir"])
        select_fare=slt.radio("Choose the bus fare range",["50-1000","1000-2000","2000 and above"])

        #kerela bus fare filtering
        if s=="Kerala":
            k=slt.selectbox("List of Routes",list_k)
            if select_fare=="50-1000":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
              
                query="SELECT * FROM BUS_DETAILS WHERE PRICES BETWEEN %s AND %s AND ROUTE_NAME= %s ORDER BY PRICES DESC"
                params = (50, 1000, k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)

            if select_fare=="1000-2000":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES  BETWEEN %s AND %s AND ROUTE_NAME= %s ORDER BY PRICES DESC"
                params=(1000,2000,k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)
            if select_fare=="2000 and above":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES > %s AND ROUTE_NAME= %s ORDER BY PRICES DESC"
                params=(2000,k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)
        #TELENGANA BUS DETAILS:
        if s=="Telengana":
            k=slt.selectbox("List of Routes",list_TS)
            if select_fare=="50-1000":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES BETWEEN %s AND %s AND ROUTE_NAME= %s ORDER BY PRICES DESC"
                params = (50, 1000, k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)

            if select_fare=="1000-2000":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES  BETWEEN %s AND %s AND ROUTE_NAME= %s ORDER BY PRICES DESC"
                params=(1000,2000,k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)
            if select_fare=="2000 and above":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES > %s AND  ROUTE_NAME= %s ORDER BY PRICES DESC"
                params=(2000,k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)
        #KADAMBA BUSES:
        if s=="Kadamba":
            k=slt.selectbox("List of Routes",list_KT)
            if select_fare=="50-1000":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES BETWEEN %s AND %s AND ROUTE_NAME= %s ORDER BY PRICES DESC"
                params = (50, 1000, k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)

            if select_fare=="1000-2000":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES  BETWEEN %s AND %s AND  ROUTE_NAME= %s ORDER BY PRICES DESC"
                params=(1000,2000,k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)
            if select_fare=="2000 and above":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES > %s AND  ROUTE_NAME= %s ORDER BY PRICES DESC"
                params=(2000,k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)
        #ASSAM
        if s=="Assam":
            k=slt.selectbox("List of Routes",list_A)
            if select_fare=="50-1000":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES BETWEEN %s AND %s AND ROUTE_NAME= %s ORDER BY PRICES DESC"
                params = (50, 1000, k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)

            if select_fare=="1000-2000":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES  BETWEEN %s AND %s AND ROUTE_NAME= %s ORDER BY PRICES DESC"
                params=(1000,2000,k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)
            if select_fare=="2000 and above":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES > %s AND ROUTE_NAME= %s ORDER BY PRICES DESC"
                params=(2000,k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)
        #"West Bengal"
        if s=="West Bengal":
            k=slt.selectbox("List of Routes",list_W)
            if select_fare=="50-1000":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES BETWEEN %s AND %s AND ROUTE_NAME= %s ORDER BY PRICES DESC"
                params = (50, 1000, k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)

            if select_fare=="1000-2000":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES  BETWEEN %s AND %s AND ROUTE_NAME= %s ORDER BY PRICES DESC"
                params=(1000,2000,k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)
            if select_fare=="2000 and above":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES > %s AND ROUTE_NAME= %s ORDER BY PRICES DESC"
                params=(2000,k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)
        #"Chandigarh"
        if s=="Chandigarh":
            k=slt.selectbox("List of Routes",list_C)
            if select_fare=="50-1000":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES BETWEEN %s AND %s AND ROUTE_NAME= %s ORDER BY PRICES DESC"
                params = (50, 1000, k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)

            if select_fare=="1000-2000":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES  BETWEEN %s AND %s AND  ROUTE_NAME= %s ORDER BY PRICES DESC"
                params=(1000,2000,k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)
            if select_fare=="2000 and above":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES > %s AND  ROUTE_NAME= %s ORDER BY PRICES DESC"
                params=(2000,k)
                
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)
        #"Punjab"
        if s=="Punjab":
            k=slt.selectbox("List of Routes",list_P)
            if select_fare=="50-1000":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES BETWEEN %s AND %s AND ROUTE_NAME= %s ORDER BY PRICES DESC"
                params = (50, 1000, k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)

            if select_fare=="1000-2000":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES  BETWEEN %s AND %s AND  ROUTE_NAME= %s ORDER BY PRICES DESC"
                params=(1000,2000,k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)
            if select_fare=="2000 and above":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES > %s AND  ROUTE_NAME= %s ORDER BY PRICES DESC"
                params=(2000,k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)

        #"North Bengal"
        if s=="North Bengal":
            k=slt.selectbox("List of Routes",list_N)
            if select_fare=="50-1000":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES BETWEEN %s AND %s AND ROUTE_NAME= %s ORDER BY PRICES DESC"
                params = (50, 1000, k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)

            if select_fare=="1000-2000":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES  BETWEEN %s AND %s AND  ROUTE_NAME= %s ORDER BY PRICES DESC"
                params=(1000,2000,k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)
            if select_fare=="2000 and above":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES > %s  AND ROUTE_NAME= %s ORDER BY PRICES DESC"
                params=(2000,k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)
        
        #"Bihar",
        if s=="Bihar":
            k=slt.selectbox("List of Routes",list_B)
            if select_fare=="50-1000":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES BETWEEN %s AND %s AND ROUTE_NAME= %s ORDER BY PRICES DESC"
                params = (50, 1000,k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)

            if select_fare=="1000-2000":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES BETWEEN %s AND %s AND ROUTE_NAME= %s ORDER BY PRICES DESC"
                params=(1000,2000,k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)
            if select_fare=="2000 and above":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES > %s AND ROUTE_NAME= %s ORDER BY PRICES DESC"
                params=(2000,k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)
        #"Jammu & Kashmir"
        if s=="Jammu & Kashmir":
            k=slt.selectbox("List of Routes",list_J)
            if select_fare=="50-1000":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES BETWEEN %s AND %s AND ROUTE_NAME= %s ORDER BY PRICES DESC"
                params = (50, 1000, k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)

            if select_fare=="1000-2000":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES  BETWEEN %s AND %s  AND ROUTE_NAME= %s ORDER BY PRICES DESC"
                params=(1000,2000,k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)
            if select_fare=="2000 and above":
                conn=mysql.connector.connect(host="localhost",user="root",password="Jsi@112214",database="REDBUS_DETAILS")
                my_cursor=conn.cursor()
                query="SELECT * FROM BUS_DETAILS WHERE PRICES > %s AND  ROUTE_NAME= %s ORDER BY PRICES DESC"
                params=(2000,k)
                my_cursor.execute(query,params)
                out=my_cursor.fetchall()
                df=pd.DataFrame(out,columns=["ID","Bus_name","BUS_TYPE","START_TIME","END_TIME","TIME_DURATION","RATING","PRICES","SEAT_AVAILABILITY","ROUTE_NAME","ROUTE_LINK"])
                slt.write(df)

