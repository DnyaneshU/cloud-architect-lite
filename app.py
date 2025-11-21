import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Cloud Tower: Architect's Quest",
    page_icon="☁️",
    layout="wide",
)

# --------------------------------------------------
# LAYERS (FLOORS OF THE TOWER)
# --------------------------------------------------
LAYERS = [
    {"key": "networking", "name": "Networking",
     "description": "How users and systems connect to your app over networks and the internet."},
    {"key": "servers", "name": "Servers",
     "description": "The physical machines that provide CPU, RAM, and disk for your workloads."},
    {"key": "virtualization", "name": "Virtualization",
     "description": "VMs/containers that let you run many logical machines on one physical server."},
    {"key": "os", "name": "Operating System (OS)",
     "description": "System software like Linux/Windows that runs on servers and hosts your apps."},
    {"key": "runtime", "name": "Runtime",
     "description": "Language/platform environment like Python, Java, Node.js where your code runs."},
    {"key": "middleware", "name": "Middleware",
     "description": "APIs, queues, gateways, and messaging that connect app components."},
    {"key": "data", "name": "Data Layer",
     "description": "Databases and data models that store and manage structured information."},
    {"key": "storage", "name": "Storage",
     "description": "File/object storage for large files, backups, and unstructured data."},
    {"key": "apps", "name": "Application Layer",
     "description": "How your app is structured: monolith, microservices, or serverless."},
]

# --------------------------------------------------
# SCENARIOS (CHAPTERS)
# --------------------------------------------------
# Each scenario has 9 questions, one per layer (same order as LAYERS).
# Each question: prompt, options, correct index, explanation_correct, explanation_wrong.

