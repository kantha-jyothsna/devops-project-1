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
                    docker stop jenkins-test
                    docker rm jenkins-test
                '''
            }
        }
    }
}
