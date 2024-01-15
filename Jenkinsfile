pipeline {
    
    agent {
        docker { image 'python:3.11.4' }
    }
    
    environment {
            VERSION = '0.0.1'
        }


    stages {
        stage('Prepare image pre reqs') {
                steps {
                    script {
                        sh 'apt update && apt install make'
                    }
                }
            }
        stage('Installing App packages') {
                steps {
                    script {
                        sh 'make install'
                    }
                }
            }
        stage('Code quality check: pep8, typing and sorting') {
                steps {
                    script {
                        sh 'make code-quality'
                    }
                }
            }
        stage('Test') {
            steps {
                echo 'Testing stage..'
                sh 'make test'
            }
        }
        stage('Build') {
            when {
                // Only execute build stage on develop branch
                expression { env.GIT_BRANCH == 'origin/develop' }
            }
            steps {
                echo 'Building stage..'
                // sh 'make test'
            }
        }
        stage('Deploy') {
            when {
                // Only execute deploy stage on develop branch
                expression { env.GIT_BRANCH == 'origin/develop' }
            }
            steps {
                echo 'Deploying stage..'
            }
        }
    }
}