# Module 1 - Create a Blockchain

# To be installed:
# Flask==0.12.2: pip install Flask==0.12.2
# Postman HTTP Client: https://www.getpostman.com/

# Importing the libraries
import datetime
import hashlib
import json
from flask import Flask, jsonify, request, render_template, redirect, url_for, session
from flask_session import Session
from werkzeug.utils import secure_filename
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
import os
import shelve
from datetime import date
import datetime as datetime_
date_time = datetime_.datetime
import ipfshttpclient
from cryptography.fernet import Fernet
import sqlite3
import subprocess

db = sqlite3.connect("db.sqlite3", check_same_thread=False)
cursor = db.cursor()

# Part 1 - Building a Blockchain

global username,login_check
login_check = False
username = ""

try:client = ipfshttpclient.connect("/dns/localhost/tcp/5001/http")
except:
    print("Some Error Occur While connecting to IPFS")
    # print("Trying to connect Again")
    # output = subprocess.run(["powershell", "-Command", '"ipfs daemon"'], capture_output=True)
    # client = ipfshttpclient.connect("/dns/localhost/tcp/5001/http")
    # print("started")
    # print(output)

class Blockchain:

    def __init__(self):
        self.chain = []
        # load list from file
        res = cursor.execute("SELECT chain from Blockchain").fetchall()
        print(res)
        if len(res) == 1:
            if len(res[0]) == 1 and res[0] != '':
                print("==1")
                # print(res[0][0])
                self.chain = json.loads(res[0][0])["chain"]
                # print(self.chain,type(self.chain))
            else:
                print("if else")
                self.create_block(proof=1, previous_hash='0')
        elif len(res) > 1:
            print(">1")
            cursor.execute("DELETE * FROM table WHERE NOT(chain=res[0][0][-1])")
            db.commit()
        else:
            print("else")
            self.create_block(proof=1, previous_hash='0')


    def create_block(self, proof, previous_hash, FileHash=None,FileName=None):
        block = {
            'index': len(self.chain) + 1,
             'timestamp': str(datetime.datetime.now()),
             'proof': proof,
             'previous_hash': previous_hash,
        }
        if FileHash != None:
            block['filehash'] = FileHash
            block['filename'] = FileName
        self.chain.append(block)
        print("creat_block")
        self.save_chain()
        return block

    def mine_block(self,FileHash=None,FileName=None):
        previous_block = blockchain.get_previous_block()
        previous_proof = previous_block['proof']
        proof = blockchain.proof_of_work(previous_proof)
        previous_hash = blockchain.hash(previous_block)
        block = blockchain.create_block(proof, previous_hash, FileHash,FileName)
        print("mine_block")
        self.save_chain()
        return block["index"]-1

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def proof_of_authority(self, document):
        document_hash = self.document_to_hash(document)
        for block in self.chain:
            if block['hash'] == document_hash:
                return block['proof']
        return None

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True

    def document_to_hash(self, document):
        encoded_document = json.dumps(document, sort_keys=True).encode()
        return hashlib.sha256(encoded_document).hexdigest()

    def file_to_sha256(self, file_name):
        file = open(file_name, 'rb')
        file_content = file.read()
        file.close()
        return hashlib.sha256(file_content).hexdigest()


    def encrypt_file(self, file_name, entered_user):
        key = cursor.execute("Select encryKey from main where username=?", (entered_user,)).fetchone()
        fernet = Fernet(bytes(key[0], 'utf-8'))
        file = open(file_name, 'rb')
        file_content = file.read()
        # key = Fernet.generate_key()
        # print(key,type(key))
        # fernet = Fernet(key)
        encrypted_file = fernet.encrypt(file_content)
        with open(file_name, 'wb') as f:
            f.write(encrypted_file)
        return encrypted_file,key

    def decrypt_file(self, file_name):
        if os.path.exists(os.path.join(UPLOAD_FOLDER, 'certi.pdf')):
            print("decrypt")
            client.cat("")
            file_name = os.path.join(UPLOAD_FOLDER, 'certi.pdf')
            key = cursor.execute("Select encryKey from main where username=?", (username,)).fetchone()
            print(key, ",", bytes(key[0], 'utf-8'))
            file = open(file_name, 'rb')
            file_content = file.read()
            fernet = Fernet(bytes(key[0], 'utf-8'))
            decrypted_file = fernet.decrypt(file_content)
            with open(file_name, 'wb') as f:
                f.write(decrypted_file)

    def save_chain(self):
        res = cursor.execute("SELECT chain from Blockchain").fetchall()
        print(res)
        chain = json.dumps({'chain': self.chain})
        if len(res) == 0:
            print("if")
            cursor.execute("INSERT INTO Blockchain(chain) values(?)", (chain,))
        else:
            print("del_else")
            cursor.execute("UPDATE Blockchain set chain=?", (chain,))
        db.commit()
        print("saved")


    def __del__(self):
        self.save_chain()






