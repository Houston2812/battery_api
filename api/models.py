from api import db

class Laptop(db.Model):
    __tablename__ = "laptops"
    id = db.Column(db.Integer, primary_key = True, unique = True, nullable = False)
    device_name = db.Column(db.String(60), unique = False, nullable = False)
    power = db.Column(db.String(10), unique = False, nullable = True)
    percentage = db.Column(db.Integer, unique = False, nullable = True)
    status = db.Column(db.Boolean, nullable = False, default = False)

    def __repr__(self):
        return f"ID : {self.id}\nDevice name : {self.device_name}\nPower : {self.power}\nPercentage : {self.percentage}\nStatus : {self.status}\n"
        
    
    def get_dict(self):
        dict_ = {
            'id' : self.id,
            'device_name' : self.device_name,
            'power' : self.power,
            'percentage' : self.percentage,
            'status' : self.status
        }
        return dict_