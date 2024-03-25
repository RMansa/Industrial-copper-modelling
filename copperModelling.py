import streamlit as st
import pickle
import numpy as np
import sklearn
from streamlit_option_menu import option_menu


# Functions
def predict_status(ctry,itmtp,aplcn,wth,prdrf,qtlg,cstlg,tknslg,slgplg,itmdt,itmmn,itmyr,deldtdy,deldtmn,deldtyr):

    #change the datatypes "string" to "int"
    itdd= int(itmdt)
    itdm= int(itmmn)
    itdy= int(itmyr)

    dydd= int(deldtdy)
    dydm= int(deldtmn)
    dydy= int(deldtyr)


    #modelfile of the classification
    with open("C:/Users/Sujay/New folder/Classification_model.pkl","rb") as f:
        model_class=pickle.load(f)

    user_data= np.array([[ctry,itmtp,aplcn,wth,prdrf,qtlg,cstlg,tknslg,
                       slgplg,itdd,itdm,itdy,dydd,dydm,dydy]])
    
    y_pred= model_class.predict(user_data)

    if y_pred == 1:
        return 1
    else:
        return 0

def predict_selling_price(ctry,sts,itmtp,aplcn,wth,prdrf,qtlg,cstlg,
                   tknslg,itmdt,itmmn,itmyr,deldtdy,deldtmn,deldtyr):

    #change the datatypes "string" to "int"
    itdd= int(itmdt)
    itdm= int(itmmn)
    itdy= int(itmyr)

    dydd= int(deldtdy)
    dydm= int(deldtmn)
    dydy= int(deldtyr)
    #modelfile of the classification
    with open("C:/Users/Sujay/New folder/Regression_Model.pkl","rb") as f:
        model_regg=pickle.load(f)

    user_data= np.array([[ctry,sts,itmtp,aplcn,wth,prdrf,qtlg,cstlg,tknslg,
                       itdd,itdm,itdy,dydd,dydm,dydy]])
    
    y_pred= model_regg.predict(user_data)

    ac_y_pred= np.exp(y_pred[0])

    return ac_y_pred