# Part 2 - Mining our Blockchain

# Creating a Web App
app = Flask(__name__)
# app.config[r'C:\Users\DELL\Desktop\Transcript Management Project\static\uploads']
app.config['UPLOAD_FOLDER'] = '.\static\\uploads'
app.config['DOWNLOAD_FOLDER'] = '.\static\\downloads'
UPLOAD_FOLDER = app.config['UPLOAD_FOLDER']
DOWNLOAD_FOLDER = app.config['DOWNLOAD_FOLDER']
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['ALLOWED_EXTENSIONS'] = set(['pdf', 'png', 'jpg', 'jpeg'])



# Creating a Blockchain
blockchain = Blockchain()
blockchain.mine_block()

@app.route('/login', methods=['GET', 'POST'])
def login():
    print("hello123")
    print(request)
    global login_check
    if request.method == 'POST':
        print("post")
        global username
        e_username = request.form.get('username', "username")
        e_password = request.form.get('password', "password")
        print(e_username, e_password)

        dbpassword = cursor.execute("select password from main where username=?",(e_username,)).fetchone()
        # print(dbpassword[0])
        if dbpassword != None:
            if e_password == dbpassword[0]:
                print("right")
                login_check = True
                username = e_username
                return redirect('/')
        else:
            return render_template('login.html',login_success=False)

    return render_template('login.html',login_success=None)

    # username = request.form.get('username')
    # password = request.form.get('password')
    # print(username, password)

@app.route('/logout', methods=['GET'])
def logout():
    global login_check
    login_check = False
    username = ""
    return redirect('/login')


@app.route('/add_user', methods=['GET', 'POST'])
def AddUser():
    # print(request)
    if request.method == 'POST':
        name = request.form.get('name').strip()
        user = request.form.get('roll_no').strip()
        email = request.form.get('email').strip()
        first_name = name.split(" ")[0] if " " in name else name
        password = first_name+user
        encryKey = str(Fernet.generate_key())[2:-1]
        hash = hashlib.sha256(str(user).encode()).hexdigest()
        print("Add user email: ", email)
        print("Add user Username: ", user)
        print("Add user password: ", password)
        print("Add user encryption Key: ", encryKey)
        print("hash", hash)
        cursor.execute("INSERT INTO main(name, email, username, password, encryKey, listOfBlocks, hash) values(?, ?, ?, ?, ?, ?, ?)",(name, email, user, password, encryKey, "", hash,))
        db.commit()
    return render_template('addUser.html')