SCENARIOS = {
    "social": {
        "title": "Viral Social App",
        "avatar": "🧑‍💻",
        "tagline": "Unpredictable traffic, global users, fast growth.",
        "intro": (
            "You’re building a **social media app** that could go viral any day.\n"
            "Your main challenges are **unpredictable traffic**, **global reach**, and **keeping costs sane**."
        ),
        "questions": [
            # 0 Networking
            {
                "prompt": "Networking: how should users connect globally to your app?",
                "options": [
                    "One small on-prem network in a single city, no extra optimization.",
                    "Use cloud virtual networks (VPCs) plus a CDN-style edge layer for static content.",
                    "Ask every user to VPN into your office network before using the app.",
                ],
                "correct": 1,
                "ex_correct": (
                    "✅ Good choice for a viral social app.\n\n"
                    "- Cloud virtual networks (like VPC) let you define secure subnets in software\n"
                    "- A CDN brings content closer to users worldwide, reducing latency\n"
                    "- You still control routing rules, security groups, and firewalls at the logical level"
                ),
                "ex_wrong": (
                    "💥 **App feels slow and unreliable.**\n\n"
                    "With a single on-prem network or forced VPN, global users experience high latency and\n"
                    "unnecessary friction. Cloud networking + CDNs are key to global scale."
                ),
            },
            # 1 Servers
            {
                "prompt": "Servers: how will you handle compute capacity for unpredictable load?",
                "options": [
                    "Buy fixed on-prem servers sized for your highest possible traffic peak.",
                    "Use cloud VMs with auto-scaling rules that add/remove instances based on load.",
                    "Rent one single cheap VPS and hope for the best.",
                ],
                "correct": 1,
                "ex_correct": (
                    "✅ Auto-scaling cloud servers are ideal here.\n\n"
                    "- You avoid massive up-front hardware costs\n"
                    "- Capacity grows and shrinks as traffic changes\n"
                    "- This demonstrates cloud **elasticity** and **pay-as-you-go** pricing"
                ),
                "ex_wrong": (
                    "💥 **App crashed from overload or wasted money.**\n\n"
                    "Fixed on-prem or one tiny VPS either can’t handle spikes or wastes money\n"
                    "when traffic is low. Cloud compute with scaling is a core benefit here."
                ),
            },
            # 2 Virtualization
            {
                "prompt": "Virtualization: how should you organize compute on top of servers?",
                "options": [
                    "Run everything directly on bare-metal servers with one huge process.",
                    "Use VMs/containers to isolate services and let the cloud orchestrate them.",
                    "Avoid virtualization and run dev, test, prod all on the same OS instance.",
                ],
                "correct": 1,
                "ex_correct": (
                    "✅ Using VMs/containers with orchestration is the right call.\n\n"
                    "- You isolate services for safety and easier deployments\n"
                    "- The cloud can schedule containers across nodes\n"
                    "- This is the **virtualization** layer doing real work for you"
                ),
                "ex_wrong": (
                    "💥 **Deployment chaos and resource conflicts.**\n\n"
                    "Without proper virtualization, one bug or heavy process can take down everything.\n"
                    "Cloud-native apps rely heavily on VMs/containers."
                ),
            },
            # 3 OS
            {
                "prompt": "OS: how should operating systems be managed?",
                "options": [
                    "Manually SSH into each server and patch OS by hand at random times.",
                    "Use cloud images and automation/managed OS services to apply updates consistently.",
                    "Ignore OS updates completely to avoid downtime.",
                ],
                "correct": 1,
                "ex_correct": (
                    "✅ Managed or automated OS updates reduce toil and risk.\n\n"
                    "- You still choose OS families (Linux/Windows), but\n"
                    "- Cloud tooling handles patching and consistency\n"
                    "- This reduces attack surface and maintenance at the OS layer"
                ),
                "ex_wrong": (
                    "💥 **Your app became vulnerable or inconsistent.**\n\n"
                    "Ignoring or manually patching OSes doesn’t scale. Vulnerabilities appear,\n"
                    "and different servers behave differently."
                ),
            },
            # 4 Runtime
            {
                "prompt": "Runtime: how will you run your Python/Node/Java code?",
                "options": [
                    "Install runtimes manually on ad-hoc servers with no version control.",
                    "Use a managed runtime or serverless platform where the provider runs the runtime.",
                    "Compile everything into a single binary and hope it runs everywhere.",
                ],
                "correct": 1,
                "ex_correct": (
                    "✅ Managed runtimes/serverless are powerful for social apps.\n\n"
                    "- The provider patches languages and runtimes\n"
                    "- You focus on business logic\n"
                    "- This is the **platform / runtime** layer being delegated to cloud"
                ),
                "ex_wrong": (
                    "💥 **Runtime mismatch and deployment bugs.**\n\n"
                    "Ad-hoc runtimes often lead to 'works on my machine' issues and security gaps."
                ),
            },
            # 5 Middleware
            {
                "prompt": "Middleware: how should app components communicate?",
                "options": [
                    "Hard-code direct calls between every service; no queues or APIs.",
                    "Use APIs and managed queues/streams to connect services loosely.",
                    "Have all services write messages into a shared text file.",
                ],
                "correct": 1,
                "ex_correct": (
                    "✅ APIs + managed queues/streams make your app more resilient.\n\n"
                    "- Spikes in one component can be buffered\n"
                    "- Middleware like message queues is a core cloud building block\n"
                    "- This reduces tight coupling in the **middleware** layer"
                ),
                "ex_wrong": (
                    "💥 **Tight coupling caused cascading failures.**\n\n"
                    "Without proper middleware, one slow service can block the entire app."
                ),
            },
            # 6 Data
            {
                "prompt": "Data: how will you store user profiles, posts, and relationships?",
                "options": [
                    "Single on-prem SQL server with no replication or backups.",
                    "Use a managed database service with replication and automated backups.",
                    "Store complex data only in flat CSV files on disk.",
                ],
                "correct": 1,
                "ex_correct": (
                    "✅ Managed database services match a social app well.\n\n"
                    "- Built-in replication and backup\n"
                    "- Scaling options without manual hardware work\n"
                    "- You still design schemas and queries at the **data** layer"
                ),
                "ex_wrong": (
                    "💥 **Data loss or poor performance.**\n\n"
                    "A single DB with no redundancy or a pile of CSVs cannot handle\n"
                    "real social data at scale."
                ),
            },
            # 7 Storage
            {
                "prompt": "Storage: where should you store user-uploaded images and videos?",
                "options": [
                    "On a single VM’s local disk.",
                    "In scalable cloud object storage designed for large files.",
                    "Inside your relational database as large BLOB fields.",
                ],
                "correct": 1,
                "ex_correct": (
                    "✅ Cloud object storage is made for this use case.\n\n"
                    "- Very high durability\n"
                    "- Almost infinite scale\n"
                    "- Pay for what you store\n"
                    "- This is the **storage** layer in the cloud world"
                ),
                "ex_wrong": (
                    "💥 **Storage filled up or became slow.**\n\n"
                    "Single disks and DB BLOBs are not designed for huge numbers of large files."
                ),
            },
            # 8 Apps
            {
                "prompt": "Application layer: how do you structure the app?",
                "options": [
                    "One huge monolith on a single server.",
                    "A set of services or functions that can scale independently in the cloud.",
                    "A cron job that runs once a day and emails users a static page.",
                ],
                "correct": 1,
                "ex_correct": (
                    "✅ Cloud-friendly architectures split the app logically.\n\n"
                    "- Different parts of the app can scale independently\n"
                    "- Failures are more isolated\n"
                    "- This is how the **application** layer leverages cloud under it"
                ),
                "ex_wrong": (
                    "💥 **Single point of failure at the app layer.**\n\n"
                    "A giant monolith on one server makes it hard to scale and easy to break."
                ),
            },
        ],
    },
    "bank": {
        "title": "Secure Banking Portal",
        "avatar": "👩‍💼",
        "tagline": "High security, strict regulations, and zero tolerance for leaks.",
        "intro": (
            "You’re designing an **online banking portal**.\n"
            "Your main challenges are **security**, **compliance**, and **reliability**."
        ),
        "questions": [
            # 0 Networking
            {
                "prompt": "Networking: how should users and branches connect?",
                "options": [
                "Use a secure network: private subnets, firewalls, and VPNs / private links.",
                "Expose all databases directly to the public internet for easier access.",
                "Connect branches over open HTTP with no encryption.",
                ],
                "correct": 0,
                "ex_correct": (
                    "✅ Correct. Banking systems rely on **private networking and encryption**.\n\n"
                    "- VPNs/private links protect data in transit\n"
                    "- Private subnets and firewalls limit exposure\n"
                    "- This is the **networking** layer securing sensitive systems"
                ),
                "ex_wrong": (
                    "💥 **Data intercepted or exposed.**\n\n"
                    "Publicly exposing core systems or using unencrypted links is unacceptable\n"
                    "for financial data."
                ),
            },
            # 1 Servers
            {
                "prompt": "Servers: where do you run core banking systems?",
                "options": [
                    "Only on transient cloud spot instances that can disappear anytime.",
                    "On well-controlled on-prem or dedicated cloud servers with strong governance.",
                    "On random employee laptops acting as servers.",
                ],
                "correct": 1,
                "ex_correct": (
                    "✅ Controlled, governed servers are key.\n\n"
                    "- Banks may use on-prem, private cloud, or dedicated cloud resources\n"
                    "- But they keep strict control and monitoring over these servers\n"
                    "- The **server** layer must be predictable and auditable"
                ),
                "ex_wrong": (
                    "💥 **Unreliable or non-compliant compute.**\n\n"
                    "Core banking workloads cannot run on disposable or unmanaged machines."
                ),
            },
            # 2 Virtualization
            {
                "prompt": "Virtualization: how do you isolate different banking services?",
                "options": [
                    "Run all services in a single OS instance with no separation.",
                    "Use VMs/containers with strict policies and network segmentation.",
                    "Let all services share the same credentials and file system.",
                ],
                "correct": 1,
                "ex_correct": (
                    "✅ Isolation via VMs/containers is essential.\n\n"
                    "- Reduces blast radius if one component is compromised\n"
                    "- Enables separate update cycles and policies\n"
                    "- This is the **virtualization** layer supporting security"
                ),
                "ex_wrong": (
                    "💥 **One breach exposed everything.**\n\n"
                    "Without isolation, a single vulnerability can compromise multiple services."
                ),
            },
            # 3 OS
            {
                "prompt": "OS: how do you manage operating systems for banking workloads?",
                "options": [
                    "Consistent, hardened OS images with regular, audited patching.",
                    "Random OS versions installed manually with no patching strategy.",
                    "Unsupported OS versions that never receive security fixes.",
                ],
                "correct": 0,
                "ex_correct": (
                    "✅ Hardened, consistently patched OSes are mandatory.\n\n"
                    "- Standard images reduce drift\n"
                    "- Regular patches close vulnerabilities\n"
                    "- The **OS** layer is a key security boundary"
                ),
                "ex_wrong": (
                    "💥 **Security audit failed at the OS layer.**\n\n"
                    "Out-of-date or inconsistent OSes are a common cause of breaches."
                ),
            },
            # 4 Runtime
            {
                "prompt": "Runtime: how do you handle application runtimes (e.g. Java, .NET)?",
                "options": [
                    "Use approved, supported runtimes with controlled updates and testing.",
                    "Let each developer install any runtime they like directly on prod.",
                    "Run unmaintained runtime versions from many years ago.",
                ],
                "correct": 0,
                "ex_correct": (
                    "✅ Controlled runtimes keep the platform stable.\n\n"
                    "- Security patches can be tested and rolled out\n"
                    "- Behavior is predictable across environments\n"
                    "- This is **runtime governance**, not chaos"
                ),
                "ex_wrong": (
                    "💥 **Runtime-level vulnerabilities and inconsistencies.**\n\n"
                    "Uncontrolled runtimes make it impossible to ensure secure, predictable behavior."
                ),
            },
            # 5 Middleware
            {
                "prompt": "Middleware: how do you connect internal banking services?",
                "options": [
                    "Use secure message buses, APIs, and audited service-to-service communication.",
                    "Allow direct DB access from every app without any abstraction.",
                    "Exchange CSVs by email between teams as the main integration.",
                ],
                "correct": 0,
                "ex_correct": (
                    "✅ Secure middleware is critical.\n\n"
                    "- APIs/gateways enforce authentication and authorization\n"
                    "- Message buses enable reliable, traceable communication\n"
                    "- This makes the **middleware** layer a control point"
                ),
                "ex_wrong": (
                    "💥 **Integration errors and security gaps.**\n\n"
                    "Direct DB access everywhere or ad-hoc file passing is fragile and insecure."
                ),
            },
            # 6 Data
            {
                "prompt": "Data: where should core customer data (balances, transactions) live?",
                "options": [
                    "In a well-controlled private/ on-prem or private cloud database, with encrypted backups (possibly in public cloud).",
                    "In a public, world-readable cloud bucket for convenience.",
                    "Across random spreadsheets on employees’ desktops.",
                ],
                "correct": 0,
                "ex_correct": (
                    "✅ A controlled primary database with secure backups is ideal.\n\n"
                    "- The main DB stays in a tightly governed environment\n"
                    "- Encrypted backups (including cloud) improve durability and recovery\n"
                    "- This is the **data** layer tuned for compliance"
                ),
                "ex_wrong": (
                    "💥 **Data breach or loss.**\n\n"
                    "Public or ad-hoc data storage breaks confidentiality and integrity requirements."
                ),
            },
            # 7 Storage
            {
                "prompt": "Storage: what about logs, statements, and documents?",
                "options": [
                    "Store them in encrypted, access-controlled storage with retention policies.",
                    "Print everything on paper and stack it in an unlocked room.",
                    "Upload them unencrypted to an anonymous file-sharing site.",
                ],
                "correct": 0,
                "ex_correct": (
                    "✅ Secure, policy-driven storage is the way.\n\n"
                    "- Encryption at rest and in transit\n"
                    "- Controlled access and retention\n"
                    "- The **storage** layer helps with auditability"
                ),
                "ex_wrong": (
                    "💥 **Sensitive documents leaked or lost.**\n\n"
                    "Improper storage of documents/logs is a major compliance violation."
                ),
            },
            # 8 Apps
            {
                "prompt": "Application layer: how should you structure the banking app itself?",
                "options": [
                    "A well-structured application with clear separation of concerns and strong authz/authn.",
                    "Random scripts deployed directly to production with shared admin passwords.",
                    "One giant app that mixes admin, customer, and internal tools in the same UI with no role separation.",
                ],
                "correct": 0,
                "ex_correct": (
                    "✅ Good application design is your final defense.\n\n"
                    "- Clear separation of roles and responsibilities\n"
                    "- Strong authentication/authorization\n"
                    "- The **application** layer must enforce business and security rules"
                ),
                "ex_wrong": (
                    "💥 **Critical access control failure.**\n\n"
                    "Poor app design can undo protections at all lower layers."
                ),
            },
        ],
    },
}

# --------------------------------------------------
# SESSION STATE INITIALIZATION
# --------------------------------------------------

def init_state():
    if "phase" not in st.session_state:
        st.session_state.phase = "splash"   # splash -> scenario_select -> scenario_intro -> layer -> crash/success
        st.session_state.scenario_key = None
        st.session_state.layer_index = 0
        st.session_state.score = 0
        st.session_state.crashed = False
        st.session_state.crash_reason = ""
        st.session_state.crash_layer_name = ""
        st.session_state.feedback_text = ""
        st.session_state.feedback_for_layer = -1  # which layer index feedback belongs to


# --------------------------------------------------
# UI HELPERS
# --------------------------------------------------

def render_tower(current_index: int):
    """Render the Cloud Tower layers on the left side."""
    st.markdown("### 🏢 Cloud Tower")
    for i, layer in enumerate(LAYERS):
        prefix = "▫️"
        if i == current_index:
            prefix = "👉"
            st.markdown(f"**{prefix} Floor {i+1}: {layer['name']}**")
        else:
            st.markdown(f"{prefix} Floor {i+1}: {layer['name']}")


def goto_scenario(key: str):
    st.session_state.scenario_key = key
    st.session_state.layer_index = 0
    st.session_state.score = 0
    st.session_state.crashed = False
    st.session_state.crash_reason = ""
    st.session_state.crash_layer_name = ""
    st.session_state.feedback_text = ""
    st.session_state.feedback_for_layer = -1
    st.session_state.phase = "scenario_intro"


