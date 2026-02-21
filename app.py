import streamlit as st
import streamlit.components.v1 as components
from fractions import Fraction


st.markdown("---")
ad_code = """
<script>
  atOptions = {
    'key' : '5b015c1057edbc7ee57ab89750fbcd24',
    'format' : 'iframe',
    'height' : 90,
    'width' : 728,
    'params' : {}
  };
</script>
<script src="https://www.highperformanceformat.com/5b015c1057edbc7ee57ab89750fbcd24/invoke.js"></script>
"""

components.html(ad_code, height=100)

st.set_page_config(page_title="Mega Multi-Calculator", layout="wide")
# ------------------ Dark Grey Background ------------------
st.markdown(
    """
    <style>
    /* Full page background */
    .reportview-container, .css-18e3th9 {
        background-color: rgba(30,30,30,1);
        color: #a8ff60;
    }
    /* Sidebar background if using one */
    .css-1d391kg {
        background-color: rgba(30,30,30,1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Mega Multi-Calculator")

# ------------------ Categories ------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "🧮 Basic Math",
    "📐 Advanced & Equations",
    "🌍 Conversions",
    "⚕️ Health"
])

with tab1:
    st.subheader("Basic Calculator")
    num1 = st.number_input("First number", key="b1")
    num2 = st.number_input("Second number", key="b2")
    operation = st.selectbox("Operation", ["+", "-", "*", "/", "^", "mod"])

    if st.button("Calculate", key="basic_btn"):
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2 if num2 != 0 else "Error"
        elif operation == "^":
            result = num1 ** num2
        elif operation == "mod":
            result = num1 % num2 if num2 != 0 else "Error"
        st.success(f"Result: {result}")

    st.subheader("Fraction Calculator")
    frac1 = st.text_input("First fraction (e.g., 1/2)", key="f1")
    frac2 = st.text_input("Second fraction (e.g., 3/4)", key="f2")
    frac_op = st.selectbox("Operation", ["+", "-", "*", "/"], key="fop")

    if st.button("Calculate Fraction", key="frac_btn"):
        try:
            f1 = Fraction(frac1)
            f2 = Fraction(frac2)
            if frac_op == "+":
                res = f1 + f2
            elif frac_op == "-":
                res = f1 - f2
            elif frac_op == "*":
                res = f1 * f2
            elif frac_op == "/":
                res = f1 / f2
            st.success(f"Result: {res}")
        except:
            st.error("Invalid fraction")

with tab2:
    st.subheader("Equation Solver (ax + b = 0)")
    a = st.number_input("a (coefficient)", key="eq_a")
    b = st.number_input("b (constant)", key="eq_b")

    if st.button("Solve Equation"):
        if a == 0:
            st.warning("No solution or infinite solutions")
        else:
            x = -b / a
            st.success(f"x = {x}")

with tab3:
    st.subheader("Currency Converter")
    amount = st.number_input("Amount", key="cur_amount")
    currency = st.selectbox(
        "Conversion",
        ["USD → GEL", "GEL → USD", "USD → EUR", "EUR → USD", "USD → GBP", "GBP → USD"]
    )
    rates = {
        "USD → GEL": 2.7,
        "GEL → USD": 1/2.7,
        "USD → EUR": 0.92,
        "EUR → USD": 1/0.92,
        "USD → GBP": 0.81,
        "GBP → USD": 1/0.81
    }

    if st.button("Convert Currency"):
        res = amount * rates[currency]
        st.success(f"Result: {res:.2f}")

    st.subheader("Temperature Converter")
    temp = st.number_input("Temperature", key="temp_val")
    temp_type = st.selectbox("Conversion Type", ["C → F", "F → C", "C → K", "K → C"])

    if st.button("Convert Temperature"):
        if temp_type == "C → F":
            res = temp * 9/5 + 32
        elif temp_type == "F → C":
            res = (temp - 32) * 5/9
        elif temp_type == "C → K":
            res = temp + 273.15
        elif temp_type == "K → C":
            res = temp - 273.15
        st.success(f"Result: {res:.2f}")

with tab4:
    st.subheader("BMI Calculator")
    weight = st.number_input("Weight (kg)", key="bmi_w")
    height = st.number_input("Height (m)", key="bmi_h")

    if st.button("Calculate BMI"):
        if height > 0:
            bmi = weight / (height ** 2)
            st.success(f"BMI: {bmi:.2f}")
        else:
            st.error("Height must be greater than 0")
          
st.markdown("---")

components.html(ad_code, height=100)








