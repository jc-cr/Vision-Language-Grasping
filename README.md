# A Joint Modeling of Vision-Language-Action for Target-oriented Grasping in Clutter

This is a docker setup for the above work.


## Setup

### Requirements

- Docker: [Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Docker Compose](https://docs.docker.com/compose/install/)
- Nvidia Docker: [Nvidia Docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)


###  Installation

This installation has been modified to work with docker. Once built, the docker container can be run with the provided docker-compose file.

To build the docker image, follow the steps below:

1. `docker-compose build vilg` some version may run as `docker compose build vilg`


### Running the Docker Container

Once built, any script can be run inside the docker container. Simply update the `command` in the `docker-compose.yml` file to the desired script and run the following command:

1. `docker-compose up vilg` or `docker compose up vilg`


If you need to render via X11, you can use the following command:

```bash
xhost +local:root
docker-compose run vilg
```

This will allow the docker container to connect to the X11 server on the host machine and display the GUI.


---

## Original README
#### Contact

Any question, please let me know: kcxu@zju.edu.cn


### Assets
We provide the processed object models in this [link](https://drive.google.com/drive/folders/1WxKDFXJktoqiP0jmkDZrMCcNNBx5u-YM?usp=drive_link). Please download the file and unzip it in the `assets` folder.

### Pretrained Model
We provide the pretrained model in this [link](https://drive.google.com/drive/folders/1LCuoXX92X8L9wqJTbVqvskjRhTJrDDay?usp=sharing). 


## Training

```
python scripts/train.py
```

## Evaluation
To test the pre-trained model, simply change the location of `--model_path`:

```python
python scripts/test.py --load_model --model_path 'PATH OF YOUR CHECKPOINT FILE'
```

## Demos
<div align="left">

| <img src="images/a.gif" width="150" height="200"/> | <img src="images/b.gif" width="150" height="200" /> |
|:--:|:--:|
|"give me the cup"|"I need a fruit"|
| <img src="images/c.gif" width="150" height="200" title="c" alt="alt text"/>  | <img src="images/d.gif" width="150" height="200"/> |
|"get something to drink"|"grasp a round object"|


## Citation

If you find this work useful, please consider citing:

```
@INPROCEEDINGS{10161041,
  author={Xu, Kechun and Zhao, Shuqi and Zhou, Zhongxiang and Li, Zizhang and Pi, Huaijin and Zhu, Yifeng and Wang, Yue and Xiong, Rong},
  booktitle={2023 IEEE International Conference on Robotics and Automation (ICRA)}, 
  title={A Joint Modeling of Vision-Language-Action for Target-oriented Grasping in Clutter}, 
  year={2023},
  pages={11597-11604},
  doi={10.1109/ICRA48891.2023.10161041}}
```