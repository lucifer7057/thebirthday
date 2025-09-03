import streamlit as st
import time
import base64

def file_to_base64(file_path):
    """Converts a local file to a base64 string for embedding in HTML."""
    try:
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        return None

def app():
    # --- STYLING (CSS) ---
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&family=Great+Vibes&display=swap');
    /* Keyframes and other styles remain the same */
    @keyframes glow {
        0%, 100% { text-shadow: 0 0 10px #1a73e8, 0 0 12px #1a73e8, 0 0 15px #1a73e8; }
        50% { text-shadow: 0 0 15px #4285f4, 0 0 20px #4285f4, 0 0 25px #4285f4; }
    }
    @keyframes glow-gold {
        0%, 100% { text-shadow: 0 0 10px #ffd700, 0 0 12px #ffd700, 0 0 15px #ffd700; }
        50% { text-shadow: 0 0 15px #ffec8b, 0 0 20px #ffec8b, 0 0 25px #ffec8b; }
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    h1 {
        font-family: 'Poppins', sans-serif;
        text-align: center;
        color: #e0e0e0;
        animation: glow 3s ease-in-out infinite;
    }
    
    /* This card style is now ONLY for the logged-in view */
    .card {
        background: rgba(40, 40, 60, 0.6);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 2rem;
        width: 100%;
        max-width: 750px;
        margin: 1rem auto;
        animation: fadeIn 0.8s ease-out;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }

    /* FIX: New style to target the Streamlit form container directly */
    [data-testid="stForm"] {
        background: rgba(40, 40, 60, 0.6);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 2rem;
        width: 100%;
        margin: 1rem auto;
        animation: fadeIn 0.8s ease-out;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    [data-testid = "stBaseButton-secondaryFormSubmit"] {
        background-color: #1a73e8;
        color: white;
        border: none;
    }
    [data-testid = "stBaseButton-secondaryFormSubmit"]:hover{
        background-color: #4285f4;
        transform: scale(1.05);
        color: white;
        border: none;
        box-shadow: 0 4px 15px rgba(66, 133, 244, 0.5);
    }

    .stButton > button {
        background-color: #1a73e8;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        font-family: 'Poppins', sans-serif;
        transition: all 0.3s ease;
        display: block;
        margin: 1rem auto 0 auto;
    }
    .stButton > button:hover {
        background-color: #4285f4;
        transform: scale(1.05);
        box-shadow: 0 0 15px rgba(66, 133, 244, 0.6);
    }
    .note-container {
        background-color: rgba(0, 0, 0, 0.2);
        border-left: 5px solid #4285f4;
        padding: 15px;
        margin: 20px 0;
        border-radius: 8px;
        font-style: italic;
        color: #d0d0d0;
        line-height: 1.6;
    }
    .two-column-layout {
        display: flex;
        align-items: center;
        gap: 1.5rem;
    }
    .image-column { flex: 2; }
    .text-column { flex: 3; }
    .column-image {
        width: 100%;
        border-radius: 15px;
        border: 3px solid rgba(255, 255, 255, 0.3);
    }
    .birthday-title {
        font-family: 'Great Vibes', cursive;
        font-size: 2.5em;
        text-align: center;
        color: #f0e68c;
        animation: glow-gold 3s ease-in-out infinite;
        line-height: 1.2;
    }
    .birthday-subtitle {
        font-family: 'Poppins', sans-serif;
        font-style: italic;
        font-size: 1.1em;
        text-align: center;`
        color: #d0d0d0;
        margin-top: 0.5rem;
    }
                .custom-audio-container {
        display: flex;
        align-items: center;
        justify-content: center;
        background: rgba(40, 40, 60, 0.6);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 1rem 2rem;
        width: 100%;
        max-width: 400px;
        margin: 1rem auto;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        transition: all 0.3s ease;
    }
    .custom-play-btn {
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
    }
    .custom-play-btn:hover {
        background-color: #4285f4;
        transform: scale(1.1);
        box-shadow: 0 0 15px rgba(66, 133, 244, 0.6);
    }
    .custom-audio-text {
        font-family: 'Poppins', sans-serif;
        color: #e0e0e0;
        font-size: 1.1em;
        margin-left: 1.5rem;
        font-weight: 600;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("A Little Surprise from your Rosy 🎂")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.username = None

    if st.session_state.logged_in:
        st.markdown(f"<h3 style='text-align: center;'>Hello, my dear Somu Chan 💞!</h3>", unsafe_allow_html=True)

        note_text = """
        I don’t know how you’ll feel about this, but still—I did it because some things matter to me, and this is my way of celebrating.
        <br><br>
        It’s just a small gift from my side, but it comes with a lot of thought and heart. You’ve been a constant support—whether in laughs, roasts, or even those deep talks that mean more than words can say.
        It hasn't been long since we first met, but still the things progressed so smoothly and calmy (ofc with the fun and tease along the way) that
        it never felt we were strangers.
        <br><br>
        I wish I could do more than this, but since I wanted to do something special, I came up with this idea 
        to celebrate your special day with this little surprise.<br>
        <b>Wishing you a cheerful, blissful, heartful, and soulful Birthday!</b>
        """ # Truncated
        st.markdown(f'<div class="note-container">{note_text}</div>', unsafe_allow_html=True)


        
        image_path = "vanitas.jpg"
        base64_image = file_to_base64(image_path)
        if base64_image:
            birthday_card_html = f"""
            <div class="card">
                <div class="two-column-layout">
                    <div class="image-column">
                        <img src="data:image/png;base64,{base64_image}" class="column-image">
                    </div>
                    <div class="text-column">
                        <h2 class="birthday-title">Happiest Birthday my Vanitas ✨</h2>
                        <p class="birthday-subtitle">(Now quickly check the surprise page!)</p>
                    </div>
                </div>
            </div>
            """
            st.markdown(birthday_card_html, unsafe_allow_html=True)
        else:
            st.warning(f"Could not find '{image_path}'.")
            
        if st.button("Log Out"):
            with st.spinner("Logging out..."):
                time.sleep(2)
            st.session_state.logged_in = False
            st.session_state.username = None
            st.rerun()

    else:
        st.info("Log in to see your surprise. 😉")
        with st.form("login_form"):
            name = st.text_input("Your Name that I call you by in game")
            nickname = st.text_input("Your Nickname that I call you by personally")
            submit_button = st.form_submit_button("Let's Go!")

            if submit_button:
                if name and nickname:
                    if name.lower() == "moochie" and nickname.lower() == "somu":
                        with st.spinner("Unlocking the surprise..."):
                            time.sleep(2)
                        st.session_state.logged_in = True
                        st.session_state.username = name
                        st.success("Surprise Unlocked!")
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.error("Incorrect details. Are you sure you're my somu? 🤔")
                else:
                    st.warning("Please fill in both fields.")