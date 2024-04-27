**NeRF/3DGS - Assignment 3 Report**
=====================================

**Introduction**
---------------

In this assignment, I trained a Neural Radiance Field (NeRF) model on my custom data using nerfstudio, and performed dense structure from motion (SFM) reconstruction.<br>The goal was to reconstruct a 3D scene from a set of 2D images and evaluate the results.

**Data Preparation**
-------------------

I captured a video of a Living Room Shelf using my smartphone and extracted frames from it. I then used COLMAP to generate sparse points from camera calibration, which were used as input data for training the NeRF model.

`ns-process-data video --data ./LivingRoom.MOV --output-dir LivingRoom`

**NeRF Training**
--------------
I trained the NeRF model using nerfstudio with the following configuration:

* Data: `data/nerfstudio/LivingRoom`
* Model: `nerfacto`
* Checkpoint: `outputs/LivingRoom/nerfacto/2024-04-22_08:20:39/nerfstudio_models/step-000029999.ckpt`

`ns-train nerfacto --data data/nerfstudio/LivingRoom/`


Can be loaded using the following command:<br>
`ns-viewer --load-config outputs/LivingRoom/nerfacto/2024-04-22_082039/config.yml`

The training process took approximately 2 hours to complete.

**Dense SFM Reconstruction**
---------------------------
I used COLMAP to perform dense SFM reconstruction on the captured video with the following configuration:<br>

* Data: `data/colmap/LivingRoom`
* Model: `DenseSFM`
* Pointcloud: `data/nerfstudio/LivingRoom/colmap/dense/0/fused.ply`

`data/nerfstudio/LivingRoom/colmap/dense/` folder is copied to google drive due to github size limitation:<br>
[Google Drive Colmap Folder](https://drive.google.com/drive/folders/1LyOOBDPafjhCL_58T4aCGAQo_rEUx-l3?usp=sharing)

The training process took approximately 18 hours to complete.


**Results**
----------

### NeRF Evaluation

I evaluated the trained NeRF model using nerfstudio's evaluation tool, which generated a JSON file containing various metrics. <br>
`ns-eval --load-config ./outputs/LivingRoom/nerfacto/2024-04-22_082039/config.yml` 

The results are as follows:
* PSNR: 25.37
* PSNR_STD: 1.89
* SSIM: 0.80
* SSIM_STD: 0.07
* LPIPS: 0.12
* LPIPS_STD: 0.03

### COLMAP Evaluation

I also evaluated the sparse SFM result from COLMAP using a custom Python script, `Parse3DPoints.py`, which calculated the overall error across all images.

This require conversion of `.bin` files to `.txt` using the COLMAP provided script `read_write_model.py`: <br>`python read_write_model.py --input_model data/nerfstudio/LivingRoom/colmap/sparse/0 --input_format .bin --output_model data/nerfstudio/LivingRoom/colmap/sparse/0 --output_format .txt` 

The results are as follows:
* Overall Average Error: 0.6679106222907204


**Visualizations**
-----------------

I captured an image (`renders/LivingRoom/Colmap Render.png`) from COLMAP's dense SFM result.

<img src="renders/LivingRoom/Colmap Render.png">

I rendered the NeRF model using nerfstudio and generated a video (`renders/LivingRoom/Nerf Render.mp4`) showing the reconstructed 3D scene from different viewpoints. 

<video src="https://github.com/lee3072/CSCI599-Assignment3-NeRF-3DGS/assets/42813404/9c109cee-963a-4e86-97da-6edc5a72675a">
