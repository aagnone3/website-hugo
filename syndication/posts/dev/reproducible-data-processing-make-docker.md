### _Avoiding reproducibility hell with dependency management and containerization_

## Motivation

When performing experiments in data science and machine learning, two main blockers of initial progress are delays building/using &#8220;base code&#8221; and lack of reproducibility.
Thanks to some great open source tools, you don&#8217;t have to be a software guru to circumvent these obstacles and get meaning from your data in a much smoother process.

<p class="has-medium-font-size">
  &#8220;Hey there, I got this error when I ran your code&#8230;can you help me?&#8221;
</p>

<div class="wp-block-image">
  <figure class="aligncenter"><img src="https://anthonyagnone.com/wp-content/uploads/2019/05/Screen-Shot-2019-05-18-at-6.37.49-PM-1024x254.png" alt="" class="wp-image-89" srcset="https://anthonyagnone.com/wp-content/uploads/2019/05/Screen-Shot-2019-05-18-at-6.37.49-PM-1024x254.png 1024w, https://anthonyagnone.com/wp-content/uploads/2019/05/Screen-Shot-2019-05-18-at-6.37.49-PM-300x75.png 300w, https://anthonyagnone.com/wp-content/uploads/2019/05/Screen-Shot-2019-05-18-at-6.37.49-PM-768x191.png 768w, https://anthonyagnone.com/wp-content/uploads/2019/05/Screen-Shot-2019-05-18-at-6.37.49-PM-850x211.png 850w" sizes="(max-width: 1024px) 100vw, 1024px" /><figcaption>oh yeah, that file&#8230;</figcaption></figure>
</div>

&#8230;and it&#8217;s something facepalm-worthy. Here you are, trying to hit the ground running with a friend or colleague on an interesting idea, and you&#8217;re now side-tracked debugging a file-not-found error. Welcome back to your intro programming course!

I&#8217;m sure the owner of the code also loves nothing more than to spend a bunch of time helping someone step through these issues at a snail&#8217;s pace. The sheer euphoria you two have just shared over the promise of recent experimental results has now morphed into unspoken embarrassment and frustration that the demonstration has failed before showing any worth, whatsoever.

<div class="wp-block-image">
  <figure class="aligncenter"><img src="https://anthonyagnone.com/wp-content/uploads/2019/07/over.jpg" alt="" class="wp-image-121" srcset="https://anthonyagnone.com/wp-content/uploads/2019/07/over.jpg 621w, https://anthonyagnone.com/wp-content/uploads/2019/07/over-300x194.jpg 300w" sizes="(max-width: 621px) 100vw, 621px" /></figure>
</div>

But it&#8217;s fine. It&#8217;s fine! Your buddy knows just where to find that missing file. You&#8217;re told that you will have it within minutes, and then you will be on your way!

<p class="has-medium-font-size">
  &#8220;Alright, download that file &#8212; I just emailed it to you. Then run train.py, you should get 98% accuracy in 20 epochs.&#8221;
</p>

Aha! This is it! The time has come to join the ranks of esteemed data magicians, casting one keyboard spell after another, watching your data baby&#8217;s brain get progressively more advanced as it beckons for a role in a new Terminator movie! Let&#8217;s see what we get!

<div class="wp-block-image">
  <figure class="aligncenter"><img src="https://anthonyagnone.com/wp-content/uploads/2019/05/Screen-Shot-2019-05-18-at-6.46.42-PM.png" alt="" class="wp-image-90" srcset="https://anthonyagnone.com/wp-content/uploads/2019/05/Screen-Shot-2019-05-18-at-6.46.42-PM.png 474w, https://anthonyagnone.com/wp-content/uploads/2019/05/Screen-Shot-2019-05-18-at-6.46.42-PM-300x128.png 300w" sizes="(max-width: 474px) 100vw, 474px" /><figcaption>but I did what you said 🙁</figcaption></figure>
</div>

&#8230;yeah, we&#8217;ve all been there.

What could it be? Well, maybe it&#8217;s something obvious. I know python, and I know what your code should be doing. I&#8217;ll just pop open your `train.py` to poke around and&#8230;NOPE.

<div class="wp-block-image">
  <figure class="aligncenter"><img src="https://i.chzbgr.com/full/6157943808/h9C44E570/" alt="" /></figure>
</div>

