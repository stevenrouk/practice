# Testing auto-sklearn

Running auto-sklearn on Windows or Mac can be difficult, so let's just use Docker. We can pull a Docker image for auto-sklearn from here: https://hub.docker.com/r/mfeurer/auto-sklearn/. We could also build one from scratch if we wanted, using the [continuumio/anaconda3](https://github.com/ContinuumIO/docker-images/tree/master/anaconda3) image as the base.

First, we pull the image and run it in interactive mode.

```shell
$ docker pull mfeurer/auto-sklearn
$ docker run -it mfeurer/auto-sklearn bin/bash
```

Now that we're "inside" the Docker container, we can test importing autosklearn using ipython.

```shell
# ipython -c "import autosklearn"
```

If that doesn't throw an error, then we're good to go!

Now, you can start up Jupyter notebooks in the Docker container so that you can access them in your host browser.

```shell
docker run -it -v $PWD:/opt/notebooks -p 8889:8888 mfeurer/auto-sklearn /bin/bash -c "mkdir -p /opt/notebooks && jupyter notebook --notebook-dir=/opt/notebooks --ip='0.0.0.0' --port=8888 --no-browser --allow-root"
```

Make sure to save anything on your host drive (e.g. `opt/notebooks/...` in the example above), because the files aren't persisted in the Docker container after you exit.

Notes:
* In the above container, many packages aren't installed. Here are some of the ones I usually use that aren't installed:
    - statsmodels
    - seaborn
    - matplotlib
* You can install these through Jupyter Notebooks if needed (in a terminal, or in the notebook itself using `!pip install ...`), but a better option would probably be to create a custom Docker image using a Dockerfile.
