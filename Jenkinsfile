pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t jenkins-dockerapp .'
            }
        }

        stage('Test') {
            steps {
                sh '''
                    docker run -d --name jenkins-test -p 5000:5000 jenkins-dockerapp:latest
                    sleep 3
                    curl --fail http://localhost:5000
                '''
            }
        }
        stage('Credential Test') {
            steps {
                withCredentials([
                   usernamePassword(
                       credentialsId: 'demo-credential',
                       usernameVariable: 'DEMO_USER',
                       passwordVariable: 'DEMO_PASS'
                )
            ]) {
                sh '''
                   echo "Credential username is available: $DEMO_USER"
                   echo "Credential password is available to the script"
                 '''
            }
        }
    }
    

    post {
        always {
            sh '''
                docker stop jenkins-test || true
                docker rm jenkins-test || true
            '''
        }
    }
}
