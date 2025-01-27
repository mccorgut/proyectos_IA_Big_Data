import streamlit as st
import joblib
import os

# Cargar el modelo desde la carpeta 'models/'
model_path = os.path.join(os.path.dirname(__file__), 'models', 'svm_model.pkl')
model = joblib.load(model_path)

# Título de la aplicación
st.title("Titanic Survival Predictor")

# Entradas del usuario
st.write("Ingresa los datos para predecir si sobrevivirías en el Titanic:")
pclass = st.selectbox("Clase (Pclass)", [1, 2, 3])
sex = st.selectbox("Sexo", ["Male", "Female"])
age = st.number_input("Edad", min_value=0, max_value=100)
sibsp = st.number_input("Número de hermanos/cónyuges (SibSp)", min_value=0)
parch = st.number_input("Número de padres/hijos (Parch)", min_value=0)
fare = st.number_input("Tarifa (Fare)", min_value=0.0)
embarked = st.selectbox("Puerto de embarque (Embarked)", ["S", "C", "Q"])

# Convertir entradas a formato numérico
sex = 0 if sex == "Male" else 1
embarked = 0 if embarked == "S" else 1 if embarked == "C" else 2

# Predecir si el pasajero sobreviviría
if st.button("Predecir"):
    features = [pclass, sex, age, sibsp, parch, fare, embarked]
    prediction = model.predict([features])
    st.write("Sobrevivirías" if prediction[0] == 1 else "No sobrevivirías")