Don&#8217;t worry, this isn&#8217;t going to be a pinky-waving article about how to always write a software masterpiece and scoff at anything you deem insubordinate. That&#8217;s a sticky subject in general, as it&#8217;s wrought with subjectivity and competing standards. These examples aim to just emphasize how there are a myriad of ways in which we would <span style="text-decoration: underline;">not</span> prefer for new experiments to start.

We&#8217;re interested in _re-producing_ and _improving_ on results in a _convenient_ fashion, not stumbling to re-create past achievements. With that in mind, let&#8217;s have a look at some popular tools that can be used to streamline the start of any new ML software project: [Docker][1] and [Make][2].

## Docker

The python ecosystem has some great features for dealing with dependencies, such as [pip][3] and [virtualenv][4]. These tools allow for one to easily get up and running according to some specification of what needs to be installed to proceed with running some code.

For example, say you have just come across the [scikit-learn][5] library (and it&#8217;s love at first sight, of course). You are particularly drawn to one of its demo examples, but would like to re-produce it with the data housed in a [pandas][6] DataFrame. Furthermore, another project you are working on requires an ancient version of pandas, but you would like to use features available only in a newer version. With pip and virtualenv, you have nothing to fear (&#8230;but fear itself).

```bash
# create and activate environment
virtualenv pandas_like_ml
source pandas_like_ml/bin/activate

# install your desired libraries
pip install --upgrade pip
pip install scikit-learn==0.21.1
pip install pandas==0.19.1

# the main event
python eigenfaces.py -n 20000

# we're done here, so exit the environment
source deactivate
```

When you learn this flow for the first time, you feel freed from the hellish existence that is dependency management. You triumphantly declare that you shall never, ever be conquered again by the wrath of a missing package or a bloated monolithic system environment. However, this unfortunately isn&#8217;t always enough&#8230;

<blockquote class="wp-block-quote is-style-large">
  <p>
    Python environment tools fall short when the dependency is not at the language level, but at the system level.
  </p>
</blockquote>

For example, say you would like to set up your machine learning project with a [MongoDB][7] database backend. No problem! `pip install pymongo` and then we&#8217;re home free! Not so fast&#8230;

<div class="wp-block-image">
  <figure class="aligncenter"><img src="https://anthonyagnone.com/wp-content/uploads/2019/05/Screen-Shot-2019-05-18-at-7.16.23-PM-1-1024x329.png" alt="" class="wp-image-92" srcset="https://anthonyagnone.com/wp-content/uploads/2019/05/Screen-Shot-2019-05-18-at-7.16.23-PM-1-1024x329.png 1024w, https://anthonyagnone.com/wp-content/uploads/2019/05/Screen-Shot-2019-05-18-at-7.16.23-PM-1-300x96.png 300w, https://anthonyagnone.com/wp-content/uploads/2019/05/Screen-Shot-2019-05-18-at-7.16.23-PM-1-768x247.png 768w, https://anthonyagnone.com/wp-content/uploads/2019/05/Screen-Shot-2019-05-18-at-7.16.23-PM-1-850x273.png 850w" sizes="(max-width: 1024px) 100vw, 1024px" /></figure>
</div>

Well&#8230;that didn&#8217;t go as expected. Now, in addition to setting up my library dependencies, we need to also manage a library outside of python? Gah! Further delays! Time to google for the package name for mongoDB&#8230;

What if I don&#8217;t even know what operating system my colleague is using? I can&#8217;t give him some `sudo apt-get install` snippet if he&#8217;s on CentOS. Even more to the point, there&#8217;s no easy way to _automate_ this step for future projects. Make me do something once, I&#8217;ll do it. Make me do it again&#8230;zzzz.

So, we&#8217;re faced with the desire to standardize and automate setting up software libraries and other system dependencies for new data-related endeavors, and sadly our usual python tools have fallen short. Enter Docker: an [engine][8] for running services on an OS as lightweight virtualization packages called _containers_. Docker containers are the realization of the definition of a Docker _image_, which is specified by a file called a `Dockerfile`.

```bash
# you can specify a base image as a foundation to build on
FROM ubuntu:16.04

# make a partition, and specify the working directory
VOLUME /opt
WORKDIR /opt

# install some base system packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-dev \
    python3-pip \
    python3-setuptools

# install some python packages
RUN pip3 install --upgrade pip
RUN pip3 install \
    scikit-learn==0.21.1 \
    pandas==0.19.1

# set the container's entry point, just a bash shell for now.
# this can also be a single program to run, i.e. a python script.
ENTRYPOINT ["/bin/bash"]
```

Think of a Dockerfile as a (detailed) recipe of setup steps we would need to do in order to get the system in the state we would like for the experiment. Examples include things like setting up a database, installing libraries, and initializing a directory structure. If you&#8217;ve ever made a nice shell script to do some setup like this for you, you were not far from the typical Docker workflow. There are many benefits that Docker has over a shell script for this, most notably being _containerization_: with Docker containers, we are abstracted away from the host system that the container is running on. The virtual system that the container is running in is defined in its own process. Because of this, we can have multiple containers running completely different setups, but on the same host machine. How&#8217;s that for some insulation against system dependency hell?

Additionally, we are further insulated from issues like missing files and differences of system state. We know _exactly_ what the system state will be when it is run. We know this because we have made it so via the explicit instructions in the Dockerfile.

To actually build the image, we use a command like the following:

```bash
docker build \
    -t my_first_container \
    -f Dockerfile
```

At this point, we have built the image. With this image, we can repeatedly instantiate it as desired, e.g. to perform multiple experiments.

```bash
docker run \
    --rm \
    -it \
    my_first_container
```

Voila!

If we left at this point and ran in N directions to do various different experiments, these commands may get rather cumbersome to type&#8230;

```bash
docker run \
    --mount type=bind,source="$(pwd)",target=/opt \
    --mount type=bind,source=${CORPORA_DIR},target=/corpora \
    -p ${JUPYTER_PORT}:${JUPYTER_PORT} \
    -ti \
    --rm \
    my_advanced_container \
    jupyter-lab \
        --allow-root \
        --ip=0.0.0.0 \
        --port=${JUPYTER_PORT} \
        --no-browser \
        2>&1 | tee log.txt
```

Don&#8217;t worry if your eyes gloss over at this. The point is it&#8217;s a lot to keep typing. That&#8217;s fine though, we have shell scripts for a reason. With shell scripts, we can encapsulate minute details of making a very specific sequence of commands into something as mindless as `bash doit.sh`. However, consider also a scenario in which your Dockerfile definition depends on other files (i.e. a requirements.txt file or a file of environment variables to use). In this case, we also would like to know _automatically_ when the Docker image needs to be re-created, based on upstream _dependencies_.

So what has four letters, saves you from typing long, arduous commands, and automates dependency management?

## Make

GNU Make is a wonderous tool, gifted to us by the same software movement that has made the digital world what it is today. I&#8217;ll save you a more sparkly introduction and jump into the core abstraction of what it is: a [DAG][9]-based approach to intelligently managing dependencies of actions in a process, in order to _efficiently_ achieve a desired outcome.

Ok, it&#8217;s also a convenient way to compile C code. But focus on the first definition, and think bigger! Re-using the general DAG-based dependency management idea has led to some great tools over the years, like [Drake][10] (not the rapper), [Luigi][11] (not Mario&#8217;s brother), and perhaps most notably [Airflow][12] (AirBnB&#8217;s baby, but now part of the Apache Foundation).

Consider the contrived example below. We&#8217;d like to make predictions on audio-visual data with a trained model. As a new raw image appears, do we need to re-train the model in order to create a prediction? Setting aside applications such as online learning, we do not. Similarly, say we just updated some parameters of our trained model. Do we need to re-cull the raw images, in order to re-create the _same data sample_? Nope.

<div class="wp-block-image">
  <figure class="aligncenter"><img src="https://anthonyagnone.com/wp-content/uploads/2019/05/graph-1.png" alt="" class="wp-image-102" srcset="https://anthonyagnone.com/wp-content/uploads/2019/05/graph-1.png 448w, https://anthonyagnone.com/wp-content/uploads/2019/05/graph-1-300x297.png 300w" sizes="(max-width: 448px) 100vw, 448px" /></figure>
</div>

This is where Make comes into play. By specifying a [Makefile][13] with &#8220;targets&#8221; that correspond to (one or more) desired outputs in the DAG, invoking that target will automatically provide that outcome for you, while only re-invoking dependency processes that are necessary.

Make can be used for pretty much anything that involves actions and their dependencies. It&#8217;s not always right tool in the shed (see [Airflow][12] for this process on distributed applications), but it can get you pretty far. I even used it to generate the image above! Here&#8217;s what the Makefile looks like.

```bash
# the "graph.png" target specifies "graph.dot" as a dependency
# when "graph.png" is invoked, it invokes "graph.dot" only if necessary

graph.png: graph.dot
    dot graph.dot -Tpng > graph.png

# the "graph.dot" target specifies "make_graph.py" as a dependency
# so, this command is only re-run when...
#   1) make_graph.py changes
#   2) graph.dot is not present
graph.dot: make_graph.py
    python make_graph.py
```

## Marrying the Two

So we&#8217;ve ailed over to struggles of reproducible work and introduced great tools to manage environment encapsulation (Docker) and dependency management (Make). These are two pretty cool cats, we should introduce them to each other!<figure class="wp-block-image">

<img src="https://anthonyagnone.com/wp-content/uploads/2019/07/product-school-mEpShydwItI-unsplash-1024x683.jpg" alt="" class="wp-image-116" srcset="https://anthonyagnone.com/wp-content/uploads/2019/07/product-school-mEpShydwItI-unsplash-1024x683.jpg 1024w, https://anthonyagnone.com/wp-content/uploads/2019/07/product-school-mEpShydwItI-unsplash-300x200.jpg 300w, https://anthonyagnone.com/wp-content/uploads/2019/07/product-school-mEpShydwItI-unsplash-768x512.jpg 768w, https://anthonyagnone.com/wp-content/uploads/2019/07/product-school-mEpShydwItI-unsplash-850x567.jpg 850w" sizes="(max-width: 1024px) 100vw, 1024px" /><figcaption>Photo by&nbsp;[Product School][14]&nbsp;on&nbsp;[Unsplash][15]  
P.S. Which one is Docker, and which is Make?</figcaption></figure> 

Let&#8217;s say we&#8217;ve just found the [Magenta][16] project, and would like to set up an environment to consistently run demos and experiments in, without further regard to what version of `this_or_that.py` is running on someone&#8217;s computer. After all, on some level, we don&#8217;t care what version of `this_or_that.py` is running on your machine. What we care is that you are able to experience the same demo/result that the sender has experienced, with minimal effort.

So, let&#8217;s set up a basic `Dockerfile` definition that can accomplish this. Thankfully, the Magenta folks have done the due diligence of creating a [base Docker image][17] themselves, to make it _trivial_ to build from:

```bash
# base image
FROM tensorflow/magenta

# set partition and working directory
VOLUME /opt
WORKDIR /opt

# install base system packages
RUN apt-get update && apt-get install -y \
    vim \
    portaudio19-dev

# install python libraries
COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt

# container entry point
ENTRYPOINT ["/bin/bash"]
```

After specifying the base image as Magenta&#8217;s, we set a working directory on an `/opt` volume, install some system-level and python-level dependencies, and make a simple `bash` entry point until we have a working application. A typical `requirements.txt` file might look like this:

```bash
jupyterlab
seaborn
scikit-learn
matplotlib
pyaudio
```

Awesome. So now we have a specification of our desired environment. We can now make a `Makefile` which handles some of the dependencies at play:

```bash
# use the name of the current directory as the docker image tag
DOCKERFILE ?= Dockerfile
DOCKER_TAG ?= $(shell echo ${PWD} | rev | cut -d/ -f1 | rev)
DOCKER_IMAGE = ${DOCKER_USERNAME}/${DOCKER_REPO}:${DOCKER_TAG}

$(DOCKERFILE): requirements.txt
    docker build \
        -t ${DOCKER_IMAGE} \
        -f ${DOCKERFILE} \
        .

.PHONY image
image: $(DOCKERFILE)

.PHONY: run
run:
     nvidia-docker run \
         --mount type=bind,source="$(shell pwd)",target=/opt \
         -i \
         --rm \
         -t $(DOCKER_IMAGE)
```

This `Makefile` specifies targets for `run`, `image`, and `$(DOCKERFILE)`. The `$(DOCKERFILE)` target lists `requirements.txt` as a dependency, and thus will trigger a re-build of the Docker image when that file changes. The `image` target is a simple alias for the `$(DOCKERFILE)` target. Finally, the `run` target allows a concise call to execute the desired program in the Docker container, as opposed to typing out the laborious command each time.

## One Docker to Rule Them All?

<div class="wp-block-image">
  <figure class="aligncenter"><img src="https://anthonyagnone.com/wp-content/uploads/2019/07/docker-docker-docker-docker-docker-docker.jpg" alt="" class="wp-image-111" srcset="https://anthonyagnone.com/wp-content/uploads/2019/07/docker-docker-docker-docker-docker-docker.jpg 400w, https://anthonyagnone.com/wp-content/uploads/2019/07/docker-docker-docker-docker-docker-docker-300x225.jpg 300w" sizes="(max-width: 400px) 100vw, 400px" /></figure>
</div>

At this point, you may be motivated to go off and define every possible dependency in a `Dockerfile`, in order to never again be plagued with the troubles of ensuring an appropriate environment for your next project. For example, Floydhub has an [all-in-one Docker image][18] for deep learning projects. This image specification includes _numerous_ deep learning frameworks and supporting python libraries.

Don&#8217;t do that!

For the sake of argument, let&#8217;s take that to the limit. After the next 100 projects that you work on, what will your Docker image look like? And what about after the next 1000 projects? Over time, it will just become as bloated as if you had incrementally changed your main OS in each project. This goes against the containerization philosophy of Docker &#8212; your containers should be lightweight while remaining sufficient.

Furthermore, with all of that bloat you lose the ability to sustain multiple directions of projects that require different versions of dependencies. What if one of your projects requires the latest version of Tensorflow to run, but you don&#8217;t want to update the 99 previous projects (and deal with all of the failures the updates bring)?

## Conclusion

In this part of the Towards Efficient and Reproducible (TEAR) ML Workflows series, we&#8217;ve established the basis for making experiments and applications a relatively painless process. We used containerization via Docker to ensure experiments and applications are **reproducible** and easy to execute. We then used some automatic dependency management via Make for keeping experiment pipelines **efficient** and simple to run.<figure class="wp-block-image">

<img src="https://anthonyagnone.com/wp-content/uploads/2019/07/susan-holt-simpson-2nSdQEd-Exc-unsplash-1024x689.jpg" alt="" class="wp-image-114" srcset="https://anthonyagnone.com/wp-content/uploads/2019/07/susan-holt-simpson-2nSdQEd-Exc-unsplash-1024x689.jpg 1024w, https://anthonyagnone.com/wp-content/uploads/2019/07/susan-holt-simpson-2nSdQEd-Exc-unsplash-300x202.jpg 300w, https://anthonyagnone.com/wp-content/uploads/2019/07/susan-holt-simpson-2nSdQEd-Exc-unsplash-768x517.jpg 768w, https://anthonyagnone.com/wp-content/uploads/2019/07/susan-holt-simpson-2nSdQEd-Exc-unsplash-850x572.jpg 850w" sizes="(max-width: 1024px) 100vw, 1024px" /><figcaption>Photo by&nbsp;[Susan Holt Simpson][19]&nbsp;on&nbsp;[Unsplash][20]</figcaption></figure> 

It&#8217;s worth noting that there are numerous alternative solutions to these two; however, they follow the same general _patterns_: containerization gives you reproducibility and automatic dependency management gives you efficiency. From there, the value added in other solutions usually comes down to bells and whistles like cloud integration, scalability, or general ease of use. To each, your own choice of tools.

Next, we’ll look at giving some more power to each of these processes, saving us more time and making them more reusable. We’ll also look at some best practices on how to properly collaborate with others when building these processes.

[1]: https://www.docker.com/
[2]: https://www.gnu.org/software/make/
[3]: https://realpython.com/what-is-pip/
[4]: https://docs.python-guide.org/dev/virtualenvs/
[5]: https://scikit-learn.org
[6]: https://pandas.pydata.org/
[7]: https://www.mongodb.com/
[8]: https://docs.docker.com/engine/docker-overview/
[9]: https://en.wikipedia.org/wiki/Directed_acyclic_graph
[10]: https://github.com/Factual/drake
[11]: https://github.com/spotify/luigi
[12]: https://airflow.apache.org/
[13]: http://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/
[14]: https://unsplash.com/@productschool?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
[15]: https://unsplash.com/search/photos/meet?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
[16]: https://magenta.tensorflow.org/
[17]: https://hub.docker.com/r/tensorflow/magenta/tags
[18]: https://github.com/floydhub/dl-docker
[19]: https://unsplash.com/@shs521?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
[20]: https://unsplash.com/collections/4885214/blog-photos?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText