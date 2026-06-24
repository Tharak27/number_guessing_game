import streamlit as st
import random

st.set_page_config(page_title="Number Guessing Game", page_icon="🎯")

st.title("🎯 Number Guessing Game")

# ---------- INITIAL SETUP ----------

if "game_started" not in st.session_state:
st.session_state.game_started = False

# ---------- START SCREEN ----------

if not st.session_state.game_started:

```
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

        st.rerun()

    else:
        st.error("Please enter a valid positive number.")
```

# ---------- GAME SCREEN ----------

else:

```
st.write(f"### Remaining Chances: {st.session_state.remaining}")

# Previous guesses
if st.session_state.history:
    st.write("### Previous Guesses")
    st.write(", ".join(map(str, st.session_state.history)))

# Show input only if game is active
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

                st.error(
                    "Please enter a number between 1 and 100"
                )

            else:

                st.session_state.history.append(guess)

                if guess == st.session_state.secret_number:

                    st.success(
                        "🎉 Congratulations! You guessed correctly!"
                    )

                    st.balloons()
                    st.session_state.game_over = True

                else:

                    st.session_state.remaining -= 1

                    if guess < st.session_state.secret_number:

                        st.warning("⬆️ Try a Higher Number")

                    else:

                        st.warning("⬇️ Try a Lower Number")

                    if st.session_state.remaining == 0:

                        st.session_state.game_over = True

                        st.error(
                            f"💀 Game Over! The secret number was "
                            f"{st.session_state.secret_number}"
                        )

else:

    if st.session_state.remaining == 0:

        st.error(
            f"💀 Game Over! The secret number was "
            f"{st.session_state.secret_number}"
        )

    else:

        st.success("🎉 Congratulations! You won!")

# Restart button
if st.button("🔄 Restart Game"):

    st.session_state.clear()
    st.rerun()
```
