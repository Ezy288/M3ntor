import streamlit as st
import qrcode
from PIL import Image
import os

# =========================================================================
# ✨ ✍️ EDIT YOUR TEXT DIALOGUES HERE! ✍️ ✨
# All your custom phrases, kaomojis, and updates are locked in below.
# =========================================================================

# --- 1. Top Headers & Titles ---
WEBSITE_TITLE = "For my beloved mentor 🤍"
SUB_HEADER = "Scroll down to see my appreciation for you, mentor!!! (,,> ᴗ <,,)"

# --- 2. Option 1: The Timeline Section ---
SLIDER_TITLE = "My opinion about us"

TIMELINE_1_TITLE = "˙𐃷˙"
TIMELINE_1_BODY = "*Our first encounter at an MLBB match, I thought that you were really cool with your main hero, Sun. Because I've never seen anyone else play him that well before.*"

TIMELINE_2_TITLE = "My realisation O_O!"
TIMELINE_2_BODY = "*When we talked about our very own lives, I realized we have so much more in common than I thought. Suddenly, you became a light in my world that i thought would never lit up.*"

TIMELINE_3_TITLE = "My Promise to You"
TIMELINE_3_BODY = "*I promise to share the emotional burden of weight in ur life so you'll never have to carry it all by yourself <3 I will choose you everyday, over and over again.*"

# --- 3. Option 2: The Random Cute Notes Section ---
CARD_2_HEADER = "My appreciation for you ♡"
CARD_2_SUBTEXT = "Click below to reveal something very very interesting!"
BUTTON_REVEAL_TEXT = "Open it~ It's my admiration towards you mentor!"

CUTE_NOTES = [
    "👉 You're cool, amazing, mesmerizing, handsome, and cute! I love your voice, your gameplay, your coolness, and.. EVEERRRYTHING!!!",
    "👉 You're the best person in the whole wide world! U make me feel like the happiest girl alive. :3",
    "👉 You're like super duper cool! I love you, Mentor. Let's stay together forever, I'm loyal to only you :("
]

# --- 4. Option 3: The Big Question Section ---
CARD_3_HEADER = "One Last Thing..."
LOVE_DECLARATION = "I love you so much Arif, even these small words wouldn't be able to describe how much love I hold for u in my heart. Goodmorning though, I hope you enjoyed what i made specially for you •ᴗ•"
YES_BUTTON_TEXT = "I love you too. (That'll mean you wanna marry me 👀)"
NO_BUTTON_TEXT = "I don't"

# --- 5. The Tricked "No" Button Errors ---
ANGRY_DENIED_TEXT = "Ur not serious right.. mentor? :‹"
ANGRY_SUB_TEXT = "Let's stay together.. FOREVER mentor <3 You're stuck w me :3"

# --- 6. The Happy Success Screen ---
HAPPY_FINAL_HEADER = "Hehe, I knew it!"
HAPPY_FINAL_BODY = "Let's stay together forever, my favorite teammate! You're stuck with me!"


