import random
import os

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
user_card=[]
pc_card=[]
playGame=True
continued=True
def dealCard(card):
    """Restituisce una carta dal mazzo"""
    card.append(random.choice(cards))
            
def verificaAce(card):
    if 11 in card and sum(card)>21:
        card.remove(11)
        card.append(1)    
    return card        
     
def stampaPunteggio(userAmount, pcAmount):
    print(f"La tua mano finale è: {user_card}, il tuo punteggio finale è: {userAmount}")
    print(f"Mano finale computer: {pc_card}, punteggio finale: {pcAmount}")

def verificaPunteggio(userCard, pcCard):
    user_card_amount=sum(userCard)
    pc_card_amount=sum(pcCard)
    if user_card_amount>21:
        stampaPunteggio(user_card_amount, pc_card_amount)
        print("Hai sballato - perdi !!")
            
    elif user_card_amount>pc_card_amount:
        stampaPunteggio(user_card_amount, pc_card_amount)
        print("Hai vinto !!")
        
    elif pc_card_amount>21 and user_card_amount<=21:
        stampaPunteggio(user_card_amount, pc_card_amount)
        print("Il computer ha sballato - Hai vinto !!")
        
    elif pc_card_amount>user_card_amount:
        stampaPunteggio(user_card_amount, pc_card_amount)
        print("Il computer vince, tu perdi !!") 
    else:
        stampaPunteggio(user_card_amount, pc_card_amount)
        print("'DRAW!!' - Il computer vince, tu perdi !!")    
        

def blackJack(userCard, pcCard): 
    continued=True
    if sum(userCard)==21 and userCard.count(11):
        print(f"BlackJack, hai vinto!!")
        print(f"La tua mano finale : {user_card}, punteggio finale: {sum(userCard)}")
        print(f"Punteggio finale computer: {sum(pcCard)}")
        continued=False
    elif sum(pcCard)==21 and pcCard.count(11):
        print(f"La tua mano finale: {user_card}, il tuo punteggio finale: {sum(userCard)}")
        print(f"Punteggio finale computer: {sum(pcCard)}")
        print("Il banco vince, ha fatto blackJack")
        continued=False
    else:
        calcolaPunteggio(user_card,pc_card)    
    return continued        
            
                          
def calcolaPunteggio(userCard, pcCard):
    user_card_amount=sum(userCard)
    pc_card_amount=sum(pcCard)
    if user_card_amount<=21 and pc_card_amount<=21:
        print(f"Le tue carte: {userCard}, il tuo punteggio: {user_card_amount}")
        print(f"Prima carta del computer: {pcCard[0]}")
    return
        
       
def startGame(continued):
    #Distribuzione carte
    for _ in range(2):
        dealCard(user_card)
        dealCard(pc_card)
    #Se non si è fatto blackJack    
    if blackJack(user_card,pc_card):
        while continued:
            if sum(user_card)<21 and sum(pc_card)<21:
                another_card=input("Vuoi un'altra carta ? . scrivi si o no:  ").lower()
                os.system("cls")
                if another_card=="si":
                    dealCard(user_card)
                    dealCard(pc_card)
                    calcolaPunteggio(user_card,pc_card)
                    print("")
                elif another_card=="no":
                    dealCard(pc_card)
                    verificaPunteggio(user_card,pc_card)
                    continued=False
            else:
                userAmount=verificaAce(user_card)
                pcAmount=verificaAce(pc_card)
                verificaPunteggio(userAmount,pcAmount)
                continued=False          
            
                   
while playGame:
    print(" ")
    run_game=input("Vuoi giocare a BlackJack, scrivi si o no: ").lower()
    os.system("cls")
    if run_game=="si":
        print(logo)
        user_card=[]
        pc_card=[]
        startGame(continued)
    elif run_game=="no":
        playGame=False
        print("Grazie e arrivederci")
    else:
        print("Scelta non consentita")                       
                
       
                   
        




         