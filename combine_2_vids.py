from moviepy.editor import VideoFileClip, concatenate_videoclips


clip_1 = VideoFileClip("results/nh_simulation1.mp4")
clip_2 = VideoFileClip("results/nh_simulation2.mp4")
final_clip = concatenate_videoclips([clip_1,clip_2])
final_clip.write_videofile("results/nh_final.mp4")