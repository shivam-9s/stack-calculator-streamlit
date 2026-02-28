import streamlit as st

# Page setup
st.set_page_config(page_title="Stack Calculator", layout="centered")

# CSS styling
st.markdown("""
<style>

div.stButton > button {
    height:65px;
    font-size:22px;
    border-radius:12px;
    color:white !important;
    background-color:#0f172a;
    border:1px solid #374151;
}

div.stButton > button:hover {
    background-color:#2563eb;
}

.display-box {
    background:#1e293b;
    padding:20px;
    border-radius:10px;
    font-size:32px;
    text-align:right;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# Session variables
if "expression" not in st.session_state:
    st.session_state.expression = ""

if "history" not in st.session_state:
    st.session_state.history = []

# Functions
def add(val):
    st.session_state.expression += val

def clear():
    st.session_state.expression = ""

def calculate():
    try:
        result = str(eval(st.session_state.expression))
        st.session_state.history.append(
            st.session_state.expression + " = " + result
        )
        st.session_state.expression = result
    except:
        st.session_state.expression = ""

# Title
st.title("🧮 Stack Based Calculator")

# Display panel
st.markdown(
    f'<div class="display-box">{st.session_state.expression}</div>',
    unsafe_allow_html=True
)

st.write("")

# Button layout
rows = [
    ["7","8","9","÷"],
    ["4","5","6","×"],
    ["1","2","3","−"],
    ["0","C","=","PLUS"]
]

for row in rows:

    cols = st.columns(4)

    for i,val in enumerate(row):

        label = val

        if val == "PLUS":
            label = "➕"

        if cols[i].button(label, use_container_width=True):

            if val == "C":
                clear()

            elif val == "=":
                calculate()

            elif val == "÷":
                add("/")

            elif val == "×":
                add("*")

            elif val == "−":
                add("-")

            elif val == "PLUS":
                add("+")

            else:
                add(val)

# History
st.write("")
st.subheader("📜 History")

if len(st.session_state.history) == 0:
    st.write("No calculations yet")

for h in reversed(st.session_state.history):
    st.write(h)