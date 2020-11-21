import random
Ranks = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King")
Suits = ("Clubs", "Hearts", "Diamonds", "Spades")
Values = {"Ace" : 11, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}

class Cards:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = Values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit
    
    
    
class Deck:
    
    def __init__(self):
        self.deck = []
        for rank in Ranks:
            for suit in Suits:
                new_card = Cards(suit,rank)
                self.deck.append(new_card)
                
    def shuffle(self):
        random.shuffle(self.deck)
        
    def hit(self):
        return self.deck.pop()
    
    
    
class New_hand:
    
    def __init__(self):
        self.hand = []
        
    def add_to_hand(self, card):
        self.hand.append(card)
        print ("You have drawn the " + str(card))
        
    def computer_draws(self, card):
        self.hand.append(card)
    
    def print_hand(self):
        for cards in self.hand:
            print (cards)
            
    def sum_of_hand(self):
        sum_of_hand = 0
        for cards in self.hand:
            sum_of_hand += cards.value
        print("\nThe sum of your hand is: " + str(sum_of_hand) + "\n")
        return sum_of_hand
    
    def computer_sum(self):
        sum_of_comp_hand = 0
        for cards in self.hand:
            sum_of_comp_hand += cards.value
        return sum_of_comp_hand
    
    def ranks(self):
        ranks_of_hand = []
        for cards in self.hand:
            ranks_of_hand.append(cards.rank)
        return ranks_of_hand
    
def game():
    
    
    play_again = 'yes'
    while play_again == 'yes' or play_again == 'Yes':
        
        
        lost = False
        
        
        print("\n")
        
        
        game_deck = Deck()
        game_deck.shuffle()
        
        
        players_hand = New_hand()
        
        
        new_card = game_deck.hit()
        players_hand.add_to_hand(new_card)
        new_card = game_deck.hit()
        players_hand.add_to_hand(new_card)
        sum_of_hand = players_hand.sum_of_hand()
        ranks_in_hand = players_hand.ranks()
        
        
        computers_hand = New_hand()
        
        
        new_card = game_deck.hit()
        computers_hand.computer_draws(new_card)
        print("The computer has drawn two cards, one of which is the " + str(new_card))
        new_card = game_deck.hit()
        computers_hand.computer_draws(new_card)
        sum_computers_hand = computers_hand.computer_sum()
        ranks_in_comp_hand = computers_hand.ranks()
        
        
        print("\nHit or Stand?")
        next_action = ''
        next_action = input()
        
        
        while next_action == 'Hit' or next_action == 'hit':           
            
            
            print("\n")
            new_card = game_deck.hit()
            players_hand.add_to_hand(new_card)
            sum_of_hand += new_card.value
            ranks_in_hand.append(new_card.rank)
            
            
            if sum_of_hand > 21:
                number_of_aces = 0
                if "Ace" in ranks_in_hand:
                    number_of_aces = ranks_in_hand.count("Ace")
                while sum_of_hand > 21 and number_of_aces > 0:
                    print("\nYou have gone over 21, but since you have an Ace, the sum of your hand has been reduced by 10")
                    sum_of_hand -= 10  
                    number_of_aces -= 1
                    ranks_in_hand.remove("Ace")
                
                
            print("\nThe sum of your hand is: " + str(sum_of_hand) + "\n")
            
            
            if sum_of_hand > 21:
              print("You have lost!")
              lost = True
              break
            
            
            print("Hit or Stand?")
            next_action = input()
        
        
        if lost == False:
            
            
            computer_loss = False
            
            
            print("\nThe computer has the following cards: ")
            computers_hand.print_hand()
            print("\nThe sum of the computers hand is: " + str(sum_computers_hand))
            
            
            while sum_computers_hand < 15:
                
                
                new_card = game_deck.hit()
                computers_hand.computer_draws(new_card)
                print("\nThe computer has drawn the " + str(new_card))
                sum_computers_hand += new_card.value
                print("\nThe sum of the computers hand is: " + str(sum_computers_hand))
                ranks_in_comp_hand.append(new_card.rank)
                
                
                if sum_computers_hand > 21:
                    number_of_comp_aces = 0
                    if "Ace" in ranks_in_comp_hand:
                        number_of_comp_aces = ranks_in_comp_hand.count("Ace")
                    while sum_computers_hand > 21 and number_of_comp_aces > 0:
                        sum_computers_hand -= 10
                        number_of_comp_aces -= 1
                        ranks_in_comp_hand.remove("Ace")
            
            
                if sum_computers_hand > 21:
                    print("\nYou have won!, the dealer has gone over 21!") 
                    computer_loss = True
                    break
             
            
            if computer_loss == False:     
                if sum_of_hand > sum_computers_hand:
                    print("\nYou have won!")
                elif sum_computers_hand == 21:
                    print("\nYou have lost! The dealer has 21!")
                elif sum_of_hand < sum_computers_hand:
                    print("\nYou have lost! The dealer is closer to 21!")
               
        
        print("\nWould you like to play again?")
        play_again = input()
        
game()
        
        

