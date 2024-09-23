# A Joint Modeling of Vision-Language-Action for Target-oriented Grasping in Clutter
This is the official repository for the paper: A Joint Modeling of **Vi**sion-**L**anguage-Action for Target-oriented **G**rasping in Clutter (ICRA 2023).

[Paper](https://arxiv.org/abs/2302.12610) | [Video](https://www.bilibili.com/video/BV1yh4y1a7Ha/?spm_id_from=333.999.0.0)

![introductory video](images/vilg_video.gif)

We focus on the task of language-conditioned grasping in clutter, in which a robot is supposed to grasp the target object based on a language instruction. Previous works separately conduct visual grounding to localize the target object, and generate a grasp for that object. However, these works require object labels or visual attributes for grounding, which calls for handcrafted rules in planner and restricts the range of language instructions. In this paper, we propose to jointly model vision, language and action with object-centric representation. Our method is applicable under more flexible language instructions, and not limited by visual grounding error. Besides, by utilizing the powerful priors from the pre-trained multi-modal model and grasp model, sample efficiency is effectively improved and the sim2real problem is relived without additional data for transfer. A series of experiments carried out in simulation and real world indicate that our method can achieve better task success rate by less times of motion under more flexible language instructions. Moreover, our method is capable of generalizing better to scenarios with unseen objects and language instructions.

![system overview](images/system.png)

#### Contact

Any question, please let me know: kcxu@zju.edu.cn

## Setup
###  Installation

This installation has been modified to work with docker. The following steps are required to run the code:

1. Build the vilg docker image. The docker-compose file is provided but was setup to work with Nvidia GPUs compatible with CUDA 11.1. `docker-compose build vilg`

The container can now be run with `docker-compose up vilg`. 

To run a specific script such as training or testing, update the `docker-compose.yml` in the `command` section to the desired script. 

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

