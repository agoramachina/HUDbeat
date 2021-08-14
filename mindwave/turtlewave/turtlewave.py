import time, glob, os, io, math
from collections import deque
import numpy as np
import pandas as pd
import turtle
import svgwrite

# define folder and file names
#foldername = "./" + time.strftime("%Y-%m-%d/")
filename = "./turtles/turtle_" + time.strftime("%Y-%m-%d_") + time.strftime("%H-%M-%S") + ".ps"

# Get last n samples of csv file
def get_samples(sample_size):
    with open (file, 'r') as f:
        q = deque(f,sample_size+1)
        dfq = pd.read_csv(io.StringIO('\n'.join(q)))
        dfq.columns = df.columns
        dfv = dfq.values
        return dfq

def draw_turtle(turtle, distance, angle):
    turtle.forward(int(distance*50))
    turtle.left(int(120))
    turtle.forward(int(distance*50))
    turtle.left(int(120))
    turtle.forward(int(distance*50))
    turtle.left(int(120))
    turtle.left(int(angle))
    #turtle.backward(int(distance*10))
    ts.getcanvas().postscript(file=filename)
    
def main():

  # get last n samples
  while (True):

      os.system('cls' if os.name == 'nt' else 'clear')

      samples = 10
      data = get_samples(samples)
      powers = data.iloc[:,4:12]
      print(powers)
      
      deltas = powers.values[:,0]
      thetas = powers.values[:,1]
      alphas = powers.values[:,2]
      Alphas = powers.values[:,3]
      betas  = powers.values[:,4]
      Betas  = powers.values[:,5]
      gammas = powers.values[:,6]
      Gammas = powers.values[:,7]

      #print("Deltas: ", deltas)

      power_log = np.log(powers.values[0,:])
      ldiff = np.subtract(np.log(powers.values[samples-1,:]).round(3), np.log(powers.values[samples-2,:]).round(3))


      print()
      print(power_log)
      print(ldiff)
      
      for t in range(8):
          draw_turtle(turtles[t],power_log[t],ldiff[t])
      #time.sleep(1)

if __name__ == '__main__':
  # Find most recent folder and file
  dir = max([f.path for f in os.scandir('../EEG_data/') if f.is_dir()])
  file = max(glob.glob(os.path.join(dir, 'EEGlog_*.csv')),key=os.path.getctime)

  # get initial data frame
  df = pd.read_csv(file,header=1)
  header = list(df)

  sample_size = 1;

  ts = turtle.Screen()
  ts.bgcolor("black")
  ts.getcanvas().postscript(file=filename)

  
#  turtle.color('white')
#  style = ('Courier', 30, 'italic')
#  turtle.write('Hello World', font=style, align='left')
#  turtle.hideturtle()

  turtles = []
  for t in range(8):
      turtles.append(turtle.Turtle())
      turtles[t].speed(0)
      turtles[t].left(45*t)
  turtles[0].color("red")
  turtles[1].color("orange")
  turtles[2].color("yellow")
  turtles[3].color("green")
  turtles[4].color("lime")
  turtles[5].color("cyan")
  turtles[6].color("blue")
  turtles[7].color("purple")
     
  main()
  