# --------------------------------------------------
# SCREENS
# --------------------------------------------------

def screen_splash():
    st.title("☁️ Cloud Tower: Architect's Quest")
    st.subheader("Learn cloud computing layers by saving (or crashing) real apps.")

    st.markdown(
        """
Welcome! In this game you are a **cloud architect**.

- Choose an application scenario  
- Climb the **Cloud Tower** (all the way from networking to apps)  
- On each floor, make an architectural decision  
- Good choices keep your app alive ✅  
- Bad choices can **crash it** 💥 – and you’ll see why  

Every floor maps to a real layer of cloud computing:

**Networking · Servers · Virtualization · OS · Runtime · Middleware · Data · Storage · Apps**
"""
    )
    st.markdown("---")
    if st.button("🚀 Play"):
        st.session_state.phase = "scenario_select"


def screen_scenario_select():
    st.title("Choose your scenario")

    col1, col2 = st.columns(2)

    with col1:
        s = SCENARIOS["social"]
        st.markdown(f"## {s['avatar']} {s['title']}")
        st.caption(s["tagline"])
        st.write(s["intro"])
        if st.button("Build this app", key="pick_social"):
            goto_scenario("social")

    with col2:
        s = SCENARIOS["bank"]
        st.markdown(f"## {s['avatar']} {s['title']}")
        st.caption(s["tagline"])
        st.write(s["intro"])
        if st.button("Build this app", key="pick_bank"):
            goto_scenario("bank")

    st.markdown("---")
    if st.button("⬅️ Back to home"):
        st.session_state.phase = "splash"


