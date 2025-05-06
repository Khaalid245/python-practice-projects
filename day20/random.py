import streamlit as st
import random

st.title("🎲 Dice Roll Challenge")

st.write("Roll the dice. If you get a 6, you win!")

# Store dice roll in session
if 'roll' not in st.session_state:
    st.session_state.roll = None

# Dice image URLs - white dice with black dots
dice_images = {
    1: "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Alea_1.png/200px-Alea_1.png",
    2: "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Alea_2.png/200px-Alea_2.png",
    3: "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Alea_3.png/200px-Alea_3.png",
    4: "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Alea_4.png/200px-Alea_4.png",
    5: "https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Alea_5.png/200px-Alea_5.png",
    6: "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Alea_6.png/200px-Alea_6.png"
}

# Roll Button
if st.button("Roll the Dice 🎲"):
    st.session_state.roll = random.randint(1, 6)

# Show result if rolled
if st.session_state.roll:
    st.image(dice_images[st.session_state.roll], width=100)
    st.subheader(f"You rolled a {st.session_state.roll}!")

    if st.session_state.roll == 6:
        st.success("🎉 You win!")
    else:
        st.info("😅 Not a 6. Try again!")

# Play Again Button
if st.button("Play Again 🔁"):
    st.session_state.roll = None
    st.experimental_rerun()
