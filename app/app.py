import streamlit as st
import joblib
import pandas as pd

# Load the trained model
# Cargar el modelo entrenado
model = joblib.load('models/real_estate_model.pkl')

# App title
# Título de la aplicación
st.title('Real Estate Price Prediction / Predicción de Precios Inmobiliarios')

# User inputs
# Entradas del usuario
land_area = st.number_input('Enter the land area (in m²): / Ingrese el área del terreno (en m²):')  # Land area
bedrooms = st.number_input('Enter the number of bedrooms: / Ingrese el número de habitaciones:')  # Number of bedrooms
bathrooms = st.number_input('Enter the number of bathrooms: / Ingrese el número de baños:')  # Number of bathrooms
first_floor_area = st.number_input('Enter the first-floor area (in m²): / Ingrese el área del primer piso (en m²):')  # First floor area
floors = st.number_input('Enter the number of floors (e.g., basement=1, second floor=2, third floor=3): / Ingrese el número de pisos (por ejemplo, basement=1, segundo piso=2, tercer piso=3):')  # Number of floors
has_basement = st.selectbox('Does the property have a basement? (0 = No, 1 = Yes): / ¿La propiedad tiene basement? (0 = No, 1 = Sí):', [0, 1])  # Whether it has basement

# Check if any of the inputs is 0 and display an error message
# Verificar si alguno de los valores es 0 y mostrar un mensaje de error
if land_area == 0 or bedrooms == 0 or bathrooms == 0 or first_floor_area == 0 or floors == 0:
    st.error('Error: All input values must be greater than 0. Please provide valid values.')  # Display error message
else:
    # Calculate the total built area considering the floors and basement
    # Calcular el área total construida considerando los pisos y el basement
    total_area = first_floor_area * floors + has_basement * first_floor_area

    # Prediction when the user clicks the 'Predict' button
    # Realizar la predicción cuando el usuario haga clic en el botón 'Predecir'
    if st.button('Predict / Predecir'):
        # Create a DataFrame with the user-provided data
        # Crear un DataFrame con los datos proporcionados por el usuario
        input_data = pd.DataFrame([[land_area, bedrooms, bathrooms, total_area, floors, has_basement]], 
                                  columns=['land_area', 'bedrooms', 'bathrooms', 'total_area', 'floors', 'has_basement'])

        # Make prediction using the loaded model
        # Hacer la predicción usando el modelo cargado
        prediction = model.predict(input_data)

        # Show the prediction result
        # Mostrar el resultado de la predicción
        st.write(f'The predicted price for the property is: ${prediction[0]:,.2f} / El precio previsto para la propiedad es: ${prediction[0]:,.2f}')
