<<<<<<< HEAD
node {

    stage('Requirement Analysis') {
        echo "=== SDLC Phase 1: Requirement Analysis ==="
        sh '''
python3 - << 'EOF'
print("Gathering requirements from client...")
print("Understanding the problem and needs...")
EOF
        '''
=======
pipeline {
    agent any

    stages {
        stage('Run Python Script') {
            steps {
                echo "Running Python Script..."
                sh 'python3 demo.py'
            }
        }
>>>>>>> 8a50f84 (Added)
    }

    stage('Planning') {
        echo "=== SDLC Phase 2: Planning ==="
        sh '''
python3 - << 'EOF'
print("Planning resources, timeline, team allocation...")
print("Creating project roadmap...")
EOF
        '''
    }

    stage('Design') {
        echo "=== SDLC Phase 3: System Design ==="
        sh '''
python3 - << 'EOF'
print("Designing architecture, components, data flow...")
print("Creating design documents...")
EOF
        '''
    }

    stage('Destage('Testing') {
    echo "=== SDLC Phase 5: Testing ==="
    sh '''
python3 - << 'EOF'
print("Executing test cases...")
print("Identifying and fixing bugs...")
EOF
    '''
}stage('Deployment') {
    echo "=== SDLC Phase 6: Deployment ==="
    sh '''
python3 - << 'EOF'
print("Deploying application to the server...")
print("Version released to production...")
EOF
    '''
}stage('Maintenance') {
    echo "=== SDLC Phase 7: Maintenance ==="
    sh '''
python3 - << 'EOF'
print("Monitoring application...")
print("Applying patches and updates...")
EOF
    '''
}
