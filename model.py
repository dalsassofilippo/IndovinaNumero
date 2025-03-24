import random

class Model(object):
    def __init__(self):
        self._NMax=100
        self._TMax=6
        self._T=self._TMax
        self._segreto=None # PER PRASSI INIZIALIZZIAMO TUTTE LE VARIABILI NEL COSTRUTTORE

    def reset(self): #METODO PER RESETTARE IL GIOCO IN QUALSIASI MOMENTO
        self._segreto=random.randint(0,self._NMax)
        self._T=self._TMax

    def play(self,guess): #METODO PER GIOCARE
        # DA FUORI CI ARRIVA UN TENTATIVO (guess), CONFRONTIAMO IL TENTATIVO CON IL SEGRETO
        """
        Funzione che esegue uno step del gioco
        :param guess: tentativo
        :return: 0 se ho vinto, -1 se numero + piccolo, 1 se + grande, 2 se ho perso
        """
        self._T-=1

        if guess==self._segreto:
            return 0 #HO VINTO!
        if self._T==0:
            return 2 #HO PERSO DEFINITIVAMENTE
        if guess>self._segreto:
            return -1 #IL SEGRETO E' + PICCOLO

        return 1 #IL SEGRETO E' + GRANDE

    @property
    def NMax(self): # PER RENDERE LE VARIABILI ANCORA + PRIVATE, SI PUO' NON FARE
        return self._NMax

    @property
    def TMax(self):
        return self._TMax

    @property
    def T(self):
        return self._T

    @property
    def segreto(self):
        return self._segreto

# if __name__=="__main__":
#     m=Model()
#     m.reset()
#     m.play(80)
#     m.play(10)