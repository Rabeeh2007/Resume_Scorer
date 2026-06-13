import re
import json
import nltk
import numpy as np
import pandas as pd
import joblib
from datetime import datetime
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pytesseract
import pymupdf
from PIL import Image
import io
import fitz
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


nltk.download("stopwords")
nltk.download("wordnet")
lemma = WordNetLemmatizer()
stpw = stopwords.words('english')
bc=bc_acr=bc_mul=bc_uni=bc_wei =None
ml=ml_acr=ml_mul=ml_uni=ml_wei=None
ds=ds_acr=ds_mul=ds_uni=ds_wei=None
se=se_acr=se_mul=se_uni=se_wei=None
allu=deg=deg_w=ws=edu= None
cybersec=cybersec_acr=cybersec_mul=cybersec_uni=cybersec_wei=None


def extract_pdf(pdf_path):
    with fitz.open(pdf_path) as pdf:
        text = " ".join(
            page.get_text() or ""
            for page in pdf
        )
    text = re.sub(r'\s+', ' ', text)
    return text

def extract_scanned_pdf(pdf_path):
    pdf = pymupdf.open(pdf_path)
    text = ""
    for page in pdf:
        pix = page.get_pixmap(matrix=pymupdf.Matrix(2, 2))
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        text += pytesseract.image_to_string(img)
    return text
def file():
    global bc, bc_acr, bc_mul, bc_uni,bc_wei
    global ds, ds_acr, ds_mul, ds_uni,ds_wei
    global ml, ml_acr, ml_mul, ml_uni, ml_wei
    global se, se_acr, se_mul, se_uni, se_wei
    global cybersec, cybersec_acr, cybersec_mul, cybersec_uni,cybersec_wei
    global allu,deg,deg_w,ws,edu
    q = open(os.path.join(BASE_DIR, "json/ws.json"),"r")
    r = open(os.path.join(BASE_DIR, "json/edu.json"),"r")
    al = open(os.path.join(BASE_DIR, "json/all.json"), "r")
    d = open(os.path.join(BASE_DIR, "json/degree.json"), "r")
    dw = open(os.path.join(BASE_DIR, "json/degree_wei.json"), "r")
    f = open(os.path.join(BASE_DIR, "json/blockchain.json"), "r")
    acr = open(os.path.join(BASE_DIR, "json/blockchain_acr.json"), "r")
    mul = open(os.path.join(BASE_DIR, "json/blockchain_mulw.json"), "r")
    uni = open(os.path.join(BASE_DIR, "json/blockchain_uni.json"), "r")
    wei = open(os.path.join(BASE_DIR, "json/blockchain_weight.json"), "r")
    ws = json.load(q)
    edu = json.load(r)
    allu = json.load(al)
    deg = json.load(d)
    deg_w = json.load(dw)
    bc = json.load(f)
    bc_acr = json.load(acr)
    bc_mul = json.load(mul)
    bc_uni = json.load(uni)
    bc_wei = json.load(wei)
    f.close(); acr.close(); mul.close(); uni.close(); wei.close()
    f = open(os.path.join(BASE_DIR, "json/ds.json"), "r")
    acr = open(os.path.join(BASE_DIR, "json/ds_acr.json"), "r")
    mul = open(os.path.join(BASE_DIR, "json/ds_mulw.json"), "r")
    uni = open(os.path.join(BASE_DIR, "json/ds_uni.json"), "r")
    wei = open(os.path.join(BASE_DIR, "json/ds_weight.json"), "r")
    ds = json.load(f)
    ds_acr = json.load(acr)
    ds_mul = json.load(mul)
    ds_uni = json.load(uni)
    ds_wei = json.load(wei)
    f.close(); acr.close(); mul.close(); uni.close(); wei.close()
    f = open(os.path.join(BASE_DIR, "json/ml.json"), "r")
    acr = open(os.path.join(BASE_DIR, "json/ml_acr.json"), "r")
    mul = open(os.path.join(BASE_DIR, "json/ml_mulw.json"), "r")
    uni = open(os.path.join(BASE_DIR, "json/ml_uni.json"), "r")
    wei = open(os.path.join(BASE_DIR, "json/ml_weight.json"), "r")
    ml = json.load(f)
    ml_acr = json.load(acr)
    ml_mul = json.load(mul)
    ml_uni = json.load(uni)
    ml_wei = json.load(wei)
    f.close(); acr.close(); mul.close(); uni.close(); wei.close()
    f = open(os.path.join(BASE_DIR, "json/se.json"), "r")
    acr = open(os.path.join(BASE_DIR, "json/se_acr.json"), "r")
    mul = open(os.path.join(BASE_DIR, "json/se_mulw.json"), "r")
    uni = open(os.path.join(BASE_DIR, "json/se_uni.json"), "r")
    wei = open(os.path.join(BASE_DIR, "json/se_weight.json"), "r")
    se = json.load(f)
    se_acr = json.load(acr)
    se_mul = json.load(mul)
    se_uni = json.load(uni)
    se_wei = json.load(wei)
    f.close(); acr.close(); mul.close(); uni.close(); wei.close()
    f = open(os.path.join(BASE_DIR, "json/cybersec.json"), "r")
    acr = open(os.path.join(BASE_DIR, "json/cybersec_acr.json"), "r")
    mul = open(os.path.join(BASE_DIR, "json/cybersec_mulw.json"), "r")
    uni = open(os.path.join(BASE_DIR, "json/cybersec_uni.json"), "r")
    wei = open(os.path.join(BASE_DIR, "json/cybersec_weight.json"), "r")
    cybersec = json.load(f)
    cybersec_acr = json.load(acr)
    cybersec_mul = json.load(mul)
    cybersec_uni = json.load(uni)
    cybersec_wei = json.load(wei)
    f.close(); acr.close(); mul.close(); uni.close(); wei.close()
    al.close(); q.close(); d.close(); r.close(); dw.close()


