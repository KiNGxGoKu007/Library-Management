drop database ta_lib;
create database ta_lib;
use ta_lib;
create table Books(
Book_Id int Primary key,
Book_name varchar(50),
Sub varchar(50),
ISBN varchar(50),
Standard varchar(15),
Author varchar(50),
Price float
);

create table Members(
Member_Id int Primary key,
Member_name varchar(50),
Email varchar(50),
Contact_no varchar(10),
Standard varchar(15),
DOJL date
);

create table Issue_return(
Issue_Id int Primary key auto_increment,
Book_Id int references Books(Book_Id),
Member_Id int references Members(Member_Id),
Issue_date date,
Return_date date,
Fine int,
Rating int
);

desc Books;
desc Members;
desc Issue_return;
insert into Members values(1,'Aman','aman@mail.com','9876543215','XII','2022-01-01');
insert into Members values(2,'Baman','baman@mail.com','9876543654','XI','2022-01-01');
insert into Members values(3,'Chaman','chaman@mail.com','3216549874','IX','2022-01-01');
insert into Members values(4,'Daman','daman@mail.com','5165135468','XI','2022-01-01');
insert into Members values(5,'Raman','raman@mail.com','8797453216','XII','2022-01-01');
insert into Members values(6,'Abhinav','abhinav@mail.com','9865932656','XII','2021-01-01');
insert into Members values(7,'Tanish','tanish@mail.com','8817390893','XI','2020-02-11');
insert into Members values(8,'Manas','manas@mail.com','8817295735','X','2021-02-19');
insert into Members values(9,'Koushik','koushik@mail.com','8819305729','XII','2020-03-21');
insert into Members values(10,'Vatsal','vatsal@mail.com','8843010194','XII','2020-01-17');
insert into Members values(11,'Harshwardhan','harsh@mail.com','9301846573','X','2021-01-23');
insert into Members values(12,'Akshat','akshat@mail.com','5677705140','IX','2022-04-12');
insert into Members values(13,'Ishita','ishita@mail.com','9876543215','X','2022-04-21');
insert into Members values(14,'Manya','manya@mail.com','9876512342','XI','2020-06-22');
insert into Members values(15,'Ishan','ishan@mail.com','3216827651','XII','2020-03-09');
insert into Members values(16,'Kankana','kankana@mail.com','5165137768','XI','2021-06-07');
insert into Members values(17,'Poorvi','poorvi@mail.com','8117400216','IX','2022-04-21');
insert into Members values(18,'Prabhanshu','prabhanshu@mail.com','5677668215','XI','2021-06-11');
insert into Members values(19,'Anish','anish@mail.com','9865779956','XII','2021-01-01');
insert into Members values(20,'Rohit','rohit@mail.com','8817340093','XI','2020-02-11');
insert into Members values(21,'Suman','suman@mail.com','8811115735','X','2021-02-19');
insert into Members values(22,'Karan','karan@mail.com','8073105729','XII','2020-03-21');
insert into Members values(23,'Vikram','vikram@mail.com','8843559094','XII','2020-01-17');
insert into Members values(24,'Havish','havish@mail.com','2356846573','X','2021-01-23');
insert into Members values(25,'Armaan','armaan@mail.com','3498705140','IX','2022-04-12');
insert into Members values(26,'Irina','irina@mail.com','2933543215','X','2022-04-21');
insert into Members values(27,'Megha','megha@mail.com','3316512342','XI','2020-06-22');
insert into Members values(28,'Imran','imran@mail.com','3299827651','XII','2020-03-09');
insert into Members values(29,'Kabir','kabir@mail.com','5112347768','XI','2021-06-07');
insert into Members values(30,'Pushpa','pushpa@mail.com','8117055316','IX','2022-04-21');


select * from Members;
select * from Books;
select * from Issue_return;

