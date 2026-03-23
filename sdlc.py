import time

def line():
    print("\n" + "-" * 70 + "\n")

def requirement_analysis():
    line()
    print("📘 SDLC PHASE 1: REQUIREMENT ANALYSIS")
    steps = [
        "Gathering requirements from stakeholders...",
        "Understanding user needs and system expectations...",
        "Documenting functional and non-functional requirements...",
        "Finalizing project scope..."
    ]
    for step in steps:
        print(" -", step)
        time.sleep(0.5)

def planning():
    line()
    print("📝 SDLC PHASE 2: PLANNING")
    steps = [
        "Estimating cost, time, and resources...",
        "Creating project plan and timeline...",
        "Risk identification and mitigation planning...",
        "Team assignment and communication setup..."
    ]
    for step in steps:
        print(" -", step)
        time.sleep(0.5)

def design():
    line()
    print("🎨 SDLC PHASE 3: SYSTEM DESIGN")
    steps = [
        "Designing system architecture...",
        "Creating database schema and API contracts...",
        "Designing UI/UX components...",
        "Preparing design documentation..."
    ]
    for step in steps:
        print(" -", step)
        time.sleep(0.5)

def development():
    line()
    print("💻 SDLC PHASE 4: DEVELOPMENT")
    steps = [
        "Writing code and implementing features...",
        "Integrating modules...",
        "Performing code reviews...",
        "Following coding standards..."
    ]
    for step in steps:
        print(" -", step)
        time.sleep(0.5)

def testing():
    line()
    print("🧪 SDLC PHASE 5: TESTING")
    steps = [
        "Running unit tests and integration tests...",
        "Reporting bugs and issues...",
        "Validating test results...",
        "Preparing test reports..."
    ]
    for step in steps:
        print(" -", step)
        time.sleep(0.5)

def deployment():
    line()
    print("☁️ SDLC PHASE 6: DEPLOYMENT")
    steps = [
        "Deploying application to production...",
        "Configuring servers and services...",
        "Post-deployment testing...",
        "Releasing to end users..."
    ]
    for step in steps:
        print(" -", step)
        time.sleep(0.5)

def maintenance():
    line()
    print("🔧 SDLC PHASE 7: MAINTENANCE")
    steps = [
        "Monitoring system performance...",
        "Fixing issues reported by users...",
        "Releasing updates and patches...",
        "Ensuring long-term system reliability..."
    ]
    for step in steps:
        print(" -", step)
        time.sleep(0.5)

def main():
    print("\n======== SOFTWARE DEVELOPMENT LIFE CYCLE (SDLC) SIMULATION ========\n")
    time.sleep(0.5)

    requirement_analysis()
    planning()
    design()
    development()
    testing()
    deployment()
    maintenance()

    line()
    print("🎉 SDLC PROCESS COMPLETED SUCCESSFULLY!")
    line()

if __name__ == "__main__":
    main()