def load_cert_files():
    bc =      open(os.path.join(BASE_DIR, "json/blockchain_cert.json"), "r")
    ds =      open(os.path.join(BASE_DIR, "json/ds_cert.json"), "r")
    ml =      open(os.path.join(BASE_DIR, "json/ml_cert.json"), "r")
    se =      open(os.path.join(BASE_DIR, "json/se_cert.json"), "r")
    cybersec= open(os.path.join(BASE_DIR, "json/cybersec_cert.json"), "r")
    cert_dbs = {
        "Blockchain": json.load(bc),
        "Data Science": json.load(ds),
        "Machine Learning": json.load(ml),
        "Software Engineering": json.load(se),
        "Cybersecurity": json.load(cybersec),
    }
    bc.close(); ds.close(); ml.close(); se.close(); cybersec.close()
    return cert_dbs


def time_score(win,raw,allu):
    x = 0
    for i in ws:
        if " " in i:
            if i in raw:
                x += 3
        else:
            if i in win:
                x+=3
    for i in win:
        if i in allu:
            x+=4
    for i in edu:
        if " " in i:
            if i in raw:
                x -= 5
        else:
            if i in win:
                x -= 5
    return x

def ext_yrs(x):
    text = x.lower()
    text = re.sub(r'[^a-z0-9\s+#.\-]',' ',text)
    exp = re.finditer(r'(\d+(?:\.\d+)?)\s*\+?\s*(?:years?|yrs?|yr|yoe)\s*(?:of\s+experience|experience|exp)?',text)
    a = []
    for i in exp:
        start = i.start()
        end = i.end()
        win = text[max(0,start-100):min(len(text),end+100)]
        win = re.sub(r'[^a-zA-Z0-9\s]',' ',win)
        raw = win
        win = set(win.split())
        score = time_score(win,raw,allu)
        if score < 1:
            continue
        b = float(i.group(1))
        a.append(min(b,40))
    return max(a) if a else 0

