
from flask import Flask, abort, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import delete
work=Flask(__name__)
work.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:arvin@localhost:5432/project'
work.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(work)

# classe Categorie et et ses fonctions
class Categorie(db.Model):
        __tablename__='categories'
        id=db.Column(db.Integer,primary_key=True)
        libelle_categorie=db.Column(db.String(50),nullable=False)
        ca=db.relationship('Livre',backref='categories',lazy=True)

        def __init__(self,libelle_categorie):
            self.libelle_categorie=libelle_categorie
        def insert(self):
            db.session.add(self)
            db.session.commit()    
        def update(self):
            db.session.commit()
        def delete(self):
            db.session.delete(self)
            db.session.commit()
        def format (self):
            return{
                'id':self.id,
                'libelle categorie':self.libelle_categorie
            }           
#classe Livre et ses fonctions
class Livre(db.Model):
    __tablename__='livres'
    id=db.Column(db.Integer,primary_key=True)
    titre=db.Column(db.String(50),nullable=False)
    isbn=db.Column(db.String(50),unique=True)
    date_publication=db.Column(db.DateTime,nullable=False)
    auteur=db.Column(db.String(50),nullable=False)
    editeur=db.Column(db.String(50),nullable=False)
    categories_id=db.Column(db.Integer,db.ForeignKey('categories.id'),nullable=False)

    def __init__(self,titre,isbn,date_publication,auteur,editeur,categories_id):
        self.titre=titre
        self.isbn=isbn
        self.date_publication=date_publication
        self.auteur=auteur
        self.editeur=editeur
        self.categories_id=categories_id
    def insert(self):
         db.session.add(self)
         db.session.commit()

    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()  
    def format(self):
        return{
            'titre':self.titre,
            'code ISBN':self.isbn,
            'date publication':self.date_publication,
            'nom auteur':self.auteur,
            'nom editeur':self.editeur,
            'categories_id':self.categories_id
        }  


        
          
db.create_all()

    # liste de tous les livres
@work.route('/livres',methods=['GET'])
def get_all_livres():
        livres=Livre.query.all()
        formated_books=[livre.format() for livre in livres]
        return jsonify({
            'success':True,
            'livres':formated_books,
            'total':len(Livre.query.all())
        })

    # chercher un livre par son id
@work.route('/livres/<int:id>',methods=['GET'])
def get_one_book(id):
        livres=Livre.query.get(id)
        if livres is None:
            abort(404)
        else:
            return jsonify({
                'success':True,
                'selected_id':id,
                'selected_books':livres.format()

            })  
     

    #supprimer un livre
@work.route('/livres/<int:id>',methods=['DELETE'])
def delete_books(id):
        livres=Livre.query.get(id)
        if livres is None:
            abort(404)
        else:
            livres.delete()
            return jsonify({
                "deleted_id":id,
                "success":True,
                "total":Livre.query.count(),
                "deleted_book":livres.format()

            })

    #modifier un livre

@work.route('/livres/<int:id>',methods=['PATCH'])
def update_book(id):
        body=request.get_json()
        li=Livre.query.get(id)
        li.titre=body.get('titre',None)
        li.isbn=body.get('isbn',None)
        li.date_publication=body.get('date_publication',None)
        li.auteur=body.get('auteur',None)
        li.editeur=body.get('editeur',None)
        li.categories_id=body.get('categories_id',None)
    
        if li.titre is None or li.isbn is None or li.date_publication is None or li.auteur is None or li.editeur or li.categories_id is None:

            li.update()
            return jsonify({
                "success":True,
                "updated_id_book":id,
                "new_livres":li.format()
            })

#livres d'une categorie
@work.route ('/categories/<int:id>/livres',methods=['GET'])
def get_livres_in_categories(id):
    try:
        livres=Livre.query.filter_by(categories_id=id).all()
        if livres is None:
            abort(404)
        else:
            formated_livres=[livre.format() for livre in livres] 
            return jsonify({
                'success':True,
                'livres':formated_livres,
                'total':len(livres)
            })   
    except:
        abort(400)

                      

    
#listes de toutes les categories
@work.route('/categories',methods=['GET'])
def get_categories():
        cate=Categorie.query.all()
        formated_cate=[cat.format() for cat in cate]
        return jsonify({
            'success':True,
            'livres':formated_cate,
            'total':len(Categorie.query.all())
        })

 #chercher une categorie par son id
@work.route('/categories/<int:id>',methods=['GET'])
def get_one_categorie(id):
        cate=Categorie.query.get(id)
        if Categorie is None:
            abort(404)
        else:
            return jsonify({
                'success':True,
                'selected_id':id,
                'selected_categories':cate.format()

            }) 

#supprimer une categorie
@work.route('/categories/<int:id>',methods=['DELETE'])
def delete_categorie(id):
        cate=Categorie.query.get(id)
        if cate is None:
            abort(404)
        else:
            cate.delete()
            return jsonify({
                "deleted_id":id,
                "success":True,
                "total":Categorie.query.count(),
                "deleted_categorie":cate.format()

            }) 

 #modifier le libelle d'une categorie                            
@work.route('/categories/<int:id>',methods=['PATCH'])
def update_categorie(id):
        body=request.get_json()
        cate=Categorie.query.get(id)
        cate.libelle_categorie=body.get('libelle_categorie',None)
    
        if cate.libelle_categorie is None :
            abort(400)
        else: 
            cate.update()
            return jsonify({
                "success":True,
                "updated_id_categorie":id,
                "new_categorie":cate.format()
            })      