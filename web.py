import os
import pickle #pre trained model loading
import streamlit as st #web app
from streamlit_option_menu import option_menu


st.set_page_config(page_title='OutbreakSense-Predict outbreaks with intelligent insights', layout='wide', page_icon='🩺')

model_path = os.path.join(os.getcwd(), "saved-models", "diabetes_model.sav")
diabetes_model = pickle.load(open(model_path, 'rb'))
model_path = os.path.join(os.getcwd(), "saved-models", "parkinsons_model.sav")
parkinsons_model = pickle.load(open(model_path, 'rb'))
model_path = os.path.join(os.getcwd(), "saved-models", "hearts_model.sav")
hearts_model = pickle.load(open(model_path, 'rb'))

with st.sidebar:
    st.title("🩺 OutbreakSense")
    st.info("Select a disease prediction model or predict an outbreak in your area.")

    selected = option_menu(
        "Prediction Options",
        ["Disease Prediction", "Outbreak Prediction"],
        menu_icon="hospital-fill",
        icons=["stethoscope", "exclamation-triangle"],
        default_index=0
    )

    # ✅ Show Disease Selection Only If "Disease Prediction" Is Selected
    disease_selected = None  # Prevents 'undefined variable' error
    if selected == "Disease Prediction":
        disease_selected = option_menu(
            "Select Disease",
            ["Diabetes", "Heart Disease", "Parkinsons"],
            menu_icon="hospital-fill",
            icons=["activity", "heart", "person"],
            default_index=0
        )


#diabetes
def diabetes_prediction():
    st.title('🩸 Diabetes Prediction using ML')
    with st.form("diabetes_form"):
        col1,col2 = st.columns(2)
        with col1:
            Pregnancies = st.number_input("Number of Pregnancies", min_value=0, step=1)
            BloodPressure = st.number_input("Blood Pressure", min_value=0.0)
            Insulin = st.number_input("Insulin Level", min_value=0.0)
            DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0)
        with col2:
            Glucose = st.number_input("Glucose Level", min_value=0.0)
            SkinThickness = st.number_input("Skin Thickness", min_value=0.0)
            BMI = st.number_input("Body Mass Index (BMI)", min_value=0.0)
            Age = st.number_input("Age", min_value=1, step=1)

        submitted = st.form_submit_button("Predict Diabetes")
        if submitted:
            with st.spinner("Analyzing your inputs..."):
                user_input = [Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
                # user_input = [float(x) for x in user_input]
                diab_prediction = diabetes_model.predict([user_input])
                if diab_prediction[0] == 1:
                    diab_diagnosis = 'You are Diabetic😔'
                else:
                    diab_diagnosis = 'You are not Diabetic 😊'
                st.success(diab_diagnosis)


#hearts disease
def heart_disease_prediction():
    st.title("❤️ Heart Disease Prediction using ML")
    with st.form("heart_form"):
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Age", min_value=1, step=1)
            sex = st.radio("Gender", ["Male", "Female"])
            cp = st.number_input("Chest Pain Type (cp)", min_value=0, max_value=3)
            trestbps = st.number_input("Resting Blood Pressure", min_value=0)
            chol = st.number_input("Cholesterol Level", min_value=0)
            slope = st.number_input("Slope")
            thal = st.number_input("Thal")
        with col2:
            fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])
            restecg = st.number_input("Resting ECG Results", min_value=0, max_value=2)
            thalach = st.number_input("Maximum Heart Rate Achieved", min_value=0)
            exang = st.radio("Exercise Induced Angina", ["Yes", "No"])
            oldpeak = st.number_input("ST Depression", min_value=0.0)
            ca = st.number_input("ca")

        submitted = st.form_submit_button("Predict Heart Disease")
        if submitted:
            with st.spinner("Processing your inputs..."):
                user_input = [age, 1 if sex == "Male" else 0, cp, trestbps, chol, 1 if fbs == "Yes" else 0, restecg, thalach, 1 if exang == "Yes" else 0, oldpeak, slope, ca, thal]
                # user_input = [float(x) for x in user_input]
                hearts_prediction = hearts_model.predict([user_input])
                if hearts_prediction[0] == 1:
                    hearts_diagnosis = "You may have a heart's disease😔"
                else:
                    hearts_diagnosis = "You do not have a heart's disease😊"
                st.success(hearts_diagnosis)


