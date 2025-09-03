import streamlit as st
import base64
import textwrap
from pathlib import Path

def file_to_base64(file_path):
    """Converts a local file to a base64 string for embedding in HTML."""
    try:
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        return None

def display_poem():
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
    st.markdown("<h5 style='text-align: center; color: #d0d0d0;'>🎶 Listen to the song while you read...</h5>", unsafe_allow_html=True)

    # This creates the interactive audio player
    audio_path = "Smile for You.mp3"
    base64_audio = file_to_base64(audio_path)

    if base64_audio:
        # Create a self-contained HTML string
        component_html = f"""
        <style>
            .custom-audio-container {{
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 1.5rem;
                padding: 1rem;
                /* You can add more styling here if you like */
            }}
            .custom-play-btn {{
                background-color: #1a73e8;
                color: white;
                border: none;
                border-radius: 50%;
                width: 60px;
                height: 60px;
                font-size: 1.5em;
                display: flex;
                align-items: center;
                justify-content: center;
                cursor: pointer;
                transition: all 0.3s ease;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
            }}
            .custom-play-btn:hover {{
                background-color: #4285f4;
                transform: scale(1.1);
            }}
            .custom-audio-text {{
                font-family: 'Poppins', sans-serif;
                color: #e0e0e0;
                font-size: 1.1em;
                font-weight: 600;
            }}
        </style>

        <div class="custom-audio-container">
            <button id="playBtn" class="custom-play-btn">▶</button>
            <span class="custom-audio-text">Play The Song</span>
        </div>

        <audio id="myAudio" src="data:audio/mp3;base64,{base64_audio}"></audio>

        <script>
            const audio = document.getElementById('myAudio');
            const playBtn = document.getElementById('playBtn');

            playBtn.addEventListener('click', function() {{
                if (audio.paused) {{
                    audio.play();
                    playBtn.innerHTML = '❚❚';
                }} else {{
                    audio.pause();
                    playBtn.innerHTML = '▶';
                }}
            }});

            // Optional: Reset the button when the song ends
            audio.addEventListener('ended', function() {{
                playBtn.innerHTML = '▶';
                audio.currentTime = 0; // Rewind to the start
            }});
        </script>
        """
        
        # Use st.components.v1.html to render the component
        st.components.v1.html(component_html, height=90)

    else:
        st.warning(f"Could not find '{audio_path}'.")

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
    May blessings hit harder than our Divine Smite ⚡.
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

