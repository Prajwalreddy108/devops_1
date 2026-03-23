
import time

# Helper function for formatting
def divider():
    print("\n" + "-" * 50 + "\n")

# SDLC Phases
def requirement_analysis():
    divider()
    print("📘 REQUIREMENT ANALYSIS")
    print(" - Collecting requirements...")
    time.sleep(0.3)
    print(" - Understanding client needs...")
    time.sleep(0.3)
    print(" - Preparing requirement document...")

def planning():
    divider()
    print("📝 PLANNING")
    print(" - Estimating resources and budget...")
    time.sleep(0.3)
    print(" - Creating project plan and timelines...")
    time.sleep(0.3)
    print(" - Identifying risks...")

def design():
    divider()
    print("🎨 SYSTEM DESIGN")
    print(" - Designing architecture...")
    time.sleep(0.3)
    print(" - Database schema design...")
    time.sleep(0.3)
    print(" - Preparing UI/UX sketches...")

def development():
    divider()
    print("💻 DEVELOPMENT")
    print(" - Writing source code...")
    time.sleep(0.3)
    print(" - Implementing modules...")
    time.sleep(0.3)
    print(" - Code review and integration...")

def testing():
    divider()
    print("🧪 TESTING")
    print(" - Running unit & integration tests...")
    time.sleep(0.3)
    print(" - Reporting bugs...")
    time.sleep(0.3)
    print(" - Validating functionality...")

def deployment():
    divider()
    print("🚀 DEPLOYMENT")
    print(" - Deploying application to production...")
    time.sleep(0.3)
    print(" - Performing smoke testing...")
    time.sleep(0.3)
    print(" - Application live for end users...")

def maintenance():
    divider()
    print("🔧 MAINTENANCE")
    print(" - Monitoring system performance...")
    time.sleep(0.3)
    print(" - Releasing updates & patches...")
    time.sleep(0.3)
    print(" - Fixing user‑reported issues...")

# Main function
def main():
    print("\n==== SOFTWARE DEVELOPMENT LIFE CYCLE (SDLC) ====\n")

    requirement_analysis()
    planning()
    design()
    development()
    testing()
    deployment()
    maintenance()

    divider()
    print("🎉 SDLC PROCESS COMPLETED SUCCESSFULLY!")
    divider()

if __name__ == "__main__":
    main()
