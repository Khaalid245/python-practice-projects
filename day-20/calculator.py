import streamlit as st

# Title
st.title("📱 Mobile Phone Calculator")

# Store the expression in session state
if 'expression' not in st.session_state:
    st.session_state.expression = ""

# Function to update the expression
def update_expression(value):
    st.session_state.expression += str(value)

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(st.session_state.expression)
        st.session_state.expression = str(result)
    except:
        st.session_state.expression = "Error!"

# Function to clear the expression
def clear_expression():
    st.session_state.expression = ""

# Layout for the calculator screen (expression area)
st.text_input("Expression", value=st.session_state.expression, disabled=True, key="display")

# Layout for the calculator buttons in a 4x4 grid (mimicking a phone's calculator)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# Create a 4x4 grid of buttons
for row in buttons:
    cols = st.columns(4)
    for i, button in enumerate(row):
        if cols[i].button(button):
            if button == "C":
                clear_expression()
            elif button == "=":
                evaluate_expression()
            else:
                update_expression(button)