insert into Books values(1001, "Harry Potter and the Sorcere's Stone", "Fantasy", 5461, "xii", "JK Rowling", 699);
insert into Books values(1002, "Harry Potter and the Chamber of Secrets", "Fantasy", 5462, "xii", "JK Rowling", 599);
insert into Books values(1003, "Harry Potter and the Prisoner of Azkaban", "Fantasy", 5463, "xii", "JK Rowling", 599);
insert into Books values(1004, "Harry Potter and the Goblet of Fire", "Fantasy", 5464, "xii", "JK Rowling", 699);
insert into Books values(1005, "Harry Potter and the Order of the Phoenix", "Fantasy", 5465, "xii", "JK Rowling", 599);
insert into Books values(1006, "Harry Potter and the Half-Blood Prince", "Fantasy", 5466, "xii", "JK Rowling", 699);
insert into Books values(1007, "Harry Potter and the Deathly Hallows", "Fantasy", 5467, "xii", "JK Rowling", 799);
insert into Books values(1008, "Harry Potter and the Cursed Child", "Fantasy", 5468, "xii", "JK Rowling", 899);
insert into Books values(1009, "The Princeton Companion to Mathematics", "Mathematics", 5469, "xii", "June Barrow-Green", 550);
insert into Books values(1010, "Encyclopedia of Mathematics", "Mathematics", 5470, "xii", "James Stuart Tanton", 850);
insert into Books values(1011, "A Mathematical Introduction to Logics", "Mathematics", 5471, "xii", "Herbert Ederton", 500);
insert into Books values(1012, "Categories for Working Mathematicians", "Mathematics", 5472, "xii", "Sauders Mac Lane", 400);
insert into Books values(1013, "Classic Set Theory", "Mathematics", 5473, "xii", "Derek C Goldrei", 600);
insert into Books values(1014, "Abstract Algebra", "Mathematics", 5474, "xii", "Richard M Foote", 350);
insert into Books values(1015, "Calculus Made Easy", "Mathematics", 5475, "xii", "Silvanus Thompson", 250);
insert into Books values(1016, "Linear Algebra", "Mathematics", 5476, "xii", "Sheldon Axler", 400);
insert into Books values(1017, "The four pillar of Geometry", "Mathematics", 5477, "xii", "John Stillwell", 400);
insert into Books values(1018, "Elementary Number Theory", "Mathematics", 5478, "xii", "Gareth A Jones", 150);
insert into Books values(1019, "An Introduction To Probability", "Mathematics", 5479, "xii", "Willian Feller", 300);
insert into Books values(1020, "Principles of Mathematical Analysis", "Mathematics", 5480, "xii", "Walter Rudin", 200);
insert into Books values(1021, "Introductory Statistics", "Mathematics", 5481, "xii", "Neil A Weiss", 770);
insert into Books values(1022, "Introduction to Topology and Modern Analysis", "Mathematics", 5482, "xii", "George F Simmons", 600);
insert into Books values(1023, "Basic Mathematics", "Mathematics", 5483, "xii", "Serge Lang", 270);
insert into Books values(1024, "Absolution Gap", "Fiction", 5484, "xii", "Alastair Reynoldsg", 800);
insert into Books values(1025, "Battlefield Earth", "Fiction", 5485, "xii", "Ron Hubbard", 800);
insert into Books values(1026, "The Bell-Tower", "Fiction", 5486, "xii", "Fiction", 800);
insert into Books values(1027, "A Billion Days of Earth", "Fiction", 5487, "xii", "Doris Piserchia", 900);
insert into Books values(1028, "The Canopy of Time", "Fiction", 5488, "xii", "Brian W Aldiss", 800);
insert into Books values(1029, "Child of Fortune", "Fiction", 5489, "xii", "Norman Spinrad", 700);
insert into Books values(1030, "City of Illusions", "Fiction", 5490, "xii", "Ursula K Le Guin", 700);
insert into Books values(1031, "QED: The Strange Theory of Light", "Science", 5491, "xii", "Richard Feynman", 865);
insert into Books values(1032, "On Growth and Form", "Science", 5492, "xii", " DArcy Wentworth Thompson", 780);
insert into Books values(1033, "Ideas And Opinions", "Science", 5493, "xii", " Albert Einstein", 640);
insert into Books values(1034, "Double Helix", "Science", 5494, "xii", " James D Watson", 660);
insert into Books values(1035, "Lives of a Cell", "Science", 5495, "xii", "Lewis Thomas", 520);
insert into Books values(1036, "The Structure of Scientific Revolutions", "Science", 5496, "xii", " Thomas Kuhn", 735);
insert into Books values(1037, "Knowledge and Wonder", "Science", 5497, "xii", "Victor Weisskopf", 985);
insert into Books values(1038, "What Evolution Is", "Science", 5498, "xii", "Ernst Mayr", 640);
insert into Books values(1039, "The Superorganism", "Science", 5499, "xii", "Bert Holldobler", 880);
insert into Books values(1040, "The Selfish Gene", "Science", 5500, "xii", "Richard Dawkins", 670);
insert into Books values(1041, "The Music of Life: Biology Beyond Genes", "Science", 5501, "xii", "Denis Noble", 950);
insert into Books values(1042, "A Brief History of Time", "Science", 5502, "xii", "Stephen Hawking", 980);
insert into Books values(1043, "The Making of the Atomic Bomb", "Science", 5503, "xii", "Richard Rhodes", 490);
insert into Books values(1044, "The Elegant Universe", "Science", 5504, "xii", "Brian Greene", 790);
insert into Books values(1045, "Physics and Philosophy", "Science", 5505, "xii", "Werner Heisenberg", 660);
insert into Books values(1046, "Nimona", "Comic Novel", 5506, "xii", "Noelle Stevenson", 250);
insert into Books values(1047, "Watchmenr", "Comic Novel", 5507, "xii", "Watchmen", 250);
insert into Books values(1048, "Maus: A Survivors Tale", "Comic Novel", 5508, "xii", "Art Spiegelman", 320);
insert into Books values(1049, "Daytripper", "Comic Novel", 5509, "xii", "Gabriel Ba", 250);
insert into Books values(1050, "This One Summer", "Comic Novel", 5510, "xii", "Mariko Tamaki", 280);
insert into Books values(1051, "Sweet Tooth", "Comic Novel", 5511, "xii", "Jeff Lemire", 350);
insert into Books values(1052, "Through The Woods", "Comic Novel", 5512, "xii", "Emily Carroll", 300);
insert into Books values(1053, "Blankets", "Comic Novel", 5513, "xii", "Craig Thompson", 200);
insert into Books values(1054, "Jimmy Corrigan", "Comic Novel", 5514, "xii", "Chris Ware", 240);
insert into Books values(1055, "Blacksad", "Comic Novel", 5515, "xii", "Juanjo Guarnido", 260);
insert into Books values(1056, "The Pilgrim’s Progress", "Novel", 5516, "xii", "John Bunyan", 780);
insert into Books values(1057, "Robinson Crusoe", "Novel", 5517, "xii", "Daniel Defoe", 880);
insert into Books values(1058, "Gulliver’s Travels", "Novel", 5518, "xii", "Jonathan Swift", 680);
insert into Books values(1059, "Clarissa", "Novel", 5519, "xii", "Samuel Richardson", 980);
insert into Books values(1060, "Tom Jones", "Novel", 5520, "xii", "Henry Fielding", 940);
insert into Books values(1061, "Frankenstein", "Novel", 5521, "xii", "Mary Shelley", 440);
insert into Books values(1062, "Gothic Tales", "Horror", 5522, "xii", "Elizabeth Gaskell", 550);
insert into Books values(1063, "Carmilla", "Horror", 5523, "xii", "Sheridan Le Fanu", 780);
insert into Books values(1064, "Dracula", "Horror", 5524, "xii", "Bram Stoker", 820);
insert into Books values(1065, "The Turn of the Screw", "Horror", 5525, "xii", "Henry James", 690);
insert into Books values(1066, "Collected Ghost Stories", "Horror", 5526, "xii", "M. R. James", 480);
insert into Books values(1067, "Goosebumps", "Horror", 5527, "xii", "R L Stine", 710);

select * from Books;
select * from Issue_return;