#parkinsons
def parkinsons_prediction():
    st.title("🧠 Parkinson’s Disease Prediction using ML")
    with st.form("parkinsons_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            MDVPFo = st.number_input('MDVP:Fo(Hz):')
            MDVPJitter = st.number_input('MDVP:Jitter(%):')
            MDVPPPQ = st.number_input('MDVP:PPQ:')
            MDVPShimmerdb = st.number_input('MDVP:Shimmer(dB):')
            MDVPAPQ = st.number_input('MDVP:APQ:')
            HNR = st.number_input('HNR:')
            spread1 = st.number_input('spread1:')
            PPE = st.number_input('PPE:')
        with col2:
            MDVPFhi = st.number_input('MDVP:Fhi(Hz):')
            MDVPJitterAbs = st.number_input('MDVP:Jitter(Abs):')
            JitterDDP = st.number_input('Jitter:DDP:')
            ShimmerAPQ3 = st.number_input('Shimmer:APQ3:')
            ShimmerDDA = st.number_input('Shimmer:DDA')
            RPDE = st.number_input('RPDE:')
            spread2 = st.number_input('spread2:')
        with col3:
            MDVPFlo = st.number_input('MDVP:Flo(Hz):')
            MDVPRAP = st.number_input('MDVP:RAP:')
            MDVPShimmer = st.number_input('MDVP:Shimmer:')
            ShimmerAPQ5 = st.number_input('Shimmer:APQ5:')
            NHR = st.number_input('NHR:')
            DFA = st.number_input('DFA:')
            D2 = st.number_input('D2:')

        submitted = st.form_submit_button("Predict Parkinson's")
        if submitted:
            with st.spinner("Analyzing your voice parameters..."):
                user_input = [MDVPFo,MDVPFhi,MDVPFlo,MDVPJitter,MDVPJitterAbs,MDVPRAP,MDVPPPQ,JitterDDP,MDVPShimmer,MDVPShimmerdb,ShimmerAPQ3,ShimmerAPQ5,MDVPAPQ,ShimmerDDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]
                user_input = [float(x) for x in user_input]
                park_prediction = parkinsons_model.predict([user_input])
                if park_prediction[0] == 1:
                    park_diagnosis = 'You have Parkinsons Disease 😔'
                else:
                    park_diagnosis = 'You do not have Parkinsons Disease 😊'
            st.success(park_diagnosis)

def outbreak_prediction():
    st.title("Outbreak Prediction")
    st.markdown("**Note:** This model demonstrates a simple approach to outbreak risk estimation.")
    
    with st.form("outbreak_form"):
        region = st.text_input("Enter Region Name")
        population = st.number_input("Population in the Area", min_value=1, step=1, value=1000)
        current_cases = st.number_input("Current Reported Cases", min_value=0, step=1, value=0)
        threshold = st.number_input("Outbreak Threshold (cases per 1000 people)", min_value=0.0, step=0.1, value=1.0)

        submitted = st.form_submit_button("Predict Outbreak")
        if submitted:
            cases_per_1000 = (current_cases / population) * 1000
            st.write(f"**Cases per 1000 people:** {cases_per_1000:.2f}")
            if cases_per_1000 > threshold:
                st.error(f"🚨 Outbreak Detected in {region}!")
            else:
                st.success(f"No outbreak detected in {region}.")

if selected == "Disease Prediction" and disease_selected:
    if disease_selected == "Diabetes":
        diabetes_prediction()
    elif disease_selected == "Heart Disease":
        heart_disease_prediction()
    elif disease_selected == "Parkinsons":
        parkinsons_prediction()
elif selected == "Outbreak Prediction":
    outbreak_prediction()
