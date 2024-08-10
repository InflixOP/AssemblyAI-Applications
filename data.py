import random

import numpy as np
import pandas as pd

# Constants
NUM_ROWS = 10000  # Number of synthetic data rows

# Functions to generate feature values
def generate_pressure():
    return np.random.randint(25, 35)  # Tire pressure in PSI

def generate_condition():
    return random.choice(['Good', 'Ok', 'Needs Replacement'])

def generate_battery_water_level():
    return random.choice(['Good', 'Ok', 'Low'])

def generate_battery_condition():
    return random.choice(['Damaged', 'Ok'])

def generate_battery_leak():
    return random.choice(['Y', 'N'])

def generate_replacement_date():
    return np.random.randint(1, 10)  # years ago

def generate_yes_no():
    return random.choice(['Y', 'N'])

def generate_color():
    return random.choice(['Clean', 'Brown', 'Black'])

# Generate synthetic data
data = []
for _ in range(NUM_ROWS):
    left_front_pressure = generate_pressure()
    right_front_pressure = generate_pressure()
    left_front_condition = generate_condition()
    right_front_condition = generate_condition()
    left_rear_pressure = generate_pressure()
    right_rear_pressure = generate_pressure()
    left_rear_condition = generate_condition()
    right_rear_condition = generate_condition()
    battery_water_level = generate_battery_water_level()
    battery_condition = generate_battery_condition()
    battery_leak = generate_battery_leak()
    replacement_date = generate_replacement_date()
    rust_dent_damage_exterior = generate_yes_no()
    oil_leak_suspension = generate_yes_no()
    brake_fluid_level = random.choice(['Good', 'Ok', 'Low'])
    brake_condition_front = generate_condition()
    brake_condition_rear = generate_condition()
    emergency_brake = random.choice(['Good', 'Ok', 'Low'])
    rust_dent_damage_engine = generate_yes_no()
    engine_oil_condition = random.choice(['Good', 'Bad'])
    engine_oil_color = generate_color()
    brake_fluid_condition = random.choice(['Good', 'Bad'])
    brake_fluid_color = generate_color()
    oil_leak_engine = generate_yes_no()

    # Compute the total costing based on conditions
    costing = 5000
    if left_front_pressure < 28 or left_front_pressure > 32:
        costing += 5000
    if right_front_pressure < 28 or right_front_pressure > 32:
        costing += 5000
    if left_front_condition == 'Needs Replacement':
        costing += 10000
    if right_front_condition == 'Needs Replacement':
        costing += 10000
    if left_rear_pressure < 28 or left_rear_pressure > 32:
        costing += 5000
    if right_rear_pressure < 28 or right_rear_pressure > 32:
        costing += 5000
    if left_rear_condition == 'Needs Replacement':
        costing += 10000
    if right_rear_condition == 'Needs Replacement':
        costing += 10000
    if battery_water_level == 'Low':
        costing += 15000
    elif battery_water_level == 'Ok':
        costing += 5000
    if battery_condition == 'Damaged':
        costing += 20000
    if battery_leak == 'Y':
        costing += 20000
    if replacement_date > 5:
        costing += 20000
    if rust_dent_damage_exterior == 'Y':
        costing += 10000
    if oil_leak_suspension == 'Y':
        costing += 10000
    if brake_fluid_level == 'Low':
        costing += 10000
    if brake_condition_front == 'Needs Replacement':
        costing += 10000
    if brake_condition_rear == 'Needs Replacement':
        costing += 10000
    if emergency_brake == 'Low':
        costing += 10000
    if rust_dent_damage_engine == 'Y':
        costing += 15000
    if engine_oil_condition == 'Bad':
        costing += 15000
    if brake_fluid_condition == 'Bad':
        costing += 15000
    if oil_leak_engine == 'Y':
        costing += 15000

    # Append row to data
    data.append([
        left_front_pressure, right_front_pressure, left_front_condition, right_front_condition,
        left_rear_pressure, right_rear_pressure, left_rear_condition, right_rear_condition,
        battery_water_level, battery_condition, battery_leak, replacement_date,
        rust_dent_damage_exterior, oil_leak_suspension, brake_fluid_level, brake_condition_front,
        brake_condition_rear, emergency_brake, rust_dent_damage_engine, engine_oil_condition,
        engine_oil_color, brake_fluid_condition, brake_fluid_color, oil_leak_engine, costing
    ])

# Create DataFrame and save to CSV
columns = [
    'Left Front Pressure', 'Right Front Pressure', 'Left Front Condition', 'Right Front Condition',
    'Left Rear Pressure', 'Right Rear Pressure', 'Left Rear Condition', 'Right Rear Condition',
    'Battery Water Level', 'Battery Condition', 'Battery Leak', 'Battery Replacement Date',
    'Rust/Dent/ Damage Exterior', 'Oil Leak in Suspension', 'Brake Fluid Level', 'Brake Condition Front',
    'Brake Condition Rear', 'Emergency Brake', 'Rust/Dent/Damage Engine', 'Engine Oil Condition',
    'Engine Oil Color', 'Brake Fluid Condition', 'Brake Fluid Color', 'Oil Leak in Engine', 'Total Costing'
]
df = pd.DataFrame(data, columns=columns)
df.to_csv('synthetic_data.csv', index=False)
