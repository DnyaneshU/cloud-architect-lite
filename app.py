import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Cloud Architect Lite – Scenarios",
    page_icon="☁️",
    layout="centered",
)


# --------------------------------------------------
# SCENARIOS & QUESTIONS
# --------------------------------------------------

# Each scenario is a small story.
# Each question has:
# - prompt: text shown to user
# - options: list of answer choices
# - correct: index of correct option in options[]
# - correct_explanation: text shown on correct answer
# - wrong_explanation: "app crashed" text on wrong answer

SCENARIOS = {
    "social_app": {
        "title": "Viral Social App",
        "avatar": "🧑‍💻",
        "description": (
            "You are building a **social media app** that might go viral any day.\n"
            "User traffic is unpredictable. Sometimes low, sometimes 100x higher."
        ),
        "questions": [
            {
                "prompt": "Q1: For this kind of unpredictable traffic, how should you run your **compute**?",
                "options": [
                    "Buy a few fixed on-prem servers and hope they are enough",
                    "Use cloud compute that can auto-scale up and down",
                    "Host everything on a single cheap shared server",
                ],
                "correct": 1,
                "correct_explanation": (
                    "Great choice! For unpredictable traffic, **cloud compute with auto-scaling** is ideal.\n\n"
                    "- You can automatically add or remove capacity\n"
                    "- You avoid huge upfront hardware costs\n"
                    "- This reflects the scalability advantage of cloud"
                ),
                "wrong_explanation": (
                    "💥 **Application crashed due to overload.**\n\n"
                    "On-prem or fixed small servers could not handle a sudden spike in users.\n"
                    "This shows why **scalability** is a key reason to use cloud compute."
                ),
            },
            {
                "prompt": "Q2: Users will upload millions of photos and videos. Where should you store them?",
                "options": [
                    "On the local disk of one application server",
                    "In a scalable cloud object storage service",
                    "Inside a single relational database as BLOBs",
                ],
                "correct": 1,
                "correct_explanation": (
                    "Correct! **Cloud object storage** (like S3-style services) is designed for:\n\n"
                    "- Massive scale (millions of files)\n"
                    "- High durability (data is replicated)\n"
                    "- Pay-as-you-go cost model\n"
                ),
                "wrong_explanation": (
                    "💥 **Application crashed due to storage failure.**\n\n"
                    "Storing everything on one server or jamming large files into a single DB is not scalable\n"
                    "and becomes a single point of failure. Cloud storage solves this with durability and scale."
                ),
            },
            {
                "prompt": "Q3: Your users are global. How should they reach your app with good performance?",
                "options": [
                    "Host everything in one local data center with no optimizations",
                    "Use cloud virtual networking plus a CDN to serve content closer to users",
                    "Ask users to connect via your office Wi-Fi VPN",
                ],
                "correct": 1,
                "correct_explanation": (
                    "Exactly! **Cloud networking + CDN** means:\n\n"
                    "- Users connect to edge locations near them\n"
                    "- Static content is cached, reducing latency\n"
                    "- Your app feels faster globally\n"
                ),
                "wrong_explanation": (
                    "💥 **Users abandoned the app due to high latency.**\n\n"
                    "A single unoptimized location can't serve global users well.\n"
                    "Cloud networking and CDNs are core ideas for improving global performance."
                ),
            },
        ],
        "success_summary": (
            "You successfully launched a **Viral Social App** using cloud-friendly decisions.\n\n"
            "- Cloud compute handled unpredictable load\n"
            "- Cloud storage handled millions of user files\n"
            "- Cloud networking & CDN gave good experience globally\n\n"
            "This scenario highlighted **scalability, elasticity, and global reach** — core cloud benefits."
        ),
    },
    "bank_app": {
        "title": "Secure Banking Portal",
        "avatar": "👩‍💼",
        "description": (
            "You are building an **online banking portal**.\n"
            "Customer data is highly sensitive and must follow strict regulations."
        ),
        "questions": [
            {
                "prompt": "Q1: What is the **top priority** for this banking application?",
                "options": [
                    "Only lowest possible cost",
                    "High security and compliance",
                    "Making the UI super flashy, security can wait",
                ],
                "correct": 1,
                "correct_explanation": (
                    "Correct. For banking, **security and compliance** come first.\n\n"
                    "Cloud doesn't remove your responsibility, but it gives you security tools\n"
                    "and controls to help meet these requirements."
                ),
                "wrong_explanation": (
                    "💥 **Application failed a security audit.**\n\n"
                    "Banking apps must prioritize security and regulations.\n"
                    "Cloud can still be used, but only with strong security configuration."
                ),
            },
            {
                "prompt": "Q2: Where should the **core customer data** (account balances, transactions) live?",
                "options": [
                    "In a public cloud storage bucket that anyone on the internet can read",
                    "In a well-secured on-prem or private environment, with encrypted backups in the cloud",
                    "On an unencrypted USB drive plugged into a random PC",
                ],
                "correct": 1,
                "correct_explanation": (
                    "Nice! A **hybrid approach** works well here:\n\n"
                    "- Keep core banking data in a tightly controlled private/ on-prem or private cloud setup\n"
                    "- Use the public cloud for encrypted backups and disaster recovery\n"
                    "- This mixes control with cloud resilience"
                ),
                "wrong_explanation": (
                    "💥 **Data breach! Application shut down.**\n\n"
                    "Sensitive banking data must never be stored in public, unencrypted places.\n"
                    "This scenario shows how **data sensitivity** affects cloud vs on-prem choices."
                ),
            },
            {
                "prompt": "Q3: Branch offices and cloud components must communicate securely. How should you connect them?",
                "options": [
                    "Over plain HTTP on the open internet",
                    "Using a secure VPN or dedicated private link between on-prem and cloud",
                    "By emailing CSV files back and forth",
                ],
                "correct": 1,
                "correct_explanation": (
                    "Correct again. **VPNs or private links** are key for hybrid banking systems:\n\n"
                    "- Encrypted connections between on-prem and cloud\n"
                    "- Helps comply with security requirements\n"
                    "- Lets you safely mix cloud services with private systems"
                ),
                "wrong_explanation": (
                    "💥 **Sensitive data intercepted in transit.**\n\n"
                    "Unsecured connections are unacceptable for banking.\n"
                    "This highlights the importance of secure networking in cloud and hybrid designs."
                ),
            },
        ],
        "success_summary": (
            "You successfully designed a **Secure Banking Portal** with a hybrid mindset.\n\n"
            "- Security and compliance were the main drivers\n"
            "- Core data stayed in a tightly controlled environment\n"
            "- Cloud was used carefully for backups and connectivity\n\n"
            "This scenario focused on **security, compliance, and hybrid cloud** thinking."
        ),
    },
}


