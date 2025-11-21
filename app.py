import streamlit as st
import random

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
# Each scenario has a list "questions" of length 9 (one per layer),
# and each element is a *list* of question dicts. We will pick one
# at random per floor.
# Each question has:
#   prompt, options (list), correct (index), ex_correct, ex_wrong
# --------------------------------------------------

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
            # 0 NETWORKING – list of questions
            [
                {
                    "prompt": "Networking: how should users connect globally to your app?",
                    "options": [
                        "One small on-prem network in a single city, no extra optimization.",
                        "Cloud virtual networks (VPC-like) plus a CDN/edge layer for static content.",
                        "Ask every user to VPN into your office network before using the app.",
                        "Run everything on localhost; only you can access it.",
                        "Let ISPs randomly route traffic without any planning.",
                    ],
                    "correct": 1,
                    "ex_correct": (
                        "✅ Good choice for a viral social app.\n\n"
                        "- Cloud virtual networks let you define secure subnets in software\n"
                        "- A CDN/edge layer brings content closer to users worldwide\n"
                        "- Latency goes down, and you still control routing & firewall rules"
                    ),
                    "ex_wrong": (
                        "💥 **App feels slow and unreliable.**\n\n"
                        "With a single on-prem network or forced VPN, global users get high latency "
                        "and friction. Cloud networking + CDNs are key to serving the world."
                    ),
                },
                {
                    "prompt": "Networking: what should expose your app to the internet?",
                    "options": [
                        "Expose each database server directly to the internet.",
                        "Use a load balancer in front of stateless app instances.",
                        "Let users SSH into app servers and run code manually.",
                        "Use a random IP that changes every hour.",
                        "Only serve traffic on an internal private IP.",
                    ],
                    "correct": 1,
                    "ex_correct": (
                        "✅ A load balancer in front of stateless app instances is ideal.\n\n"
                        "- It distributes traffic automatically\n"
                        "- You can add/remove instances behind it\n"
                        "- It fits perfectly with cloud auto-scaling"
                    ),
                    "ex_wrong": (
                        "💥 **Users can't reliably reach your app, or it's insecure.**\n\n"
                        "Exposing DBs, SSH, or random IPs to the world is not how modern apps are fronted."
                    ),
                },
            ],
            # 1 SERVERS
            [
                {
                    "prompt": "Servers: how will you handle compute capacity for unpredictable load?",
                    "options": [
                        "Buy fixed on-prem servers sized for peak traffic, even if often idle.",
                        "Use cloud VMs with auto-scaling based on CPU/requests.",
                        "Run everything on your personal laptop 24/7.",
                        "Put the app on a single shared hosting plan with no scaling.",
                        "Run one tiny VM and just pray it holds.",
                    ],
                    "correct": 1,
                    "ex_correct": (
                        "✅ Auto-scaling cloud servers are ideal here.\n\n"
                        "- Avoid huge upfront hardware costs\n"
                        "- Capacity grows/shrinks with actual traffic\n"
                        "- Demonstrates cloud **elasticity** and **pay-as-you-go**"
                    ),
                    "ex_wrong": (
                        "💥 **App crashed or wasted a lot of money.**\n\n"
                        "Fixed on-prem or tiny static servers either can't handle spikes or stay idle most of the time."
                    ),
                },
                {
                    "prompt": "Servers: how do you keep instances healthy?",
                    "options": [
                        "Never monitor anything; wait for Twitter complaints.",
                        "Use health checks and replace failed instances automatically.",
                        "Turn servers off at random times to “test resilience”.",
                        "Run everything as root with no logs.",
                        "Keep only one instance; backups are unnecessary.",
                    ],
                    "correct": 1,
                    "ex_correct": (
                        "✅ Health checks + automatic replacement is cloud-native thinking.\n\n"
                        "- Failing instances are removed\n"
                        "- New instances join the pool\n"
                        "- Your app stays up even when individual VMs die"
                    ),
                    "ex_wrong": (
                        "💥 **Silent failures killed your app.**\n\n"
                        "Without monitoring and health checks, you don't know what's broken until users scream."
                    ),
                },
            ],
            # 2 VIRTUALIZATION
            [
                {
                    "prompt": "Virtualization: how should you organize services on servers?",
                    "options": [
                        "Run all services in a single process on a single server.",
                        "Use containers/VMs to isolate services and deploy independently.",
                        "Run everything in a browser tab on your laptop.",
                        "Give every developer SSH root access to prod.",
                        "Put prod and local dev in the same container.",
                    ],
                    "correct": 1,
                    "ex_correct": (
                        "✅ Containers/VMs give you isolation and easier deployments.\n\n"
                        "- One misbehaving service won't kill everything\n"
                        "- Each service can scale separately\n"
                        "- This is the **virtualization** layer doing its job"
                    ),
                    "ex_wrong": (
                        "💥 **One bug took down the whole system.**\n\n"
                        "Without isolation, it's too easy for one process to hog resources or crash everything."
                    ),
                },
                {
                    "prompt": "Virtualization: how do you scale microservices?",
                    "options": [
                        "Run multiple container instances behind a load balancer.",
                        "Run one giant container with every service inside it.",
                        "Run each service on a random home router.",
                        "Avoid microservices; put logic into cron jobs only.",
                        "Use physical servers only, no VMs/containers.",
                    ],
                    "correct": 0,
                    "ex_correct": (
                        "✅ Multiple container instances behind a load balancer is a microservice classic.\n\n"
                        "- Each service can scale horizontally\n"
                        "- Failures affect only that service's instances\n"
                        "- This maximizes the benefit of virtualization"
                    ),
                    "ex_wrong": (
                        "💥 **Scaling and isolation broke down.**\n\n"
                        "Packing everything into one big container or random hosts defeats the purpose of microservices."
                    ),
                },
            ],
            # 3 OS
            [
                {
                    "prompt": "OS: how should OS updates be handled?",
                    "options": [
                        "Never patch OS; downtime is worse than vulnerabilities.",
                        "Use golden images + automatic patching/rollout.\n",
                        "Let each developer log into prod and update OS whenever they want.",
                        "Use 10 different OS versions to “increase diversity”.",
                        "Run beta OS versions only in production.",
                    ],
                    "correct": 1,
                    "ex_correct": (
                        "✅ Golden images + automated patching keep systems secure and consistent.\n\n"
                        "That's how cloud users keep the **OS layer** healthy at scale."
                    ),
                    "ex_wrong": (
                        "💥 **Security holes or inconsistent behavior.**\n\n"
                        "Random or no patching at the OS level is dangerous and unpredictable."
                    ),
                },
                {
                    "prompt": "OS: where should app logs go?",
                    "options": [
                        "Throw them away to keep disks empty.",
                        "Send them to a centralized logging service from each OS instance.",
                        "Store logs only in /tmp and delete on reboot.",
                        "Write logs to a file with no rotation until disk is full.",
                        "Print logs on paper and archive them in a box.",
                    ],
                    "correct": 1,
                    "ex_correct": (
                        "✅ Centralized logging from OS instances is best.\n\n"
                        "- Helps debugging and monitoring\n"
                        "- Works well with auto-scaling instances that come and go"
                    ),
                    "ex_wrong": (
                        "💥 **No useful logs when things broke.**\n\n"
                        "Without proper log handling, production issues are painful to debug."
                    ),
                },
            ],
            # 4 RUNTIME
            [
                {
                    "prompt": "Runtime: how will you manage language runtimes for your app?",
                    "options": [
                        "Let every server have a slightly different runtime version.",
                        "Use container images or managed runtimes with pinned versions.",
                        "Run random nightly builds of runtimes directly in prod.",
                        "Compile everything with unknown flags and hope.",
                        "Change runtime versions in prod before testing.",
                    ],
                    "correct": 1,
                    "ex_correct": (
                        "✅ Containers/managed runtimes with pinned versions keep behavior consistent.\n\n"
                        "This is the **runtime** layer being controlled instead of chaotic."
                    ),
                    "ex_wrong": (
                        "💥 **Different behavior on different servers.**\n\n"
                        "Uncontrolled runtimes cause 'works on my machine' in production too."
                    ),
                },
                {
                    "prompt": "Runtime: how do you scale your stateless web runtime?",
                    "options": [
                        "Add more identical runtime instances behind a load balancer.",
                        "Scale by SSHing into the same instance and starting random background processes.",
                        "Run all requests through a single-threaded runtime instance.",
                        "Turn off runtime instances during peak to save money.",
                        "Run each request as a separate full VM boot.",
                    ],
                    "correct": 0,
                    "ex_correct": (
                        "✅ Stateless runtimes scale by adding more instances.\n\n"
                        "Cloud makes it easy to add/remove runtime containers or functions under load."
                    ),
                    "ex_wrong": (
                        "💥 **Runtime couldn't handle the load.**\n\n"
                        "Relying on a single process or manual hacks doesn't scale."
                    ),
                },
            ],
            # 5 MIDDLEWARE
            [
                {
                    "prompt": "Middleware: how should services communicate?",
                    "options": [
                        "Direct synchronous calls only; if one fails, everything fails.",
                        "Use APIs + message queues/streams to decouple services.",
                        "Send commands via email between teams.",
                        "Write commands into a shared spreadsheet.",
                        "Let services poll random URLs without contracts.",
                    ],
                    "correct": 1,
                    "ex_correct": (
                        "✅ APIs + queues/streams give you reliability and decoupling.\n\n"
                        "This is the **middleware** layer absorbing spikes and failures."
                    ),
                    "ex_wrong": (
                        "💥 **Cascade failure:** one slow service blocked everything.\n\n"
                        "No middleware or very ad-hoc integration makes failures contagious."
                    ),
                },
                {
                    "prompt": "Middleware: how do you process spikes of notifications?",
                    "options": [
                        "Drop half the notifications to keep servers alive.",
                        "Push all messages into a queue and let workers consume at their own pace.",
                        "Block the user request until all notifications are sent.",
                        "Store messages in a local text file and hope it doesn't corrupt.",
                        "Send everything through a single, fragile cron job.",
                    ],
                    "correct": 1,
                    "ex_correct": (
                        "✅ Queues let you handle spikes smoothly.\n\n"
                        "Workers consume messages without blocking the main user path."
                    ),
                    "ex_wrong": (
                        "💥 **Notification system overloaded user requests.**\n\n"
                        "Directly tying user requests to heavy processing causes timeouts."
                    ),
                },
            ],
            # 6 DATA
            [
                {
                    "prompt": "Data: how do you store user profiles and relationships?",
                    "options": [
                        "A single on-prem DB with no replication or backups.",
                        "A managed DB with replication and automated backups.",
                        "Only CSV files on disk, updated manually.",
                        "One big JSON file shared over email.",
                        "Flat text logs that you parse manually.",
                    ],
                    "correct": 1,
                    "ex_correct": (
                        "✅ Managed databases fit this well.\n\n"
                        "- Replication and backups are built in\n"
                        "- You still design schema & queries at the **data** layer"
                    ),
                    "ex_wrong": (
                        "💥 **Data loss or slow queries.**\n\n"
                        "Ad-hoc data storage can't handle a real social network."
                    ),
                },
                {
                    "prompt": "Data: how should you handle analytics queries?",
                    "options": [
                        "Run expensive analytics directly on the production OLTP DB.",
                        "Export data to a separate analytics store or warehouse.",
                        "Ask interns to manually read logs and count.",
                        "Never look at analytics; just guess.",
                        "Use only last 10 users as sample data.",
                    ],
                    "correct": 1,
                    "ex_correct": (
                        "✅ Splitting OLTP (live app DB) from analytics is smart.\n\n"
                        "Analytics have their own data layer tuned for heavy reads."
                    ),
                    "ex_wrong": (
                        "💥 **Analytics queries slowed down the app.**\n\n"
                        "Heavy reads on the main DB hurt real-time user traffic."
                    ),
                },
            ],
            # 7 STORAGE
            [
                {
                    "prompt": "Storage: where should photos & videos live?",
                    "options": [
                        "Local disk of a single VM.",
                        "Cloud object storage designed for large files.",
                        "Inside the main relational DB as huge BLOBs.",
                        "In a zip file emailed to yourself daily.",
                        "On a random USB drive plugged into a server.",
                    ],
                    "correct": 1,
                    "ex_correct": (
                        "✅ Cloud object storage is perfect for media.\n\n"
                        "Huge scale, high durability, pay-as-you-go → ideal **storage** layer choice."
                    ),
                    "ex_wrong": (
                        "💥 **Storage filled or became unreliable.**\n\n"
                        "Single disks or DB BLOBs don't scale for massive media."
                    ),
                },
                {
                    "prompt": "Storage: how do you handle user content lifecycle?",
                    "options": [
                        "Keep everything forever in the hottest storage tier.",
                        "Use lifecycle rules to move older content to cheaper tiers.",
                        "Manually delete random files when disks are full.",
                        "Zip everything once a year and delete originals.",
                        "Trust that users will delete content themselves.",
                    ],
                    "correct": 1,
                    "ex_correct": (
                        "✅ Lifecycle rules control cost over time.\n\n"
                        "Older/rarely used data can move to colder storage automatically."
                    ),
                    "ex_wrong": (
                        "💥 **Storage costs exploded.**\n\n"
                        "Ignoring lifecycle means paying top-tier prices for rarely used data."
                    ),
                },
            ],
            # 8 APPS
            [
                {
                    "prompt": "Apps: how should the social app be structured?",
                    "options": [
                        "One huge monolith on a single server.",
                        "A set of services that can scale and deploy independently.",
                        "A cron job that emails users a static page once a day.",
                        "A script you run manually from your laptop.",
                        "A desktop app only you install.",
                    ],
                    "correct": 1,
                    "ex_correct": (
                        "✅ Services/functions that scale independently are ideal.\n\n"
                        "This is the **application** layer using the power of cloud under it."
                    ),
                    "ex_wrong": (
                        "💥 **Single point of failure at the app layer.**\n\n"
                        "A fragile monolith or manual scripts can't handle viral growth."
                    ),
                },
                {
                    "prompt": "Apps: how do you roll out new versions safely?",
                    "options": [
                        "Deploy directly to all servers at once, no rollback.",
                        "Use rolling or blue/green deployments with health checks.",
                        "Change production code manually with a text editor.",
                        "Deploy to random servers at random times.",
                        "Wait until Friday night and deploy everything then.",
                    ],
                    "correct": 1,
                    "ex_correct": (
                        "✅ Rolling/blue-green deployments protect availability.\n\n"
                        "The app layer evolves safely while cloud infra handles routing."
                    ),
                    "ex_wrong": (
                        "💥 **Bad deployment took the whole app down.**\n\n"
                        "No rollout strategy means high risk with every change."
                    ),
                },
            ],
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
            # 0 NETWORKING
            [
                {
                    "prompt": "Networking: how should users and branches connect?",
                    "options": [
                        "Secure private networking (VPN/private links, private subnets, firewalls).",
                        "Expose all databases directly to the public internet.",
                        "Use only HTTP with no TLS encryption.",
                        "Allow access from any IP with no restrictions.",
                        "Connect via open Wi-Fi hotspots only.",
                    ],
                    "correct": 0,
                    "ex_correct": (
                        "✅ Banking needs **private, encrypted networking**.\n\n"
                        "VPNs/private links + private subnets keep traffic protected."
                    ),
                    "ex_wrong": (
                        "💥 **Traffic could be intercepted or exposed.**\n\n"
                        "Public exposure or no encryption is unacceptable for financial data."
                    ),
                },
                {
                    "prompt": "Networking: what should be publicly reachable?",
                    "options": [
                        "Only the web front-end through a secure gateway.",
                        "Every internal admin API and database endpoint.",
                        "SSH on all servers with password 'bank123'.",
                        "Core transaction systems directly on the internet.",
                        "Nothing at all; even customers cannot reach it.",
                    ],
                    "correct": 0,
                    "ex_correct": (
                        "✅ Only the web/app front-end should be public.\n\n"
                        "All sensitive internals stay behind secure gateways and networks."
                    ),
                    "ex_wrong": (
                        "💥 **Attack surface too big.**\n\n"
                        "Exposing internals (DBs/admin APIs) makes breaches much easier."
                    ),
                },
            ],
            # 1 SERVERS
            [
                {
                    "prompt": "Servers: where do core banking systems run?",
                    "options": [
                        "On dedicated, well-governed servers (on-prem or dedicated cloud).",
                        "On random employee laptops.",
                        "Only on free trial cloud instances that can disappear anytime.",
                        "On old end-of-life hardware with no support.",
                        "On IoT light bulbs in the office.",
                    ],
                    "correct": 0,
                    "ex_correct": (
                        "✅ Core banking workloads need controlled, auditable servers.\n\n"
                        "This is the **server** layer under strong governance."
                    ),
                    "ex_wrong": (
                        "💥 **Unreliable or non-compliant compute.**\n\n"
                        "Critical systems can't run on random/unmanaged machines."
                    ),
                },
                {
                    "prompt": "Servers: how do you ensure high availability?",
                    "options": [
                        "Use multiple servers across availability zones/data centers.",
                        "Run everything on one big server in a broom closet.",
                        "Accept that downtime is normal in banking.",
                        "Turn servers off at night to save power.",
                        "Run hot workload on a backup server only.",
                    ],
                    "correct": 0,
                    "ex_correct": (
                        "✅ Redundancy across zones/locations is essential.\n\n"
                        "Server failures shouldn't bring down banking services."
                    ),
                    "ex_wrong": (
                        "💥 **Single server failure caused outage.**\n\n"
                        "No redundancy at the server layer is a major risk."
                    ),
                },
            ],
            # 2 VIRTUALIZATION
            [
                {
                    "prompt": "Virtualization: how should banking services be isolated?",
                    "options": [
                        "Separate VMs/containers with strict policies and segmentation.",
                        "All services in one OS instance, same user, same folder.",
                        "Test and prod share the exact same container and DB.",
                        "Run services on public shared hosting for cheaper price.",
                        "Let vendors install random software on prod directly.",
                    ],
                    "correct": 0,
                    "ex_correct": (
                        "✅ Isolation reduces blast radius.\n\n"
                        "VMs/containers with segmentation protect other systems if one is compromised."
                    ),
                    "ex_wrong": (
                        "💥 **One compromised service exposed others.**\n\n"
                        "No isolation at the virtualization layer is a big security gap."
                    ),
                },
                {
                    "prompt": "Virtualization: how do you separate environments?",
                    "options": [
                        "Use different accounts/VM groups for dev, test, and prod.",
                        "Use the same VM for dev and prod to save money.",
                        "Let developers SSH into prod and change things directly.",
                        "Share credentials between all environments.",
                        "Allow test data and prod data to mix.",
                    ],
                    "correct": 0,
                    "ex_correct": (
                        "✅ Environment separation is key.\n\n"
                        "Virtualization and accounts help isolate dev/test from prod."
                    ),
                    "ex_wrong": (
                        "💥 **Test or dev changes impacted prod.**\n\n"
                        "Lack of separation at the virtualization/account level is dangerous."
                    ),
                },
            ],
            # 3 OS
            [
                {
                    "prompt": "OS: how should operating systems be managed?",
                    "options": [
                        "Use hardened, standard images with regular, audited patching.",
                        "Allow each team to pick any OS and version for prod.",
                        "Never patch OS to avoid reboots.",
                        "Use unsupported OS versions forever.",
                        "Use beta OS builds on core banking servers.",
                    ],
                    "correct": 0,
                    "ex_correct": (
                        "✅ Hardened, consistently patched OS images are mandatory.\n\n"
                        "The **OS layer** is a critical security boundary."
                    ),
                    "ex_wrong": (
                        "💥 **OS vulnerabilities opened the door to attackers.**\n\n"
                        "Inconsistent or unpatched OSes fail audits and increase breach risk."
                    ),
                },
                {
                    "prompt": "OS: how do you manage admin access?",
                    "options": [
                        "Use least privilege, audited access, and just-in-time elevation.",
                        "Share a single root password with everyone.",
                        "Allow passwordless SSH from any device.",
                        "Never log admin actions to keep logs small.",
                        "Use 'admin/admin' as credentials for convenience.",
                    ],
                    "correct": 0,
                    "ex_correct": (
                        "✅ Controlled, auditable admin access is crucial.\n\n"
                        "OS-level admin is powerful, so it must be tightly managed."
                    ),
                    "ex_wrong": (
                        "💥 **Untracked admin changes violated policy.**\n\n"
                        "Poor OS-level access control is a major compliance issue."
                    ),
                },
            ],
            # 4 RUNTIME
            [
                {
                    "prompt": "Runtime: which policy fits banking apps?",
                    "options": [
                        "Approved, supported runtimes with controlled upgrades.",
                        "Any developer can run any runtime in prod.",
                        "Use experimental runtime builds straight from nightly.",
                        "Mix random runtime versions across servers.",
                        "Never update runtimes after first release.",
                    ],
                    "correct": 0,
                    "ex_correct": (
                        "✅ Runtime governance keeps behavior predictable and secure.\n\n"
                        "This is control at the **runtime** layer."
                    ),
                    "ex_wrong": (
                        "💥 **Runtime vulnerabilities or mismatches occurred.**\n\n"
                        "Uncontrolled runtimes are risky for banking workloads."
                    ),
                },
                {
                    "prompt": "Runtime: how do you handle config for runtimes?",
                    "options": [
                        "Use version-controlled config and secrets management.",
                        "Hard-code secrets directly into application code.",
                        "Store config only in environment variables on random servers.",
                        "Let each server have a different config with no record.",
                        "Ask devs to remember secrets in their heads.",
                    ],
                    "correct": 0,
                    "ex_correct": (
                        "✅ Version-controlled config + secret management is safe.\n\n"
                        "Runtime behavior stays consistent and auditable."
                    ),
                    "ex_wrong": (
                        "💥 **Misconfig or leaked secrets.**\n\n"
                        "Poor handling at the runtime/config layer leads to outages or leaks."
                    ),
                },
            ],
            # 5 MIDDLEWARE
            [
                {
                    "prompt": "Middleware: how do core banking services talk?",
                    "options": [
                        "Secure API gateway + message bus with auth and logging.",
                        "Every app directly queries every DB without rules.",
                        "Pass spreadsheets around by email.",
                        "Use shared file folders with no permissions.",
                        "Let services call each other over unauthenticated HTTP.",
                    ],
                    "correct": 0,
                    "ex_correct": (
                        "✅ Middleware (API gateway, message bus) is the control point.\n\n"
                        "It enforces auth, auditing, and reliability."
                    ),
                    "ex_wrong": (
                        "💥 **Uncontrolled service-to-service calls.**\n\n"
                        "No central middleware means poor visibility and messy security."
                    ),
                },
                {
                    "prompt": "Middleware: how do you handle long-running operations (e.g. batch interest calc)?",
                    "options": [
                        "Queue work and process asynchronously with workers.",
                        "Run everything synchronously in the web request.",
                        "Ask users to refresh the page repeatedly.",
                        "Let operations run only on dev's laptop.",
                        "Run jobs randomly without tracking them.",
                    ],
                    "correct": 0,
                    "ex_correct": (
                        "✅ Queues + workers keep web requests fast and auditable.\n\n"
                        "Middleware absorbs heavy workloads."
                    ),
                    "ex_wrong": (
                        "💥 **Banking portal felt slow and unstable.**\n\n"
                        "Long-running jobs in user requests hurt UX and stability."
                    ),
                },
            ],
            # 6 DATA
            [
                {
                    "prompt": "Data: where should customer balances and transactions live?",
                    "options": [
                        "A well-controlled primary DB (on-prem/private/regulated cloud) with encrypted backups.",
                        "A public, world-readable cloud bucket.",
                        "Random spreadsheets on analysts' desktops.",
                        "A shared network folder with no permissions.",
                        "On memory sticks mailed between branches.",
                    ],
                    "correct": 0,
                    "ex_correct": (
                        "✅ Controlled DB + encrypted backups is the right pattern.\n\n"
                        "The **data** layer must meet strong confidentiality and integrity requirements."
                    ),
                    "ex_wrong": (
                        "💥 **Data breach or loss.**\n\n"
                        "Improper data storage breaks compliance and trust."
                    ),
                },
                {
                    "prompt": "Data: how do you enforce data access rules?",
                    "options": [
                        "Use role-based access control at DB and app layers.",
                        "Give every employee full access to all tables.",
                        "Let apps connect as a single superuser account.",
                        "No access rules; rely on honor system.",
                        "Share DB passwords over chat.",
                    ],
                    "correct": 0,
                    "ex_correct": (
                        "✅ RBAC across data + app layers is essential.\n\n"
                        "Data layer access is audited and controlled."
                    ),
                    "ex_wrong": (
                        "💥 **Too much access caused a policy violation.**\n\n"
                        "Weak data access controls are a major risk."
                    ),
                },
            ],
            # 7 STORAGE
            [
                {
                    "prompt": "Storage: how to store statements & documents?",
                    "options": [
                        "Encrypted, access-controlled storage with retention policies.",
                        "Public file sharing site with open links.",
                        "Printed papers stacked in an unlocked room.",
                        "Unencrypted files on a shared USB drive.",
                        "Temporary folders that get wiped unexpectedly.",
                    ],
                    "correct": 0,
                    "ex_correct": (
                        "✅ Secure storage with retention meets audit needs.\n\n"
                        "The **storage** layer enforces confidentiality & lifecycle."
                    ),
                    "ex_wrong": (
                        "💥 **Documents leaked or lost.**\n\n"
                        "Improper storage is a serious compliance failure."
                    ),
                },
                {
                    "prompt": "Storage: how do you keep logs for audits?",
                    "options": [
                        "Store logs in write-once storage with proper retention and access control.",
                        "Delete logs daily to save space.",
                        "Let logs roll over immediately with no backups.",
                        "Keep logs only on local disks with no replication.",
                        "Never log anything; too noisy.",
                    ],
                    "correct": 0,
                    "ex_correct": (
                        "✅ Immutable/controlled log storage is key for audits.\n\n"
                        "Storage layer can protect log integrity over time."
                    ),
                    "ex_wrong": (
                        "💥 **Insufficient logs during investigation.**\n\n"
                        "Poor log storage makes it hard to prove what happened."
                    ),
                },
            ],
            # 8 APPS
            [
                {
                    "prompt": "Apps: how should you structure the banking portal?",
                    "options": [
                        "Well-structured app with clear layers and strong auth/authz.",
                        "Random scripts deployed directly to prod with shared admin password.",
                        "One UI showing admin and customer views with no separation.",
                        "Allow URL guessing to access any account.",
                        "No login; everything is public.",
                    ],
                    "correct": 0,
                    "ex_correct": (
                        "✅ App layer must enforce business rules & security.\n\n"
                        "Good design at the top of the stack is as important as lower layers."
                    ),
                    "ex_wrong": (
                        "💥 **Critical access control failure.**\n\n"
                        "Bad app-layer design negates protections in all lower layers."
                    ),
                },
                {
                    "prompt": "Apps: how do you handle user sessions?",
                    "options": [
                        "Use secure session management with timeouts and regeneration.",
                        "Store session IDs in URLs forever.",
                        "Use the same session for all users.",
                        "Never expire sessions.",
                        "Let users reuse old session tokens after logout.",
                    ],
                    "correct": 0,
                    "ex_correct": (
                        "✅ Proper session management is non-negotiable.\n\n"
                        "The app layer has to protect user accounts."
                    ),
                    "ex_wrong": (
                        "💥 **Session hijacking risk.**\n\n"
                        "Weak session handling exposes customer accounts."
                    ),
                },
            ],
        ],
    },
}

