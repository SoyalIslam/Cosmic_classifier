import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os
import base64
import time
import plotly.express as px
from datetime import datetime

# Custom CSS and Styling
def load_custom_css():
    st.markdown("""
        <style>
        /* Main container styling */
        .stApp {
            background-color: #0a192f;
            color: white;
        }

        /* Loading animation */
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }

        /* Slider container styling */
        .slider-container {
            background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.2) 100%);
            backdrop-filter: blur(10px);
            padding: 20px;
            border-radius: 15px;
            margin: 10px 0;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            border: 1px solid rgba(255, 255, 255, 0.18);
            transition: all 0.3s ease;
        }

        .slider-container:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.45);
        }

        /* Slider styling */
        .stSlider > div > div > div {
            background-color: rgba(255, 255, 255, 0.2) !important;
            height: 4px !important;
        }

        .stSlider > div > div > div > div {
            background-color: #64ffda !important;
            width: 20px !important;
            height: 20px !important;
            border-radius: 50% !important;
        }

        /* Button styling */
        .stButton > button {
            --black-700: hsla(0, 0%, 12%, 1);
            --border_radius: 9999px;
            --transition: 0.3s ease-in-out;
            --offset: 2px;
            cursor: pointer;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            transform-origin: center;
            padding: 1rem 2rem;
            background-color: transparent;
            border: none;
            color: white;
            font-size: 1rem;
            font-weight: bold;
            border-radius: var(--border_radius);
            transform: scale(calc(1 + (var(--active, 0) * 0.1)));
            transition: transform var(--transition);
            z-index: 1;
        }

        .stButton > button::before {
            content: "";
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 100%;
            height: 100%;
            background-color: var(--black-700);
            border-radius: var(--border_radius);
            box-shadow: inset 0 0.5px hsl(0, 0%, 100%), 
                        inset 0 -1px 2px 0 hsl(0, 0%, 0%),
                        0px 4px 10px -4px hsla(0, 0%, 0%, calc(1 - var(--active, 0))),
                        0 0 0 calc(var(--active, 0) * 0.375rem) hsl(260, 97%, 50%, 0.75);
            transition: all var(--transition);
            z-index: -1;
        }

        .stButton > button::after {
            content: "";
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 100%;
            height: 100%;
            background-color: hsla(260, 97%, 61%, 0.75);
            background-image: radial-gradient(
                at 51% 89%, hsla(266, 45%, 74%, 1) 0px, transparent 50%
            ), radial-gradient(
                at 100% 100%, hsla(266, 36%, 60%, 1) 0px, transparent 50%
            ), radial-gradient(
                at 22% 91%, hsla(266, 36%, 60%, 1) 0px, transparent 50%
            );
            background-position: top;
            opacity: var(--active, 0);
            border-radius: var(--border_radius);
            transition: opacity var(--transition);
            z-index: -2;
        }

        .stButton:is(:hover, :focus-visible) {
            --active: 1;
            transform: scale(1.1);
        }
        .stButton:active {
            transform: scale(1);
        }

        /* Dots border effect */
        .stButton .dots_border {
            --size_border: calc(100% + 2px);
            overflow: hidden;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: var(--size_border);
            height: var(--size_border);
            background-color: transparent;
            border-radius: var(--border_radius);
            z-index: -10;
        }

        .stButton .dots_border::before {
            content: "";
            position: absolute;
            top: 30%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 100%;
            height: 2rem;
            background-color: white;
            mask: linear-gradient(transparent 0%, white 120%);
            animation: rotate 2s linear infinite;
        }

        @keyframes rotate {
            to {
                transform: rotate(360deg);
            }
        }

        /* Sparkle effect */
        .stButton .sparkle {
            position: absolute;
            top: -5px;
            left: 50%;
            transform: translateX(-50%);
            width: 1.75rem;
            z-index: 10;
            animation: sparkle 1.5s infinite;
        }

        @keyframes sparkle {
            0%, 100% { opacity: 0; transform: scale(0.8); }
            50% { opacity: 1; transform: scale(1.2); }
        }

        /* Button Text */
        .stButton > button span {
            position: relative;
            z-index: 2;
            background-image: linear-gradient(
                90deg,
                hsla(0, 0%, 100%, 1) 0%,
                hsla(0, 0%, 100%, var(--active, 0)) 120%
            );
            background-clip: text;
            -webkit-background-clip: text;
            color: white;
        }
        }
        /* Title styling */
        .main-title {
            text-align: center;
            color: #64ffda;
            font-size: 3em;
            margin-bottom: 30px;
            text-shadow: 0 0 10px rgba(100, 255, 218, 0.3);
        }

        /* Feature title styling */
        .feature-title {
            color: #64ffda;
            text-align: center;
            margin: 10px 0;
            font-size: 1.2em;
        }

        /* Prediction card styling */
        .prediction-card {
            background: linear-gradient(135deg, rgba(100, 255, 218, 0.1) 0%, rgba(0, 180, 216, 0.2) 100%);
            padding: 20px;
            border-radius: 15px;
            margin: 20px 0;
            text-align: center;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(100, 255, 218, 0.18);
        }

        /* Loading animation */
         .hacker-loader {
            position: relative;
            width: 300px;
            height: 80px;
            background-color: #0a0a0a;
            border: 3px solid #00ff00;
            border-radius: 10px;
            padding: 15px;
            overflow: hidden;
            box-shadow: 0 0 15px rgba(0, 255, 0, 0.5);
            text-align: center;
            margin: auto;
        }

        .loader-text {
            color: #00ff00;
            font-family: monospace;
            font-size: 18px;
            margin-bottom: 10px;
            position: relative;
            display: inline-block;
        }

        .text-glitch::before,
        .text-glitch::after {
            content: attr(data-text);
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }

        .text-glitch::before {
            left: -2px;
            text-shadow: 2px 0 #ff00ff;
            animation: glitch-effect 0.3s infinite alternate;
        }

        .text-glitch::after {
            left: 2px;
            text-shadow: -2px 0 #00ffff;
            animation: glitch-effect 0.2s infinite alternate;
        }

        @keyframes glitch-effect {
            0% { clip: rect(10px, 9999px, 50px, 0); }
            50% { clip: rect(20px, 9999px, 30px, 0); }
            100% { clip: rect(30px, 9999px, 40px, 0); }
        }

        .loader-bar {
            width: 100%;
            height: 8px;
            background-color: #003300;
            border-radius: 4px;
            overflow: hidden;
            margin-top: 10px;
        }

        .bar-fill {
            height: 100%;
            background-color: #00ff00;
            width: 0%;
            animation: bar-fill-animation 2s infinite ease-in-out;
        }

        @keyframes bar-fill-animation {
            0% { width: 0%; }
            50% { width: 100%; }
            100% { width: 0%; }
        }


        @keyframes rotate {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 10px;
        }

        ::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.1);
        }

        ::-webkit-scrollbar-thumb {
            background: rgba(100, 255, 218, 0.3);
            border-radius: 5px;
        }

        /* Tooltip styling */
        .tooltip {
            position: relative;
            display: inline-block;
        }

        .tooltip .tooltiptext {
            visibility: hidden;
            width: 200px;
            background-color: rgba(0, 0, 0, 0.8);
            color: #fff;
            text-align: center;
            border-radius: 6px;
            padding: 5px;
            position: absolute;
            z-index: 1;
            bottom: 125%;
            left: 50%;
            margin-left: -100px;
            opacity: 0;
            transition: opacity 0.3s;
        }

        .tooltip:hover .tooltiptext {
            visibility: visible;
            opacity: 1;
        }
        </style>
    """, unsafe_allow_html=True)

def add_video_background(video_file):
    # Encode video file to base64
    with open(video_file, "rb") as f:
        video_bytes = f.read()
        encoded_video = base64.b64encode(video_bytes).decode()

    # Inject custom HTML and CSS for video background
    st.markdown(
        f"""
        <style>
        /* Video stays in background */
        .video-background {{
            position: fixed;
            right: 0;
            bottom: 0;
            min-width: 100%;
            min-height: 100%;
            object-fit: cover;
            z-index: -1;
            pointer-events: none; /* Allows clicks through the video */
        }}
        .stApp {{
            background: transparent;
        }}
        </style>

        <video autoplay muted loop class="video-background">
            <source src="data:video/mp4;base64,{encoded_video}" type="video/mp4">
        </video>
        """,
        unsafe_allow_html=True
    )

def show_loading_animation():
    """Displays a temporary loading animation with a clearing effect."""
    st.session_state.loading = True
    loading_placeholder = st.empty()  # Create a dynamic placeholder

    for _ in range(1):  # Show animation for 3 seconds
        loading_placeholder.markdown("""
            <div class="hacker-loader">
                <div class="loader-text">   
                    <span class="text-glitch" data-text="Initializing...">Initializing...</span>
                </div>
                <div class="loader-bar">
                    <div class="bar-fill"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(1)  # Simulate loading effect

    st.session_state.loading = False
    loading_placeholder.empty()  # Clears the animation properly

# Function to plot feature importance
def plot_feature_importance(input_values, feature_names):
    fig = px.bar(
        x=feature_names,
        y=input_values,
        title="Feature Values Distribution",
        template="plotly_dark"
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white"
    )
    return fig

# Function to display prediction card
def display_prediction_card(prediction, probability=None):
    if probability is None:
        probability = np.random.uniform(0.6, 0.9)  # Mock probability for demonstration
    
    st.markdown(f"""
        <div class="prediction-card">
            <h2>Prediction Results</h2>
            <div class="prediction-value">Classification: {prediction}</div>
            <div class="probability-bar" style="width: {probability*100}%"></div>
            <p>Confidence: {probability*100:.2f}%</p>
            <p>Prediction made at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </div>
    """, unsafe_allow_html=True)

def attribute(prediction):
    att = {
        1: "Bewohnbar",
        2: "Terraformierbar",
        3: "Rohstoffreich",
        4: "Wissenschaftlich",
        5: "Gasriese",
        6: "Wüstenplanet",
        7: "Eiswelt",
        8: "Toxischetmosäre",
        9: "Hohestrahlung",
        10: "Toterahswelt"
    }
    return att.get(prediction[0], "Unknown")

    # Main app function
def main():
    # Page configuration
    st.set_page_config(page_title="Planetary Habitability Predictor", layout="wide")
    
    # Load custom CSS
    load_custom_css()
    # Initialize session state
    if 'page' not in st.session_state:
        st.session_state.page = 'home'
        

    # Home Page
    if st.session_state.page == 'home':
        # Add background image
        add_video_background("my_video.mp4")

        # Create a centered layout
        col1, col2, col3 = st.columns([1,2,1])
        
        with col2:
            # Title with enhanced styling
            st.markdown("""
                <div class='main-title'>
                    <h1>🌍 Planetary Habitability Explorer</h1>
                </div>
            """, unsafe_allow_html=True)
            
            # Enhanced animated planet
            st.markdown("""
    <style>
        /* Typing Animation */
        @keyframes typing {
            0% { width: 0; }
            100% { width: 100%; }
        }

        /* Glowing Effect */
        @keyframes glow {
            0% { text-shadow: 0 0 10px #64ffda, 0 0 20px #64ffda; }
            50% { text-shadow: 0 0 20px #64ffda, 0 0 40px #64ffda; }
            100% { text-shadow: 0 0 10px #64ffda, 0 0 20px #64ffda; }
        }

        /* Container for Typing Effect */
        .typing-container {
            text-align: center;
            font-size: 36px;
            font-family: 'Courier New', monospace;
            color: rgba(255, 255, 255, 0.8); /* Semi-transparent text */
            width: 100%;
            white-space: nowrap;
            overflow: hidden;
            display: inline-block;
            animation: typing 3s steps(40, end) infinite alternate, glow 1.5s infinite alternate;
        }

        /* Subtitle with soft glow */
        .glow-text {
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            color: rgba(255, 255, 255, 0.7);
            animation: glow 1.5s infinite alternate;
        }
    </style>

    <div style='text-align: center;'>
        <h1 class="typing-container">Welcome to the Planetary Analysis System</h1>
        <br>
        <p class="glow-text">Explore the habitability potential of different planetary conditions</p> 
    </div>
""", unsafe_allow_html=True)

            

            
            # Enhanced start button
            if st.button("🚀 Begin Exploration"):
                show_loading_animation()
                st.session_state.page = 'prediction'
                st.rerun()

    # Prediction Page
    elif st.session_state.page == 'prediction':
        try:
            # Load the trained model
            model_path = "decision_tree_model.pkl"
            if not os.path.exists(model_path):
                st.error("⚠️ Model is not Here! Bro path sahi se check kar le 😊!")
            else:
                with open(model_path, "rb") as model_file:
                    model = pickle.load(model_file)

            # Enhanced header with animation
            st.markdown("""
                <div class='main-title'>
                    <h1>🌟 Planetary Analysis Dashboard</h1>
                </div>
            """, unsafe_allow_html=True)
            # Feature ranges with descriptions
            feature_ranges = {
                "Atmospheric Density": {
                    "range": (0.0, 9.32),
                    "description": "Measures the mass of atmosphere per unit volume",
                    "icon": "🌫️",
                    "unit":"kg/m²"
                },
                "Surface Temperature": {
                    "range": (0.0, 630.0),
                    "description": "Average temperature at the surface level",
                    "icon": "🌡️",
                    "unit":"K"
                },
                "Gravity": {
                    "range": (0, 25.0),
                    "description": "Gravitational force at the surface",
                    "icon": "🪨",
                    "unit":"m/s²"
                },
                "Water Content": {
                    "range": (0, 100.0),
                    "description": "Percentage of water present",
                    "icon": "💧",
                    "unit":"%"
                },
                "Mineral Abundance": {
                    "range": (0, 5.0),
                    "description": "Concentration of essential minerals",
                    "icon": "⛰️",
                    "unit":"ppm"
                },
                "Orbital Period": {
                    "range": (20.0, 1000.0),
                    "description": "Time taken to orbit the star",
                    "icon": "🔄",
                    "unit":"Earth years"
                },
                "Proximity to Star": {
                    "range": (0.0, 20.0),
                    "description": "Distance from the host star. 1 AU ~ 150 Million Km",
                    "icon": "⭐",
                    "unit":"AU"
                },
                "Magnetic Field Strength": {
                    "range": (1.00, 20.00),
                    "description": "Strength of the planetary magnetic field",
                    "icon": "🧲",
                    "unit":"T"
                },
                "Radiation Levels": {
                    "range": (1.00, 20.00),
                    "description": "Amount of radiation present",
                    "icon": "☢️",
                    "unit":"mSv/year"
                },
                "Atmospheric Composition Index": {
                    "range": (-4.01, 3.85),
                    "description": "Measure of atmospheric composition",
                    "icon": "🌪️",
                    "unit":"Composition Score"
                }
            }

            # Create tabs for different sections
            # tab1 = st.tabs(["Input Parameters"])

            # with tab1:
            # Create matrix layout for features
            input_values = []
            features_list = list(feature_ranges.items())

            for i in range(0, len(features_list), 3):
                    cols = st.columns(3)
                    for j, col in enumerate(cols):
                        if i + j < len(features_list):
                            feature, info = features_list[i + j]
                            with col:
                                with st.container():
                                    st.markdown(f"""
                                        <div class="slider-container">
                                            <h4>{info['icon']} {feature}</h4>
                                            <div class="tooltip">
                                                ℹ️ {info['description']}
                                            </div>
                                        </div>
                                    """, unsafe_allow_html=True)
                                    
                                    value = st.slider(
                                         f"{feature} ({info['unit']})",
                                        min_value=float(info['range'][0]),
                                        max_value=float(info['range'][1]),
                                        value=float(sum(info['range'])/2),
                                        key=f"slider_{feature}"
                                    )
                                    input_values.append(value)

                # Convert input values to DataFrame
            input_df = pd.DataFrame([input_values], columns=[f[0] for f in features_list])
            if st.button("🔮 Analyze Planet", key="predict_button"):
                    loading_placeholder = st.empty()
                    show_loading_animation()
        

                    # Make prediction
                    prediction = model.predict(input_df)
                    loading_placeholder.empty()
                    #     splay prediction card
                    display_prediction_card(prediction[0])
                
                    #     ot feature importance
                    st.plotly_chart(
                            plot_feature_importance(
                                input_values,
                                [f[0] for f in features_list]
                            ),
                            use_container_width=True
                        )
        

            # Enhanced navigation
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🏠 Return to Home"):
                    st.session_state.page = 'home'
                    st.rerun()
            with col2:
                if st.button("📥 Export Results"):
                    # Create download link for results
                    csv = input_df.to_csv(index=False)
                    b64 = base64.b64encode(csv.encode()).decode()
                    href = f'<a href="data:file/csv;base64,{b64}" download="planetary_analysis.csv">Download Analysis Results</a>'
                    st.markdown(href, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            if st.button("🔄 Restart Application"):
                st.session_state.page = 'home'
                st.rerun()

# Run the app
if __name__ == "__main__":
    main()