# Formula-Ai
Trying to teach a neural netwrok to play F1 22

Screengrab : Running the game at 1280 x 720 and display scale at 100% (rather than recommended 125%) just to get more space to work with

Fucntions in Screengrab : 
1) process_img : 
    => Turns the image from BRG to Gray to reduce image dimentions and size
    => Applies canny edge detection algorithm to find edges (found suitable threshold to be 100 and 200)

2) regionOfInterest :
    => Masks the part that's not required and leaves us with region of interest (defined by verticies) using a bitwise and operator