# --------------------------------------------------
# SESSION STATE INITIALIZATION
# --------------------------------------------------

def init_state():
    if "phase" not in st.session_state:
        st.session_state.phase = "splash"
        st.session_state.scenario_key = None
        st.session_state.layer_index = 0
        st.session_state.score = 0
        st.session_state.crashed = False
        st.session_state.crash_reason = ""
        st.session_state.crash_layer_name = ""
        st.session_state.feedback_text = ""
        st.session_state.feedback_for_layer = -1
        # new: map layer_index -> chosen question index
        st.session_state.current_q_indices = {}


# --------------------------------------------------
# UI HELPERS
# --------------------------------------------------

def render_tower(current_index: int):
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
    st.session_state.current_q_indices = {}
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
- Climb the **Cloud Tower** (Networking → Servers → Virtualization → OS → Runtime → Middleware → Data → Storage → Apps)  
- On each floor, make an architectural decision  
- Good choices keep your app alive ✅  
- Bad choices can **crash it** 💥 – and you’ll see why  
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
**Networking · Servers · Virtualization · OS · Runtime · Middleware · Data · Storage · Apps**

For each floor, one random question will be chosen from a pool.
One bad decision can crash the app, but you can retry that floor.
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

    # pick or reuse random question index for this floor
    q_list = scenario["questions"][layer_index]
    if layer_index not in st.session_state.current_q_indices:
        st.session_state.current_q_indices[layer_index] = random.randrange(len(q_list))
    q_idx = st.session_state.current_q_indices[layer_index]
    question = q_list[q_idx]

    st.title(f"{scenario['avatar']} {scenario['title']}")
    st.caption(scenario["tagline"])

    left, right = st.columns([1, 2])

    with left:
        render_tower(layer_index)

    with right:
        st.markdown(f"### Floor {layer_index + 1}: {layer['name']}")
        st.caption(layer["description"])
        st.markdown("---")

        # already answered correctly? show feedback + next
        if st.session_state.feedback_for_layer == layer_index and st.session_state.feedback_text:
            st.success(st.session_state.feedback_text)
            st.markdown("---")

            if st.button("➡️ Continue to next floor"):
                if layer_index + 1 < len(LAYERS):
                    st.session_state.layer_index += 1
                    st.session_state.feedback_text = ""
                    st.session_state.feedback_for_layer = -1
                    st.session_state.phase = "layer"
                else:
                    st.session_state.phase = "success"
            return

        st.write(question["prompt"])

        chosen = st.radio(
            "Choose one:",
            question["options"],
            key=f"layer_{key}_{layer_index}",
        )

        if st.button("✅ Lock in my choice"):
            chosen_index = question["options"].index(chosen)
            if chosen_index == question["correct"]:
                st.session_state.score += 1
                st.session_state.feedback_text = question["ex_correct"]
                st.session_state.feedback_for_layer = layer_index
            else:
                st.session_state.crashed = True
                st.session_state.crash_reason = question["ex_wrong"]
                st.session_state.crash_layer_name = layer["name"]
                st.session_state.phase = "crash"

        st.markdown("---")
        st.caption("Tip: Think about cost, scalability, security, and who manages this layer (you vs cloud).")


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

