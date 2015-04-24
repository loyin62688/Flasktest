__author__ = 'loyin'
from testflask import db

class Keyinfo(db.Model):
    __table__ = 'keyinfo'
    id = db.Column(db.Integer, primary_key=True)
    keyname = db.Column(db.String(80), unique=True)
    value_decrypt = db.Column(db.String(64), default=None)
    value_encrypt = db.Column(db.String(128), default=None)
    conffile_key = db.relationship('ConfFileKeyInfo', backref='Keyinfo', lazy='dynamic')

    def __init__(self, keyname, value_decrypt, value_encrypt):
        self.keyname = keyname
        self.value_decrypt = value_decrypt
        self.value_encrypt = value_encrypt

    def __repr__(self):
        return '<Keyinfo %r>' % self.keyname

class ConfFileKeyInfo(db.Model):
    __table__ = 'configfile_keyinfo'
    id = db.Column(db.Integer, primary_key=True)
    conffilekey = db.Column(db.String(128), unique=True)
    conffilekey_type = db.Column(db.String(16))
    key_id = db.Column(db.Integer, db.ForeignKey('Keyinfo.id'))

    def __init__(self, conffilekey, conffilekey_type):
        self.conffilekey = conffilekey
        self.conffilekey_type = conffilekey_type

    def __repr__(self):
        return '<ConfKeyinfo %r>' % self.conffilekey



