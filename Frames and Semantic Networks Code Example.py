# Basic Frame for "Car"
car_frame = {
    "type": "Car",
    "make": "Toyota",
    "model": "Corolla",
    "year": 2020,
    "features": ["Air Conditioning", "Bluetooth", "Cruise Control"]
}

# Inheritance Example: Specific Car (inherits from general "Car" frame)
sports_car_frame = car_frame.copy()
sports_car_frame.update({
    "type": "Sports Car",
    "model": "Supra",
    "features": car_frame["features"] + ["Turbocharged Engine", "Spoiler"]
})

print(sports_car_frame)