# =========================================================================
# ⚙️ CODE ENGINE & FLOATING CLOUD LAYER (No need to touch anything below!)
# =========================================================================
st.set_page_config(page_title=WEBSITE_TITLE, page_icon="☁️", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, #ffffff, #e6f2ff, #cce6ff);
        font-family: 'Helvetica Neue', sans-serif;
        overflow-x: hidden;
        position: relative;
    }
    h1, h2, h3, p {
        color: #1a3a5f !important;
        text-align: center;
    }
    .love-card {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0px 8px 20px rgba(0, 50, 100, 0.05);
        margin-bottom: 20px;
        text-align: center;
        border: 1px solid #e1f0ff;
        z-index: 10;
        position: relative;
    }
    div.stButton > button {
        background-color: #4a90e2 !important;
        color: white !important;
        border-radius: 30px !important;
        border: none !important;
        padding: 10px 25px !important;
        font-size: 16px !important;
        font-weight: bold !important;
        width: 100%;
        transition: all 0.3s ease;
        white-space: normal !important;
        word-wrap: break-word !important;
    }
    div.stButton > button:hover {
        transform: scale(1.03);
        background-color: #357abd !important;
    }
    .cloud-container {
        position: fixed;
        left: 0;
        width: 100vw;
        pointer-events: none;
        z-index: 1;
    }
    .top-clouds { top: 15px; }
    .bottom-clouds { bottom: 15px; }
    .cloud-text {
        font-size: 35px;
        color: rgba(255, 255, 255, 0.85);
        white-space: nowrap;
        position: absolute;
        text-shadow: 0 0 10px rgba(255,255,255,0.5);
    }
    .c1 { animation: floatLeftToRight 25s linear infinite; }
    .c2 { animation: floatRightToLeft 30s linear infinite; }
    @keyframes floatLeftToRight {
        0% { left: -150px; }
        100% { left: 100vw; }
    }
    @keyframes floatRightToLeft {
        0% { right: -150px; }
        100% { right: 100vw; }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="cloud-container top-clouds"><span class="cloud-text c1">☁️ㅤㅤ☁️</span></div>', unsafe_allow_html=True)
st.markdown('<div class="cloud-container bottom-clouds"><span class="cloud-text c2">☁️ㅤㅤ☁️ㅤ☁️</span></div>', unsafe_allow_html=True)

# --- APP HEADER ---
st.markdown(f"<p style='font-size: 1.25em; font-style: italic; font-weight: bold; margin-top: 30px; color: #1a3a5f;'>{SUB_HEADER}</p>", unsafe_allow_html=True)

# --- TIMELINE CARD ---
st.markdown('<div class="love-card">', unsafe_allow_html=True)
st.markdown(f"### {SLIDER_TITLE}")
milestone = st.select_slider(
    "Slide through time:",
    options=[TIMELINE_1_TITLE, TIMELINE_2_TITLE, TIMELINE_3_TITLE],
    label_visibility="collapsed"
)
if TIMELINE_1_TITLE in milestone:
    st.info(TIMELINE_1_BODY)
elif TIMELINE_2_TITLE in milestone:
    st.success(TIMELINE_2_BODY)
elif TIMELINE_3_TITLE in milestone:
    st.warning(TIMELINE_3_BODY)
st.markdown('</div>', unsafe_allow_html=True)

# --- REASONS CARD ---
st.markdown('<div class="love-card">', unsafe_allow_html=True)
st.markdown(f"### {CARD_2_HEADER}")
st.write(CARD_2_SUBTEXT)
if 'reason_idx' not in st.session_state:
    st.session_state.reason_idx = 0
if st.button(BUTTON_REVEAL_TEXT):
    st.session_state.reason_idx = (st.session_state.reason_idx + 1) % len(CUTE_NOTES)
st.markdown(f"<p style='font-weight: bold; font-size: 1.1em; color: #1a3a5f;'>{CUTE_NOTES[st.session_state.reason_idx]}</p>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- PROPOSAL CARD ---
st.markdown('<div class="love-card">', unsafe_allow_html=True)
st.markdown(f"### {CARD_3_HEADER}")
st.markdown(f"<p style='font-size: 1.2em; font-weight: bold;'>{LOVE_DECLARATION}</p>", unsafe_allow_html=True)

if 'tried_no' not in st.session_state:
    st.session_state.tried_no = False
if 'answered_yes' not in st.session_state:
    st.session_state.answered_yes = False

col1, col2 = st.columns(2)
with col1:
    if st.button(YES_BUTTON_TEXT):
        st.session_state.answered_yes = True
        st.session_state.tried_no = False
with col2:
    if st.button(NO_BUTTON_TEXT):
        st.session_state.tried_no = True

if st.session_state.tried_no:
    st.markdown(f"<h4 style='color: #d9534f !important;'>{ANGRY_DENIED_TEXT}</h4>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #d9534f; font-weight: bold;'>{ANGRY_SUB_TEXT}</p>", unsafe_allow_html=True)

if st.session_state.answered_yes:
    st.balloons()
    st.markdown(f"""
        <div style='background-color: #e6f2ff; padding: 15px; border-radius: 10px; border: 2px dashed #4a90e2; margin-top: 15px;'>
            <h3 style='color: #4a90e2 !important;'>{HAPPY_FINAL_HEADER}</h3>
            <p style='font-weight: bold;'>{HAPPY_FINAL_BODY}</p>
        </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- QR CODE GENERATOR ---
def generate_love_qr(url_path):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(url_path)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#1a3a5f", back_color="#e6f2ff")
    img.save("Special_Appreciation_qr.png")

YOUR_DEPLOYED_URL_HERE = "https://share.streamlit.io/" 
generate_love_qr(YOUR_DEPLOYED_URL_HERE)
