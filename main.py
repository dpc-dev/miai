from flask import *
import random,os,pymysql,hashlib,sys,re
import st,user_test,datetime
app = Flask(__name__)
db = pymysql.connect("localhost","root","1478963520.ai","qxun")
cur = db.cursor()
app.config['SECRET_KEY'] = b'\xa3P\x06\x1a\xf8\xc6\xff\xa4!\xd2\xb5\n\x96\x05\xed\xc3\xc90=\x07\x8d>\x8e\xeb'
@app.route("/",methods=["GET","POST"])
def home():
    #获取Session
    cont = 0
    information = []
    name = session.get("uname")
    pwd = session.get("upwd")
    if name:
        hashlib_pwd = hashlib.md5(pwd.encode())
        cur.execute("select judge,uid1 from user_web where uname='%s' and pwd='%s'"%(name,hashlib_pwd.hexdigest()))
        querying2 = cur.fetchone()
        if not querying2:
            return redirect(url_for("login"))
        if querying2[0] == "0":
            return redirect(url_for("perfect"))
        if request.method == "GET":
            req={}
            req['name'] = name
        #用户登录后的推荐，优先级推荐喜好，地点
            cur.execute("select max(uid1) from user_web ")
            querying4 = cur.fetchone()
            cur.execute("select location1,hobby from user_if where uid2=%s "%querying2[1])
            querying6 = cur.fetchone()
            baif = "%"
            cur.execute("select uid2,head_p,true_name,job,location1,hobby from user_if where location1 like '%s%s%s' and hobby like '%s%s%s'"%(baif,querying6[0],baif,baif,querying6[1],baif))
            querying7 = cur.fetchall()
            if len(querying7) == 0:
                cur.execute("select uid2,head_p,true_name,job,location1,hobby from user_if where location1 like '%s%s%s' "%(baif,querying6[0],baif))
                querying8 = cur.fetchall()
                if len(querying8)==0:
                    cur.execute("select uid2,head_p,true_name,job,location1,hobby from user_if where hobby like '%s%s%s' "%(baif,querying6[1],baif))
                    querying9 = cur.fetchone()
                    if len(querying9) == 0:
                        #随机查询
                        cur.execute("select max(uid1) from user_web ")
                        querying4 = cur.fetchone()
                        for i in range(6):
                #注意深浅拷贝的问题
                            shuiji = random.randint(1001,querying4[0])
                            shuiji = str(shuiji)
                            cur.execute("select head_p,true_name,job,location1,hobby from user_if where uid2=%s "%shuiji)
                            querying10 = cur.fetchone()
                            
                            information.append({"url_u":"id=%s"%shuiji,"ture_name":querying10[1],"job":querying10[2],"location":querying10[3], "hobby":querying10[4],"head_p":querying10[0]})
                    else:
                        if len(querying9) > 6:
                            for i in range(6):
                        #注意深浅拷贝的问题
                                shuiji = random.randint(0,len(querying9)-1)        
                                information.append({"url_u":"id=%s"%querying9[shuiji][0],"ture_name":querying9[shuiji][2],"job":querying9[shuiji][3],"location":querying9[shuiji][4], "hobby":querying9[shuiji][5],"head_p":querying9[shuiji][1]})
                        else:
                            for i in range(len(querying9)):
                #注意深浅拷贝的问题
                                cont += 1       
                                information.append({"url_u":"id=%s"%querying9[i][0],"ture_name":querying9[i][2],"job":querying9[i][3],"location":querying9[i][4], "hobby":querying9[i][5],"head_p":querying9[i][1]})
                            cont = 6 - cont
                            for i in range(cont):
                                shuiji = random.randint(1001,querying4[0])
                                shuiji = str(shuiji)
                                cur.execute("select head_p,true_name,job,location1,hobby from user_if where uid2=%s "%shuiji)
                                querying10 = cur.fetchone()
                            
                                information.append({"url_u":"id=%s"%shuiji,"ture_name":querying10[1],"job":querying10[2],"location":querying10[3], "hobby":querying10[4],"head_p":querying10[0]})
                else:
                    if len(querying8) > 6:
                        for i in range(6):
                    #注意深浅拷贝的问题
                            shuiji = random.randint(0,len(querying8)-1)        
                            information.append({"url_u":"id=%s"%querying8[shuiji][0],"ture_name":querying8[shuiji][2],"job":querying8[shuiji][3],"location":querying8[shuiji][4], "hobby":querying8[shuiji][5],"head_p":querying8[shuiji][1]})
                    else:
                        cur.execute("select uid2,head_p,true_name,job,location1,hobby from user_if where hobby like '%s%s%s' "%(baif,querying6[1],baif))
                        querying9 = cur.fetchone()
                        if len(querying8) >= 3:
                            for i in range(len(querying9)):
                    #注意深浅拷贝的问题
                                cont += 1       
                                information.append({"url_u":"id=%s"%querying8[i][0],"ture_name":querying8[i][2],"job":querying8[i][3],"location":querying8[i][4], "hobby":querying8[i][5],"head_p":querying8[i][1]})
                            cont = 6 - cont
                            for i in range(cont):
                                shuiji = random.randint(1001,querying4[0])
                                shuiji = str(shuiji)
                                cur.execute("select head_p,true_name,job,location1,hobby from user_if where uid2=%s "%shuiji)
                                querying10 = cur.fetchone()
                            
                                information.append({"url_u":"id=%s"%shuiji,"ture_name":querying10[1],"job":querying10[2],"location":querying10[3], "hobby":querying10[4],"head_p":querying10[0]})
                        else:
                            for i in range(len(querying8)):
                #注意深浅拷贝的问题
                                cont += 1       
                                information.append({"url_u":"id=%s"%querying8[i][0],"ture_name":querying8[i][2],"job":querying8[i][3],"location":querying8[i][4], "hobby":querying8[i][5],"head_p":querying8[i][1]})
                            if len(querying9) >= 6:
                                for i in range(6):
                            #注意深浅拷贝的问题
                                    cont += 1
                                    if cont == 6:
                                        return render_template("index.html",information=information,**req)
                                    shuiji = random.randint(0,len(querying9)-1)        
                                    information.append({"url_u":"id=%s"%querying9[shuiji][0],"ture_name":querying9[shuiji][2],"job":querying9[shuiji][3],"location":querying9[shuiji][4], "hobby":querying9[shuiji][5],"head_p":querying9[shuiji][1]})
                            else:
                                cont = 6 - cont
                                for i in range(cont):
                                    shuiji = random.randint(1001,querying4[0])
                                    shuiji = str(shuiji)
                                    cur.execute("select head_p,true_name,job,location1,hobby from user_if where uid2=%s "%shuiji)
                                    querying10 = cur.fetchone()
                                
                                    information.append({"url_u":"id=%s"%shuiji,"ture_name":querying10[1],"job":querying10[2],"location":querying10[3], "hobby":querying10[4],"head_p":querying10[0]})

            else:
                
                if len(querying7) > 6:
                    for i in range(6):
                #注意深浅拷贝的问题
                        shuiji = random.randint(0,len(querying7)-1)        
                        information.append({"url_u":"id=%s"%querying7[shuiji][0],"ture_name":querying7[shuiji][2],"job":querying7[shuiji][3],"location":querying7[shuiji][4], "hobby":querying7[shuiji][5],"head_p":querying7[shuiji][1]})
                else:
                    cur.execute("select uid2,head_p,true_name,job,location1,hobby from user_if where location1 like '%s%s%s' "%(baif,querying6[0],baif))
                    querying8 = cur.fetchall()
                    if len(querying7) >= 3:
                        for i in range(len(querying7)):
                #注意深浅拷贝的问题
                            cont += 1       
                            information.append({"url_u":"id=%s"%querying7[i][0],"ture_name":querying7[i][2],"job":querying7[i][3],"location":querying7[i][4], "hobby":querying7[i][5],"head_p":querying7[i][1]})
                        cont = 6 - cont
                        for i in range(cont):
                            shuiji = random.randint(1001,querying4[0])
                            shuiji = str(shuiji)
                            cur.execute("select head_p,true_name,job,location1,hobby from user_if where uid2=%s "%shuiji)
                            querying10 = cur.fetchone()
                        
                            information.append({"url_u":"id=%s"%shuiji,"ture_name":querying10[1],"job":querying10[2],"location":querying10[3], "hobby":querying10[4],"head_p":querying10[0]})
                    else:
                        for i in range(len(querying7)):
                #注意深浅拷贝的问题
                            cont += 1       
                            information.append({"url_u":"id=%s"%querying7[i][0],"ture_name":querying7[i][2],"job":querying7[i][3],"location":querying7[i][4], "hobby":querying7[i][5],"head_p":querying7[i][1]})
                        if len(querying8) >= 5:
                            for i in range(6):
                        #注意深浅拷贝的问题
                                cont += 1
                                if cont == 6:
                                    return render_template("index.html",information=information,**req)
                                shuiji = random.randint(0,len(querying8)-1)        
                                information.append({"url_u":"id=%s"%querying8[shuiji][0],"ture_name":querying8[shuiji][2],"job":querying8[shuiji][3],"location":querying8[shuiji][4], "hobby":querying8[shuiji][5],"head_p":querying8[shuiji][1]})
                        else:
                            print(querying8)
                            for i in range(len(querying8)):
                        #注意深浅拷贝的问题
                                cont += 1
                                    
                                information.append({"url_u":"id=%s"%querying8[i][0],"ture_name":querying8[i][2],"job":querying8[i][3],"location":querying8[i][4], "hobby":querying8[i][5],"head_p":querying8[i][1]})
                            cont = 6 - cont
                            for i in range(cont):
                                shuiji = random.randint(1001,querying4[0])
                                shuiji = str(shuiji)
                                cur.execute("select head_p,true_name,job,location1,hobby from user_if where uid2=%s "%shuiji)
                                querying10 = cur.fetchone()
                            
                                information.append({"url_u":"id=%s"%shuiji,"ture_name":querying10[1],"job":querying10[2],"location":querying10[3], "hobby":querying10[4],"head_p":querying10[0]})
            return render_template("index.html",information=information,**req)

    else:
        req = {}
        # req["name"] = name

        information = []

        cur.execute("select max(uid1) from user_web ")
        querying4 = cur.fetchone()
        #对未登陆用户展示随机的6位对象，不论男女，不可以重复
       
        for i in range(6):
            #注意深浅拷贝的问题
            shuiji = random.randint(1001,querying4[0])
            shuiji = str(shuiji)
            cur.execute("select head_p,true_name,job,location1,hobby from user_if where uid2=%s "%shuiji)
            querying5 = cur.fetchone()
            
            information.append({"url_u":"id=%s"%shuiji,"ture_name":querying5[1],"job":querying5[2],"location":querying5[3], "hobby":querying5[4],"head_p":querying5[0]})
        return render_template("index.html",information=information)
