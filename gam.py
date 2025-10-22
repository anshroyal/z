import streamlit as st
import random



st.set_page_config(page_title="z-Acxo", layout="centered")
#name = st.text_input("Name", max_chars=10)
st.title("Z-acxo ")
ai_name = "Jimmy"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

name  =st.text_input("Player Name ")
st.write(f'{name} your symbol is X      AI  symbol is O')
st.write("   🙎‍♂️   vs     🤖 ")

# --- Initialize Game State ---
if "board" not in st.session_state:
    st.session_state.board = [" "] * 9
    st.session_state.turn = "X"  # Player always starts first
    st.session_state.winner = None

# --- Game Logic ---
def check_winner(board):
    win_combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in win_combos:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    if " " not in board:
        return "Draw"
    return None

def ai_move(board):
    # Simple AI: Try to win, block player, or pick random
    # 1. Check if AI can win
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_winner(board) == "O":
                return
            board[i] = " "

    # 2. Check if player can win next
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_winner(board) == "X":
                board[i] = "O"
                return
            board[i] = " "

    # 3. Otherwise, random move
    empty = [i for i in range(9) if board[i] == " "]
    if empty:
        board[random.choice(empty)] = "O"

# --- Game UI ---

#st.write(f"{name} are **X**, the AI is **O**. Try to win!")

cols = st.columns(3)
for i in range(3):
    for j in range(3):
        idx = i * 3 + j
        with cols[j]:
            if st.button(st.session_state.board[idx] or " ", key=idx, use_container_width=True):
                if st.session_state.board[idx] == " " and not st.session_state.winner:
                    st.session_state.board[idx] = "X"
                    st.session_state.winner = check_winner(st.session_state.board)
                    if not st.session_state.winner:
                        ai_move(st.session_state.board)
                        st.session_state.winner = check_winner(st.session_state.board)
                st.rerun()

# --- Display Result ---


if st.session_state.winner:
    
    if st.session_state.winner == "Draw":
        st.info("🤝 It's a Draw!")
    elif st.session_state.winner == "X":
        st.success(f"🏆 🙎‍♂️{name} Win!")
    else:
        
        st.error(f"🤖 {ai_name} AI Wins!")

# --- Restart Button ---
if st.button("🔄 Restart"):
    st.session_state.board = [" "] * 9
    st.session_state.turn = "X"
    st.session_state.winner = None
    st.rerun()

st.text("" \
"" \
"" \
"" \
"" \
"" \
"")

st.link_button(icon="🅾" , url="https://www.instagram.com/superacxo?igsh=NTQwYWE3cWFsNW1p",label='instagram')