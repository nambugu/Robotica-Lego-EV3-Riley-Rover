#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile

#Criando a classe para controle de abertura e fechamento da garra acoplada na frente do robo.
class Garra:
    def __init__(self, porta_motor):
        self.motor = Motor(porta_motor) #Definindo Motor
    
    def calibrar(self): #Função que gira o motor da garra para abrir até bater no limite físico
        self.motor.run_until_stalled(-200, then=Stop.COAST, duty_limit=30) # duty_limit=30 limita a força para não forçar as peças
        
        self.motor.reset_angle(0)#Agora que abriu tudo, definimos esse ponto como o ZERO do motor
        
    def abrir(self):
        self.motor.run_target(speed=300, target_angle=0) #Target angle funciona para definirmos o angulo em que a garra alcançara para ser considerada aberta ou fechada.
        
    def fechar(self):
        self.motor.run_until_stalled(-300, then=Stop.HOLD, duty_limit=50) 
        
 #Criando a classe mestra, contem todos os motores e sensores, para controle e codificação do robo e suas ações.       
class RileyRover:
    def __init__(self):
        self.ev3 = EV3Brick()
        
        self.motor_esq = Motor(Port.A)
        self.motor_dir = Motor(Port.B)
        self.base = DriveBase(self.motor_esq, self.motor_dir, wheel_diameter=56, axle_track=104)
        
        self.garra = Garra(Port.C)
        self.sensor_distancia = UltrasonicSensor(Port.S4)
        
    def iniciar_missao(self): #iniciar_missão é onde esta a logica do projeto, onde definimos oque o robo ira fazer ao achar um objeto, e suas ações pós isso.
        self.ev3.speaker.beep()
        self.garra.abrir()
        
        while True:
            distancia = self.sensor_distancia.distance()
            
            if distancia < 150: #aqui definimos a distancia que o sensor ultrasonico vai identificar, em mm. ou seja, todo objeto a menos de 15cm do sensor vai retornar um valor, fazendo o robo realizar uma ação.
                self.base.stop()
                self.ev3.speaker.beep()
                self.garra.fechar()
                wait(2000)
                break
            else: 
                self.base.drive(100, 0)
                
            wait(10)
            
if __name__ == "__main__":
    meu_robo = RileyRover()
    meu_robo.iniciar_missao()
    
