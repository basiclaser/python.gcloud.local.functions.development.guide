### Python Google Cloud Functions Development Guide.

Please read this whole document. Please read the comments in each template function in `main.py`.

#### how to install

```
cd myProjectsFolder
git clone git@github.com:basiclaser/python.gcloud.local.development.guide.git
cd python.gcloud.local.development.guide
pip install -r requirements.txt
```

#### how to use

Treat this local project like a normal GIT project. Make commits as you make changes. This will enable you to roll back to previous versions if you make a mistake.

##### development

Working from a local project such as this is recommended over clicking through the google cloud platform to set up functions for a number of reasons. Mainly you get a real text editor that can lint, validate and format your code. It's also much faster to locally test than constantly redeploying your code to test it. Most importantly you can use version control (GIT) to protect your work over time. It would be very dangerous to directly create and edit cloud functions on the google cloud platform website, as you could accidentally break/delete things without any backups.

You can edit your cloud functions in the `main.py` file. Don't delete the comments, as they tell gcloud which functions are which. To test your functions locally (skips rebuild time), run:

```
functions-framework --target=http_template
```

this runs the http_template function in main.py. Then you'll get a URL such as `http://192.168.178.29:8080/` that you can test with - this is a local equivalent of the usual "webhook" URL.

I recommend using the REST client ([link](https://github.com/Huachao/vscode-restclient)) VSCode plugin to organise and write test requests to your HTTP functions (I've made an example in HTTP/post.http).

### deployment

To deploy the http_template function, for gcloud internal use only:

```
gcloud functions deploy http_template \
--runtime python39 --trigger-http --allow-unauthenticated --ingress-settings=internal-only
```

To deploy the pubsub function, and set its trigger to the "MYTOPIC" topic:

```
gcloud functions deploy pubsub_template \
--runtime python39 --trigger-topic=MYTOPIC
```