# --------------------------------------------------
# SESSION STATE INITIALIZATION
# --------------------------------------------------

def init_state():
    if "phase" not in st.session_state:
        st.session_state.phase = "intro"          # intro -> scenario_pick -> question -> summary
        st.session_state.selected_scenario = None
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.session_state.crashed = False
        st.session_state.crash_reason = ""
        st.session_state.crash_question = ""
        st.session_state.feedback_text = ""
        st.session_state.feedback_for_q = -1      # which question index feedback belongs to


# --------------------------------------------------
# UI HELPERS
# --------------------------------------------------

def show_intro():
    st.title("☁️ Cloud Architect Lite")
    st.subheader("Learn cloud fundamentals through interactive scenarios")

    st.markdown(
        """
You’ll play as a **tech decision-maker**.

A friendly character will ask:

> *“What type of application do you want to build?”*

You’ll then:
- Pick a **scenario**
- Answer a few **multiple-choice questions**
- See if your app **succeeds** or **crashes 💥**
- Learn *why* each cloud/on-prem choice was good or bad

All of this focuses on core concepts:
**compute, storage, networking, scalability, cost, security, and cloud vs on-prem.**
"""
    )

    st.markdown("---")
    if st.button("🚀 Start Game"):
        st.session_state.phase = "scenario_pick"


def show_scenario_picker():
    st.header("👋 Meet your product owners")

    col1, col2 = st.columns(2)

    with col1:
        s = SCENARIOS["social_app"]
        st.markdown(f"### {s['avatar']} {s['title']}")
        st.write(s["description"])
        if st.button("Build this app", key="pick_social"):
            start_scenario("social_app")

    with col2:
        s = SCENARIOS["bank_app"]
        st.markdown(f"### {s['avatar']} {s['title']}")
        st.write(s["description"])
        if st.button("Build this app", key="pick_bank"):
            start_scenario("bank_app")

    st.markdown("---")
    if st.button("⬅️ Back to intro"):
        st.session_state.phase = "intro"


