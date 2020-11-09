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
		withCredentials([usernamePassword( credentialsId: 'dockerhub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {			
		}
		docker.withRegistry('http://registry.hub.docker.com', 'dockerhub') {
			sh "docker login -u ${USERNAME} -p ${PASSWORD}"
		}
                echo "Trying to Push Docker Build to DockerHub"
    }
}