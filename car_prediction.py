import datetime

import pandas as pd
import streamlit as st

import xgboost as xgb


def main():
    html_temp = """
    <div style="background-color:lightblue;padding:16px">
    <h2 style="color:black;text-align:center;">car price prediction using ML</h2>
    </div>"""
    model = xgb.XGBRegressor()
    model.load_model(r"C:\Users\sivak\Documents\ml\xgb_model.sav")
    st.markdown(html_temp, unsafe_allow_html=True)
    st.write("")
    st.write("")

    st.markdown(
        "#### Are you planning to sell your car!?\n##### So Let's try evaluating the price")

    p1 = st.number_input(
        "what is the current ex-showroom price of the car(IN lakhs)", 2.5, 25.0, step=1.0)
    p2 = st.number_input(
        "what is the distance completed by the car in kilometers?", 100, 5000000, step=100)
    s1 = st.selectbox("what type of the car?", ("Petrol", "Disel", "CNG"))
    if (s1 == "Petrol"):
        p3 = 0
    elif s1 == "Disel":
        p3 = 1
    elif s1 == "CNG":
        p3 = 2
    s2 = st.selectbox("Are you a Dealer or Individual?",
                      ("Dealer", "Individual"))
    if (s2 == "Dealer"):
        p4 = 0
    elif s2 == "Individual":
        p4 = 1
    s2 = st.selectbox("what is the transmission type?",
                      ("Manual", "Automatic"))
    if (s2 == "Manual"):
        p5 = 0
    elif s2 == "Automatic":
        p5 = 1

    p6 = st.slider("Number of owners the car previously had?", 0, 3)

    date_time = datetime.datetime.now()

    years = st.number_input(
        "In which year car was purchased", 1990, date_time.year)
    p7 = date_time.year-years
    data_new = pd.DataFrame({
        'Present_Price': p1,
        'Kms_Driven': p2,
        'Fuel_Type': p3,
        'Seller_Type': p4,
        'Transmission': p5,
        'Owner': p6,
        'Age': p7
}, index=[0])
    try:
        if st.button("Predict"):
            pred = model.predict(data_new)
            if pred>0:
                st.balloons()
                st.success("you can sell your car far {:.2f} Lakhs".format(pred[0]))
            else:
                st.warning("you can't able to sell this car")
    except:
        st.warning("something went wrong please try again")


if __name__ == '__main__':
    main()
