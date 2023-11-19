pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // 檢出代碼
                checkout scm
            }
        }

        stage('Build') {
            steps {
                // 添加您的構建步驟
                echo 'Building...'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                // 執行 SonarQube 掃描
                script {
                    def sonarScannerHome = tool 'sonarqube-9.1';
                    withSonarQubeEnv('sonarqube-9.1') {
                        sh "${sonarScannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }

        // 其他階段...
    }
}