def timeline_exp(x):
    month_pool = {"jan": 1,"january": 1,"feb": 2,"february": 2,"mar": 3,"march": 3,"apr": 4,"april": 4,"may": 5,"jun": 6,"june": 6,"jul": 7,
                 "july": 7,"aug": 8,"august": 8,"sep": 9,"sept": 9,"september": 9,"oct": 10,"october": 10,"nov": 11,"november": 11,"dec": 12,"december": 12
    }
    x = re.sub(
        r'(0[1-9]|1[0-2])(\d{4})((0[1-9]|1[0-2])(\d{4})|present|current|ongoing|now)',
        lambda m: (
            f"{m.group(1)}/{m.group(2)} {m.group(3)[:2]}/{m.group(3)[2:]}"
            if m.group(3)[:2].isdigit()
            else f"{m.group(1)}/{m.group(2)} {m.group(3)}"
        ),
        x
    )
    x = x.lower()
    curr_year = datetime.now().year
    curr_month = datetime.now().month
    x = re.sub(r'[–—]', '-', x)
    months = r'(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|jul(?:y)?|aug(?:ust)?|sep(?:tember)?|sept(?:ember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?|\d{1,2})?'
    timeline_match = re.finditer(rf'({months})?(?:/)?(?:\s*|(?=\d{{4}}))(\d{{4}})'rf'(?:\s*-\s*|\s*to\s*|\s+|(?=\d{{4}}|present|current|ongoing|now))'rf'({months})?(?:/)?(?:\s*|(?=\d{{4}}|present|current|ongoing|now))'rf'(\d{{4}}|present|current|ongoing|now)',
        x,
        re.VERBOSE
    )
    periods = []
    for i in timeline_match:
        start_i = i.start()
        end_i = i.end()
        win = x[max(0,start_i-70):min(len(x),end_i+70)]
        win = re.sub(r'[^a-zA-Z0-9\s]',' ',win)
        raw = win
        win = set(win.split())
        score = time_score(win,raw,allu)
        start_m,start_yr,end_m,end_yr = i.groups()
        if score < 2:
            continue
        if start_m and start_m.isdigit():
            start_m = int(start_m)
        else:
            start_m = month_pool.get(start_m, 1)
        start_yr = int(start_yr)
        if start_yr < 1980 or start_yr > curr_year:
            continue
        if end_yr in {"present", "current", "ongoing", "now"}:
            end_yr = curr_year
            end_m = curr_month
        else:
            if end_m and end_m.isdigit():
                end_m = int(end_m)
            else:
                end_m = month_pool.get(end_m, 12)
            end_yr = int(end_yr)
        if start_yr < 1980 or start_yr > curr_year:
            continue
        if end_yr < 1980 or end_yr > curr_year:
            continue
        if not (1<=start_m<=12):
            continue
        if not (1<=end_m<=12):
            continue
        start = start_yr*12 + start_m
        end = end_yr*12 + end_m
        if start > end:
            continue
        periods.append((start, end))
    if len(periods) == 0:
        return 0
    periods.sort()
    merged_periods = [periods[0]]
    for start, end in periods[1:]:
        last_start, last_end = merged_periods[-1]
        if start <= last_end+1:
            merged_periods[-1] = (last_start, max(last_end, end))
        else:
            merged_periods.append((start, end))
    total_exp = 0
    for start, end in merged_periods:
        total_exp += (end - start)+1
    exp1 = round(total_exp/12,2)
    exp2 = ext_yrs(x)
    if exp1 == 0:
        return exp2
    if exp2 == 0:
        return exp1
    if abs(exp1 - exp2) <= 2:
        return max(exp1, exp2)
    return exp1

def ext_cert(train,cert_dbs):
    category = train.get("Category", "")
    text = train.get("Text", "")
    cert_db = cert_dbs.get(category, {})
    z = []
    for key, value in cert_db.items():
        tier = value["tier"]
        words = [key] + value.get("aliases", [])
        for i in words:
            z.append((i.lower(), key, tier))
    clean = re.sub(r'[^a-zA-Z0-9\s+#.\-]', ' ', text).lower()
    clean = re.sub(r'\s+', ' ', clean)
    found = {}
    z.sort(key=lambda x: len(x[0]),reverse=True)
    for word, key_word, tier in z:
        if key_word in found:
            continue
        pattern = r'(?<![a-z0-9])' + re.escape(word) + r'(?![a-z0-9])'
        if re.search(pattern, clean):
            found[key_word] = tier
    certs_found = list(found.keys())
    tier_sum = sum(found.values())
    return certs_found, tier_sum

def degree(x):
    a = set()
    text = x.lower()
    raw = re.sub(r'[^a-zA-Z0-9\s+#.\-]', ' ', text)
    word = raw.split()
    word = [i for i in word if i not in stpw]
    for i in deg:
        if " " in i:
            if i in raw:
                a.add(deg_w[deg[i]])
        else:
            if i in word:
                a.add(deg_w[deg[i]])
    return max(a) if a else 0

def ext_skill(x):
    n = 0
    sk = set()
    skl = set()
    hr = {"go": " ", "move": " ", "near": " ", "recall": " "}
    text = re.sub(r'[^a-zA-Z0-9\s+#.\-]', ' ', x["Text"])
    if x["Category"] == "Blockchain":
        acr = bc_acr; mul = bc_mul; uni = bc_uni; wei = bc_wei; n = 4
    elif x["Category"] == "Data Science":
        acr = ds_acr; mul = ds_mul; uni = ds_uni; wei = ds_wei; n = 4
    elif x["Category"] == "Machine Learning":
        acr = ml_acr; mul = ml_mul; uni = ml_uni; wei = ml_wei; n = 3
    elif x["Category"] == "Software Engineering":
        acr = se_acr; mul = se_mul; uni = se_uni; wei = se_wei; n = 4
    elif x["Category"] == "Cybersecurity":
        acr = cybersec_acr; mul = cybersec_mul; uni = cybersec_uni; wei = cybersec_wei; n = 4
    ph = text.lower()
    word1 = ph.split()
    word2 = text.split()
    for i in range(n,1,-1):
        for j in range(len(word1) - i + 1):
            win = word1[j: j+i]
            if None in win:
                continue
            phrase = " ".join(win)
            if phrase in mul:
                if mul[phrase] == " ":
                    sk.add(phrase)
                else:
                    sk.add(mul[phrase])
                for k in range(j, i + j):
                    word2[k] = None
                    word1[k] = None
    word2 = [i for i in word2 if i not in stpw]
    sw2 = set(word2)
    for i in acr:
        if i.upper() in sw2:
            if acr[i] == " ":
                sk.add(i)
            else:
                sk.add(acr[i])
    for j,i in enumerate(word2):
        if i==None:
            continue
        if i.lower() in uni:
            if i.lower() in hr:
                if((j != 0 and (word2[j-1] is None or word2[j-1].lower() in allu)) or (j !=len(word2)-1 and (word2[j+1] is None or word2[j+1].lower() in allu))):
                    if uni[i.lower()] == " ":
                        sk.add(i.lower())
                    else:
                        sk.add(uni[i.lower()])
            else:
                if uni[i.lower()] == " ":
                    sk.add(i.lower())
                else:
                    sk.add(uni[i.lower()])
        elif i.lower() in allu:
            if i.lower() in hr:
                if((j != 0 and (word2[j-1] is None or word2[j-1].lower() in allu)) or (j !=len(word2)-1 and (word2[j+1] is None or word2[j+1].lower() in allu))):
                    if allu[i.lower()] == " ":
                        skl.add(i.lower())
                    else:
                        skl.add(allu[i.lower()])
            else:
                if allu[i.lower()] == " ":
                    skl.add(i.lower())
                else:
                    skl.add(allu[i.lower()])
    skill = []
    for i in sk:
        skill.append(wei[i])
    for i in skl:
        if x["Category"] == "Blockchain":
            if i in cybersec_wei:
                skill.append(max(0,cybersec_wei[i]-1))
            elif i in se_wei:
                skill.append(max(0,se_wei[i]-3))
            elif i in ml_wei:
                skill.append(max(0,ml_wei[i]-4))
            elif i in ds_wei:
                skill.append(max(0,ds_wei[i]-5))
        elif x["Category"] == "Data Science":
            if i in ml_wei:
                skill.append(max(0,ml_wei[i]))
            elif i in se_wei:
                skill.append(max(0,se_wei[i]-2))
            elif i in cybersec_wei:
                skill.append(max(0,cybersec_wei[i]-4))
            elif i in bc_wei:
                skill.append(max(0,bc_wei[i]-5))
        elif x["Category"] == "Machine Learning":
            if i in ds_wei:
                skill.append(max(0,ds_wei[i]))
            elif i in se_wei:
                skill.append(max(0,se_wei[i]-2))
            elif i in cybersec_wei:
                skill.append(max(0,cybersec_wei[i]-3))
            elif i in bc_wei:
                skill.append(max(0,bc_wei[i]-5))
        elif x["Category"] == "Software Engineering":
            if i in bc_wei:
                skill.append(max(0,bc_wei[i]-2))
            elif i in ml_wei:
                skill.append(max(0,ml_wei[i]-2))
            elif i in cybersec_wei:
                skill.append(max(0,cybersec_wei[i]-3))
            elif i in ds_wei:
                skill.append(max(0,ds_wei[i]-5))
        elif x["Category"] == "Cybersecurity":
            if i in bc_wei:
                skill.append(max(0,bc_wei[i]-1))
            elif i in se_wei:
                skill.append(max(0,se_wei[i]-3))
            elif i in ml_wei:
                skill.append(max(0,ml_wei[i]-4))
            elif i in ds_wei:
                skill.append(max(0,ds_wei[i]-5))
    skill = sorted(skill,reverse=True)[:15]
    return sum(skill)**0.5

