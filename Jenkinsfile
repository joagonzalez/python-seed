pipeline {
    agent {
        docker { image 'joagonzalez/jenkins_builder:python-3.11.4' }
    }

    environment {
            // Repository
            REPOSITORY = 'joagonzalez/python-seed'

            // Telegram configure
            TOKEN = credentials('telegramToken')
            CHAT_ID = credentials('telegramChatid')
            GITHUB_TOKEN = credentials('github-token')

            // Telegram Message Pre Build
            CURRENT_BUILD_NUMBER = "${currentBuild.number}"
            GIT_MESSAGE = sh(returnStdout: true, script: "git log -n 1 --format=%s ${GIT_COMMIT}").trim()
            GIT_AUTHOR = sh(returnStdout: true, script: "git log -n 1 --format=%ae ${GIT_COMMIT}").trim()
            GIT_COMMIT_SHORT = sh(returnStdout: true, script: "git rev-parse --short ${GIT_COMMIT}").trim()

            BRANCH_NAME = "${env.GIT_BRANCH}"
            VERSION = 'default'
            API_VERSION = "placeholder"
            GIT_INFO = "placeholder"
            TEXT_BREAK = "--------------------------------------------------------------"
            TEXT_PRE_BUILD = "placeholder"
            
            // Docker registry config
            REGISTRY = 'joagonzalez'
            REGISTRY_IMAGE_API = "$REGISTRY/python-seed-api"
            DOCKERFILE_PATH_API = "build/calculator/Dockerfile"
            REGISTRY_USER = credentials('registryUser')
            REGISTRY_PASSWORD = credentials('registryPassword')

            // Telegram Message Success and Failure
            TEXT_SUCCESS_BUILD = "${JOB_NAME} is Success"
            TEXT_FAILURE_BUILD = "${JOB_NAME} is Failure"

            // Coveralls
            COVERALL_TOKEN = credentials('coverallToken')
    }

    stages {
        stage('Prepare image pre reqs') {
                steps {
                    script {
                        def branchName = "${BRANCH_NAME}"
                        if (branchName.contains('-')) {
                            VERSION = sh(returnStdout: true, script: "echo ${branchName}").split('-')[1].trim()
                        } else {
                            // Handle the case where there is no '-' in BRANCH_NAME
                            echo "Branch name does not contain '-', setting VERSION to default value"
                            VERSION = "default"
                        }
                        API_VERSION = "${VERSION}-${GIT_COMMIT_SHORT}-${CURRENT_BUILD_NUMBER}"
                        GIT_INFO = "Branch(Version): ${GIT_BRANCH}\nLast Message: ${GIT_MESSAGE}\nAuthor: ${GIT_AUTHOR}\nCommit: ${GIT_COMMIT_SHORT}\nApp Version: ${API_VERSION}"
                        TEXT_PRE_BUILD = "${TEXT_BREAK}\n${GIT_INFO}\n${JOB_NAME} is Building"
                        echo "VERSION: ${VERSION}"
                    }
                    sh "curl --location --request POST 'https://api.telegram.org/bot${TOKEN}/sendMessage' --form text='${TEXT_PRE_BUILD}' --form chat_id='${CHAT_ID}'"
                    sh 'apt update && apt install make'
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
        stage('Publish coverage') {
            when {
                expression {
                    return env.GIT_BRANCH =~ /^origin\/master.*/
                }
            }
            steps {
                echo 'Publish coverage and tests to coveralls..'
                sh "COVERALLS_REPO_TOKEN=${COVERALL_TOKEN} coveralls"
                sh 'make clean'
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
                sh "docker build -t $REGISTRY_IMAGE_API:$API_VERSION -f $DOCKERFILE_PATH_API ."
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
                sh 'docker login -u $REGISTRY_USER -p $REGISTRY_PASSWORD'
                sh "docker push $REGISTRY_IMAGE_API:$API_VERSION"
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
                echo "Deploying version: $API_VERSION and $VERSION to production"
                sh """
                    export API_VERSION=$API_VERSION
                    make deploy
                """
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
                // ${GITHUB_TOKEN}
                sh '''#!/bin/bash
                    LAST_LOG=$(git log --format='%H' --max-count=1 origin/master)
                    echo "LAST_LOG:$LAST_LOG"
                    LAST_MERGE=$(git log --format='%H' --merges --max-count=1 origin/master)
                    echo "LAST_MERGE:$LAST_MERGE"
                    LAST_MSG=$(git log --format='%s' --max-count=1 origin/master)
                    echo "LAST_MSG:$LAST_MSG"
                    VERSION=$(echo $LAST_MSG | grep --only-matching v[0-9].[0-9].[0-9])
                    echo "VERSION:$VERSION"
                    
                    if [[ $LAST_LOG == $LAST_MERGE && -n $VERSION ]]
                    then

                        # Check if the release already exists
                        RELEASE_ID=$(curl -H "Authorization: token $GITHUB_TOKEN" \
                            "https://api.github.com/repos/$REPOSITORY/releases/tags/$VERSION" | jq -r .id)
                        
                        if [[ $RELEASE_ID != "null" ]]
                        then
                            echo "Release with tag $VERSION already exists. Deleting it..."
                            curl -X DELETE -H "Authorization: token $GITHUB_TOKEN" \
                                "https://api.github.com/repos/$REPOSITORY/releases/$RELEASE_ID"
                        fi

                        DATA='{
                            "tag_name": "'$VERSION'",
                            "target_commitish": "master",
                            "name": "'$VERSION'",
                            "body": "'$LAST_MSG'",
                            "draft": false,
                            "prerelease": false
                        }'
                        curl -H "Authorization: token $GITHUB_TOKEN" --data "$DATA" "https://api.github.com/repos/$REPOSITORY/releases"
                    fi
                '''
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