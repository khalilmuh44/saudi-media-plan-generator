import streamlit as st
from media_plan import generate_media_plan
from blueprint import generate_blueprint

st.set_page_config(page_title="Ameen AI Suite", layout="wide")

st.title("🚀 Ameen AI Suite")
st.subheader("AI Growth Reports Generator")

if "service" not in st.session_state:
    st.session_state.service = "media"

col1, col2 = st.columns(2)

with col1:
    if st.button("📈 Media Plan", use_container_width=True):
        st.session_state.service = "media"

with col2:
    if st.button("🚀 Business Growth Blueprint", use_container_width=True):
        st.session_state.service = "blueprint"

st.divider()

store_name = st.text_input("Business / Store Name")
store_url = st.text_input("Website / Store URL")
niche = st.text_input("Business Niche")
budget = st.text_input("Monthly Budget", value="10000 SAR")

country = st.selectbox(
    "Target Country",
    ["Saudi Arabia", "UAE", "Qatar", "Kuwait"]
)

business_type = st.selectbox(
    "Business Type",
    ["E-commerce Store", "Service Business", "Restaurant", "Clinic", "Real Estate", "Other"]
)

main_goal = st.selectbox(
    "Main Goal",
    [
        "Increase Sales",
        "Improve Ads Performance",
        "Improve Website Conversion",
        "SEO Growth",
        "Understand Competitors",
        "Build 90-Day Growth Plan"
    ]
)

current_problem = st.text_area("Current Main Problem")

generate = st.button("Generate Report", use_container_width=True)

if generate:
    if not store_name or not store_url or not niche or not budget:
        st.error("Please fill all required fields.")
    else:
        with st.spinner("Generating report..."):

            if st.session_state.service == "media":
                html_report, markdown_report = generate_media_plan(
                    store_name, store_url, niche, budget, country
                )
                file_name = "media_plan.html"

            else:
                html_report, markdown_report = generate_blueprint(
                    store_name,
                    store_url,
                    niche,
                    budget,
                    country,
                    business_type,
                    main_goal,
                    current_problem
                )
                file_name = "business_growth_blueprint.html"

        st.success("Report generated successfully!")
        st.markdown(markdown_report)

        st.download_button(
            "Download HTML Presentation",
            data=html_report,
            file_name=file_name,
            mime="text/html"
        )