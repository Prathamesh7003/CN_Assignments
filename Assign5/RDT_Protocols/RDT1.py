import pygame
import time
from tkinter import *




class Sender(object):
    def init(self):
        pass
    
    def rdt_sent(self,data):
        self.msg=data

        print(self.msg)

        self.make_pkt(self.msg)

    def make_pkt(self,data):
        '''
        for pkt in data:
            self.udt_send(pkt)
        '''
        self.udt_send(data)


    def udt_send(self,packet):
        receiver1.rdt_rcv(packet)



class Receiver(object):
    data_list=[]

    def inint(self):
        pass
    
    def rdt_rcv(self,packet):
        self.data=packet

        self.extract(packet,self.data)

    def extract(self,packet,data):
        self.data_list.append(data)
        
        self.deliver_data(self.data_list)

    def deliver_data(self,data):
        print("Received Packets: "+str(data))


receiver1=Receiver()

sender1=Sender()


pygame.init()

senderimg=pygame.image.load('new_sender.png')
pktimg=pygame.image.load('pkt.png')

white=(255,255,255)
h,w=600,600

gameDisplay=pygame.display.set_mode((w,h))

pygame.display.set_caption('rdt 1.0')

clock=pygame.time.Clock()

crashed=False



def show_sender(x,y):
    font=pygame.font.SysFont('PRATHAMESH',10)
    text=font.render('SENDER',True,(0,0,0))
    gameDisplay.blit(senderimg,(x,y))
    gameDisplay.blit(text,(x,y+40))


def show_receiver(x,y):
    font=pygame.font.SysFont('PRATHAMESH',10)
    text=font.render('RECEİVER',True,(0,0,0))
    gameDisplay.blit(senderimg,(x,y))
    gameDisplay.blit(text,(x,y+40))

def show_pkt(x,y):
    gameDisplay.blit(pktimg,(x,y))
    


x=(0)
y=(0)
x2=500
y2=0

pkt_x=0
pkt_y=50
x_change=0

my_window=Tk()
my_canvas=Canvas(my_window,width=400,height=400,background='white')
my_canvas.grid(row=0,column=0)

i=0
while(not crashed):
    

    sender_pkt=["packet1","packet2","packet3"]
    len_msg=len(sender_pkt)
    for event in pygame.event.get():
        
        if(event.type==pygame.QUIT):
            crashed=True
    
    

        if(pkt_x<x2 and (len_msg)!=i):
            time.sleep(0.01)
            pkt_x+=15
            

        elif(pkt_x >=x2):
            sender1.rdt_sent(sender_pkt[i])
            i+=1
            
            my_canvas.create_line(0,(pkt_y-20),400,(pkt_y-10),fill='black',width=2)
            my_canvas.create_text(150,(pkt_y-20),text='packet')

            pkt_x=0
            pkt_y+=50
                
            

        #if key release
    

   
    gameDisplay.fill(white)
    show_sender(x,y)
    show_receiver(x2,y2)
    show_pkt(pkt_x,pkt_y)
    pygame.display.update()
    clock.tick(60)
    my_window.update()
    


pygame.quit()
