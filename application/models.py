from application import db

class Data(db.Model):
    inn = db.Column(db.Integer(11), unique=True, db.ForeignKey("Document.inn"), nullable=False)
    ogrn = db.Column(db.Integer(13), unique=True, nullable=False)
    year_gain = db.Column(db.Integer, db.ForeignKey("Gain.id"),nullable=False)
    v_org = db.Column(db.Integer, db.ForeignKey("Vid_org.id"), nullable=False)
    m_phone = db.Column(db.Integer, unique=False, nullable=True)
    email = db.Column(db.String(255), unique=False, nullable=True)
    pasport = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, inn):
        self.inn = inn
    def __repr__(self):
        return '<Data %r>' % self.inn

class Gain(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    year_gain = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Gain %r>' % self.id

class Vid_org(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    v_org = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Vid_org %r>' % self.id

class VSP(db.Model):
    num_vsp = db.Column(db.Integer, unique=False, db.ForeignKey("document.num_vsp") nullable=False)
    adress_vsp = db.Column(db.String, nullable=True)

        def __repr__(self):
        return '<VSP %r>' % self.adress_vsp

class Document(db.Model):
    inn = db.Column(db.Integer(11), unique=True, primary_key=True, nullable=False)
    num_vsp = db.Column(db.Integer, unique=False, primary_key=True, nullable=True)
    doc = db.Column(db.Integer, db.ForeignKey("S3.id_doc"), nullable=True)

        def __repr__(self):
        return '<Document %r>' % self.doc

class S3(db.Model):
    id_doc = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    doc = db.Column(db.String(255),nullable=False)

    def __repr__(self):
        return '<S3 %r>' % self.doc
