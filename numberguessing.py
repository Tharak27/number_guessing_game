import streamlit as st
import random

st.set_page_config(page_title="Number Guessing Game", page_icon="🎯")

st.title("🎯 Number Guessing Game")

# Initial setup
if "game_started" not in st.session_state:
    st.session_state.game_started = False

# Start Screen
if not st.session_state.game_started:

    st.subheader("Start New Game")

    with st.form("start_form"):
        chances = st.text_input("How many guesses do you need?")
        start_game = st.form_submit_button("Start Game")

    if start_game:

        if chances.isdigit() and int(chances) > 0:

            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.remaining = int(chances)
            st.session_state.history = []
            st.session_state.game_over = False
            st.session_state.game_started = True
            st.session_state.message = ""

            st.rerun()

        else:
            st.error("Please enter a valid positive number.")

# Game Screen
else:

    st.write(f"### Remaining Chances: {st.session_state.remaining}")

    if st.session_state.message:
        st.info(st.session_state.message)

    if st.session_state.history:
        st.write("### Previous Guesses")
        st.write(", ".join(map(str, st.session_state.history)))

    if (
        not st.session_state.game_over
        and st.session_state.remaining > 0
    ):

        with st.form("guess_form", clear_on_submit=True):

            guess_text = st.text_input(
                "Guess a number between 1 and 100"
            )

            submitted = st.form_submit_button("Guess")

        if submitted:

            if not guess_text.isdigit():
                st.error("Please enter a valid number.")

            else:

                guess = int(guess_text)

                if guess < 1 or guess > 100:
                    st.error("Enter a number between 1 and 100")

                else:

                    st.session_state.history.append(guess)

                    if guess == st.session_state.secret_number:

                        st.session_state.message = (
                            "🎉 Congratulations! You guessed correctly!"
                        )

                        st.session_state.game_over = True
                        st.balloons()

                    else:

                        st.session_state.remaining -= 1

                        if guess < st.session_state.secret_number:
                            st.session_state.message = (
                                "⬆️ Try a Higher Number"
                            )
                        else:
                            st.session_state.message = (
                                "⬇️ Try a Lower Number"
                            )

                        if st.session_state.remaining == 0:

                            st.session_state.message = (
                                f"💀 Game Over! The secret number was "
                                f"{st.session_state.secret_number}"
                            )

                            st.session_state.game_over = True

                    st.rerun()

    if st.button("🔄 Restart Game"):

        st.session_state.clear()
        st.rerun()
