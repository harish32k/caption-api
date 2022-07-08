# Caption API

API to get captions from images, using OFA captioning method

OFA Repo link
https://github.com/OFA-Sys/OFA.git

To use this, download the captioning checkpoint from
https://ofa-beijing.oss-cn-beijing.aliyuncs.com/checkpoints/caption_large_best_clean.pt
Or refer the model card and download the required model
https://github.com/OFA-Sys/OFA/blob/main/checkpoints.md

Rename that file to "checkpoints.pt" 
Move checkpoints.pt to a folder named checkpoints and the folder checkpoints should be in the main directory

The directory should look like this
![Directory](/markdown_images/guide1.png "Directory")

The checkpoints folder should contain the captioning checkpoint/model file (checkpoint.pt) as shown
![checkpoint.pt file in checkpoints folder](/markdown_images/guide2.png "checkpoint.pt file in checkpoints folder")


Overall directory structure should look like this
![Directory structure](/markdown_images/guide3.png "Directory structure")

Now the docker image can be built using the Dockerfile

OFA link:
https://github.com/OFA-Sys/OFA.git

More about OFA 

(Wang, P., Yang, A., Men, R., Lin, J., Bai, S., Li, Z., Ma, J., Zhou, C., Zhou, J., & Yang, H. (2022). OFA: Unifying architectures, tasks, and modalities through a simple sequence-to-sequence learning framework. https://doi.org/10.48550/ARXIV.2202.03052)

