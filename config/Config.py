class Develpoment():
    SQLAlCHEMY_DATABASE_URI='postgresql://postgres:#0724246005@127.0.0.1:5432/sales_demo'
    SECRET_KEY='65c9a73ac461c4e5ab41f0b21832432d'
    DEBUG=True

class Production():
    SQLAlCHEMY_DATABASE_URI='postgres://zybajjmxdcxifh:dd4edbc6a45269afd058d06be1048c36ee15ddd5981706091c25369f7793b438@ec2-54-246-100-246.eu-west-1.compute.amazonaws.com:5432/d4kacttqsc0o4q'
    SECRET_KEY='65c9a73ac461c4e5ab41f0b21832432d'
    DEBUG=True
