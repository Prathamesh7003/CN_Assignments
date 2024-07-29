import pygame
import time
import random


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
    paket_status=True
    i=0
    def inint(self):
        pass
    
    def rdt_rcv(self,packet):
        self.data=packet
        x=random.randint(1,100)/10
        #print("rand"+str(x))
        if(x<7):#NOTcorrupted
            self.extract(packet,self.data)
            self.paket_status=True
            self.i+=1

        else:
            self.paket_status=False #if it is false
                                    #It means bit error occured 
                                    #then you return NACK

        return self.paket_status,self.i

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

ACKimg=pygame.image.load('ACK.png')

NACKimg=pygame.image.load('NACK.png')

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


def show_ACK(x,y,pkt_seq):
    gameDisplay.blit(ACKimg,(x,y))
    font=pygame.font.SysFont('PRATHAMESH',10)
    text=font.render('Paket '+str(pkt_seq),True,(0,0,0))
    gameDisplay.blit(text,(x,y+40))


def show_NACK(x,y,pkt_seq):
    gameDisplay.blit(NACKimg,(x,y))
    font=pygame.font.SysFont('PRATHAMESH',10)
    text=font.render('Paket '+str(pkt_seq),True,(0,0,0))
    gameDisplay.blit(text,(x,y+40))

from tkinter import *

x=(0)
y=(0)
x2=500
y2=0

pkt_x=0
pkt_y=50

ack_x=500
ack_y=50

i=0
ack_status=False
nack_status=False



pkt_status=True

pkt_seq=None


my_window=Tk()
my_canvas=Canvas(my_window,width=400,height=400,background='white')
my_canvas.grid(row=0,column=0)

canvas_X=0
canvas_Y=0
canvas_ack_i=0


while(not crashed):
    sender_pkt=["packet1","packet2","packet3",'packet4','packet5']
   
    len_msg=len(sender_pkt)
    for event in pygame.event.get():
        
        if(event.type==pygame.QUIT):
            crashed=True
    
    

        if(pkt_x<x2 and (len_msg)!=i):
            #time.sleep(0.01)
            pkt_x+=15
            

        elif(pkt_status==False):

            ack_x-=20
            if(ack_x<=20):#ACK Varmış ise
                x=random.randint(0,10)
                if(x>7):
                    print("NACK OR ACK BİT ERROR")
                    #ACK OR NACK erro bit
                    ack_status=False
                    nack_status=False
                    pkt_status=True
                    pkt_x=0
                    ack_x=500
                    i-=1
                else:
                    #ACK ise greeen cavas
                    if(ack_status==True):
                        my_canvas.create_line(0,(canvas_Y+10),400,(canvas_Y),fill='green',width=2)
                        canvas_Y+=30
                    elif(nack_status==True):
                        my_canvas.create_line(0,(canvas_Y+10),400,(canvas_Y),fill='red',width=2)
                        canvas_Y+=30

                    ack_status=False
                    
                    nack_status=False
                    pkt_status=True
                    pkt_x=0
                    ack_x=500
               
                

        elif(pkt_x >=x2):
            sender1.rdt_sent(sender_pkt[i])
            if(receiver1.paket_status==True):
                ack_status=True
                pkt_seq=receiver1.i#Seqeunce
                pkt_status=False
                i+=1
                canvas_X=0
                canvas_Y=pkt_y-20
                my_canvas.create_line(0,canvas_Y,400,(canvas_Y+10),fill='black',width=2)
                my_canvas.create_text(150,canvas_Y,text='packet'+str(i-1))
                canvas_Y+=20
                pkt_x=0
                pkt_y+=40

            elif(receiver1.paket_status==False):#Paket bit errordan etkilendiği için
                nack_status=True                #Aynı paket tekrar gönderilecek 
                pkt_status=False
                i+=0
                
                pkt_x=0
                canvas_X=0
                canvas_Y=pkt_y-20
                my_canvas.create_line(0,canvas_Y,400,(canvas_Y+10),fill='black',width=2)
                my_canvas.create_text(150,canvas_Y+20,text='packet '+str(i)+'w Bit Error')
                pkt_y+=40
                canvas_Y+=20
                
            

        #if key release
    

   
    gameDisplay.fill(white)
    show_sender(x,y)
    show_receiver(x2,y2)
   
    if(pkt_status==True):
        show_pkt(pkt_x,pkt_y)
    if(ack_status==True):
        show_ACK(ack_x,ack_y,pkt_seq)
    if(nack_status==True):
        show_NACK(ack_x,ack_y,pkt_seq)
    pygame.display.update()
    clock.tick(60)
    my_window.update()



pygame.quit()
