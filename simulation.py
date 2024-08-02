from kandinsky import fill_rect
from random import random
from time import sleep

class Case:
    def __init__(self, x: int, y: int, value: int = 1): self.x,self.y,self.v = x,y,value
    def __repr__(self) -> str: return str(self.v)
    def isfire(self) -> bool: return self.v == 0

class Matrice:
    def __init__(self, x: int = 110, y: int = 60, N: int = 25, p: float = 0.5, t: float = 0.01, width: int = 3, pas: int = 1, colors: dict = {"1":(0,255,0),"0":(255,0,0),"-1":(85,85,85)}):
        self.x,self.y,self.N,self.p,self.t,self.colors,self.width,self.pas,self.cases = x,y,N,p,t,colors,width,pas,None

    def __getitem__(self, xy: int) -> Case: return self.cases[xy]
    def __iter__(self) -> iter: cases = [] ; _l = [[cases.append(case) for case in line] for line in self.cases] ; del _l ; return iter(cases)
    def fire(self, p: float) -> int: return 1 if random() < p else 0
    def neighbors(self, case: Case) -> bool: return (case.x-1 >= 0 and case.y-1 >= 0 and self[case.x-1][case.y-1].isfire()) or (case.x-1 >= 0 and case.y+1 < self.N and self[case.x-1][case.y+1].isfire()) or (case.x-1 >= 0 and self[case.x-1][case.y].isfire())

    def draw(self):
        for case in self: fill_rect(self.x+case.x*(self.width+self.pas),self.y+case.y*(self.width+self.pas),self.width,self.width,self.colors[str(case.v)])

    def run(self):
        def updates(): self.draw() ; sleep(self.t)
        self.cases = [[Case(x,y) for y in range(self.N)] for x in range(self.N)] ; updates()
        for case in self[0]: case.v = 0 if self.fire(self.p) else 1
        updates()
        for n in range(1,self.N):
            for case in self[n]: case.v = 0 if self.fire(self.p) and self.neighbors(case) else 1
            for line in self[:n]:
                for case in line: case.v = -1 if case.isfire() and self.fire(0.2) else case.v
            updates()