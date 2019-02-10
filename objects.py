
class neuron:
    count=0
    def __init__(self):
        self.threshold=None
        self.potential=None
        self.hasSpiked=False
        self.input_weightMatrix=None
        self.output_weight_matrix=None
        self.adding_rate=None
        neuron.count+=1
    def add_potential(self,change_amount):
        self.potential +=change_amount
        if self.potential >=self.threshold:
            self.hasSpiked=True
            self.potential=0