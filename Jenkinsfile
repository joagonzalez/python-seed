pipeline {
    agent {
        docker { image 'joagonzalez/jenkins_builder:python-3.11.4' }
    }

    environment {
            // Telegram configre
            TOKEN = credentials('telegramToken')
            CHAT_ID = credentials('telegramChatid')

            // Telegram Message Pre Build
            CURRENT_BUILD_NUMBER = "${currentBuild.number}"
            GIT_MESSAGE = sh(returnStdout: true, script: "git log -n 1 --format=%s ${GIT_COMMIT}").trim()
            GIT_AUTHOR = sh(returnStdout: true, script: "git log -n 1 --format=%ae ${GIT_COMMIT}").trim()
            GIT_COMMIT_SHORT = sh(returnStdout: true, script: "git rev-parse --short ${GIT_COMMIT}").trim()
            GIT_INFO = "Branch(Version): ${GIT_BRANCH}\nLast Message: ${GIT_MESSAGE}\nAuthor: ${GIT_AUTHOR}\nCommit: ${GIT_COMMIT_SHORT}"
            TEXT_BREAK = "--------------------------------------------------------------"
            TEXT_PRE_BUILD = "${TEXT_BREAK}\n${GIT_INFO}\n${JOB_NAME} is Building"

            // REGISTRY = 'dockerhub.com'
            // REGISTRY_IMAGE = "$REGISTRY/joagonzalez/"
            // REGISTRY_USER = credentials('registryUser')
            // REGISTRY_PASSWORD = credentials('registryPassword')
            // GIT_COMMIT_SHORT = sh(returnStdout: true, script: "git rev-parse --short ${GIT_COMMIT}").trim()

            VERSION = '0.0.1'

            // Telegram Message Success and Failure
            TEXT_SUCCESS_BUILD = "${JOB_NAME} is Success"
            TEXT_FAILURE_BUILD = "${JOB_NAME} is Failure"
    }

    stages {
        stage('Prepare image pre reqs') {
                steps {
                    sh "curl --location --request POST 'https://api.telegram.org/bot${TOKEN}/sendMessage' --form text='${TEXT_PRE_BUILD}' --form chat_id='${CHAT_ID}'"
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
            }
        }
        stage('Build') {
            when {
                expression {
                    return env.GIT_BRANCH =~ /^origin\/rc-v.*/
                }
            }
            steps {
                echo 'Build only on release candidate branches..'
            }
        }
        stage('Push') {
            when {
                expression {
                    return env.GIT_BRANCH =~ /^origin\/rc-v.*/
                }
            }
            steps {
                echo 'Push new image to docker hub registry..'
            //     sh 'docker login -u $REGISTRY_USER -p $REGISTRY_PASSWORD $REGISTRY'
            //     sh 'docker push $REGISTRY_IMAGE:$GIT_COMMIT_SHORT-jenkins-$CURRENT_BUILD_NUMBER'
            }
        }
        stage('Deploy') {
            when {
                expression {
                    return env.GIT_BRANCH =~ /^origin\/rc-v.*/
                }
            }
            steps {
                echo 'Deploy only on release candidate branches..'
                sh 'make deploy'
            }
        }
        stage('Create release at Github') {
            when {
                expression {
                    return env.GIT_BRANCH =~ /^origin\/master.*/
                }
            }
            steps {
                echo 'Create a new release at Github'
            }
        }
    }

    post {
        success {
            script{
                sh "curl --location --request POST 'https://api.telegram.org/bot${TOKEN}/sendMessage' --form text='${TEXT_SUCCESS_BUILD}' --form chat_id='${CHAT_ID}'"
            }
        }
        failure {
            script{
                sh "curl --location --request POST 'https://api.telegram.org/bot${TOKEN}/sendMessage' --form text='${TEXT_FAILURE_BUILD}' --form chat_id='${CHAT_ID}'"
            }
        }
    }
}