def start_scenario(scenario_key: str):
    st.session_state.selected_scenario = scenario_key
    st.session_state.question_index = 0
    st.session_state.score = 0
    st.session_state.crashed = False
    st.session_state.crash_reason = ""
    st.session_state.crash_question = ""
    st.session_state.feedback_text = ""
    st.session_state.feedback_for_q = -1
    st.session_state.phase = "question"


def show_question():
    scenario_key = st.session_state.selected_scenario
    scenario = SCENARIOS[scenario_key]
    q_index = st.session_state.question_index
    questions = scenario["questions"]
    question = questions[q_index]

    st.header(f"{scenario['avatar']} {scenario['title']}")
    st.markdown(scenario["description"])
    st.markdown("---")

    st.subheader(f"Question {q_index + 1} of {len(questions)}")
    st.write(question["prompt"])

    # Options as labels
    option_labels = question["options"]
    selected_label = st.radio(
        "Choose an answer:",
        options=option_labels,
        key=f"q_{scenario_key}_{q_index}"
    )

    # If we already have feedback for this question, show it and a Next button
    if st.session_state.feedback_for_q == q_index and st.session_state.feedback_text:
        st.success(st.session_state.feedback_text)
        st.markdown("---")

        if st.button("➡️ Next", key=f"next_{scenario_key}_{q_index}"):
            # Move to next question or summary
            if q_index + 1 < len(questions):
                st.session_state.question_index += 1
                st.session_state.feedback_text = ""
                st.session_state.feedback_for_q = -1
            else:
                st.session_state.phase = "summary"
        return

    if st.button("✅ Submit answer", key=f"submit_{scenario_key}_{q_index}"):
        # Evaluate answer
        chosen_index = option_labels.index(selected_label)
        correct_index = question["correct"]

        if chosen_index == correct_index:
            # Correct answer: store feedback and stay on same question until user presses Next
            st.session_state.score += 1
            st.session_state.feedback_text = question["correct_explanation"]
            st.session_state.feedback_for_q = q_index
        else:
            # Wrong answer: app crashed, go to summary
            st.session_state.crashed = True
            st.session_state.crash_reason = question["wrong_explanation"]
            st.session_state.crash_question = question["prompt"]
            st.session_state.phase = "summary"

    st.markdown("---")
    st.caption("Tip: Think about scalability, security, and how much you need the cloud to help you.")


def show_summary():
    scenario_key = st.session_state.selected_scenario
    scenario = SCENARIOS[scenario_key]
    total_questions = len(scenario["questions"])

    st.header("📊 Scenario Summary")

    st.markdown(f"### {scenario['avatar']} {scenario['title']}")

    if st.session_state.crashed:
        st.error("💥 Your application crashed during this scenario.")
        st.markdown(f"**Where it failed:** {st.session_state.crash_question}")
        st.write(st.session_state.crash_reason)

        st.markdown(
            """
Even though the app crashed, this is actually useful:

It shows how **one wrong architectural decision** at the compute, storage or networking level\n
can break availability, performance, or security in real life.
"""
        )
    else:
        st.success("🎉 Your application stayed healthy through all questions!")
        st.write(scenario["success_summary"])

    st.markdown("---")
    st.subheader("Your Score")
    st.write(f"✅ Correct answers: **{st.session_state.score} / {total_questions}**")

    st.markdown(
        """
### What you just practiced

- Thinking about **compute**: on-prem vs cloud vs hybrid  
- Deciding **where data should live**: local, cloud, or both  
- Understanding **networking & connectivity** in cloud scenarios  
- Seeing how **wrong choices can 'crash' an application** (overload, insecurity, bad design)
"""
    )

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔁 Play this scenario again"):
            start_scenario(scenario_key)
    with col2:
        if st.button("🧭 Choose another scenario"):
            st.session_state.phase = "scenario_pick"

    st.markdown("---")
    if st.button("🏠 Back to intro"):
        st.session_state.phase = "intro"


# --------------------------------------------------
# MAIN APP
# --------------------------------------------------

def main():
    init_state()

    phase = st.session_state.phase

    if phase == "intro":
        show_intro()
    elif phase == "scenario_pick":
        show_scenario_picker()
    elif phase == "question":
        show_question()
    elif phase == "summary":
        show_summary()
    else:
        st.error("Unknown phase – resetting game.")
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        init_state()
        show_intro()


if __name__ == "__main__":
    main()