def screen_scenario_intro():
    key = st.session_state.scenario_key
    scenario = SCENARIOS[key]

    st.title(f"{scenario['avatar']} {scenario['title']}")
    st.subheader(scenario["tagline"])
    st.markdown(scenario["intro"])
    st.markdown(
        """
You’ll now climb the **Cloud Tower** floor by floor.

Each floor represents one layer:
Networking → Servers → Virtualization → OS → Runtime → Middleware → Data → Storage → Apps

Make the best choice for this scenario. One bad decision can crash the app!
"""
    )
    st.markdown("---")
    if st.button("Start at Floor 1"):
        st.session_state.phase = "layer"


def screen_layer():
    key = st.session_state.scenario_key
    scenario = SCENARIOS[key]
    layer_index = st.session_state.layer_index
    layer = LAYERS[layer_index]
    question = scenario["questions"][layer_index]

    st.title(f"{scenario['avatar']} {scenario['title']}")
    st.caption(scenario["tagline"])

    left, right = st.columns([1, 2])

    with left:
        render_tower(layer_index)

    with right:
        st.markdown(f"### Floor {layer_index + 1}: {layer['name']}")
        st.caption(layer["description"])
        st.markdown("---")

        # If we already have feedback for this layer, show it and a Next button
        if st.session_state.feedback_for_layer == layer_index and st.session_state.feedback_text:
            st.success(st.session_state.feedback_text)
            st.markdown("---")

            if st.button("➡️ Continue to next floor"):
                # Move to next layer or success screen
                if layer_index + 1 < len(LAYERS):
                    st.session_state.layer_index += 1
                    st.session_state.feedback_text = ""
                    st.session_state.feedback_for_layer = -1
                    st.session_state.phase = "layer"
                else:
                    st.session_state.phase = "success"
            return

        st.write(question["prompt"])

        option_labels = question["options"]
        chosen = st.radio(
            "Choose one:",
            option_labels,
            key=f"layer_{key}_{layer_index}",
        )

        if st.button("✅ Lock in my choice"):
            chosen_index = option_labels.index(chosen)
            if chosen_index == question["correct"]:
                # Correct answer → store feedback, stay on this screen
                st.session_state.score += 1
                st.session_state.feedback_text = question["ex_correct"]
                st.session_state.feedback_for_layer = layer_index
            else:
                # Wrong answer → crash app
                st.session_state.crashed = True
                st.session_state.crash_reason = question["ex_wrong"]
                st.session_state.crash_layer_name = layer["name"]
                st.session_state.phase = "crash"

        st.markdown("---")
        st.caption("Tip: Think about this layer’s role in cost, scalability, security, and responsibility.")


