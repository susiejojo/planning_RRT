ffmpeg -r 5 -f image2 -i nh_wheel_data/snap%d.png -s 1000x1000 -pix_fmt yuv420p -y simulation.mp4
