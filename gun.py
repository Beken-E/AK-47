class Gun:
    
    def __init__(self, bullet):
        self.bullet = bullet
    
    def reload(self, amo):
        self.bullet += amo
        print ( f"Reloaded to {amo} bullet, now you have {self.bullet} bullets" )

    def shot(self):
        self.bullet -= 1
        return  f"BANG! Now you have {self.bullet} bullets"
        


class Soldier:
    def __init__(self):
        pass
    def fire(self, amo):
        self.bullet -= amo
        r = "Bang " * amo
        s = f"Now you have {self.bullet} bullets"
        print( r, s )


class ActofShooting(Soldier, Gun):
    def __init__(self, bullet):
        self.bullet = bullet
        r = int(input("Enter quantity of shot"))
        if r <= self.bullet:
            self.fire(r)
        else:
            self.fire(self.bullet)
            print("We have no more amos")

        r = int(input("Enter quantity of bullets to reload"))
        self.reload(r)
        self.fire(self.bullet)
    
    def __str__(self):
        return "End"
    

Rayan = ActofShooting(30)

print(Rayan)