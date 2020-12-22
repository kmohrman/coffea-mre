# coffea-mre
This directory contains files for reproducing an example of an error.

### The error  

We see this error when running in an environment with coffea 0.6.49, but do not see the error when in an environment with coffea 0.6.39. We are not sure if we are just doing something wrong, or if it is maybe due to a difference between the two versions. The error is below:

The error is `ValueError: object of too small depth for desired array` and seems to be caused by this line in the processor `hout['dummy'].fill(sample=dataset, dummy=1, weight=events.size)`.

### How to reproduce the error

Run `python mre_run.py` from an environment where the current version of coffea has been installed. For example:

`conda create --name test-coffea-env python=3.6.8`
`conda activate test-coffea-env`
`conda install -y -c conda-forge coffea`

`git clone https://github.com/kmohrman/coffea-mre.git`
`cd coffea-mre`
`python mre_run.py`

