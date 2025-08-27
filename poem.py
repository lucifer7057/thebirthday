import streamlit as st
import base64
import textwrap
from pathlib import Path

def autoplay_audio(file_path: str):
    """
    Plays an audio file automatically in a Streamlit app.
    This version uses pathlib to create a robust file path.
    """
    audio_file_path = Path(file_path)
    if not audio_file_path.is_file():
        st.warning(f"Audio file not found at {file_path}")
        return

    with open(audio_file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        
    md = f"""
        <audio autoplay="true" loop="true">
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
    st.markdown(md, unsafe_allow_html=True)

def display_poem():
    # Play the audio file automatically
    autoplay_audio("happybirthday.mp3")

    # --- STYLING (CSS) ---
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&family=Great+Vibes&display=swap');
    
    /* Keyframes for animations */
    @keyframes glow-pink {
        0%, 100% { text-shadow: 0 0 10px #ff69b4, 0 0 12px #ff69b4, 0 0 15px #ff69b4; }
        50% { text-shadow: 0 0 15px #ff85c1, 0 0 20px #ff85c1, 0 0 25px #ff85c1; }
    }
    @keyframes glow-gold {
        0%, 100% { text-shadow: 0 0 10px #ffd700, 0 0 12px #ffd700, 0 0 15px #ffd700; }
        50% { text-shadow: 0 0 15px #ffec8b, 0 0 20px #ffec8b, 0 0 25px #ffec8b; }
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    /* NEW: Keyframe for the pulsing heart */
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.25); }
    }

    /* Main title styling */
    h1 {
        font-family: 'Poppins', sans-serif;
        text-align: center;
        color: #e0e0e0;
        animation: glow-pink 3s ease-in-out infinite;
    }

    /* Styling for the main content cards */
    .card {
        background: rgba(40, 40, 60, 0.6);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 2rem;
        width: 100%;
        max-width: 700px;
        margin: 2rem auto;
        animation: fadeIn 0.8s ease-out;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    
    .poem-container {
        color: #e0e0e0;
        font-family: 'Georgia', serif;
        font-size: 1.15em;
        line-height: 1.8;
        text-align: center;
        white-space: pre-wrap;
    }
    
    /* NEW: Styling for the closing text and heart */
    .closing-text {
        text-align: center;
        margin-top: 4rem;
        font-family: 'Great Vibes', cursive;
        font-size: 2.2em;
        color: #d0d0d0;
        opacity: 0;
        animation: fadeIn 2s ease-out 1s forwards; /* Fades in after a 1-second delay */
    }
    .heart-pulse {
        display: inline-block; /* Allows the transform to work */
        animation: pulse 1.5s ease-in-out infinite;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("A Special Poem for You 🎂")

    # --- The Poem Card ---
    poem_text = """
    What should I say, I fall short on words,
    Not trynna glaze here, but you’re one of the rare birds 🕊️.
    From the first time till today, a lot changed on the way,
    Yet somehow, with you, it all feels okay 🌸.<br>

    Through lobbies, through laughs, through every wild fight 🎮,
    You turned pixels to memories, dark nights to light.
    That calling me “Rosy,” both mocking and sweet 🌹,
    A teasing tone only you could repeat.

    And then there are times, when the jokes fade away,
    We talk deep, in a raw and honest way .
    About life, about fears, the weight we both bear,
    Those moments prove how much you truly care 🤍.

    You roast like a pro, act rude on the stage,
    But I’ve seen the care that hides in that cage.
    When my thoughts spiral, you steady my mind 🌊,
    A quiet protector, unspoken, yet kind.

    Behind all the sass, the jokes, and the flame 🔥,
    Is a heart that’s soft—though you’ll never claim.
    So here’s to you, my pookie in disguise 🐻,
    With wit that stings but warmth that ties.

    Happy Birthday—may your day be wild and bright 🎉,
    May blessings hit harder than Divine Smite ⚡.
    Because the world feels lighter with a friend like you,
    Rare as a mythic, and just as true 💎.
    """
    
    clean_poem = textwrap.dedent(poem_text).strip()
    st.markdown(f'<div class="card poem-container">{clean_poem}</div>', unsafe_allow_html=True)

    # --- NEW: Animated Closing Text ---
    closing_html = """
    <div class="closing-text">
        <p>Made with <span class="heart-pulse">❤️</span> by Rosy</p>
    </div>
    """
    st.markdown(closing_html, unsafe_allow_html=True)

