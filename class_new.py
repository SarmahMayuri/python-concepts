class ABC_Insurance:
    def CompanyName(self):
        pass


class Policies:
    def __init__(self, PolicyNumber, PolicyTerm, PolicyOwner, PolicyAddress, ContactDetails):
        self.PolicyNumber= PolicyNumber
        self.PolicyTerm= PolicyTerm
        self.PolicyOwner= PolicyOwner
        self.PolicyAddress= PolicyAddress
        self.ContactDetails= ContactDetails


    def PrintPolicyDetails(self):
        print(f"{self.PolicyNumber} is a {self.PolicyTerm} whose policy owner is {self.PolicyOwner} is from {self.PolicyAddress}. /n His Contact number is {self.ContactDetails}")


class AutoPolicies(ABC_Insurance,Policies):
    def __init__(self, PolicyNumber, PolicyTerm, PolicyOwner, PolicyAddress, ContactDetails, PolicyType, VehicleType):
        Policies.__init__(self, PolicyNumber, PolicyTerm, PolicyOwner, PolicyAddress, ContactDetails)
        self.PolicyType= PolicyType
        self.VehicleType= VehicleType

    def PrintPolicyTypeDetails(self):
        print(f"{self.PolicyNumber} is a {self.PolicyType} and a {self.PolicyTerm} policy whose policy owner is {self.PolicyOwner} is from {self.PolicyAddress}."
              f" His Contact number is {self.ContactDetails}")

    def VehicleInsured(self):
        print(f"{self.PolicyNumber} is a {self.PolicyType} policy and has {self.VehicleType} insured under it")

class MarinePolicies(ABC_Insurance,Policies):
    def __init__(self, PolicyNumber, PolicyTerm, PolicyOwner, PolicyAddress, ContactDetails, PolicyType, BoatType):
        Policies.__init__(self, PolicyNumber, PolicyTerm, PolicyOwner, PolicyAddress, ContactDetails)
        self.PolicyType= PolicyType
        self.BoatType= BoatType

    def PrintPolicyTypeDetails(self):
        print(f"{self.PolicyNumber} is a {self.PolicyType} and a {self.PolicyTerm} policy whose policy owner is {self.PolicyOwner} is from {self.PolicyAddress}."
              f"His Contact number is {self.ContactDetails}")

    def BoatInsured(self):
        print(f"{self.PolicyNumber} is a {self.PolicyType} policy and has {self.BoatType} insured under it")


PolicyA = AutoPolicies(123456789, 'Annual', 'Mayuri', 'Kolkata', 9864098640, 'Auto', 'Jaguar')
PolicyA.PrintPolicyTypeDetails()
PolicyA.VehicleInsured()
PolicyB = MarinePolicies(123456700, 'Six Month', 'Sameer', 'Bangalore', 9854098540, 'Boat', 'Yacht')
PolicyB.PrintPolicyTypeDetails()
PolicyB.BoatInsured()