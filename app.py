import streamlit as st
from fractions import Fraction
import streamlit as st
import streamlit.components.v1 as components


st.title("Mega Multi-Calculator")

st.subheader("Sponsored Ad")
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

# Embed the ad
components.html(ad_code, height=100)  # adjust height to match your ad
st.set_page_config(page_title="Mega Multi-Calculator", layout="centered")


# ------------------ Basic Calculator ------------------
st.header("Basic + − × ÷ ^ mod")
num1 = st.number_input("First number", value=0.0)
num2 = st.number_input("Second number", value=0.0)
operation = st.selectbox("Operation", ["+", "-", "*", "/", "^", "mod"])

if st.button("Calculate Basic"):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2 if num2 != 0 else "Error: division by zero"
    elif operation == "^":
        result = num1 ** num2
    elif operation == "mod":
        result = num1 % num2 if num2 != 0 else "Error: division by zero"
    st.success(f"Result: {result}")

# ------------------ Fraction Calculator ------------------
st.header("Fraction Calculator")
frac1 = st.text_input("First fraction (e.g., 1/2)")
frac2 = st.text_input("Second fraction (e.g., 3/4)")
frac_op = st.selectbox("Fraction operation", ["+", "-", "*", "/"])

if st.button("Calculate Fraction"):
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
    except Exception as e:
        st.error(f"Error: {e}")

# ------------------ Equation Solver ------------------
st.header("Equation Solver (ax + b = 0)")
a = st.number_input("a (coefficient)", value=1.0)
b = st.number_input("b (constant)", value=0.0)
if st.button("Solve Equation"):
    if a == 0:
        st.warning("No solution or infinite solutions")
    else:
        x = -b / a
        st.success(f"x = {x}")

# ------------------ Currency Converter ------------------
st.header("Currency Converter")
amount = st.number_input("Amount", value=1.0)
currency = st.selectbox("Conversion", ["USD → GEL", "GEL → USD", "USD → EUR", "EUR → USD", "USD → GBP", "GBP → USD"])
rates = {"USD → GEL":2.7, "GEL → USD":1/2.7, "USD → EUR":0.92, "EUR → USD":1/0.92, "USD → GBP":0.81, "GBP → USD":1/0.81}

if st.button("Convert Currency"):
    res = amount * rates[currency]
    st.success(f"Result: {res:.2f}")

# ------------------ Temperature Converter ------------------
st.header("Temperature Converter")
temp = st.number_input("Temperature", value=0.0)
temp_type = st.selectbox("Conversion", ["C → F", "F → C", "C → K", "K → C"])

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

# ------------------ BMI Calculator ------------------
st.header("BMI Calculator")
weight = st.number_input("Weight (kg)", value=70.0)
height = st.number_input("Height (m)", value=1.75)
if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)

    st.success(f"BMI: {bmi:.2f}")
