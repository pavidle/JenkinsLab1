pipeline {
    agent { label 'python3' }
    stages {
        stage("Execute tests") {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
                sh 'python3 -m pytest -v --junitxml=report.xml tests'
            }
        }
    }
    post {
        always {
            archive '*.xml'
            junit allowEmptyResults: true, testResults: 'report.xml'
        }
    }
}