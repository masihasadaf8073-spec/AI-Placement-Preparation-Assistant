import streamlit as st
from generator import generate_interview

# Page configuration
st.set_page_config(
    page_title="AI Placement Assistant",
    page_icon="🎯",
    layout="wide"
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');

    :root {
        --ink: #17243b;
        --muted: #64748b;
        --accent: #625bf6;
        --accent-dark: #4f46e5;
        --surface: #ffffff;
        --line: #e7eaf2;
    }

    .stApp {
        background:
            radial-gradient(ellipse at 82% 0%, rgba(216, 214, 255, .36), transparent 34rem),
            #f7f8fc;
        color: var(--ink);
        font-family: 'DM Sans', sans-serif;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    [data-testid="stMainBlockContainer"] {
        max-width: 1180px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    h1, h2, h3 {
        color: var(--ink);
        font-family: 'Manrope', sans-serif;
        letter-spacing: -.035em;
    }

    h1.hero-title {
        color: #fff !important;
    }

    p, label, [data-testid="stCaptionContainer"] {
        color: var(--muted);
    }

    .hero {
        position: relative;
        overflow: hidden;
        padding: 2.4rem 2.6rem;
        margin-bottom: 1.7rem;
        border: 1px solid rgba(255, 255, 255, .72);
        border-radius: 24px;
        background: linear-gradient(118deg, #171d3b 0%, #312c72 58%, #635cf4 100%);
        box-shadow: 0 18px 48px rgba(39, 39, 95, .15);
    }

    .hero::after {
        content: "";
        position: absolute;
        width: 280px;
        height: 280px;
        right: -74px;
        top: -145px;
        border: 1px solid rgba(255, 255, 255, .16);
        border-radius: 50%;
        box-shadow: 0 0 0 35px rgba(255, 255, 255, .035), 0 0 0 70px rgba(255, 255, 255, .025);
    }

    .hero-kicker {
        margin-bottom: .65rem;
        color: #c5c6ff;
        font-size: .75rem;
        font-weight: 700;
        letter-spacing: .14em;
        text-transform: uppercase;
    }

    .hero-title {
        max-width: 720px;
        margin: 0;
        color: #fff;
        font-family: 'Manrope', sans-serif;
        font-size: clamp(2rem, 4vw, 3.15rem);
        font-weight: 800;
        line-height: 1.12;
        letter-spacing: -.055em;
    }

    .hero-copy {
        max-width: 620px;
        margin: .85rem 0 0;
        color: #d7d9f4;
        font-size: 1rem;
        line-height: 1.65;
    }

    [data-testid="stSidebar"] {
        background: #fff;
        border-right: 1px solid var(--line);
    }

    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1.4rem;
    }

    [data-testid="stSidebar"] h2 {
        color: var(--ink) !important;
        font-size: 1.2rem;
    }

    [data-testid="stSelectbox"] [data-baseweb="select"] > div,
    [data-testid="stSlider"] {
        border-radius: 10px;
    }

    [data-testid="stSelectbox"] [data-baseweb="select"] > div {
        border-color: var(--line);
        background: #fff;
        color: var(--ink);
    }

    div.stButton > button {
        min-height: 3rem;
        border: 0;
        border-radius: 11px;
        background: linear-gradient(110deg, var(--accent), #766cfb);
        box-shadow: 0 7px 16px rgba(98, 91, 246, .22);
        color: #fff !important;
        font-weight: 700;
        transition: transform .18s ease, box-shadow .18s ease;
    }

    div.stButton > button p {
        color: #fff !important;
    }

    div.stButton > button:hover {
        border: 0;
        background: linear-gradient(110deg, var(--accent-dark), #6b63ef);
        box-shadow: 0 10px 20px rgba(98, 91, 246, .29);
        transform: translateY(-1px);
    }

    [data-testid="stMetric"] {
        min-height: 112px;
        padding: 1.1rem 1.25rem;
        border: 1px solid var(--line);
        border-radius: 16px;
        background: var(--surface);
        box-shadow: 0 5px 18px rgba(26, 37, 65, .035);
    }

    [data-testid="stMetricLabel"] {
        font-size: .78rem;
        font-weight: 600;
    }

    [data-testid="stMetricValue"] {
        color: var(--ink);
        font-family: 'Manrope', sans-serif;
        font-size: 1.25rem;
        font-weight: 700;
    }

    [data-testid="stExpander"] {
        overflow: hidden;
        margin: .75rem 0;
        border: 1px solid var(--line);
        border-radius: 15px;
        background: #fff;
        box-shadow: 0 4px 14px rgba(26, 37, 65, .035);
    }

    [data-testid="stExpander"] summary {
        padding: .35rem .5rem;
        color: var(--ink);
        font-weight: 650;
    }

    [data-testid="stExpander"] [data-testid="stVerticalBlock"] {
        gap: .75rem;
    }

    [data-testid="stAlert"] {
        border-radius: 13px;
    }

    @media (max-width: 700px) {
        [data-testid="stMainBlockContainer"] {
            padding: 1rem 1rem 3rem;
        }

        .hero {
            padding: 1.7rem 1.5rem;
            border-radius: 18px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <section class="hero">
        <div class="hero-kicker">Your next opportunity starts here</div>
        <h1 class="hero-title">Prepare smarter for your next interview.</h1>
        <p class="hero-copy">
            Practice role-specific questions, explore clear model answers,
            and walk into every interview with more confidence.
        </p>
    </section>
    """,
    unsafe_allow_html=True
)

# Sidebar configuration
st.sidebar.markdown("## Build your practice set")
st.sidebar.caption("Choose what you want to focus on.")

job_role = st.sidebar.selectbox(
    "Select Job Role",
    [
        "Python Developer",
        "Java Developer",
        "AI Engineer",
        "Machine Learning Engineer",
        "Data Analyst",
        "Data Scientist",
        "GenAI Engineer",
        "Backend Developer"
    ]
)

experience_level = st.sidebar.selectbox(
    "Experience Level",
    ["Fresher", "0-1 Years", "1-3 Years", "3-5 Years"]
)

difficulty = st.sidebar.selectbox(
    "Difficulty Level",
    ["Easy", "Medium", "Hard"],
    index=1
)

num_questions = st.sidebar.slider(
    "Number of Questions",
    min_value=3,
    max_value=15,
    value=5
)

# Generate interview questions
if st.sidebar.button(
    "🚀 Generate Interview Questions",
    type="primary",
    use_container_width=True
):
    with st.spinner("Generating interview questions..."):
        try:
            result = generate_interview(
                job_role,
                experience_level,
                difficulty,
                num_questions
            )
            st.session_state["result"] = result

        except Exception as e:
            st.error(f"Something went wrong: {str(e)}")

# Display generated results
if "result" in st.session_state:
    result = st.session_state["result"]

    st.markdown("## Your interview practice")
    st.caption("A tailored set of questions to help you prepare with purpose.")
    role_col, level_col, question_col = st.columns(3)
    with role_col:
        st.metric("Role", result.job_role)
    with level_col:
        st.metric("Experience", result.experience_level)
    with question_col:
        st.metric("Questions", len(result.questions))

    for index, question in enumerate(result.questions, start=1):

        with st.expander(
            f"Q{index}. {question.question}",
            expanded=(index == 1)
        ):
            col1, col2 = st.columns(2)

            with col1:
                st.caption(
                    f"TYPE  ·  {question.question_type}"
                )

            with col2:
                st.caption(
                    f"DIFFICULTY  ·  {question.difficulty}"
                )

            st.divider()

            st.markdown("### 📝 Model Answer")
            st.markdown(question.model_answer)

            st.markdown("### 💡 Understand It Simply")
            st.info(question.explanation)

            st.markdown("### 💻 Practical Example")
            st.markdown(question.practical_example)

            st.markdown("### 🔑 Important Keywords")
            st.markdown(
                " | ".join(
                    [f"`{keyword}`" for keyword in question.keywords]
                )
            )

            st.markdown("### 🎤 Interviewer's Follow-up")
            st.warning(question.follow_up)

else:
    st.markdown(
        """
        <div style="
            padding: 1.5rem 1.6rem;
            border: 1px solid #e7eaf2;
            border-radius: 16px;
            background: rgba(255,255,255,.82);
            box-shadow: 0 5px 18px rgba(26,37,65,.035);
        ">
            <div style="font-size:1.35rem; margin-bottom:.35rem;">✨</div>
            <strong style="color:#17243b;">Ready when you are</strong>
            <div style="color:#64748b; margin-top:.3rem; line-height:1.6;">
                Set your interview preferences in the sidebar, then generate
                a personalized practice set.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )