from simulation import Matrice

# Example 1:
T = Matrice()

# Example 2:
#T = Matrice(x=110, y=60, N=25, p=0.8, t=0, width=3, pas=1, colors={"1":(0,255,0),"0":(255,0,0),"-1":(0,255,0)})

# Example 3:
#T = Matrice(x=50, y=1, N=55, p=0.55, t=0)

# Example 4:
#T = Matrice(x=80, y=30, N=15, t=0.025, width=10)

while True: T.run()
