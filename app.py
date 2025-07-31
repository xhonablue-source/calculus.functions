import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- Page Configuration ---
st.set_page_config(
    page_title="Calculus: Functions, Derivatives, and Inflection Points",
    page_icon="📈", # Changed icon to be more calculus-specific
    layout="wide",
    initial_sidebar_state="expanded" # Keep sidebar expanded for parameters
)

# --- Header ---
st.markdown("""
<div style='text-align: center;'>
    <h1 style='color: #6A0572;'>📈 Calculus: Functions, Derivatives, and Inflection Points</h1>
    <h3 style='color: #4B0082; margin-top: 0.5rem;'>Explore Concavity and Inflection Points</h3>
    <p style='color: gray; font-size: 1.1rem; margin-bottom: 2rem;'>Visualize how concavity changes and how inflection points appear using first and second derivatives.</p>
</div>
""", unsafe_allow_html=True)

# --- Sidebar Inputs ---
st.sidebar.header("Function Parameters")
st.sidebar.markdown("Choose a function to explore its curve and derivatives.")

func_options = {
    "Cubic Function: x³ - 3x": "x**3 - 3*x",
    "Quartic Function: x⁴ - 4x²": "x**4 - 4*x**2",
    "Sine Wave: sin(x)": "np.sin(x)",
    "Quintic Function: x⁵ - 5x": "x**5 - 5*x"
}

selected_func_name = st.sidebar.selectbox("Select a function:", list(func_options.keys()))
func_code = func_options[selected_func_name]

# Define x-range for plotting
x_min = st.sidebar.slider("X-axis Min", -10.0, 0.0, -5.0)
x_max = st.sidebar.slider("X-axis Max", 0.0, 10.0, 5.0)
num_points = st.sidebar.slider("Number of Points", 100, 1000, 400)

x_vals = np.linspace(x_min, x_max, num_points)
x = x_vals # 'x' is used in eval()

# Evaluate function and derivatives
try:
    f = eval(func_code)
    # Numerical differentiation using numpy.gradient
    f_prime = np.gradient(f, x_vals)
    f_double_prime = np.gradient(f_prime, x_vals)
except Exception as e:
    st.error(f"Error evaluating function: {e}. Please check the function syntax.")
    st.stop() # Stop execution if there's an error

# --- Main Layout for Plots ---
st.markdown("---") # Separator
col1, col2, col3 = st.columns(3)

# Plot f(x)
with col1:
    st.subheader("Graph of $f(x)$")
    fig1, ax1 = plt.subplots(figsize=(6, 4)) # Adjusted figure size for better display
    ax1.plot(x_vals, f, label="f(x)", color="#1f77b4", linewidth=2) # Blue
    ax1.set_title("Function Curve", fontsize=14)
    ax1.set_xlabel("x")
    ax1.set_ylabel("f(x)")
    ax1.grid(True, linestyle='--', alpha=0.7)
    ax1.axhline(0, color='black', lw=1, linestyle='-')
    ax1.axvline(0, color='black', lw=1, linestyle='-')
    ax1.legend()
    st.pyplot(fig1)

# Plot f'(x)
with col2:
    st.subheader("Graph of $f'(x)$")
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    ax2.plot(x_vals, f_prime, label="f'(x)", color="#ff7f0e", linewidth=2) # Orange
    ax2.set_title("First Derivative (Slope of f(x))", fontsize=14)
    ax2.set_xlabel("x")
    ax2.set_ylabel("f'(x)")
    ax2.grid(True, linestyle='--', alpha=0.7)
    ax2.axhline(0, color='black', lw=1, linestyle='-')
    ax2.axvline(0, color='black', lw=1, linestyle='-')
    ax2.legend()
    st.pyplot(fig2)

# Plot f''(x)
with col3:
    st.subheader("Graph of $f''(x)$")
    fig3, ax3 = plt.subplots(figsize=(6, 4))
    ax3.plot(x_vals, f_double_prime, label="f''(x)", color="#2ca02c", linewidth=2) # Green
    ax3.set_title("Second Derivative (Concavity of f(x))", fontsize=14)
    ax3.set_xlabel("x")
    ax3.set_ylabel("f''(x)")
    ax3.grid(True, linestyle='--', alpha=0.7)
    ax3.axhline(0, color='black', lw=1, linestyle='-')
    ax3.axvline(0, color='black', lw=1, linestyle='-')
    ax3.legend()
    st.pyplot(fig3)

st.markdown("""
---
### 🧠 Understanding Inflection Points
Inflection points are fascinating spots on a function's graph! They tell us where the curve changes its "bend" or concavity.

* **Concavity:**
    * If $f''(x) > 0$, the function $f(x)$ is **concave up** (like a cup holding water ∪).
    * If $f''(x) < 0$, the function $f(x)$ is **concave down** (like an upside-down cup ∩).

* **Finding Inflection Points:**
    * Inflection points occur where the **concavity of $f(x)$ changes**.
    * Mathematically, this happens where the **second derivative, $f''(x)$, changes sign** (goes from positive to negative, or negative to positive).
    * You can also spot them by looking at the graph of the **first derivative, $f'(x)$**: inflection points of $f(x)$ appear as **local maximums or minimums** on the $f'(x)$ graph. This is because the slope of $f'(x)$ (which is $f''(x)$) is zero at these points.

<div style='background-color: #E0F7FA; padding: 15px; border-radius: 10px; margin-top: 20px; border-left: 5px solid #00BCD4;'>
    <p style='font-weight: bold; color: #00838F;'>💡 Tip:</p>
    <p style='color: #006064;'>
        Look at the graphs above! When the green line ($f''(x)$) crosses the x-axis, notice how the blue line ($f(x)$) changes its curve, and the orange line ($f'(x)$) reaches a peak or valley!
    </p>
</div>
""")

