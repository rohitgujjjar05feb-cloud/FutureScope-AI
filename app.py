import streamlit as st

st.set_page_config(page_title="FutureScope AI")

st.title("🚀 FutureScope AI")
st.subheader("Startup Mentor RAG")

idea = st.text_area(
    "Enter your startup idea:",
    placeholder="Example: Food delivery by drone"
)

if st.button("Analyze Startup Idea"):

    st.markdown("## 📈 Market Analysis")
    st.write(
        f"The startup idea '{idea}' targets a growing market with strong potential for innovation and customer convenience."
    )

    st.markdown("## 🏢 Competitor Analysis")
    st.write(
        "Potential competitors include existing delivery companies and logistics startups. A unique value proposition is required."
    )

    st.markdown("## 💰 Funding Opportunities")
    st.write(
        "Funding can be obtained through Startup India, incubators, angel investors, venture capital firms, and innovation grants."
    )

    st.markdown("## ⚠️ Risk Assessment")
    st.write(
        "Key risks include regulatory approvals, operational costs, competition, scalability challenges, and customer adoption."
    )

    st.markdown("## 🛣️ Startup Roadmap")
    st.write(
        """
        Phase 1: Market Research

        Phase 2: Prototype Development

        Phase 3: Pilot Testing

        Phase 4: Funding and Expansion

        Phase 5: Commercial Launch
        """
    )