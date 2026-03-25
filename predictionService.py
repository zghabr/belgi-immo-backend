import os

import joblib
import pandas as pd


def get_prediction(data):
    property_type = data.type_of_property
    # Convert to DataFrame (standard format for most ML models)
    df = preprocess_data(data, features.get(property_type))

    # Perform prediction
    model = load_model(property_type)

    # Perform prediction
    if model:
        prediction = model.predict(df)[0]
    else:
        # Mock prediction logic if model is not loaded
        prediction = 250000.0 + (data.living_area * 2500)

    return prediction


def preprocess_data(data, features_list):
    # Convert Pydantic model to dictionary
    input_dict = data.dict()

    # Apply categorical mappings
    input_dict["fully_equipped_kitchen"] = kitchen_scale.get(
        input_dict["fully_equipped_kitchen"], 0
    )
    input_dict["state_of_the_building"] = building_scale.get(
        input_dict["state_of_the_building"], 2
    )
    # 3. Create initial DataFrame
    df_raw = pd.DataFrame([input_dict])

    # 4. Transform Categorical columns to match Features list
    # We create the "province_Hainaut" style strings manually
    df_raw["province_" + df_raw["province"]] = 1
    df_raw["region_" + df_raw["region"]] = 1

    # 5. Reindex to the features
    # This adds missing columns as NaN and drops unused ones (like zip_code)
    final_df = df_raw.reindex(columns=features_list)

    # 6. Final Clean up: Fill NaNs with 0 and Booleans to Int
    final_df = final_df.fillna(0)
    final_df = final_df.astype(float)  # Ensuring numeric types for the model

    # 7. Scale data
<<<<<<< HEAD
    house_scaler = joblib.load("models/scaler_houses.pkl")
    apart_scaler = joblib.load("models/scaler_apartments.pkl")

    if data.type_of_property == "House":
        final_df = house_scaler.transform(final_df)
    elif data.type_of_property == "Apartment":
        final_df = apart_scaler.transform(final_df)
=======
    house_scaler=joblib.load('models/scaler_houses.pkl')
    apart_scaler=joblib.load('models/scaler_apartments.pkl')

    if data.type_of_property == 'House':
        final_df=house_scaler.transform(final_df)
    elif data.type_of_property == 'Apartment':
        final_df=apart_scaler.transform(final_df)
>>>>>>> a069447a11aae8caf83a0bcdcfd1305273de8b9b

    return final_df


# --- Model Loading ---
def load_model(property_type):
    # 1. Map types to their respective file paths
    model_paths = {
        "House": "models/best_model_houses.pkl",
        "Apartment": "models/best_model_apartments.pkl",
    }

    # 2. Get the path based on the input
    path = model_paths.get(property_type)

    # 3. Check if path exists and load; otherwise return None
    if path and os.path.exists(path):
        return joblib.load(path)

    return None


# --- Mappings ---

kitchen_scale = {
    "Not equipped": 0,
    "Partially equipped": 1,
    "Super equipped": 2,
    "Fully equipped": 3,
}

building_scale = {
    "New": 4,
    "Under construction": 4,
    "Fully renovated": 3,
    "Excellent": 3,
    "Normal": 2,
    "To be renovated": 1,
    "To renovate": 1,
    "To restore": 1,
    "To demolish": 0,
}

features = {
    "House": [
        "number_of_rooms",
        "living_area",
        "fully_equipped_kitchen",
        "furnished",
        "open_fire",
        "terrace",
        "terrace_area",
        "garden",
        "garden_area",
        "surface_of_the_land",
        "number_of_facades",
        "swimming_pool",
        "state_of_the_building",
        "province_Brussels",
        "province_East Flanders",
        "province_Flemish Brabant",
        "province_Hainaut",
        "province_Limburg",
        "province_Luxembourg",
        "province_Namur",
        "province_Walloon Brabant",
        "province_West Flanders",
        "region_Wallonia",
    ],
    "Apartment": [
        "number_of_rooms",
        "living_area",
        "fully_equipped_kitchen",
        "furnished",
        "open_fire",
        "terrace",
        "terrace_area",
        "garden",
        "garden_area",
        "number_of_facades",
        "swimming_pool",
        "state_of_the_building",
        "province_Brussels",
        "province_East Flanders",
        "province_Flemish Brabant",
        "province_Hainaut",
        "province_Liege",
        "province_Limburg",
        "province_Namur",
        "province_Walloon Brabant",
        "province_West Flanders",
        "region_Wallonia",
    ],
}
