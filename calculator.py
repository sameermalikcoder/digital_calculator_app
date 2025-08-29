import streamlit as st

st.set_page_config(page_title="Calculator", layout="centered")

# Initialize session state
if "expression" not in st.session_state:
    st.session_state.expression = ""

st.title("Digital Calculator")

# Display the expression
st.text_input("", st.session_state.expression, key="display", disabled=True)

# Function to update expression
def press(key):
    if key == "Clear":
        st.session_state.expression = ""
    elif key == "=":
        try:
            st.session_state.expression = str(eval(st.session_state.expression))
        except:
            st.session_state.expression = "Error"
    else:
        st.session_state.expression += key

# Calculator Layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["Clear"]
]

# Render buttons in grid
for row in buttons:
    cols = st.columns(len(row))
    for i, key in enumerate(row):
        if cols[i].button(key):
            press(key)
