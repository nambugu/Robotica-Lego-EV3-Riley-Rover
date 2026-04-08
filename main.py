#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile

#Criando a classe para controle de abertura e fechamento da garra acoplada na frente do robo.
class Garra:
    def __init__(self, porta_motor):
        self.motor = Motor(porta_motor) #Definindo Motor
        
    def abrir(self):
        self.motor.run_time(300, 5000, then=Stop.HOLD) #Motor abre por 5 segundos.
        
    def fechar(self):
        self.motor.run_time(-300, 5000, then=Stop.HOLD) #Motor Fecha por 5 segundos.
        
 #Criando a classe mestra, contem todos os motores e sensores, para controle e codificação do robo e suas ações.       
class RileyRover:
    def __init__(self):
        self.ev3 = EV3Brick()
        self.ev3.speaker.set_volume(100) #Colocando o volume do speaker do ev3 pro maximo
        
        self.motor_esq = Motor(Port.A) #Definindo a porta fisica do robo em que o motor esta conectado
        self.motor_dir = Motor(Port.B)
        self.base = DriveBase(self.motor_esq, self.motor_dir, wheel_diameter=56, axle_track=104) #Definindo as medidas do robo para o drive base poder funcionar 100%
        
        self.garra = Garra(Port.C) #Definindo a porta fisica em que o motor da garra esta conectado
        self.sensor_distancia = UltrasonicSensor(Port.S4) #Definindo a porta fisica em que o sensor esta conectado
        
    def iniciar_missao(self): #iniciar_missão é onde esta a logica do projeto, onde definimos as ações do robo.

        self.ev3.speaker.beep()
        self.ev3.speaker.play_file(SoundFile.KUNG_FU) #Colocamos um som de kung fu apos o beep inicial, para indicar que o robo começará a andar em busca da sua gelada
        
        while True:
            distancia = self.sensor_distancia.distance()
            
            if distancia < 60: #aqui definimos a distancia que o sensor ultrasonico vai identificar, em mm. ou seja, todo objeto a menos de 6cm do sensor vai retornar um valor, fazendo o robo realizar uma ação.
                self.base.stop()
                self.ev3.speaker.beep()
                self.garra.fechar()
                wait(2000)

                self.base.turn(210)
                self.base.drive(250, 0)
                wait(3000)
                self.base.stop()
                self.garra.abrir()
                self.ev3.speaker.play_file(SoundFile.FANFARE)
                self.base.drive(-200, 0)
                wait(3000)
                self.base.stop()

                self.base.settings(250, 250, 600, 600) #Definindo as configurações do self.base para que o robo faça a dancinha com mais velocidade.
                self.base.turn(30)
                self.base.turn(-60)
                self.base.turn(60)
                self.base.turn(-60)
                self.base.turn(720)
                
                break
            else: 
                self.base.drive(250, 0)
                
            wait(10)
            
if __name__ == "__main__":
    meu_robo = RileyRover()
    meu_robo.iniciar_missao()
    