@login_required
@app.route('/', methods=['GET', 'POST'])
def Dashboard():
    global login_check
    if login_check == True:
        date_time.now().strftime("%I %b %Y")
        date1 = date(2022, 4, 15)
        date2 = date(2022, 4, 15)
        last_visit = (date2-date1).days
        if last_visit == 0:
            last_visit = "Last Visited Today"
        elif last_visit == 1:
            last_visit = "Last Visited Yesterday"
        else:
            last_visit = "Last Visited " + str(last_visit) + " days ago"

        hash_username, name, key, string_indexes = cursor.execute("Select hash, name, encryKey, listOfBlocks from main where username=?", (username,)).fetchone()
        indexes = []
        files = []
        if string_indexes is not None and string_indexes != '':
            if "," in string_indexes:
                print("if ,")
                indexes = list(string_indexes.split(","))
            else:
                print("new else")
                indexes.append(string_indexes)

            # hashes = []
            # file_names = []
            files = []
            # try:
            print("indexes",indexes)
            if "" in indexes:
                indexes.remove("")
            print("indexes", indexes)
            for index in indexes:
                if index != '':
                    index = int(index)
                    # print(blockchain.chain)
                    # hashes.append(blockchain.chain[index]['filehash']
                    # file_names.append(blockchain.chain[index]['filename'])
                    file_hash = blockchain.chain[index]['filehash']
                    file_name = blockchain.chain[index]['filename']
                    file_content = client.cat(file_hash)
                    print(key, ",", bytes(key, 'utf-8'))
                    fernet = Fernet(bytes(key, 'utf-8'))
                    decrypted_file = fernet.decrypt(file_content)
                    file_path = os.path.join(DOWNLOAD_FOLDER, file_name)
                    with open(file_path, 'wb') as f:
                        f.write(decrypted_file)
                        files.append([file_name,file_path])
                else:
                    # print("else")
                    pass
            # except Exception as e:
            #     print("Error = \n"+str(e)+"\n"+str(e.__traceback__.tb_lasti))

            print(files)
            files = [[i[0].split(".")[0].replace("_"," ") , i[1].replace("//","/")] for i in files]

            # for hash in hashes:
            #     file_content = client.cat(hash)
            #     print(file_content)
            #     print(key, ",", bytes(key, 'utf-8'))
            #     fernet = Fernet(bytes(key, 'utf-8'))
            #     decrypted_file = fernet.decrypt(file_content)
            #     file_name = os.path.join(DOWNLOAD_FOLDER, 'certi.pdf')
            #     with open(file_name, 'wb') as f:
            #         f.write(decrypted_file)
        print(indexes)
        return render_template('Dashboard.html', name=name, last_visited=last_visit, hash=hash_username,file_count=len(indexes),files=files)

    else:
        return redirect('/login')


# Mining a new block
# @app.route('/mine_block', methods=['GET'])
# def mine_block(file_hash=None):
#     previous_block = blockchain.get_previous_block()
#     previous_proof = previous_block['proof']
#     proof = blockchain.proof_of_work(previous_proof)
#     previous_hash = blockchain.hash(previous_block)
#     block = blockchain.create_block(proof, previous_hash, file_hash)
#     response = {'message': 'Congratulations, you just mined a block!',
#                 'index': block['index'],
#                 'timestamp': block['timestamp'],
#                 'proof': block['proof'],
#                 'previous_hash': block['previous_hash']}
#     return jsonify(response), 200


# Getting the full Blockchain
@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200


# Checking if the Blockchain is valid
@app.route('/is_valid', methods=['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': 'All good. The Blockchain is valid.'}
    else:
        response = {'message': 'Houston, we have a problem. The Blockchain is not valid.'}
    return jsonify(response), 200


@app.route('/upload', methods=['GET','POST'])
def upload_file():
    # res = client.add("D:\epilight_cpp_new.pdf")
    # hash = res['Hash']
    if request.method == 'POST':
        f = request.files['file']
        entered_user = request.form.get("username")
        #save file to uploads folder
        f.save(os.path.join(UPLOAD_FOLDER, secure_filename(f.filename)))
        file, key = blockchain.encrypt_file(os.path.join(UPLOAD_FOLDER, secure_filename(f.filename)),entered_user)
        res = client.add(os.path.join(UPLOAD_FOLDER, secure_filename(f.filename)))
        file_hash = res['Hash']
        #get file hash
        # file_hash = blockchain.file_to_sha256(os.path.join(UPLOAD_FOLDER, secure_filename(f.filename)))
        print("file hash =", file_hash)
        block_index = blockchain.mine_block(FileHash=file_hash,FileName=secure_filename(f.filename))

        string_indexes = cursor.execute("Select listOfBlocks from main where username=?", (entered_user,)).fetchone()
        print(string_indexes)
        if "," in string_indexes:
            indexes = list(string_indexes.split(","))
            indexes.append(block_index)
            indexes = ",".join(indexes)
        else:
            indexes = []
            indexes.append(str(block_index))
            if string_indexes != '':
                indexes.append(string_indexes[0])
            indexes = ",".join(list(indexes))
        db.execute("update main set listOfBlocks=? where username=?", (indexes, entered_user))
        db.commit()


        return render_template('upload.html', response=0)
        # except Exception as e:
        #     print(e)
        #     return render_template('upload.html', upload='fail')
    else:
        return render_template('upload.html')

def authority_check(authority):
    if authority == 'admin':
        return True
    else:
        return False

# def proof_of_authority_of_miner()


# @app.route('/uploader')
# def save_file():

# api = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/8080/http')
# print(api)

# api = ipfshttpclient.connect('127.0.0.1', 5001)
# print(api)

# Running the app
app.run(host='0.0.0.0', debug=True)