@app.route("/search")
def search():
    baif = "%"
    dpc = []
    cont = 0
    data = request.args.get("search")
    dpc.append({"error":0})
    cur.execute("select uid2,head_p,true_name,job,location1,hobby from user_if where location1 like '%s%s%s' "%(baif,data,baif))
    querying = cur.fetchall()
    if querying:
        for i in range(len(querying)):
            cont += 1
            if cont == 6:
                dpc = tuple(dpc)
                return jsonify(dpc)
            dpc.append({"url_u":"id=%s"%querying[i][0],"ture_name":querying[i][2],"job":querying[i][3],"location":querying[i][4], "hobby":querying[i][5],"head_p":querying[i][1]})
    else:
        cur.execute("select uid2,head_p,true_name,job,location1,hobby from user_if where hobby like '%s%s%s' "%(baif,data,baif))
        querying1 = cur.fetchall()
        if querying1:
            for i in range(len(querying1)):
                cont += 1
                if cont == 6:
                    dpc = tuple(dpc)
                    return jsonify(dpc)
                dpc.append({"url_u":"id=%s"%querying1[i][0],"ture_name":querying1[i][2],"job":querying1[i][3],"location":querying1[i][4], "hobby":querying1[i][5],"head_p":querying1[i][1]})
        else:
            cur.execute("select uid2,head_p,true_name,job,location1,hobby from user_if where true_name like '%s%s%s' "%(baif,data,baif))
            querying2 = cur.fetchall()
            if querying2:
                for i in range(len(querying2)):
                    cont += 1
                    if cont == 6:
                        dpc = tuple(dpc)
                        return jsonify(dpc)
                    dpc.append({"url_u":"id=%s"%querying2[i][0],"ture_name":querying2[i][2],"job":querying2[i][3],"location":querying2[i][4], "hobby":querying2[i][5],"head_p":querying2[i][1]})
            else:
                cur.execute("select uid1 from user_web where uname like '%s%s%s'"%(baif,data,baif))
                querying3 = cur.fetchall()
                if querying3:
                    for i in range(len(querying3)):
                        id1 = querying3[i][0]
                        cur.execute("select uid2,head_p,true_name,job,location1,hobby from user_if where  uid2='%s' "%(id1))
                        querying4 = cur.fetchone()
                        dpc.append({"url_u":"id=%s"%querying4[0],"ture_name":querying4[2],"job":querying4[3],"location":querying4[4], "hobby":querying4[5],"head_p":querying4[1]})
                else:
                    if re.match("^.*?男.*?$",data):
                        data = "G"
                    if re.match("^.*?女.*?$",data):
                        data = "M"
                    cur.execute("select uid2,head_p,true_name,job,location1,hobby from user_if where sex like '%s%s%s' "%(baif,data,baif))
                    querying5 = cur.fetchall()
                    if querying5:
                        for i in range(len(querying5)):
                            cont += 1
                            if cont == 6:
                                dpc = tuple(dpc)
                                return jsonify(dpc)
                            dpc.append({"url_u":"id=%s"%querying5[i][0],"ture_name":querying5[i][2],"job":querying5[i][3],"location":querying5[i][4], "hobby":querying5[i][5],"head_p":querying5[i][1]})
                    else:
                        dpc[0]["error"] = 1
    dpc = tuple(dpc)
    return jsonify(dpc)

