import streamlit as st
from streamlit_option_menu import option_menu
import home, poem

#set page config
try:
    st.set_page_config(
        page_title="Somu's Special Day",
        page_icon=":tada:",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
except:
    pass

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None


class MultiApp:
    def __init__(self):
        if st.session_state.logged_in:
            self.apps = [
                {"title": "Home", "function": home.app},
                {"title": "Surprise", "function": poem.display_poem}
                
            ]
        else:
            self.apps = [
                {"title": "Home", "function": home.app}
            ]

    def run(self):

        # Inject custom CSS
        st.markdown(
            """
            <style>
            /* Target the outermost navbar wrapper with class 'menu' */
            [data-testid = "st.menu"] {
                background-color: transparent ; /* Or match your theme */
                border-radius: 30px !important;
                box-shadow: none !important;
                margin-top: 10px;
                padding: 0 !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )


        # only display the menu if the user is logged in
        if st.session_state.logged_in:
            menu_items = ["Home","Surprise"]
            icons_list = ["house", "gift"]
        else:
            menu_items = ["Home"]
            icons_list = ["house"]

        selected = option_menu(
            menu_title=None,
            options=menu_items,
            icons=icons_list,
            orientation="horizontal",
            default_index=0,
            styles={
                "container": {
                    # "padding": "0", 
                    "background-color": "#1f1f2e",
                    "border-radius": "10px",
                },
                "nav-link": {
                    "font-size": "16px",
                    "color": "white",
                    "margin": "0",
                    "left": "0px",
                },
                "nav-link-selected": {
                    "color": "black",
                    "background-color": "#fce4ec",
                },
            }
        )



        for app in self.apps:
            if app["title"] == selected:
                app["function"]()

app = MultiApp()
app.run()