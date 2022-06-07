# Splunk .conf22 - DEV1385C Debug Deep Dive
Companion Material

[https://conf.splunk.com/sessions.html?search=dev1385c#/](https://conf.splunk.com/sessions.html?search=dev1385c#/)

# General Debugging Workflow
  1. From Visual Studio Code, **open the folder** of the Splunk app on the Splunk instance containing the thing you want to debug.  For example, to debug a modular input in an app with an ID of `TA-conf22-debugging`, open the following folder in Visual Stuido Code:

    $SPLUNK_HOME/etc/apps/TA-conf22-debugging

  * Do not open the file containing the code of the modular input directly.  Open the folder of the Splunk app.

  2. Add 4 lines of code to the thing you want to debug
  3. Start the thing you want to debug
  4. Debug the thing with Visual Studio Code

## Build
This add-on is built with Splunk's [UCC Generator](https://github.com/splunk/addonfactory-ucc-generator).  Install `ucc-gen` per the instructions. Then, execute the following from the command line in the root of this repository to build the add-on:

    ucc-gen --ta-version=<version>

Example:

    ucc-gen --ta-version=1.0.0

The add-on will be built in an `output` directory in the root of the repository.

## Launch Docker container with add-on

Create a `.env` text file in the root of your cloned repository with the following:

```
SPLUNK_APP_ID=TA-conf22-debugging
SPLUNK_VERSION=latest
SPLUNK_PASSWORD=<SPLUNK ADMIN PASSWORD>

# Optional - SPLUNKBASE_USERNAME and SPLUNKBASE_PASSWORD are used to install apps from Splunkbase when the container is built
SPLUNKBASE_USERNAME=<YOUR SPLUNKBASE USERNAME>
# Create an OS environment variable for your Splunkbase password.  Example:
# export SPLUNKBASE_PASSWORD=<YOUR SPLUNKBASE PASSWORD>

# Optional - install the Splunk Add-on for Visual Studio Code for debugging
SPLUNK_APPS_URL=https://splunkbase.splunk.com/app/4801/release/0.1.2/download
```

Launch the container using the following command from the root of the repository:

    docker compose up -d

# Resources
* [Visual Studio Code](https://code.visualstudio.com/)
* [Splunk Add-on for Microsoft Visual Studio Code](https://splunkbase.splunk.com/app/4801/) - install this on your Splunk instance where the code runs for thing you want to debug.  For example, if debugging a custom search command, install this on your search head.  If debugging a modular input, install this on your forwarder.
* [Splunk Extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=Splunk.splunk)
  * [Splunk Extension Wiki](https://github.com/splunk/vscode-extension-splunk/wiki)
* [Python Extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* [Remote SSH Extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)
* [Remote Containers Extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
* [Docker Extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)
* [Splunk UCC Generator](https://github.com/splunk/addonfactory-ucc-generator)
* [Search command examples](https://github.com/splunk/splunk-sdk-python/tree/master/examples/searchcommands_app)
* [.conf21 DEV1147C - Secrets From the Developer Kitchen - Develop On Splunk Like a Pro With UCC, Visual Studio Code and Git](https://conf.splunk.com/watch/conf-online.html?search=dev1147c)