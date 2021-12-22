create table users (
    userID int auto_increment not null primary key,
    username varchar(20) not null unique,
    email varchar2(30) not null unique,
    passwd varchar2(72) not null unique

    
);


create table customers (
    cusID int auto_increment not null,
    userID int not null,
    fname varchar(30),
    lname varchar(30),
    pro_pic varchar(500),
    lvl char(1) default '3',
    primary key (cusID),
    foreign key (userID) references users(userID)
);


create table word(
WordID int auto_increment not null,
word varchar(20) not null,
LVL char(1) default (3),
Meaning varchar(300) not null,
WordCat varchar(25) not null,
wordPro varchar(30) not null,
def_res varchar(1000) not null,
pro_res varchar(1000) not null,
primary key (WordID)
);


create table FAV(
f_ID int auto_increment not null,
cusID int not null,
WordID int not null,
primary key (f_ID),
foreign key (cusID) references customers(cusID),
foreign key (WordID) references word(WordID)

);



create table log (
id int auto_increment primary key,
ts timestamp default current_timestamp,
phrase varchar(128) not null,
letters varchar(32) not null,
ip varchar(16) not null,
browser_string varchar(256) not null,
results varchar(64) not null );





insert into word (word, Meaning, WordCat, wordPro, def_res,pro_res)
                        values ("pheromone","a chemical substance produced and released into the environment by an animal, especially a mammal or an insect, affecting the behaviour or physiology of others of its species.","Noun","ˈfɛrəməʊn","{'id': 'pheromone', 'metadata': {'operation': 'retrieve', 'provider': 'Oxford University Press', 'schema': 'RetrieveEntry'}, 'results': [{'id': 'pheromone', 
'language': 'en-gb', 'lexicalEntries': [{'entries': [{'senses': [{'definitions': ['a chemical substance produced and released into the environment by an animal, especially a mammal or an insect, affecting the behaviour or physiology of others of its species.'], 'id': 'm_en_gbus0773310.005'}]}], 'language': 'en-gb', 'lexicalCategory': {'id': 'noun', 'text': 'Noun'}, 'text': 'pheromone'}], 'type': 
'headword', 'word': 'pheromone'}], 'word': 'pheromone'}","{'id': 'pheromone', 'metadata': {'operation': 'retrieve', 'provider': 'Oxford University Press', 'schema': 'RetrieveEntry'}, 'results': [{'id': 'pheromone', 'language': 'en-gb', 'lexicalEntries': [{'entries': [{'pronunciations': [{'audioFile': 'https://audio.oxforddictionaries.com/en/mp3/pheromone_gb_1.mp3', 'dialects': ['British English'], 'phoneticNotation': 'IPA', 'phoneticSpelling': 'ˈfɛrəməʊn'}]}], 'language': 'en-gb', 'lexicalCategory': {'id': 'noun', 'text': 'Noun'}, 'text': 'pheromone'}], 'type': 'headword', 'word': 'pheromone'}], 'word': 'pheromone'})"


insert into word (word, Meaning, WordCat, wordPro, def_res,pro_res)
                        values ("always","at all times; on all occasions","Adverb","ˈɔːlweɪz","{'id': 'always', 'metadata': {'operation': 'retrieve', 'provider': 'Oxford University Press', 'schema': 'RetrieveEntry'}, 'results': [{'id': 'always', 'language': 'en-gb', 'lexicalEntries': [{'entries': [{'senses': [{'definitions': ['at all times; on all occasions'], 'id': 'm_en_gbus0026750.008', 'subsenses': [{'definitions': ['throughout a long period of the past'], 'id': 'm_en_gbus0026750.010'}, {'definitions': ['for all future time; forever'], 'id': 'm_en_gbus0026750.011'}, {'definitions': ['repeatedly and annoyingly'], 'id': 'm_en_gbus0026750.012'}]}, {'definitions': ['as a last resort; failing all else'], 'id': 'm_en_gbus0026750.014'}]}], 'language': 'en-gb', 'lexicalCategory': {'id': 'adverb', 'text': 'Adverb'}, 'text': 'always'}], 'type': 'headword', 'word': 'always'}], 'word': 'always'}","{'id': 'always', 'metadata': {'operation': 'retrieve', 'provider': 'Oxford University Press', 'schema': 'RetrieveEntry'}, 'results': [{'id': 'always', 'language': 'en-gb', 'lexicalEntries': [{'entries': [{'pronunciations': [{'audioFile': 'https://audio.oxforddictionaries.com/en/mp3/always_gb_1.mp3', 'dialects': ['British English'], 'phoneticNotation': 'IPA', 'phoneticSpelling': 'ˈɔːlweɪz'}, {'dialects': ['British English'], 'phoneticNotation': 'IPA', 'phoneticSpelling': 'ˈɔːlweɪz'}]}], 'language': 'en-gb', 'lexicalCategory': {'id': 'adverb', 'text': 'Adverb'}, 'text': 'always'}], 'type': 'headword', 'word': 'always'}], 'word': 'always'}")

create table rendered(
RID int auto_increment not null,
cusID int not null,
WordID int not null,
rtime DATETIME DEFAULT CURRENT_TIMESTAMP,
primary key (RID),
foreign key (cusID) references customers(cusID),
foreign key (WordID) references word(WordID)

);


create table wlist
(
    wlid int auto_increment not null,
    word varchar(30),
    primary key (wlid)
)

ALTER TABLE wlist ADD CONSTRAINT constraint_name UNIQUE (word)


SELECT * FROM wlist AS t1 JOIN (SELECT wlid FROM wlist ORDER BY RAND() LIMIT 10) as t2 ON t1.wlid=t2.wlid



"insert into knows (cusid, wordid) value ((select cusid from customers c, users u where username = '{}' and u.userid = c.userid),(select wordid from word where word='{}'))".format(user, famword)


 (select r.wordid from rendered r natural left join knows k where k.wordid is NULL and r.cusid=9 limit 9)

 select w.word, w.wordpro from word w inner join (select r.wordid from rendered r natural left join knows k where k.wordid is NULL and r.cusid=9 limit 9) as w2 on w.wordid = w2.wordid
 select w.word, w.wordpro from word w inner join (select r.wordid from rendered r natural left join knows k where k.wordid is NULL and r.cusid=9 limit 9) as w2 on w.wordid = w2.wordid
 select w.word, w.wordpro from word w inner join (select r.wordid from rendered r natural left join knows k where k.wordid is NULL and r.cusid=9 limit 9) as w2 on w.wordid = w2.wordid


 "update wlist set level=1 where word={}".format(word)