def screen_crash():
    key = st.session_state.scenario_key
    scenario = SCENARIOS[key]

    st.title("💥 Application Crashed!")
    st.subheader(f"Scenario: {scenario['title']}")

    st.error(f"Your app crashed at the **{st.session_state.crash_layer_name}** layer.")
    st.write(st.session_state.crash_reason)

    st.markdown(
        """
Even though the app crashed, this is the main learning point:

> **A single bad choice at any layer (networking, servers, OS, data, etc.) can break the whole system.**

Cloud computing is about choosing **which layers you want to manage** and **which layers you want the provider to manage**.
"""
    )

    st.markdown("---")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🔁 Try this scenario again"):
            goto_scenario(key)

    with col2:
        if st.button("🧭 Choose another scenario"):
            st.session_state.phase = "scenario_select"

    with col3:
        if st.button("🏠 Back to home"):
            st.session_state.phase = "splash"


def screen_success():
    key = st.session_state.scenario_key
    scenario = SCENARIOS[key]

    st.title("🎉 Application Launched Successfully!")
    st.subheader(f"Scenario: {scenario['title']}")
    st.success("You made solid decisions at every layer of the Cloud Tower.")

    total_layers = len(LAYERS)
    st.write(f"✅ Correct decisions: **{st.session_state.score} / {total_layers}**")

    st.markdown("---")
    st.markdown("### Your architecture across all layers")

    for i, layer in enumerate(LAYERS):
        q = scenario["questions"][i]
        correct_option = q["options"][q["correct"]]
        st.markdown(f"**Floor {i+1} – {layer['name']}**")
        st.caption(layer["description"])
        st.markdown(f"- ✅ Your chosen ideal option: **{correct_option}**")
        st.markdown(f"- 💡 Why: {q['ex_correct']}")
        st.markdown("---")

    st.markdown(
        """
### What you just practiced

- Seeing each layer: **Networking · Servers · Virtualization · OS · Runtime · Middleware · Data · Storage · Apps**  
- Understanding how cloud vs on-prem decisions change cost, scale, and responsibility  
- Realizing how **one bad layer decision can crash the app**  
- Getting intuition for why cloud architectures look the way they do
"""
    )

    st.markdown("---")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🔁 Replay this scenario"):
            goto_scenario(key)

    with col2:
        if st.button("🧭 Try another scenario"):
            st.session_state.phase = "scenario_select"

    with col3:
        if st.button("🏠 Back to home"):
            st.session_state.phase = "splash"


# --------------------------------------------------
# MAIN
# --------------------------------------------------

def main():
    init_state()

    phase = st.session_state.phase

    if phase == "splash":
        screen_splash()
    elif phase == "scenario_select":
        screen_scenario_select()
    elif phase == "scenario_intro":
        screen_scenario_intro()
    elif phase == "layer":
        screen_layer()
    elif phase == "crash":
        screen_crash()
    elif phase == "success":
        screen_success()
    else:
        st.error("Unknown phase – resetting game.")
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        init_state()
        screen_splash()


if __name__ == "__main__":
    main()