# --- New Section: Understanding Derivative Notation ---
st.markdown("---")
with st.expander("📚 Understanding Derivative Notation: A Quick Guide"):
    st.markdown("""
    In calculus, a **derivative** represents the instantaneous rate of change of a function. Think of it as how quickly a function's output changes with respect to its input at any given point. For instance, if a function describes your position over time, its derivative would describe your instantaneous speed.

    There are several common notations used for derivatives, each with its own advantages and historical roots. The two most prevalent are **Leibniz's notation** and **Lagrange's notation**.

    ### 1. First Derivative Notation

    The first derivative tells us about the slope of the tangent line to a function's curve at any point. It indicates whether the function is increasing, decreasing, or at a local extremum (maximum or minimum).

    * **Lagrange's Notation (Prime Notation):**
        * **Symbol:** $f'(x)$
        * **Read as:** "f prime of x"
        * **Explanation:** This is the notation used in your "Calculus" program and is very common, especially when working with functions. The prime symbol (') indicates that it's the first derivative of the function $f(x)$ with respect to its independent variable (usually $x$). If your function is named $y$, you might see it written as $y'$.
        * **Example:** If $f(x) = x^2$, then $f'(x) = 2x$.

    * **Leibniz's Notation:**
        * **Symbol:** $\frac{dy}{dx}$ or $\frac{df}{dx}$
        * **Read as:** "dy dx", "df dx", or "the derivative of y with respect to x"
        * **Explanation:** This notation, introduced by Gottfried Wilhelm Leibniz, emphasizes that the derivative is a ratio of infinitesimal changes. $dy$ represents an infinitesimal change in $y$, and $dx$ represents an infinitesimal change in $x$. It clearly indicates which variable is being differentiated with respect to. This is particularly useful in applications where the variables have specific meanings (e.g., $\frac{d(\text{position})}{d(\text{time})}$ for velocity).
        * **Example:** If $y = x^2$, then $\frac{dy}{dx} = 2x$.

    * **Euler's Notation:**
        * **Symbol:** $D_x f$ or $D f$
        * **Read as:** "D sub x of f" or "D of f"
        * **Explanation:** This notation treats differentiation as an operator ($D_x$) acting on the function $f$. It's less common in introductory calculus but is used more in advanced contexts like differential equations.

    ### 2. Second Derivative Notation

    The second derivative tells us about the concavity of a function – whether its graph is curving upwards (concave up) or downwards (concave down). It also indicates the rate of change of the slope. For example, if the first derivative is velocity, the second derivative is acceleration.

    * **Lagrange's Notation (Double Prime Notation):**
        * **Symbol:** $f''(x)$
        * **Read as:** "f double prime of x"
        * **Explanation:** Similar to the first derivative, two prime symbols (") indicate that it's the second derivative of the function $f(x)$. If your function is $y$, you might see $y''$. This is the notation used in your current program.
        * **Example:** If $f(x) = x^3$, then $f'(x) = 3x^2$, and $f''(x) = 6x$.

    * **Leibniz's Notation:**
        * **Symbol:** $\frac{d^2y}{dx^2}$ or $\frac{d^2f}{dx^2}$
        * **Read as:** "d two y dx squared" or "the second derivative of y with respect to x"
        * **Explanation:** This notation signifies that the differentiation operation has been applied twice. The $d^2$ indicates the second application of the differential operator to $y$, and $dx^2$ indicates that the differentiation is with respect to $x$ twice. It's important to note that $dx^2$ here does *not* mean $(dx)^2$.
        * **Example:** If $y = x^3$, then $\frac{dy}{dx} = 3x^2$, and $\frac{d^2y}{dx^2} = 6x$.

    * **Euler's Notation:**
        * **Symbol:** $D_x^2 f$ or $D^2 f$
        * **Read as:** "D sub x squared of f" or "D squared of f"
        * **Explanation:** Again, this shows the operator $D_x$ applied twice to the function $f$.

    ### Why Different Notations?

    Each notation has its strengths:
    * **Lagrange's notation ($f'(x)$, $f''(x)$)** is concise and excellent for showing the relationship between a function and its derivatives, especially when the independent variable is clear from context.
    * **Leibniz's notation ($\frac{dy}{dx}$, $\frac{d^2y}{dx^2}$)** is powerful for emphasizing the variables involved and is very helpful in multivariable calculus or when performing implicit differentiation and chain rule applications.

    Understanding these different symbols will help you read and interpret mathematical texts and problems more effectively as you continue your calculus journey!
    """)

# --- Footer ---
st.markdown("---")
st.markdown("""
<div style="text-align: center; margin-top: 2rem; color: #666;">
    <p>💡 <strong>Empowering Young Minds in STEAM</strong></p>
    <p>Developed by Xavier Honablue M.Ed for CognitiveCloud.ai Education</p>
</div>
""", unsafe_allow_html=True)
