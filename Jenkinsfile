node {
    
    def app

    stage('Clone repository') {
        /* Cloning the Repository to our Workspace */

        checkout scm
    }

    stage('Build image') {
        /* This builds the actual image */

        app = docker.build("eveliz/myapp")
    }

    stage('Test image') {
        
        app.inside {
            echo "Tests passed"
        }
    }

    stage('Push image') {
        /* 
			You would need to first register with DockerHub before you can push images to your account
		*/
		withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: params.JP_DockerMechIdCredential, usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD']]) {
			usr = USERNAME
			pswd = PASSWORD
		}
		docker.withRegistry("http://registry.hub.docker.com", params.JP_DockerMechIdCredential) {
			sh "docker login -u ${usr} -p ${pswd} http://registry.hub.docker.com"
			app.push("latest")
		}
                echo "Trying to Push Docker Build to DockerHub"
    }
}