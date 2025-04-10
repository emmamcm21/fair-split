import streamlit as st
import random
import pandas as pd
import time

# Simulating steps with a random number (in a real app, you'd integrate a step tracking API)
def get_steps():
    return random.randint(1000, 15000)  # Steps range from 1,000 to 15,000 for example

# Reward calculation logic
def calculate_rewards(steps):
    rewards = (steps // 1000)  # Every 1000 steps = 1 reward point
    return rewards

# Main app layout
st.title('Espresso Earnings')

# Get user input (optional: you could use email or a username for unique identification)
user_name = st.text_input('Enter your name', 'Guest')

if st.button('Track Steps'):
    # Get the steps (simulate or track via an actual API)
    steps = get_steps()
    rewards = calculate_rewards(steps)
    
    # Show results to the user
    st.write(f'Hello {user_name}, you took {steps} steps today!')
    st.write(f'You have earned {rewards} reward points!')
    
    # Optional: Show a progress bar based on steps
    st.progress(steps // 15000)  # Progress bar (steps as a percentage of max)

    # Save the data to a CSV (you can later upload this to a database)
    data = {
        "Name": [user_name],
        "Steps": [steps],
        "Rewards": [rewards],
        "Timestamp": [time.strftime("%Y-%m-%d %H:%M:%S")]
    }
    
    df = pd.DataFrame(data)
    df.to_csv('user_steps.csv', mode='a', header=False, index=False)
    st.write('Your steps have been saved!')

# Show reward history (this would normally be fetched from a database)
st.subheader('Reward History')
try:
    history_df = pd.read_csv('user_steps.csv')
    st.dataframe(history_df)
except:
    st.write('No history yet.')
import streamlit as st
import random
import pandas as pd
import time
from datetime import datetime

# Simulating steps with a random number (in a real app, you'd integrate a step tracking API)
def get_steps():
    return random.randint(1000, 15000)  # Steps range from 1,000 to 15,000 for example

# Reward calculation logic
def calculate_rewards(steps):
    rewards = (steps // 1000)  # Every 1000 steps = 1 reward point
    return rewards

# Save steps to a CSV file
def save_steps(user_name, steps):
    data = {
        "Name": [user_name],
        "Steps": [steps],
        "Timestamp": [time.strftime("%Y-%m-%d %H:%M:%S")]
    }
    
    df = pd.DataFrame(data)
    df.to_csv('user_steps.csv', mode='a', header=False, index=False)

# Retrieve steps for today
def get_steps_for_today(user_name):
    try:
        # Load all user steps data
        df = pd.read_csv('user_steps.csv')
        # Filter out today's steps for the user
        today = datetime.now().strftime("%Y-%m-%d")
        today_steps = df[(df["Name"] == user_name) & (df["Timestamp"].str.contains(today))]
        
        if today_steps.empty:
            return None  # No steps for today
        else:
            # Return the total steps for today
            return today_steps["Steps"].sum()
    except FileNotFoundError:
        return None  # File doesn't exist yet

# Main app layout
st.title('Espresso Earnings')

# Get user input (optional: you could use email or a username for unique identification)
user_name = st.text_input('Enter your name', 'Guest')

# Show current steps for today
if st.button('Show Steps Today'):
    steps_today = get_steps_for_today(user_name)
    if steps_today is None:
        st.write(f'No steps tracked for today, {user_name}.')
    else:
        st.write(f'{user_name}, you have taken {steps_today} steps today!')

# Track and save steps
if st.button('Track Steps'):
    steps = get_steps()  # Get random steps (replace with real API)
    rewards = calculate_rewards(steps)
    
    # Save the data to CSV
    save_steps(user_name, steps)
    
    # Show results to the user
    st.write(f'Hello {user_name}, you took {steps} steps today!')
    st.write(f'You have earned {rewards} reward points!')
    
    # Optional: Show a progress bar based on steps
    st.progress(steps // 15000)  # Progress bar (steps as a percentage of max)