def project_ext(x):
    action={'integrate','deploy', 'design', 'build', 'automate', 'develop', 'implement','fine-tune', 'optimize', 'scale', 'create', 'construct', 'train', 'launch','monitor','migrate','configure','provision','release','deliver','prototype','evaluate','validate','benchmark','streamline','redesign','restructure','containerize','create','secure','refactor','audit'}
    text = re.sub(r'[^a-zA-Z0-9\s+#.\-]', ' ', x["Text"])
    text = text.lower()
    word = text.split()
    word1 =[lemma.lemmatize(i,pos="v") for i in word]
    pos = []
    for j,i in enumerate(word1):
        if i in action:
            if pos and j-pos[-1] < 15:
                continue
            pos.append(j)
    win = []
    for j,i in enumerate(pos):
        if j<len(pos)-1:
            a = pos[j+1]
        else:
            a = pos[-1]+30
        win.append(" ".join(word[i:a]))
    psk = []
    for i in win:
        b = {"Category":x["Category"],"Text":i}
        psk.append(ext_skill(b))
    psk = sorted(psk,reverse=True)[:4]
    psksc = sum(psk)**0.5
    score = 0.7*psksc+0.3*min(len(win),10)
    return min(len(win),15),score


file()
_cert_dbs = load_cert_files()
_model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))

_sa = {
    "Cybersecurity": 5, "Software Engineering": 4,
    "Machine Learning": 3, "Data Science": 2, "Blockchain": 1
}

def run_scorer(filepath, domain):
    text = extract_pdf(filepath)
    if len(text) < 100:
        text = extract_scanned_pdf(filepath)
    text = re.sub(r'\s+', ' ', text)

    ab = {"Category": domain, "Text": text}

    a      = timeline_exp(text)
    b, c   = ext_cert(ab, _cert_dbs)
    d      = degree(text)
    e      = ext_skill(ab)
    f, g   = project_ext(ab)

    final      = np.asarray((a, _sa[domain], f, d, g, c, e)).reshape(1, -1)
    prediction = _model.predict(final)
    score      = round(float(np.clip(prediction[0], 0, 100)), 2)

    return {
        "score": score,
        "details": {
            "experience_years": a,
            "degree_score":     d,
            "skill_score":      round(e, 2),
            "project_count":    f,
            "cert_tier":        c,
            "certifications":   b
        }
    }


if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else input("Enter PDF path: ")
    dom  = sys.argv[2] if len(sys.argv) > 2 else input("Enter Domain: ")
    result = run_scorer(path, dom)
    print(f"Score: {result['score']}")
    print(result['details'])