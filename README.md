# PegasusWMS Workflow Visualization

Univeristy project for Numeric Analysis laboratories. Wokrflow visulazization for Pegasus WMS using Python graph-tool library and log data retrived from Pegasus application.

### Requirements: 
 - Python 3
 - graph-tool
 - numpy

### Instaling graph-tool:
Follow instruction steps from https://git.skewed.de/count0/graph-tool/wikis/Installation-instructions  
or run jupyter notebooks from inside the docker image
```
docker run -p 8888:8888 -p 6006:6006 -it -u user -w /home/user tiagopeixoto/graph-tool bash
jupyter notebook --ip 0.0.0.0
```
and connecto to localhost:8888
