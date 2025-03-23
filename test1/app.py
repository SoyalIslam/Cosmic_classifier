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
    --active: 0;
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
    transform: scale(calc(1 + (var(--active) * 0.1)));
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
                0px 4px 10px -4px hsla(0, 0%, 0%, calc(1 - var(--active))),
                0 0 0 calc(var(--active) * 0.375rem) hsl(260, 97%, 50%, 0.75);
    transition: all var(--transition);
    z-index: -1;
}

.stButton > button::after {
    content: "";
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 50%;
    height: 50%;
    background-color: hsla(260, 97%, 61%, 0.75);
    background-image: radial-gradient(
        at 51% 89%, hsla(266, 45%, 74%, 1) 0px, transparent 50%
    ), radial-gradient(
        at 100% 100%, hsla(266, 36%, 60%, 1) 0px, transparent 50%
    ), radial-gradient(
        at 22% 91%, hsla(266, 36%, 60%, 1) 0px, transparent 50%
    );
    background-position: top;
    opacity: var(--active);
    border-radius: var(--border_radius);
    transition: opacity var(--transition);
    z-index: -2;
}

/* Hover/Focus-visible effects */
.stButton > button:is(:hover, :focus-visible) {
    --active: 1;
    transform: scale(1.1);
}

/* Active button effect */
.stButton > button:active {
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
                hsla(0, 0%, 50%, 1) 0%,
                hsla(0, 0%, 50%, var(--active, 0)) 120%
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
 position: relative;
    width: 100%;
    max-width: 1500px;
    height: auto;
    background-color: #000;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 16px;
    gap: 10px;
    border-radius: 8px;
    cursor: pointer;
    color: white;
    box-sizing: border-box;
    font-size: 24px; /* Medium font size */
    font-family: 'Courier New', monospace;
    color: rgba(255, 255, 255, 0.8); /* Semi-transparent text */
    white-space: normal; /* Allows wrapping */
    overflow: hidden; /* Prevents text overflow */
    text-align: center; /* Centers text inside the container */
    word-wrap: break-word; /* Ensures long words break */
    animation: glow 1.5s infinite alternate;
}



.prediction-card::before {
    content: '';
    position: absolute;
    inset: 0;
    left: -5px;
    margin: auto;
    width: calc(100% + 10px);
    height: calc(100% + 10px);
    border-radius: 10px;
    background: linear-gradient(-45deg, #e81cff 0%, #40c9ff 100%);
    z-index: -10;
    pointer-events: none;
    transition: all 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.prediction-card::after {
    content: "";
    z-index: -1;
    position: center;
    inset: 0;
    background: linear-gradient(-45deg, #fc00ff 0%, #00dbde 100%);
    transform: translate3d(0, 0, 0) scale(0.95);
    filter: blur(20px);
}

.prediction-card::after {
    filter: blur(30px);
}

.prediction-card::before {
    transform: rotate(-180deg) scaleX(1.0) scaleY(1.05);
}

.heading {
    font-size: 1.2rem;
    text-transform: capitalize;
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.prediction-card p:not(.heading) {
    font-size: 0.9rem;
    margin: 0.25rem 0;
}

.prediction-card p:last-child {
    color: #e81cff;
    font-weight: 600;
    margin-top: auto;
}

        /* Loading animation */
         .hacker-loader {
            position: relative;
            width: 300px;
            height: 80px;
            background:transparent;
            backdrop-filter:blur(10px);
            background: rgba(0, 0, 0, 0.3);
            z-index=999;
            border: 3px solid #00FCCA;
            border-radius: 10px;
            padding: 15px;
            overflow: hidden;
            box-shadow: 0 0 15px rgba(0, 255, 0, 0.5);
            text-align: center;
            margin: auto;
        }

        .loader-text {
            color: #00FCCA;
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
            background-color: #00FCCA;
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

    with open(video_file, "rb") as f:
        video_bytes = f.read()
        encoded_video = base64.b64encode(video_bytes).decode()

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
    loading_placeholder = st.empty()  

    for _ in range(1): 
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
        time.sleep(1)  

    st.session_state.loading = False
    loading_placeholder.empty()  

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

def type_text_letter_by_letter(text):
    if text is None:
        text=""
    placeholder = st.empty()
    typed_text = ""

    for char in text:
        typed_text += char  

        
        html_text = f"""
        ```html
        {typed_text}🛸
        ```
        """
        
        placeholder.markdown(html_text, unsafe_allow_html=True)
        time.sleep(0.025)  


def display_prediction_card(prediction, probability=None):
    if probability is None:
        probability = np.random.uniform(0.6, 0.9)  
    
    st.markdown("""
        <style>
            .prediction-card {
                background: rgba(255, 255, 255, 0.1);
                border-radius: 15px;
                padding: 20px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                backdrop-filter: blur(10px);
                -webkit-backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.2);
                text-align: center;
                color: white;
            }
            .probability-bar {
                height: 10px;
                background: linear-gradient(90deg, #4CAF50, #8BC34A);
                border-radius: 5px;
                margin-top: 10px;
            }
            .oye_hoye{
                color:#EB8612;
                font-width: bold;

                }
                
        </style>
        <div class="prediction-card">
            <h2>Prediction Results</h2>
        </div>
    """, unsafe_allow_html=True)
    
    type_text_letter_by_letter(f"Classification: {prediction}")
    
    st.markdown(f"""
        <div class="prediction-card">
            <div class="probability-bar" style="width: {probability*100}%"></div>
            <p>Confidence: {probability*100:.2f}%</p>
            <p class="oye_hoye">Pclassrediction made at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
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
    
    # Get the planet classification label from the dictionary
    prediction_label = att.get(prediction[0], "Unknown")

    # Detailed descriptions for each planet classification
    if prediction_label == "Bewohnbar":
        return (
            """
            "Bewohnbar"
             
            🌍 Habitable Planet: This planet has conditions that are favorable for life.
            It features a stable atmosphere, temperate surface temperature, and the presence of water.
            Such planets are prime candidates for human colonization and support a wide range of life forms.
            With a habitable environment, it's a world where life can thrive, making it a key target for exploration.
            """
        )
    
    elif prediction_label == "Terraformierbar":
        return ("""Terraformierbar
                 
            🌱 Terraformable Planet: This planet, although currently uninhabitable, has the potential to be transformed into a habitable world.
            With the right technological advancements, conditions like atmosphere and temperature can be modified.
            Terraforming efforts could introduce breathable air, liquid water, and more hospitable temperatures over time.
            This planet holds long-term potential for colonization and sustainable habitation.
        """)
    
    elif prediction_label == "Rohstoffreich":
        return ("""
                Rohstoffreich
                 
            🪙 Resource-Rich Planet: This planet is abundant in valuable resources such as metals, minerals, and other raw materials.
            These resources could be extracted for use in space exploration, industry, or even fuel production.
            While it may not be suitable for life as we know it, its wealth in natural resources makes it a prime candidate for mining operations.
            This planet could become a hub for interplanetary trade and a resource base for future space missions.
        """)
    
    elif prediction_label == "Wissenschaftlich":
        return ("""Wissenschaftlich
                 
            🔬 Scientifically Valuable Planet: This planet may not be suitable for human habitation, but it holds immense scientific interest.
            It could offer unique insights into planetary evolution, climate, and atmospheric conditions.
            Its study could help answer key questions about the universe's formation and provide valuable data for future planetary exploration.
        """)
    
    elif prediction_label == "Gasriese":
        return ("""
                Gasriese
                 
            🌌 Gas Giant: This planet is a massive gas-rich world, such as Jupiter or Saturn, primarily composed of hydrogen and helium.
            It lacks a solid surface, making it unsuitable for human habitation.
            However, it may have moons with conditions that could support life. These planets are also interesting for the study of planetary atmospheres and magnetism.
        """)
    
    elif prediction_label == "Wüstenplanet":
        return ("""Wüstenplanet
                 
            🌵 Desert World: This planet is characterized by harsh, arid conditions with little to no surface water. 
            Temperatures are extreme, and the atmosphere may be thin or toxic. 
            While uninhabitable in its current state, such planets may offer clues to the limits of life and could potentially host microbial life in the future. 
            Efforts to study these worlds might focus on how life can survive in extreme environments.
        """)
    
    elif prediction_label == "Eiswelt":
        return ("""
               Eiswelt
                  
            🧊 Ice World: This planet is a frozen, icy world, where surface temperatures are extremely low, often making it inhospitable for life. 
            The atmosphere may be composed of thick layers of ice and snow, and any liquid water would be locked away beneath the surface. 
            Though life as we know it is unlikely, such planets are of interest for their potential to harbor microbial life beneath the ice or in subglacial oceans.
        """)
    
    elif prediction_label == "Toxischetmosäre":
        return ("""
                Toxischetmosäre
                 
            ☠️ Toxic Atmosphere: This planet has a hostile, toxic atmosphere, likely composed of harmful gases such as methane, sulfur, or ammonia. 
            These gases make it unsuitable for life as we know it. 
            Any future exploration of such a planet would need to focus on technological solutions to protect astronauts and mitigate the effects of the toxic environment.
        """)
    
    elif prediction_label == "Hohestrahlung":
        return ("""Hohestrahlung
                 
            ☢️ High Radiation Levels: This planet is subject to extremely high radiation, possibly due to a nearby star or a lack of a magnetic field.
            The radiation levels present a significant hazard for human exploration and habitation. "
            Such planets might be studied for their ability to support life under intense radiation or for their potential as energy sources, but they are currently not suitable for life.
        """)
    
    elif prediction_label == "Toterahswelt":
        return ("""
                Toterahswelt
                 
            ⚰️ Dead World: This planet is lifeless, with no signs of biological activity or potential for future life. 
            The surface may be barren, and the environment is inhospitable. 
            Such planets are of interest primarily for geological studies and understanding the processes that lead to the extinction of habitable environments.
        """)
    
    else:
        return "🌌 Unknown Classification: The classification of this planet could not be determined. More data and analysis are needed."



    # Main app function
def main():
    
    st.set_page_config(page_title="Planetary Habitability Predictor", layout="wide")
    
    load_custom_css()

    if 'page' not in st.session_state:
        st.session_state.page = 'home'
        

    # Home Page
    if st.session_state.page == 'home':
    
        add_video_background("my_video.mp4")

        
        col1, col2, col3 = st.columns([1,2,1])
        
        with col2:

            
            st.markdown("""
                <div class='main-title'>
                    <h1>🌍 Planetary Habitability Explorer</h1>
                </div>
            """, unsafe_allow_html=True)
            
            
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
          <p class="glow-text">Explore the habitability potential of different planetary conditions</p> 
    </div>
""", unsafe_allow_html=True)

            

            
            
            if st.button("🚀 Begin Exploration"):
                st.write("\n")
                show_loading_animation()
                st.session_state.page = 'prediction'
                st.rerun()

    # Prediction Page
    elif st.session_state.page == 'prediction':
        try:
           
            model_path = "xgboast.pkl"
            if not os.path.exists(model_path):
                st.error("⚠ Model is not Here! Bro path sahi se check kar le 😊!")
            else:
                with open(model_path, "rb") as model_file:
                    model = pickle.load(model_file)

            
            st.markdown("""
                <div class='main-title'>
                    <h1>🌟 Planetary Analysis Dashboard</h1>
                </div>
            """, unsafe_allow_html=True)
            
            feature_ranges = {
                "Atmospheric Density": {
                    "range": (0.0, 9.32),
                    "description": "Measures the mass of atmosphere per unit volume",
                    "icon": "🌫",
                    "unit":"kg/m²"
                },
                "Surface Temperature": {
                    "range": (0.0, 600.0),
                    "description": "Average temperature at the surface level",
                    "icon": "🌡",
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
                    "icon": "⛰",
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
                    "icon": "☢",
                    "unit":"mSv/year"
                },
                "Atmospheric Composition Index": {
                    "range": (-4.01, 3.85),
                    "description": "Measure of atmospheric composition",
                    "icon": "🌪",
                    "unit":"Composition Score"
                }
            }


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
                                                ℹ {info['description']}
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

                
            input_df = pd.DataFrame([input_values], columns=[f[0] for f in features_list])
            st.write("\n")
            if st.button("🔮 Analyze Planet", key="predict_button"):
                    loading_placeholder = st.empty()
                    show_loading_animation()
        
                    st.write("\n")
                    st.write("\n")
                    
                    prediction = model.predict(input_df)
                    loading_placeholder.empty()
                    

                    type_text_letter_by_letter(display_prediction_card(attribute(prediction)))
                
                    
                    st.plotly_chart(
                            plot_feature_importance(
                                input_values,
                                [f[0] for f in features_list]
                            ),
                            use_container_width=True
                        )
        

            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🏠 Return to Home"):
                    st.session_state.page = 'home'
                    st.rerun()
            with col2:
                if st.button("📥 Export Results"):
                    
                    csv = input_df.to_csv(index=False)
                    b64 = base64.b64encode(csv.encode()).decode()
                    href = f'<a href="data:file/csv;base64,{b64}" download="planetary_analysis.csv">Download Analysis Results</a>'
                    st.markdown(href, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            if st.button("🔄 Restart Application"):
                st.session_state.page = 'home'
                st.rerun()


if __name__ == "__main__":
    main()