@app.route("/log")
def log():
    session.pop("uname")
    session.pop("upwd")
    return redirect(url_for("home"))
#注册界面
@app.route("/register.html",methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        #注册信息提交
        name = request.form.get("uname")
        password = request.form.get("pwd")
        email = request.form.get("email")
        phone = request.form.get("phone")
        check = request.form.get("check_m")
        #checkbox是否订阅电子报
        checkbox = request.form.get("checkbox")
        uchek = session.get("ucheck")
        
        if uchek == int(check):
            if not user_test.test_name(name):
                return abort(Response("用户注册失败"))
            if not user_test.test_phone(phone):
                return abort(Response("用户注册失败"))
            if not user_test.test_pwd(password):
                return abort(Response("用户注册失败"))
            if not user_test.test_email(email):
                return abort(Response("用户注册失败"))
            
            hashlib_pwd = hashlib.md5(password.encode())
            cur.execute("insert into user_web  values (default,'%s','%s','%s','%s','0','0')"%(name,hashlib_pwd.hexdigest(),phone,email))
            db.commit()
            return redirect(url_for("login"))
        else:
            return abort(Response("用户注册失败"))
        
#从图库中获取图片信息
@app.route("/images/<imgname>")
def user_info(imgname):
    rsq=make_response('{"name":"你的大哥","sex":"不详"}')
    rsq.headers["Content-Type"] = "text/plain; charset=UTF-8"
    return rsq
#登录页面
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        #用户密码和用户名，用户名可以是手机号或者用户ID（比如：‘你的大哥’）
        name = request.form.get("user_name")
        pwd = request.form.get("user_pwd")
        hashlib_pwd = hashlib.md5(pwd.encode())
        cur.execute("select uid1,uname,pwd from user_web where uname='%s' and pwd='%s'"%(name,hashlib_pwd.hexdigest()))
        querying2 = cur.fetchone()
        #登录成功设置Session
        if querying2:
            session["uid"] = querying2[0]
            session["uname"] = name
            session["upwd"] = pwd
            return redirect(url_for("home"))
        else:
            #用户用手机号登录
            cur.execute("select phone,pwd from user_web where phone='%s' and pwd='%s'"%(name,hashlib_pwd.hexdigest()))
            querying2 = cur.fetchone()
            if querying2:
                cur.execute("select uname from user_web where phone='%s'"%(name))
                querying3 = cur.fetchone()
                name = querying3[0]
                session["uname"] = name
                session["upwd"] = pwd
                return redirect(url_for("home"))
            else:
             return abort(Response("用户登录失败"))

#用户完善个人信息界面
@app.route("/perfect",methods=["POST","GET"])
def perfect():
    name = session.get("uname")
    pwd = session.get("upwd")
    # other_user = request.GET.get("name")
    # print("我是个性用户",other_user)
    if not name:
        return redirect(url_for("login"))
    hashlib_pwd = hashlib.md5(pwd.encode())
    cur.execute("select uname,pwd from user_web where uname='%s' and pwd='%s'"%(name,hashlib_pwd.hexdigest()))
    querying2 = cur.fetchone()
    
    if querying2:
        cur.execute("select judge from user_web where uname='%s'"%(name))
        querying3 = cur.fetchone()
        judge = querying3[0]
        if judge == "1":
            return redirect(url_for("home"))
        req1={}
        req1["name"] = name
        if request.method == "GET":
            return render_template("perfect_info.html",**req1)
        if request.method == "POST":
            uploaded_file = request.files["file_img"]
            file_name = uploaded_file.filename
            file_n,file_text = os.path.splitext(file_name)
            file_name = file_n + "_"+name +file_text
            file_path = os.path.join(os.path.join(os.path.join(os.path.dirname(__file__),"static"),"images"),file_name)
            
            uploaded_file.save(file_path)
            file_name_m = "images" + "/" + file_name
            true_name = request.form.get("name")
            sex = request.values.get("sex")
            date = request.form.get("date")
            local = request.form.get("local")
            wedding = request.values.get("wedding")
            height = request.form.get("height")
            weight = request.form.get("weight")
            edu = request.values.get("edu")
            work = request.form.get("work")
            hobby = request.values.getlist("hobby")
            content = request.form.get("content")
           
            cur.execute("select uid1 from user_web where uname='%s'"%(name))
            querying3 = cur.fetchone()
            uid1 = querying3[0]
            dpp = ""
            for i in  hobby:
                dpp += " " + i
            cur.execute("insert into user_if  values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(uid1,file_name_m,true_name,sex,date,height,weight,edu,local,wedding,work,dpp,content))
            db.commit()
            cur.execute("update user_web set judge='1' where uname='%s'"%(name))
            db.commit()
            return redirect(url_for("home"))

    else:
        return redirect(url_for("login"))



#简介信息
@app.route("/single.html")
def single():
    name = session.get("uname")
    pwd = session.get("upwd")
    other_user_id = request.args.get("id")
    
    
    if name or pwd:
        hashlib_pwd = hashlib.md5(pwd.encode())
        cur.execute("select uname,pwd from user_web where uname='%s' and pwd='%s'"%(name,hashlib_pwd.hexdigest()))
        querying2 = cur.fetchone()
        if querying2:
            cur.execute("select * from user_if where uid2='%s' "%(other_user_id))
            querying11 = cur.fetchone()
            cur.execute("select uname from user_web where uid1='%s' "%(other_user_id))
            querying12 = cur.fetchone()
            ree = {}
            print("hhhhhhhhhhhhhhhhhh",other_user_id)
            ree["other_id"] = "id=%s"%other_user_id
            print("kkkkkkkkkkkkkkk",ree["other_id"])
            ree["uname"] = querying12[0]
            ree["head_p"] = querying11[1]
            ree["true_name"] = querying11[2]
            if querying11[3] == "G":
                ree["sex"] = "男"
            else:
                ree["sex"] = "女"
            ree["age"] = querying11[4]
            ree["height"] = querying11[5]
            ree["weight"] = querying11[6]
            ree["edu"] = querying11[7]
            ree["location"] = querying11[8]
            ree["huny"] = querying11[9]
            ree["job"] = querying11[10]
            ree["hobby"] = querying11[11]
            ree["about"] = querying11[12]
            return render_template("single.html",name=name,**ree)
        else:
            return redirect(url_for("login"))
    else:
        return redirect(url_for("login"))
#校验用户名接口API
@app.route("/check_uname")
def login1():
    uname = request.args.get("uname")
    rsq = {}
    #连接数据库查询,校验用户名是否存在
    cur.execute("select uname from user_web where uname='%s'"%uname)
    querying = cur.fetchone()
    if querying:
        print("校验失败")
        rsq["error"] = 1
    else:
        rsq["error"] = 0
    return jsonify(rsq)
#校验手机号，不允许重复注册
@app.route("/check_phone_t")
def check_phone_t():
    phone = request.args.get("phone")
    rsq1 = {}
    #连接数据库查询,校验手机号是否存在
    cur.execute("select phone from user_web where phone='%s'"%phone)
    querying1 = cur.fetchone()
    if querying1:
        print("校验失败")
        rsq1["error"] = 1
    else:
        rsq1["error"] = 0
    return jsonify(rsq1)
#校验手机号，发送验证码API接口
@app.route("/check_phone")
def check_phone():
    phone = request.args.get("phone_nb")
    ct = st.ZhenziSmsClient('https://sms_developer.zhenzikj.com',102927,'eb38637e-5ff8-4791-9db9-f941cd488cc1')
    code=random.randint(10000,100000)
    req = ct.send(phone, '尊敬的用户您好,欢迎加入千寻大家庭，您本次的验证码为%s,有效时间为5分钟'%code)
    session["ucheck"] = code
    return req

@app.route("/other_message_board",methods=["GET","POST"])
def other_message_board():
    req={}
    cur = db.cursor()
    res=[]
    if request.method == "GET":
        other_id = request.args.get("id")
        session["other_id"] = other_id
        print("aaaaaaaaaa",other_id)
        cur.execute("select mg_user_id,mg_text,pub_time from user_meg where uid4=%s "%other_id)
        ress = cur.fetchall()
        if ress:
            for i in range(len(ress)-1,-1,-1):
                cur.execute("select uname from user_web where uid1=%s "%ress[i][0])
                ress1 = cur.fetchone()
                mg_name = ress1[0]
                cur.execute("select head_p from user_if where uid2=%s "%ress[i][0])
                ress3 = cur.fetchone()
                head_p = ress3[0]
                res.append((mg_name,ress[i][1],ress[i][2],head_p,"id=%s"%ress[i][0]))

        return render_template("other_message_board.html", messages=res,**req)
    elif request.method == "POST":
        content = request.form.get("content")
        if content:
            if 0 < len(content) <= 320:
                # 将留言保存到数据库
                other_id = int(session.get("other_id"))
                my_uid = session.get("uid")
                mg_id = 1001
                pub_time = datetime.datetime.now()
                cur = db.cursor()
                print("ssssssssssssssss",content)
                cur.execute("insert into user_meg values (%s,%s,%s,'%s','%s','0')"%(other_id,mg_id,my_uid,content,pub_time))
                db.commit()
                # session.pop("other_id")
                return redirect("other_message_board?id=%s"%other_id)

        abort(Response("留言失败！"))


#用户中心
@app.route("/user_center")
def user_center():
    name = session.get("uname")
    pwd = session.get("upwd")
    # other_user = request.GET.get("name")
    # print("我是个性用户",other_user)
    if name or pwd:
        hashlib_pwd = hashlib.md5(pwd.encode())
        cur.execute("select uname,pwd from user_web where uname='%s' and pwd='%s'"%(name,hashlib_pwd.hexdigest()))
        querying2 = cur.fetchone()
        if querying2:
            return render_template("user_center.html",name=name)
        else:
            return redirect(url_for("login"))
    else:
        return redirect(url_for("login"))
if __name__ == "__main__":
    app.run(port=80,debug=True)