-- 创建表存储用户信息,uid(用户ID，主键),uanme(用户名,唯一),pwd(用户密码,加盐),phone(手机号),error(账号状态,0正常，1注销,2异常),status(0管理员，1普通用户)
-- judge,判断用户是否已经完善信息，0表示否，1表示是,默认为零
drop table user_web;
create table user_web (
    uid1 int unsigned auto_increment,
    uname varchar(20) not null unique,
    pwd char(32) not null,
    phone char(11) not null,
    email char(32),
    error enum("0","1","2") not null,
    judge enum("0","1") not null,
    primary key(uid1)
)engine=InnoDB auto_increment=1001 default charset=utf8;
-- 用户详细信息表
-- uid2(用户的ID，外键)
-- head_p(用户头像)
-- true_name(用户的真实姓名，必填)
-- sex（用户性别，必填）
-- age（用户年龄，必填）
-- height(用户身高,必填)
-- weight1(用户体重,必填)
-- nation(国家)
-- haddress(家乡地址)
-- location1（用户所在地，选填）
-- huny（婚姻状态，1（未婚），2（离异），3(丧偶)，选填）
-- job（用户职业，选填）
-- hobby(用户爱好，必填)
-- about（用户简介）

create table user_if (
    uid2 int unsigned not null,
    head_p varchar(300) not null,
    true_name char(20) not null,
    sex enum("G","M") not null ,
    age char(30) not null,
    height char(10) not null,
    weight1 char(10) not null,
    education char(10),
    -- nation varchar(150) not null,
    -- haddress varchar(150) not null,
    location1 varchar(150),
    huny enum("未婚","离异","丧偶") not null,
    job varchar(150),
    hobby varchar(150),
    about varchar(320),
    foreign key(uid2) references user_web(uid1)
)engine=InnoDB  default charset=utf8;
-- 用户图片信息 
-- uid3（用户id，外键约束）
-- pid（用户图片信息,int,0开始）
-- p_if (用户图片内容)
create table user_pic (
    uid3 int unsigned not null,
    pid int not null ,
    p_if varchar(300) not null,
    foreign key(uid3) references user_web(uid1)
)engine=InnoDB  default charset=utf8;
-- 用户的留言信息
-- uid4（用户ID，外键约束）
-- mg_id(留言id,从0开始)
-- mg_user_id(留言用户id，外键约束)
-- mg_text(留言内容)
--pub_time(留言时间)
-- error（留言状态，0,正常，1删除）
create table user_meg (
    uid4 int unsigned not null,
    mg_id int not null,
    mg_user_id int unsigned not null,
    mg_text varchar(320) not null,
    pud_time datetime not null,
    error enum("0","1"),
    foreign key(uid4) references user_web(uid1),
    foreign key(mg_user_id) references user_web(uid1)
)engine=InnoDB  default charset=utf8;
-- insert into user_web values(default,"root1",md5("1478963520.ai"),"18671289536","0","1");