#Streamlit
st.set_page_config(layout="wide")
st.markdown("""
    <style>
        .airbnb-title {
            background-color: #8B4513;
            color: #FFFFFF;
            text-align: center;
            font-size: 48px;
            font-weight: bold;
            padding: 15px;
            border-radius: 20px;
            margin-bottom: 20px;

        }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<p class='airbnb-title'>Industrial Copper Modelling</p>", unsafe_allow_html=True)
def background():
    st.markdown(f""" <style>.stApp {{
                        background: url("http://www.wallpapers.net/web/wallpapers/copper-surface-hd-wallpaper/thumbnail/lg.jpg");
                        background-size: cover;
                    }}
                 </style>""", unsafe_allow_html=True)

background()

select = option_menu(None, ["Predict Selling Price", "Predict Status"],
                       icons=["Money", "chart"],
                       default_index=0,
                       orientation="horizontal",
                       styles={"nav-link": {"font-size": "28px", "text-align": "center", "margin": "5px",
                                            "color": "#FFFFFF", "border-radius": "15px", "padding": "10px", 
                                            "background-color": "#B87333", "transition": "background-color 0.3s",
                                            "--hover-color": "#CD853F"},
                               "icon": {"font-size": "28px", "margin-right": "5px"},
                               "container": {"max-width": "6000px"},
                               "nav-link-selected": {"background-color": "##CD853F"}})



if select == "Predict Status":
    st.markdown("""
        <style>
            .status-title {
                background-color: rgba(184, 115, 51, 0.8);
                color: white;
                text-align: left;
                font-size: 36px;
                padding: 10px;
                border-radius: 10px;
                margin-bottom: 20px;
                font-weight: bold
            }
        </style>
    """, unsafe_allow_html=True)
    st.markdown("<p class='status-title'>Predict Outcome (Win/Loss)</p>", unsafe_allow_html=True)
    st.write(" ")

    col1,col2= st.columns(2)

    with col1:
        country= st.number_input(label="**Enter the Value for COUNTRY**/ Min:25.0, Max:113.0")
        item_type= st.number_input(label="**Enter the Value for ITEM TYPE**/ Min:0.0, Max:6.0")
        application= st.number_input(label="**Enter the Value for APPLICATION**/ Min:2.0, Max:87.5")
        width= st.number_input(label="**Enter the Value for WIDTH**/ Min:700.0, Max:1980.0")
        product_ref= st.number_input(label="**Enter the Value for PRODUCT_REF**/ Min:611728, Max:1722207579")
        quantity_tons_log= st.number_input(label="**Enter the Value for QUANTITY_TONS (Log Value)**/ Min:-0.322, Max:6.924",format="%0.15f")
        customer_log= st.number_input(label="**Enter the Value for CUSTOMER (Log Value)**/ Min:17.21910, Max:17.23015",format="%0.15f")
        thickness_log= st.number_input(label="**Enter the Value for THICKNESS (Log Value)**/ Min:-1.71479, Max:3.28154",format="%0.15f")
    
    with col2:
        selling_price_log= st.number_input(label="**Enter the Value for SELLING PRICE (Log Value)**/ Min:5.97503, Max:7.39036",format="%0.15f")
        item_date_day= st.selectbox("**Select the Day for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        item_date_month= st.selectbox("**Select the Month for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
        item_date_year= st.selectbox("**Select the Year for ITEM DATE**",("2020","2021"))
        delivery_date_day= st.selectbox("**Select the Day for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        delivery_date_month= st.selectbox("**Select the Month for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
        delivery_date_year= st.selectbox("**Select the Year for DELIVERY DATE**",("2020","2021","2022"))
        

    button= st.button("PREDICT THE STATUS",use_container_width=True)

    if button:
        status= predict_status(country,item_type,application,width,product_ref,quantity_tons_log,
                            customer_log,thickness_log,selling_price_log,item_date_day,
                            item_date_month,item_date_year,delivery_date_day,delivery_date_month,
                            delivery_date_year)
        
        if status == 1:
            st.write("## :black[**The Status is WON**]")
        else:
            st.write("## :black[**The Status is LOSE**]")

if select == "Predict Selling Price":

    st.markdown("""
        <style>
            .status-title {
                background-color: rgba(184, 115, 51, 0.8);
                color: white;
                text-align: left;
                font-size: 36px;
                padding: 10px;
                border-radius: 10px;
                margin-bottom: 20px;
                font-weight: bold
            }
        </style>
    """, unsafe_allow_html=True)
    st.markdown("<p class='status-title'>Selling Price Prediction</p>", unsafe_allow_html=True)
    st.write(" ")

    col1,col2= st.columns(2)

    with col1:
        country= st.number_input(label="**Enter the Value for COUNTRY**/ Min:25.0, Max:113.0")
        status= st.number_input(label="**Enter the Value for STATUS**/ Min:0.0, Max:8.0")
        item_type= st.number_input(label="**Enter the Value for ITEM TYPE**/ Min:0.0, Max:6.0")
        application= st.number_input(label="**Enter the Value for APPLICATION**/ Min:2.0, Max:87.5")
        width= st.number_input(label="**Enter the Value for WIDTH**/ Min:700.0, Max:1980.0")
        product_ref= st.number_input(label="**Enter the Value for PRODUCT_REF**/ Min:611728, Max:1722207579")
        quantity_tons_log= st.number_input(label="**Enter the Value for QUANTITY_TONS (Log Value)**/ Min:-0.3223343801166147, Max:6.924734324081348",format="%0.15f")
        customer_log= st.number_input(label="**Enter the Value for CUSTOMER (Log Value)**/ Min:17.21910565821408, Max:17.230155364880137",format="%0.15f")
        
    
    with col2:
        thickness_log= st.number_input(label="**Enter the Value for THICKNESS (Log Value)**/ Min:-1.7147984280919266, Max:3.281543137578373",format="%0.15f")
        item_date_day= st.selectbox("**Select the Day for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        item_date_month= st.selectbox("**Select the Month for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
        item_date_year= st.selectbox("**Select the Year for ITEM DATE**",("2020","2021"))
        delivery_date_day= st.selectbox("**Select the Day for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        delivery_date_month= st.selectbox("**Select the Month for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
        delivery_date_year= st.selectbox("**Select the Year for DELIVERY DATE**",("2020","2021","2022"))
        

    button= st.button(":Brown[PREDICT THE SELLING PRICE]",use_container_width=True)

    if button:
        price= predict_selling_price(country,status,item_type,application,width,product_ref,quantity_tons_log,
                               customer_log,thickness_log,item_date_day,
                               item_date_month,item_date_year,delivery_date_day,delivery_date_month,
                               delivery_date_year)
        
        
        st.write("## :black[The Selling Price is :]",price)