> A single bad choice at any layer (networking, servers, OS, data, etc.) can break the whole system.

Cloud computing is about deciding **which layers you manage** and **which layers the provider manages**.
"""
    )

    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("🔁 Retry this floor"):
            # keep same scenario & layer, but pick a new random question for this floor
            layer_index = st.session_state.layer_index
            if layer_index in st.session_state.current_q_indices:
                del st.session_state.current_q_indices[layer_index]
            st.session_state.crashed = False
            st.session_state.crash_reason = ""
            st.session_state.crash_layer_name = ""
            st.session_state.feedback_text = ""
            st.session_state.feedback_for_layer = -1
            st.session_state.phase = "layer"

    with col2:
        if st.button("🔁 Replay entire scenario"):
            goto_scenario(key)

    with col3:
        if st.button("🧭 Choose another scenario"):
            st.session_state.phase = "scenario_select"

    with col4:
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
        q_list = scenario["questions"][i]
        q_idx = st.session_state.current_q_indices.get(i, 0)
        q = q_list[q_idx]
        correct_option = q["options"][q["correct"]]
        st.markdown(f"**Floor {i+1} – {layer['name']}**")
        st.caption(layer["description"])
        st.markdown(f"- ✅ Ideal option: **{correct_option}**")
        st.markdown(f"- 💡 Why: {q['ex_correct']}")
        st.markdown("---")

    st.markdown(
        """
### What you just practiced

- All layers: **Networking · Servers · Virtualization · OS · Runtime · Middleware · Data · Storage · Apps**  
- Cloud vs on-prem decisions for each layer  
- Seeing how different scenarios (social vs banking) prefer different architectures  
- Experiencing how bad choices can crash the app — safely 🙂
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
