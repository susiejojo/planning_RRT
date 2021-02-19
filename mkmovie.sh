ffmpeg -r 22 -f image2 -i holonomic_data/snap%d.png -s 1000x1000 -pix_fmt yuv420p -y simulation.mp4
