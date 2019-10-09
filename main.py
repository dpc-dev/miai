from flask import *
import random,os,user_test,pymysql,hashlib,user_test
import st
app = Flask(__name__)
db = pymysql.connect("localhost","root","1478963520.ai","qxun")
cur = db.cursor()
app.config['SECRET_KEY'] = b'\xa3P\x06\x1a\xf8\xc6\xff\xa4!\xd2\xb5\n\x96\x05\xed\xc3\xc90=\x07\x8d>\x8e\xeb'
@app.route("/")
def home():
    #获取Session
    name = session.get("uname")
    req = {}
    req["name"] = name
    req["url_u"] = "name='你的大哥'"
    req["ture_name"]="邓彭川"
    req["job"]="程序员"
    req["location"] = "武汉"
    req["hobby"]="运动"
    req["head_p"]='images/a.jpg'
    return render_template("index.html",**req)

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
        print(name,password,phone,check,email,checkbox)
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
            cur.execute("insert into user_web  values (default,'%s','%s','%s','%s','0')"%(name,hashlib_pwd.hexdigest(),phone,email))
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
        cur.execute("select uname,pwd from user_web where uname='%s' and pwd='%s'"%(name,hashlib_pwd.hexdigest()))
        querying2 = cur.fetchone()
        #登录成功设置Session
        if querying2:
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

#简介信息
@app.route("/single.html")
def single():
    name = session.get("uname")
    pwd = session.get("upwd")
    # other_user = request.GET.get("name")
    # print("我是个性用户",other_user)
    hashlib_pwd = hashlib.md5(pwd.encode())
    cur.execute("select uname,pwd from user_web where uname='%s' and pwd='%s'"%(name,hashlib_pwd.hexdigest()))
    querying2 = cur.fetchone()
    if querying2:
        return render_template("single.html",name=name)
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
    
if __name__ == "__main__":
    app.run(port=80,debug=True)