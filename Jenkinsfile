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
                        echo 'Code quality check: pep8, typing and sorting'
                        sh 'make code-quality'
                    }
                }
            }
        stage('Test') {
            steps {
                echo 'Testing stage..'
                sh 'make test'
                echo "branch name is: " + ${env.GIT_BRANCH}
            }
        }
        stage('Build') {
            when {
                expression {
                    return env.GIT_BRANCH =~ /^rc-v.*/
                }
            }
            steps {
                echo 'Build only on release candidate branches..'
            }
        }
    }
}