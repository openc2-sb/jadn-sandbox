# JADN Sandbox

[![OpenC2](https://github.com/ScreamBun/SB_Utils/blob/master/assets/images/openc2.png?raw=true)](https://openc2.org/)
[![Python 3.10](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/downloads/release/python-3100/)
[![Open2C Lang Spec WD 17](https://img.shields.io/badge/Open2C%20Lang%20Spec-WD17-brightgreen)](https://github.com/dlemire60/openc2-oc2ls)

## Background

The JADN Sandbox provides the ability to create, convert, translate, transform, visualize and validate JADN compliant schemas. In addition, for applications that communicate via messaging, the app provides the ability to create and validate data against a schema, as well as, generate test data based on the provided schema. Within JADN Sandbox users can interact with the JADN information modeling tools and create schemas or data based on their application or systems needs or just to learn more about JADN with a hands on approach.
[JADN Sandbox Walkthrough PDF](https://github.com/ScreamBun/jadn-sandbox/blob/develop/documentation/JADNSandboxInfo.pdf).

## Quick Startup

1. Install [Docker](https://docs.docker.com/get-docker/)

2. Pull the latest JADN Sandbox Docker Image (Note: this is needed each time to ensure you are using the very latest version of the JADN Sandbox)

  ```bash
  docker pull screambunn/jadn_sandbox
  ```

3. Run the docker image

  ```bash
  docker run --rm -p 8082:8082 screambunn/jadn_sandbox:latest
  ```

4. Enter the url below in your browser

  <http://localhost:8082/>

5. To stop your image, just hit `ctrl+c` in your terminal or via your docker software.

## Development Startup

Prerequisites:

* [Git](https://git-scm.com/) installed
* [Python](https://www.python.org/downloads/release/python-3100/) installed
* An active [GitHub](https://github.com/ScreamBun/jadn-sandbox) account

1. Clone the JADN Sandbox from GitHub to your local workstation

2. From commandline, go to the directory where you would like the application to live, here's an example:

```bash
cd /home/username/workspace
```

3. Using git, clone the jadn-sandbox repo to your local directory

```bash
git clone https://github.com/ScreamBun/jadn-sandbox.git
```

4. (Optional, specific to Linux and Mac) Create a [virtual environment](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/) for the app

5. Run the startup script to install the app's dependencies and fire up it's servers

```bash
./startup.sh
```

### Alternate Startup

1. Fire up server

```bash
cd server
./start.sh
```

2. In another terminal, fire up the client

yarn build
yarn start

```bash
cd client
yarn
yarn build
yarn start
```

## How To

### Build a Docker Image

Ref: [Docker Image on DockerHub](https://hub.docker.com/repository/docker/screambunn/jadn_sandbox/general)

Important Notes:

* You will need to know the screambunn DockerHub login in order to push a new image.
* A new version tag and image should be pushed after each docker build and push.  
* When you run docker_push.py it will ask for the version # (v[Major].[Minor].[Bug])

1. Run this command once to build the image and push to DockerHub:

```bash
python ./docker_push.py
```

2. To start your image, enter the following, this will start the image without rebuilding

```bash
./docker_run.sh
```

3. If the latest tag is not updating in Docker Hub, take the following steps to realign the tag

Latest:
```bash
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -f ./sever/Dockerfile \
  -t screambunn/jadn_sandbox:latest \
  --push .
```

Specific Version:
```bash
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -f ./sever/Dockerfile \
  -t screambunn/jadn_sandbox:<version> \
  --push .  
```

Or run the following, you can replace 'latest' with a specific version if you have previously built it or pulled it (see quick start).

```bash
docker run --rm -p 8082:8082 screambunn/jadn_sandbox:latest
```

4. Once the build is complete go to here in your browser to verify and run smoke tests

```html
<http://localhost:8082/>
```

### Create a jadnschema Wheel

* See readme under the jadnschema repo

### Build Ruby Image and Container and use locally

Need to start Ruby Container when you are developing and want CBOR conversion logic

1. In a terminal window, from the JADN Sandbox root directory, build the image:

```bash
docker build -t sb-ruby-image -f Dockerfile_sb_ruby .
```

2. Next, build the container (/bin/bash is optional this allows you to immediately investigate the contents of the container)

```bash
docker run -it --name=sb-ruby-container sb-ruby-image /bin/bash
```

3. Go to server / webApp / data / version.toml and change the app_mode to "local".  

4. Your ruby docker container is now ready to be used.

### Develop and Test JADN Schema on the Fly

* When developing and testing JADN Schema, you can link it directly to your virtual environment to avoid recreating wheels.
  * Within your virtual environment view the python dependencies:
    * `pip freeze`
  * Remove the jadnschema wheel:
    * `pip uninstall jadnschema`
  * Add the jadnschema git repo source to the python dependencies:
    * cd to jadnschema
    * `python setup.py develop`
    * `pip freeze`
    * You should see something similar to this:
      -e git+ssh://git@ccoe-gitlab.hii-tsd.com/screamingbunny/schema/jadnschema.git@16ac517baa1499014ba221b7d1b7ffb3cef20ebe#egg=jadnschema
  * Go back to the Web Validator and start the server:
    * `./start.sh`
  * Remember when you are finished, make sure to:
    * recreate the jadnschema wheel, which contains the updated code
    * uninstall the direct link, simply `pip uninstall jadnschema`
    * install the updated jadnschema wheel

  Note: If you update the whl filename/version, then the Dockerfile will need to be updated to use this new filename as well.
