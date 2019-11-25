-- MySQL dump 10.13  Distrib 5.7.28, for Linux (x86_64)
--
-- Host: localhost    Database: vondd
-- ------------------------------------------------------
-- Server version	5.7.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `genre`
--

DROP TABLE IF EXISTS `genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `genre` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genre`
--

LOCK TABLES `genre` WRITE;
/*!40000 ALTER TABLE `genre` DISABLE KEYS */;
INSERT INTO `genre` VALUES (8,'Action'),(17,'Animation'),(1,'Biography'),(6,'Comedy'),(9,'Crime'),(11,'Documentary'),(2,'Drama'),(16,'Family'),(7,'Fantasy'),(3,'History'),(18,'Horror'),(20,'Music'),(19,'Mystery'),(21,'N/A'),(15,'News'),(14,'Romance'),(13,'Short'),(12,'Sport'),(4,'Thriller'),(5,'War'),(10,'Western');
/*!40000 ALTER TABLE `genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie`
--

DROP TABLE IF EXISTS `movie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `movie` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` varchar(500) NOT NULL,
  `imdb_url` varchar(255) DEFAULT NULL,
  `imdb_rating` varchar(4) DEFAULT NULL,
  `rotten_tomatoes_rating` varchar(3) DEFAULT NULL,
  `meta_critic_rating` varchar(7) DEFAULT NULL,
  `year` int(4) DEFAULT NULL,
  `poster_url` varchar(255) DEFAULT NULL,
  `added` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=939 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie`
--

LOCK TABLES `movie` WRITE;
/*!40000 ALTER TABLE `movie` DISABLE KEYS */;
INSERT INTO `movie` VALUES (867,'12 Years a Slave','In the antebellum United States, Solomon Northup, a free black man from upstate New York, is abducted and sold into slavery.','tt2024544',NULL,NULL,NULL,2013,'foobar','2019-11-22 12:37:40'),(868,'The 12th Man','They were 12 saboteurs. The Nazis killed 11 of them. This is the true story of the one who got away...','tt3300980',NULL,NULL,NULL,2017,'foobar','2019-11-22 12:52:31'),(869,'17 Again','Mike O\'Donnell is ungrateful for how his life turned out. He gets a chance to rewrite his life when he tried to save a janitor near a bridge and jumped after him into a time vortex.','tt0974661',NULL,NULL,NULL,2009,'foobar','2019-11-22 12:52:32'),(870,'3:10 to Yuma','A small-time rancher agrees to hold a captured outlaw who\'s awaiting a train to go to court in Yuma. A battle of wills ensues as the outlaw tries to psych out the rancher.','tt0381849',NULL,NULL,NULL,2007,'foobar','2019-11-22 12:52:32'),(871,'4 Little Girls','A documentary of the notorious racial terrorist bombing of an African American church during the Civil Rights Movement.','tt0118540',NULL,NULL,NULL,1997,'foobar','2019-11-22 12:52:32'),(872,'7 Days in Hell','A fictional documentary-style expose on the rivalry between two of the greatest tennis players of all-time who battled it out in a 2001 match that lasted seven days.','tt3895884',NULL,NULL,NULL,2015,'foobar','2019-11-22 12:52:32'),(873,'7th Annual Young Comedians Show','N/A','tt0777180',NULL,NULL,NULL,1982,'foobar','2019-11-22 12:52:32'),(874,'The 8th Annual Young Comedians Show','N/A','tt0409923',NULL,NULL,NULL,1983,'foobar','2019-11-22 12:52:32'),(875,'A Dangerous Son','Documentary following three families each coping with a child affected by serious emotional or mental illness. The families explore treatment opportunities and grapple with the struggle of living with their child\'s condition.','tt8294204',NULL,NULL,NULL,2018,'foobar','2019-11-22 12:52:33'),(876,'A Dog Year','A guy suffering from a midlife crisis takes in a dog that\'s crazier than he is.','tt0808232',NULL,NULL,NULL,2009,'foobar','2019-11-22 12:52:33'),(877,'A Girl in the River: The Price of Forgiveness','A woman in Pakistan sentenced to death for falling in love becomes a rare survivor of the country\'s harsh judicial system.','tt5144072',NULL,NULL,NULL,2015,'foobar','2019-11-22 12:52:34'),(878,'A Good Job: Stories of the FDNY','Acclaimed actor and FDNY veteran Steve Buscemi looks at what it\'s like to work as a New York City firefighter. Utilizing exclusive behind-the-scenes footage and firsthand accounts from past...','tt3983732',NULL,NULL,NULL,2014,'foobar','2019-11-22 12:52:34'),(879,'A History of Violence','A mild-mannered man becomes a local hero through an act of violence, which sets off repercussions that will shake his family to its very core in this action thriller.','tt0399146',NULL,NULL,NULL,2005,'foobar','2019-11-22 12:52:34'),(880,'A Most Wanted Man','A Chechen Muslim illegally immigrates to Hamburg, where he gets caught in the international war on terror.','tt1972571',NULL,NULL,NULL,2014,'foobar','2019-11-22 12:52:34'),(881,'A Quiet Passion','The story of American poet Emily Dickinson from her early days as a young schoolgirl to her later years as a reclusive, unrecognized artist.','tt2392830',NULL,NULL,NULL,2016,'foobar','2019-11-22 12:52:34'),(882,'A Single Man','An English professor, one year after the sudden death of his boyfriend, is unable to cope with his typical days in 1960s Los Angeles.','tt1315981',NULL,NULL,NULL,2009,'foobar','2019-11-22 12:52:34'),(883,'Abortion: Stories Women Tell','This documentary gives women a voice in the choices they\'ve had to make regarding their pregnancies.','tt5591746',NULL,NULL,NULL,2016,'foobar','2019-11-22 12:52:34'),(884,'Across the Waters','Fuglene Over Sundet is the gripping tale of the Danish Jews\' escape to Sweden in October 1943.','tt4838486',NULL,NULL,NULL,2016,'foobar','2019-11-22 12:52:34'),(885,'Addiction','A brutal act of self-defense unleashes a quiet man\'s inner demons.','tt0380167',NULL,NULL,NULL,2003,'foobar','2019-11-22 12:52:34'),(886,'Agnelli','The story of Gianni Agnelli, the legendary Italian industrialist and playboy, as told by family, lovers, professional confidants, and rivals.','tt6798422',NULL,NULL,NULL,2017,'foobar','2019-11-22 12:52:36'),(887,'Alive Day Memories: Home from Iraq','American Soldiers fighting in the Iraq war and their homecomings.','tt0933877',NULL,NULL,NULL,2007,'foobar','2019-11-22 12:52:36'),(888,'All About Ann: Governor Richards of the Lone Star State','HBO presents the life story of Ann Richards, the hilarious straight-talking Governor of Texas.','tt3176284',NULL,NULL,NULL,2014,'foobar','2019-11-22 12:52:36'),(889,'All Roads Lead to Rome','Maggie is an uptight, single mother and college writing teacher from New York City. In an effort to reconnect with her troubled teen daughter Summer, she decides to embark on a journey to a...','tt4119278',NULL,NULL,NULL,2015,'foobar','2019-11-22 12:52:36'),(890,'All the Way','Lyndon Baines Johnson becomes the President of the United States in the chaotic aftermath of John F. Kennedy\'s assassination and spends his first year in office fighting to pass the Civil Rights Act.','tt3791216',NULL,NULL,NULL,2016,'foobar','2019-11-22 12:52:36'),(891,'Alternate Endings: Six new ways to die in America','Exploring the changing attitudes, rituals and mechanics of death, including the ways it is recognized, and how the end of life is approached.','tt10720098',NULL,NULL,NULL,2019,'foobar','2019-11-22 12:52:36'),(892,'Amanda Seales: I Be Knowin\'','Comedian Amanda Seales presents her stand-up debut: I Be Knowin\'. In this hour-long HBO special, Amanda shares from her memories of romance in high school up to what it means to be a 30-year-old black woman in America today.','tt9310314',NULL,NULL,NULL,2019,'foobar','2019-11-22 12:52:37'),(893,'American Hustle','A con man, Irving Rosenfeld, along with his seductive partner Sydney Prosser, is forced to work for a wild F.B.I. Agent, Richie DiMaso, who pushes them into a world of Jersey powerbrokers and the Mafia.','tt1800241',NULL,NULL,NULL,2013,'foobar','2019-11-22 12:52:37'),(894,'American Splendor','An original mix of fiction and reality illuminates the life of comic book hero everyman Harvey Pekar.','tt0305206',NULL,NULL,NULL,2003,'foobar','2019-11-22 12:52:37'),(895,'Americans in Bed','Ten American couples--captured in the comfort of their own beds--openly discuss romance, sex, trust and love in candid interviews. From young New Yorkers who have split up 26 times to ...','tt6690860',NULL,NULL,NULL,2013,'foobar','2019-11-22 12:52:37'),(896,'Amy Schumer: Live at the Apollo','With her bold, straightforward style of comedy, Amy Schumer entertains the audience at the Apollo Theater in New York.','tt4909348',NULL,NULL,NULL,2015,'foobar','2019-11-22 12:52:37'),(897,'An American Girl: Chrissa Stands Strong','A fourth grader and her friends deal with bullying from a more popular girl in their class.','tt1340418',NULL,NULL,NULL,2009,'foobar','2019-11-22 12:52:37'),(898,'An Apology to Elephants','Narrated by Lily Tomlin, this documentary short traces mankind\'s long history with elephants and explores the many problems that arise when they are brought to live in captivity in zoos and circuses.','tt2836524',NULL,NULL,NULL,2013,'foobar','2019-11-22 12:52:37'),(899,'Anchorman 2: The Legend Continues','With the 1970s behind them, San Diego\'s top-rated newsman, Ron Burgundy, returns to take New York City\'s first twenty-four-hour news channel by storm.','tt1229340',NULL,NULL,NULL,2013,'foobar','2019-11-22 12:52:37'),(900,'Anchorman: The Legend of Ron Burgundy','Ron Burgundy is San Diego\'s top-rated newsman in the male-dominated broadcasting of the 1970s, but that\'s all about to change for Ron and his cronies when an ambitious woman is hired as a new anchor.','tt0357413',NULL,NULL,NULL,2004,'foobar','2019-11-22 12:52:37'),(901,'And Starring Pancho Villa as Himself','Hollywood makes a deal with Mexican revolutionary Pancho Villa to film his war and recreate his life.','tt0337824',NULL,NULL,NULL,2003,'foobar','2019-11-22 12:52:37'),(902,'Arbitrage','A troubled hedge fund magnate desperate to complete the sale of his trading empire makes an error that forces him to turn to an unlikely person for help.','tt1764183',NULL,NULL,NULL,2012,'foobar','2019-11-22 12:52:38'),(903,'Arthur Miller: Writer','Rebecca Miller\'s film is a portrait of her father, his times and insights, built around impromptu interviews shot over many years in the family home. This celebration of the great American ...','tt7302488',NULL,NULL,NULL,2017,'foobar','2019-11-22 12:52:38'),(904,'As You Like It','A daughter of the powerful Duke must show her courage and inventiveness to be with the man she loves.','tt0450972',NULL,NULL,NULL,2006,'foobar','2019-11-22 12:52:38'),(905,'asterix','N/A','tt6418972',NULL,NULL,NULL,1980,'foobar','2019-11-22 12:52:38'),(906,'At the Heart of Gold: Inside the USA Gymnastics Scandal','In 2016, USA Gymnastics was rocked by the revelation that national team doctor Larry Nassar had been abusing young athletes for decades. Tribeca alum Erin Lee Carr\'s unflinching documentary...','tt8299654',NULL,NULL,NULL,2019,'foobar','2019-11-22 12:52:39'),(907,'Atomic Homefront','A terrifying look at the corruption that\'s destroying our nation and our planet. This should shake every American citizen. Citizens of an American city fight back against corruption and greed and try to save their own lives.','tt6829446',NULL,NULL,NULL,2017,'foobar','2019-11-22 12:52:39'),(908,'Back on Board: Greg Louganis','Feature-length documentary about the greatest diver of all time. Four-time Olympic champion Greg Louganis has faced more than his share of challenges. In 2011, he is far from the public eye...','tt3240752',NULL,NULL,NULL,2014,'foobar','2019-11-22 12:52:39'),(909,'Backstabbing for Beginners','A young program coordinator at the United Nations stumbles upon a conspiracy involving Iraq\'s oil reserves.','tt5153288',NULL,NULL,NULL,2018,'foobar','2019-11-22 12:52:39'),(910,'Baghdad ER','Winner of four Emmy(R) Awards, including Outstanding Directing for Nonfiction Programming (Jon Alpert, Matthew O\'Neill)! The 86th Combat Support Hospital (CSH)--the U.S. Army\'s premier ...','tt0802944',NULL,NULL,NULL,2006,'foobar','2019-11-22 12:52:39'),(911,'Baltimore Rising','Baltimore Rising follows activists, police officers, community leaders and gang affiliates, who struggle to hold Baltimore together in the wake of Freddie Gray\'s death in police custody.','tt7653006',NULL,NULL,NULL,2017,'foobar','2019-11-22 12:52:40'),(912,'The Visitors: Bastille Day','Knight Godefroy de Montmirail and squire Jacquouille are stranded in 1793. Using trickery to break free from their shackles, both perilously partake in the Montmirail family\'s run away in the quest for an exiting time-shift.','tt2441982',NULL,NULL,NULL,2016,'foobar','2019-11-22 12:52:40'),(913,'Beautiful Creatures','Ethan longs to escape his small Southern town. He meets a mysterious new girl, Lena. Together, they uncover dark secrets about their respective families, their history and their town.','tt1559547',NULL,NULL,NULL,2013,'foobar','2019-11-22 12:52:41'),(914,'Becoming Mike Nichols','Filmmaker Mike Nichols sits down with theater director Jack O\'Brien to discuss his personal life and professional work.','tt5278964',NULL,NULL,NULL,2016,'foobar','2019-11-22 12:52:41'),(915,'Becoming Warren Buffett','The legendary investor started out as an ambitious, numbers-obsessed boy from Nebraska and ended up becoming one of the richest and most respected men in the world.','tt6438096',NULL,NULL,NULL,2017,'foobar','2019-11-22 12:52:41'),(916,'Before I Go to Sleep','A woman wakes up every day, remembering nothing as a result of a traumatic accident in her past. One day, new terrifying truths emerge that force her to question everyone around her.','tt1726592',NULL,NULL,NULL,2014,'foobar','2019-11-22 12:52:41'),(917,'Beginners','A young man is rocked by two announcements from his elderly father: that he has terminal cancer and that he has a young male lover.','tt1532503',NULL,NULL,NULL,2010,'foobar','2019-11-22 12:52:41'),(918,'Behind the Candelabra','A chronicle of the tempestuous six-year romance between megastar singer Liberace and his young lover Scott Thorson.','tt1291580',NULL,NULL,NULL,2013,'foobar','2019-11-22 12:52:41'),(919,'Bernard and Doris','The story of the twilight years of tobacco billionairess Doris Duke and her relationship with her gay butler, to whom she left her entire fortune.','tt0470732',NULL,NULL,NULL,2006,'foobar','2019-11-22 12:52:41'),(920,'Bessie','The story of legendary blues performer Bessie Smith, who rose to fame during the 1920s and \'30s.','tt3704352',NULL,NULL,NULL,2015,'foobar','2019-11-22 12:52:41'),(921,'Beware the Slenderman','Tells the story of two 12-year old girls, who attempted to murder one of their friends in an attempt to appease Slenderman, a fictional monster from a horror website.','tt5329376',NULL,NULL,NULL,2016,'foobar','2019-11-22 12:52:41'),(922,'Bill Maher: Live from D.C.','In his 10th HBO stand-up special, Bill Maher, the political commentator and satirist discusses midterm elections, income inequality, the Republican psyche, a Trump lawsuit, why the Pope is an atheist and why tattoos are stupid.','tt3918650',NULL,NULL,NULL,2014,'foobar','2019-11-22 12:52:41'),(923,'Bill Maher: Live from Oklahoma','Bill visits the Brady Theater in Tulsa, Oklahoma for his 11th HBO stand-up special. The topics include the current state of U.S. politics, sexuality, political correctness, aging and Bill\'s amusingly profound hatred of small children.','tt8398704',NULL,NULL,NULL,2018,'foobar','2019-11-22 12:52:41'),(924,'Bill Maher: The Decider','Comedian, writer and politically incorrect HBO talk-show host Bill Maher takes time off from his regular hosting duties to perform a hilariously scathing stand-up set in his eighth HBO ...','tt1039915',NULL,NULL,NULL,2007,'foobar','2019-11-22 12:52:41'),(925,'Bill Maher: Victory Begins at Home','Bill Maher stars in his sixth HBO stand-up special, premiering LIVE from the Hudson Theater in New York!','tt0377515',NULL,NULL,NULL,2003,'foobar','2019-11-22 12:52:41'),(926,'Billy Crystal: 700 Sundays','Billy Crystal tells the stories of his youth, growing up in the jazz world of Manhattan, his teenage years, and finally adulthood. The Tony Award-winning show is a funny and poignant exploration of family and fate, loving and loss.','tt3383040',NULL,NULL,NULL,2014,'foobar','2019-11-22 12:52:41'),(927,'Blackway','An ex-logger comes to the aid of a woman who returns to her hometown in the Pacific Northwest and finds herself harassed and stalked by a former cop turned crime lord.','tt4061010',NULL,NULL,NULL,2015,'foobar','2019-11-22 12:52:42'),(928,'Blind Justice','Canaan, a mysterious gunfighter left nearly blind from Civil War combat, roams through Mexico with a baby he has sworn to protect. On his way to a town where a family will supposedly adopt ...','tt0109294',NULL,NULL,NULL,1994,'foobar','2019-11-22 12:52:43'),(929,'Bone Tomahawk','In the dying days of the old west, an elderly sheriff and his posse set out to rescue their town\'s doctor from cannibalistic cave dwellers.','tt2494362',NULL,NULL,NULL,2015,'foobar','2019-11-22 12:52:43'),(930,'Breslin and Hamill: Deadline Artists','The story of New York City journalists Jimmy Breslin and Pete Hamill lauded in their time as the voice of New York.','tt9275202',NULL,NULL,NULL,2018,'foobar','2019-11-22 12:52:43'),(931,'Bright Lights: Starring Carrie Fisher and Debbie Reynolds','An intimate portrait of actress Debbie Reynolds and her relationship with her beloved children, Carrie Fisher and Todd Fisher.','tt5651050',NULL,NULL,NULL,2016,'foobar','2019-11-22 12:52:43'),(932,'Brillo Box (3 ¢ off)','\'Brillo Box (3¢ off)\' follows a beloved Andy Warhol Brillo Box sculpture as it makes its way from a family\'s living room to a record-breaking Christie\'s auction, blending personal narrative...','tt5113136',NULL,NULL,NULL,2016,'foobar','2019-11-22 12:52:43'),(933,'Brokeback Mountain','The story of a forbidden and secretive relationship between two cowboys, and their lives over the years.','tt0388795',NULL,NULL,NULL,2005,'foobar','2019-11-22 12:52:43'),(934,'Broken Child','N/A','tt0354436',NULL,NULL,NULL,2000,'foobar','2019-11-22 12:52:43'),(935,'Bruce Almighty','A guy who complains about God too often is given almighty powers to teach him how difficult it is to run the world.','tt0315327',NULL,NULL,NULL,2003,'foobar','2019-11-22 12:52:43'),(936,'Burn After Reading','A disk containing mysterious information from a CIA agent ends up in the hands of two unscrupulous and daft gym employees who attempt to sell it.','tt0887883',NULL,NULL,NULL,2008,'foobar','2019-11-22 12:52:43'),(937,'Burning','Jong-su bumps into a girl who used to live in the same neighborhood, who asks him to look after her cat while she\'s on a trip to Africa. When back, she introduces Ben, a mysterious guy she met there, who confesses his secret hobby.','tt7282468',NULL,NULL,NULL,2018,'foobar','2019-11-22 12:52:43'),(938,'Bury My Heart at Wounded Knee','A historic chronicle based on the book by Dee Brown explains how Native Americans were displaced as the United States expanded west.','tt0821638',NULL,NULL,NULL,2007,'foobar','2019-11-22 12:52:43');
/*!40000 ALTER TABLE `movie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie_genre`
--

DROP TABLE IF EXISTS `movie_genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `movie_genre` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `movie_id` int(11) DEFAULT NULL,
  `genre_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=319 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie_genre`
--

LOCK TABLES `movie_genre` WRITE;
/*!40000 ALTER TABLE `movie_genre` DISABLE KEYS */;
INSERT INTO `movie_genre` VALUES (1,867,1),(2,867,2),(3,867,3),(4,868,2),(5,868,3),(6,868,4),(7,868,5),(8,869,6),(9,869,2),(10,869,7),(11,870,8),(12,870,9),(13,870,2),(14,870,10),(15,871,11),(16,871,3),(17,872,6),(18,872,12),(19,873,6),(20,874,6),(21,875,11),(22,876,6),(23,876,2),(24,877,11),(25,877,13),(26,878,11),(27,879,9),(28,879,2),(29,879,4),(30,880,9),(31,880,2),(32,880,4),(33,881,1),(34,881,2),(35,882,2),(36,882,14),(37,883,11),(38,884,2),(39,884,3),(40,884,5),(41,885,4),(42,886,11),(43,887,11),(44,888,11),(45,888,6),(46,888,3),(47,888,15),(48,889,6),(49,889,2),(50,889,14),(51,890,1),(52,890,2),(53,890,3),(54,891,11),(55,892,6),(56,893,9),(57,893,2),(58,894,1),(59,894,6),(60,894,2),(61,895,11),(62,896,11),(63,896,6),(64,897,2),(65,897,16),(66,898,11),(67,898,13),(68,899,6),(69,900,6),(70,901,1),(71,901,2),(72,901,3),(73,901,5),(74,901,10),(75,902,2),(76,902,4),(77,903,11),(78,904,2),(79,904,6),(80,904,14),(81,905,17),(82,905,17),(83,905,17),(84,906,11),(85,907,11),(86,908,11),(87,908,1),(88,908,12),(89,909,2),(90,909,3),(91,909,14),(92,909,4),(93,910,11),(94,911,11),(95,912,6),(96,912,7),(97,913,2),(98,913,7),(99,913,14),(100,914,11),(101,915,11),(102,916,2),(103,916,18),(104,916,19),(105,916,4),(106,917,6),(107,917,2),(108,917,14),(109,918,1),(110,918,2),(111,918,20),(112,918,14),(113,919,1),(114,919,6),(115,919,2),(116,919,14),(117,920,1),(118,920,2),(119,920,20),(120,921,11),(121,921,1),(122,921,9),(123,922,11),(124,922,6),(125,923,11),(126,923,6),(127,924,11),(128,924,6),(129,925,11),(130,925,6),(131,926,1),(132,926,6),(133,926,2),(134,927,4),(135,928,8),(136,928,10),(137,929,2),(138,929,18),(139,929,10),(140,930,21),(141,931,11),(142,932,11),(143,932,13),(144,932,16),(145,933,2),(146,933,14),(147,934,11),(148,935,6),(149,935,2),(150,935,7),(151,936,6),(152,936,9),(153,936,2),(154,936,4),(155,937,2),(156,937,19),(157,938,2),(158,938,3),(159,938,10),(160,867,1),(161,867,2),(162,867,3),(163,868,2),(164,868,3),(165,868,4),(166,868,5),(167,869,6),(168,869,2),(169,869,7),(170,870,8),(171,870,9),(172,870,2),(173,870,10),(174,871,11),(175,871,3),(176,872,6),(177,872,12),(178,873,6),(179,874,6),(180,875,11),(181,876,6),(182,876,2),(183,877,11),(184,877,13),(185,878,11),(186,879,9),(187,879,2),(188,879,4),(189,880,9),(190,880,2),(191,880,4),(192,881,1),(193,881,2),(194,882,2),(195,882,14),(196,883,11),(197,884,2),(198,884,3),(199,884,5),(200,885,4),(201,886,11),(202,887,11),(203,888,11),(204,888,6),(205,888,3),(206,888,15),(207,889,6),(208,889,2),(209,889,14),(210,890,1),(211,890,2),(212,890,3),(213,891,11),(214,892,6),(215,893,9),(216,893,2),(217,894,1),(218,894,6),(219,894,2),(220,895,11),(221,896,11),(222,896,6),(223,897,2),(224,897,16),(225,898,11),(226,898,13),(227,899,6),(228,900,6),(229,901,1),(230,901,2),(231,901,3),(232,901,5),(233,901,10),(234,902,2),(235,902,4),(236,903,11),(237,904,2),(238,904,6),(239,904,14),(240,905,17),(241,905,17),(242,905,17),(243,906,11),(244,907,11),(245,908,11),(246,908,1),(247,908,12),(248,909,2),(249,909,3),(250,909,14),(251,909,4),(252,910,11),(253,911,11),(254,912,6),(255,912,7),(256,913,2),(257,913,7),(258,913,14),(259,914,11),(260,915,11),(261,916,2),(262,916,18),(263,916,19),(264,916,4),(265,917,6),(266,917,2),(267,917,14),(268,918,1),(269,918,2),(270,918,20),(271,918,14),(272,919,1),(273,919,6),(274,919,2),(275,919,14),(276,920,1),(277,920,2),(278,920,20),(279,921,11),(280,921,1),(281,921,9),(282,922,11),(283,922,6),(284,923,11),(285,923,6),(286,924,11),(287,924,6),(288,925,11),(289,925,6),(290,926,1),(291,926,6),(292,926,2),(293,927,4),(294,928,8),(295,928,10),(296,929,2),(297,929,18),(298,929,10),(299,930,21),(300,931,11),(301,932,11),(302,932,13),(303,932,16),(304,933,2),(305,933,14),(306,934,11),(307,935,6),(308,935,2),(309,935,7),(310,936,6),(311,936,9),(312,936,2),(313,936,4),(314,937,2),(315,937,19),(316,938,2),(317,938,3),(318,938,10);
/*!40000 ALTER TABLE `movie_genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie_review`
--

DROP TABLE IF EXISTS `movie_review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `movie_review` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rating` varchar(5) NOT NULL,
  `movie_id` int(11) DEFAULT NULL,
  `reviewer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie_review`
--

LOCK TABLES `movie_review` WRITE;
/*!40000 ALTER TABLE `movie_review` DISABLE KEYS */;
/*!40000 ALTER TABLE `movie_review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie_streaming_service_selection`
--

DROP TABLE IF EXISTS `movie_streaming_service_selection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `movie_streaming_service_selection` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `movie_id` int(11) NOT NULL,
  `streaming_service_id` int(11) DEFAULT NULL,
  `url` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=221 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie_streaming_service_selection`
--

LOCK TABLES `movie_streaming_service_selection` WRITE;
/*!40000 ALTER TABLE `movie_streaming_service_selection` DISABLE KEYS */;
INSERT INTO `movie_streaming_service_selection` VALUES (77,795,1,'https://fi.hbonordic.com/movies/12+Years+a+Slave/1f10ced-00bd71886ba'),(78,796,1,'https://fi.hbonordic.com/movies/The+12th+Man/1f10ced-0068b6e8776'),(79,797,1,'https://fi.hbonordic.com/movies/17+Again/1f10ced-00f8622f69c'),(80,798,1,'https://fi.hbonordic.com/movies/3:10+to+Yuma/1f10ced-00bd71a4d66'),(81,799,1,'https://fi.hbonordic.com/movies/4+Little+Girls/1f10ced-0062e5475ca'),(82,800,1,'https://fi.hbonordic.com/movies/7+Days+in+Hell/1f10ced-008313bde4d'),(83,801,1,'https://fi.hbonordic.com/movies/7th+Annual+Young+Comedians+Show/1f10ced-004d825f6c2'),(84,802,1,'https://fi.hbonordic.com/movies/The+8th+Annual+Young+Comedians+Show/1f10ced-004d826c6a1'),(85,803,1,'https://fi.hbonordic.com/movies/A+Dangerous+Son/1f10ced-00e58f58855'),(86,804,1,'https://fi.hbonordic.com/movies/A+Dog+Year/1f10ced-0049614e40c'),(87,805,1,'https://fi.hbonordic.com/movies/A+Girl+in+the+River:+The+Price+of+Forgiveness/1f10ced-0097475b3cb'),(88,806,1,'https://fi.hbonordic.com/movies/A+Good+Job:+Stories+of+the+FDNY/1f10ced-00656d14e52'),(89,807,1,'https://fi.hbonordic.com/movies/A+History+of+Violence/1f10ced-00bd72e58b1'),(90,808,1,'https://fi.hbonordic.com/movies/A+Most+Wanted+Man/1f10ced-0114fee6d1c'),(91,809,1,'https://fi.hbonordic.com/movies/A+Quiet+Passion/1f10ced-0102b56583d'),(92,810,1,'https://fi.hbonordic.com/movies/A+Single+Man/1f10ced-00f922d66db'),(93,811,1,'https://fi.hbonordic.com/movies/Abortion:+Stories+Women+Tell/1f10ced-00bf0388820'),(94,812,1,'https://fi.hbonordic.com/movies/Across+the+Waters/1f10ced-00f9229ed83'),(95,813,1,'https://fi.hbonordic.com/movies/Addiction/1f10ced-0067306fa56'),(96,814,1,'https://fi.hbonordic.com/movies/Agnelli/1f10ced-00d5dd03f6c'),(97,815,1,'https://fi.hbonordic.com/movies/Alive+Day+Memories:+Home+from+Iraq/1f10ced-005ea616638'),(98,816,1,'https://fi.hbonordic.com/movies/All+About+Ann:+Governor+Richards+of+the+Lone+Star+State/1f10ced-005d467c574'),(99,817,1,'https://fi.hbonordic.com/movies/All+Roads+Lead+to+Rome/1f10ced-010411ede68'),(100,818,1,'https://fi.hbonordic.com/movies/All+the+Way/1f10ced-009f95845da'),(101,819,1,'https://fi.hbonordic.com/movies/Alternate+Endings:+Six+new+ways+to+die+in+America/1f10ced-01163547121'),(102,820,1,'https://fi.hbonordic.com/movies/Amanda+Seales:+I+Be+Knowin\'/1f10ced-01043b1f195'),(103,821,1,'https://fi.hbonordic.com/movies/American+Hustle/1f10ced-0110451838d'),(104,822,1,'https://fi.hbonordic.com/movies/American+Splendor/1f10ced-0049dea1c89'),(105,823,1,'https://fi.hbonordic.com/movies/Americans+in+Bed/1f10ced-0049d48eadb'),(106,824,1,'https://fi.hbonordic.com/movies/Amy+Schumer:+Live+at+the+Apollo/1f10ced-008b06e65e0'),(107,825,1,'https://fi.hbonordic.com/movies/An+American+Girl:+Chrissa+Stands+Strong/1f10ced-0058ba4b458'),(108,826,1,'https://fi.hbonordic.com/movies/An+Apology+to+Elephants/1f10ced-004946503da'),(109,827,1,'https://fi.hbonordic.com/movies/Anchorman+2:+The+Legend+Continues/1f10ced-00e3e354219'),(110,828,1,'https://fi.hbonordic.com/movies/Anchorman:+The+Legend+of+Ron+Burgundy/1f10ced-0049e84590a'),(111,829,1,'https://fi.hbonordic.com/movies/And+Starring+Pancho+Villa+as+Himself/1f10ced-004946633b9'),(112,830,1,'https://fi.hbonordic.com/movies/Arbitrage/1f10ced-0114da7b50f'),(113,831,1,'https://fi.hbonordic.com/movies/Arthur+Miller:+Writer/1f10ced-00dc5390231'),(114,832,1,'https://fi.hbonordic.com/movies/As+You+Like+It/1f10ced-005d46ebfc3'),(115,833,1,'https://fi.hbonordic.com/movies/asterix/1f10ced-0104121914a'),(116,834,1,'https://fi.hbonordic.com/movies/At+the+Heart+of+Gold:+Inside+the+USA+Gymnastics+Scandal/1f10ced-010e7a60b6e'),(117,835,1,'https://fi.hbonordic.com/movies/Atomic+Homefront/1f10ced-00dc5381210'),(118,836,1,'https://fi.hbonordic.com/movies/Back+on+Board:+Greg+Louganis/1f10ced-0084cd14270'),(119,837,1,'https://fi.hbonordic.com/movies/Backstabbing+for+Beginners/1f10ced-0114fef5d7f'),(120,838,1,'https://fi.hbonordic.com/movies/Baghdad+ER/1f10ced-005ea6d6c68'),(121,839,1,'https://fi.hbonordic.com/movies/Baltimore+Rising/1f10ced-00d3cd3ad06'),(122,840,1,'https://fi.hbonordic.com/movies/The+Visitors:+Bastille+Day/1f10ced-0114ff0321f'),(123,841,1,'https://fi.hbonordic.com/movies/Beautiful+Creatures/1f10ced-00ed73c6c92'),(124,842,1,'https://fi.hbonordic.com/movies/Becoming+Mike+Nichols/1f10ced-0094c3c05be'),(125,843,1,'https://fi.hbonordic.com/movies/Becoming+Warren+Buffett/1f10ced-00b7bc034b6'),(126,844,1,'https://fi.hbonordic.com/movies/Before+I+Go+to+Sleep/1f10ced-00f8623e6bd'),(127,845,1,'https://fi.hbonordic.com/movies/Beginners/1f10ced-00f8624965a'),(128,846,1,'https://fi.hbonordic.com/movies/Behind+the+Candelabra/1f10ced-00bd71d1dc3'),(129,847,1,'https://fi.hbonordic.com/movies/Bernard+and+Doris/1f10ced-0049deb2cea'),(130,848,1,'https://fi.hbonordic.com/movies/Bessie/1f10ced-007f394c952'),(131,849,1,'https://fi.hbonordic.com/movies/Beware+the+Slenderman/1f10ced-00b7bc12497'),(132,850,1,'https://fi.hbonordic.com/movies/Bill+Maher:+Live+from+D.C./1f10ced-00696c919ff'),(133,851,1,'https://fi.hbonordic.com/movies/Bill+Maher:+Live+from+Oklahoma/1f10ced-00ec5b22485'),(134,852,1,'https://fi.hbonordic.com/movies/Bill+Maher:+The+Decider/1f10ced-0049eb2d8b8'),(135,853,1,'https://fi.hbonordic.com/movies/Bill+Maher:+Victory+Begins+at+Home/1f10ced-004af272f0a'),(136,854,1,'https://fi.hbonordic.com/movies/Billy+Crystal:+700+Sundays/1f10ced-005cedc8f0b'),(137,855,1,'https://fi.hbonordic.com/movies/Blackway/1f10ced-010411fee0b'),(138,856,1,'https://fi.hbonordic.com/movies/Blind+Justice/1f10ced-0070676734d'),(139,857,1,'https://fi.hbonordic.com/movies/Bone+Tomahawk/1f10ced-00fc8eb4b64'),(140,858,1,'https://fi.hbonordic.com/movies/Breslin+and+Hamill:+Deadline+Artists/1f10ced-0103b1fb8b8'),(141,859,1,'https://fi.hbonordic.com/movies/Bright+Lights:+Starring+Carrie+Fisher+and+Debbie+Reynolds/1f10ced-00b81b855ff'),(142,860,1,'https://fi.hbonordic.com/movies/Brillo+Box+(3+¢+off)/1f10ced-00c9977201e'),(143,861,1,'https://fi.hbonordic.com/movies/Brokeback+Mountain/1f10ced-008aadabf9b'),(144,862,1,'https://fi.hbonordic.com/movies/Broken+Child/1f10ced-00661ada5bb'),(145,863,1,'https://fi.hbonordic.com/movies/Bruce+Almighty/1f10ced-00f8626b618'),(146,864,1,'https://fi.hbonordic.com/movies/Burn+After+Reading/1f10ced-00f8627a639'),(147,865,1,'https://fi.hbonordic.com/movies/Burning/1f10ced-00f8625867b'),(148,866,1,'https://fi.hbonordic.com/movies/Bury+My+Heart+at+Wounded+Knee/1f10ced-0058ba5a479'),(149,867,1,'https://fi.hbonordic.com/movies/12+Years+a+Slave/1f10ced-00bd71886ba'),(150,868,1,'https://fi.hbonordic.com/movies/The+12th+Man/1f10ced-0068b6e8776'),(151,869,1,'https://fi.hbonordic.com/movies/17+Again/1f10ced-00f8622f69c'),(152,870,1,'https://fi.hbonordic.com/movies/3:10+to+Yuma/1f10ced-00bd71a4d66'),(153,871,1,'https://fi.hbonordic.com/movies/4+Little+Girls/1f10ced-0062e5475ca'),(154,872,1,'https://fi.hbonordic.com/movies/7+Days+in+Hell/1f10ced-008313bde4d'),(155,873,1,'https://fi.hbonordic.com/movies/7th+Annual+Young+Comedians+Show/1f10ced-004d825f6c2'),(156,874,1,'https://fi.hbonordic.com/movies/The+8th+Annual+Young+Comedians+Show/1f10ced-004d826c6a1'),(157,875,1,'https://fi.hbonordic.com/movies/A+Dangerous+Son/1f10ced-00e58f58855'),(158,876,1,'https://fi.hbonordic.com/movies/A+Dog+Year/1f10ced-0049614e40c'),(159,877,1,'https://fi.hbonordic.com/movies/A+Girl+in+the+River:+The+Price+of+Forgiveness/1f10ced-0097475b3cb'),(160,878,1,'https://fi.hbonordic.com/movies/A+Good+Job:+Stories+of+the+FDNY/1f10ced-00656d14e52'),(161,879,1,'https://fi.hbonordic.com/movies/A+History+of+Violence/1f10ced-00bd72e58b1'),(162,880,1,'https://fi.hbonordic.com/movies/A+Most+Wanted+Man/1f10ced-0114fee6d1c'),(163,881,1,'https://fi.hbonordic.com/movies/A+Quiet+Passion/1f10ced-0102b56583d'),(164,882,1,'https://fi.hbonordic.com/movies/A+Single+Man/1f10ced-00f922d66db'),(165,883,1,'https://fi.hbonordic.com/movies/Abortion:+Stories+Women+Tell/1f10ced-00bf0388820'),(166,884,1,'https://fi.hbonordic.com/movies/Across+the+Waters/1f10ced-00f9229ed83'),(167,885,1,'https://fi.hbonordic.com/movies/Addiction/1f10ced-0067306fa56'),(168,886,1,'https://fi.hbonordic.com/movies/Agnelli/1f10ced-00d5dd03f6c'),(169,887,1,'https://fi.hbonordic.com/movies/Alive+Day+Memories:+Home+from+Iraq/1f10ced-005ea616638'),(170,888,1,'https://fi.hbonordic.com/movies/All+About+Ann:+Governor+Richards+of+the+Lone+Star+State/1f10ced-005d467c574'),(171,889,1,'https://fi.hbonordic.com/movies/All+Roads+Lead+to+Rome/1f10ced-010411ede68'),(172,890,1,'https://fi.hbonordic.com/movies/All+the+Way/1f10ced-009f95845da'),(173,891,1,'https://fi.hbonordic.com/movies/Alternate+Endings:+Six+new+ways+to+die+in+America/1f10ced-01163547121'),(174,892,1,'https://fi.hbonordic.com/movies/Amanda+Seales:+I+Be+Knowin\'/1f10ced-01043b1f195'),(175,893,1,'https://fi.hbonordic.com/movies/American+Hustle/1f10ced-0110451838d'),(176,894,1,'https://fi.hbonordic.com/movies/American+Splendor/1f10ced-0049dea1c89'),(177,895,1,'https://fi.hbonordic.com/movies/Americans+in+Bed/1f10ced-0049d48eadb'),(178,896,1,'https://fi.hbonordic.com/movies/Amy+Schumer:+Live+at+the+Apollo/1f10ced-008b06e65e0'),(179,897,1,'https://fi.hbonordic.com/movies/An+American+Girl:+Chrissa+Stands+Strong/1f10ced-0058ba4b458'),(180,898,1,'https://fi.hbonordic.com/movies/An+Apology+to+Elephants/1f10ced-004946503da'),(181,899,1,'https://fi.hbonordic.com/movies/Anchorman+2:+The+Legend+Continues/1f10ced-00e3e354219'),(182,900,1,'https://fi.hbonordic.com/movies/Anchorman:+The+Legend+of+Ron+Burgundy/1f10ced-0049e84590a'),(183,901,1,'https://fi.hbonordic.com/movies/And+Starring+Pancho+Villa+as+Himself/1f10ced-004946633b9'),(184,902,1,'https://fi.hbonordic.com/movies/Arbitrage/1f10ced-0114da7b50f'),(185,903,1,'https://fi.hbonordic.com/movies/Arthur+Miller:+Writer/1f10ced-00dc5390231'),(186,904,1,'https://fi.hbonordic.com/movies/As+You+Like+It/1f10ced-005d46ebfc3'),(187,905,1,'https://fi.hbonordic.com/movies/asterix/1f10ced-0104121914a'),(188,906,1,'https://fi.hbonordic.com/movies/At+the+Heart+of+Gold:+Inside+the+USA+Gymnastics+Scandal/1f10ced-010e7a60b6e'),(189,907,1,'https://fi.hbonordic.com/movies/Atomic+Homefront/1f10ced-00dc5381210'),(190,908,1,'https://fi.hbonordic.com/movies/Back+on+Board:+Greg+Louganis/1f10ced-0084cd14270'),(191,909,1,'https://fi.hbonordic.com/movies/Backstabbing+for+Beginners/1f10ced-0114fef5d7f'),(192,910,1,'https://fi.hbonordic.com/movies/Baghdad+ER/1f10ced-005ea6d6c68'),(193,911,1,'https://fi.hbonordic.com/movies/Baltimore+Rising/1f10ced-00d3cd3ad06'),(194,912,1,'https://fi.hbonordic.com/movies/The+Visitors:+Bastille+Day/1f10ced-0114ff0321f'),(195,913,1,'https://fi.hbonordic.com/movies/Beautiful+Creatures/1f10ced-00ed73c6c92'),(196,914,1,'https://fi.hbonordic.com/movies/Becoming+Mike+Nichols/1f10ced-0094c3c05be'),(197,915,1,'https://fi.hbonordic.com/movies/Becoming+Warren+Buffett/1f10ced-00b7bc034b6'),(198,916,1,'https://fi.hbonordic.com/movies/Before+I+Go+to+Sleep/1f10ced-00f8623e6bd'),(199,917,1,'https://fi.hbonordic.com/movies/Beginners/1f10ced-00f8624965a'),(200,918,1,'https://fi.hbonordic.com/movies/Behind+the+Candelabra/1f10ced-00bd71d1dc3'),(201,919,1,'https://fi.hbonordic.com/movies/Bernard+and+Doris/1f10ced-0049deb2cea'),(202,920,1,'https://fi.hbonordic.com/movies/Bessie/1f10ced-007f394c952'),(203,921,1,'https://fi.hbonordic.com/movies/Beware+the+Slenderman/1f10ced-00b7bc12497'),(204,922,1,'https://fi.hbonordic.com/movies/Bill+Maher:+Live+from+D.C./1f10ced-00696c919ff'),(205,923,1,'https://fi.hbonordic.com/movies/Bill+Maher:+Live+from+Oklahoma/1f10ced-00ec5b22485'),(206,924,1,'https://fi.hbonordic.com/movies/Bill+Maher:+The+Decider/1f10ced-0049eb2d8b8'),(207,925,1,'https://fi.hbonordic.com/movies/Bill+Maher:+Victory+Begins+at+Home/1f10ced-004af272f0a'),(208,926,1,'https://fi.hbonordic.com/movies/Billy+Crystal:+700+Sundays/1f10ced-005cedc8f0b'),(209,927,1,'https://fi.hbonordic.com/movies/Blackway/1f10ced-010411fee0b'),(210,928,1,'https://fi.hbonordic.com/movies/Blind+Justice/1f10ced-0070676734d'),(211,929,1,'https://fi.hbonordic.com/movies/Bone+Tomahawk/1f10ced-00fc8eb4b64'),(212,930,1,'https://fi.hbonordic.com/movies/Breslin+and+Hamill:+Deadline+Artists/1f10ced-0103b1fb8b8'),(213,931,1,'https://fi.hbonordic.com/movies/Bright+Lights:+Starring+Carrie+Fisher+and+Debbie+Reynolds/1f10ced-00b81b855ff'),(214,932,1,'https://fi.hbonordic.com/movies/Brillo+Box+(3+¢+off)/1f10ced-00c9977201e'),(215,933,1,'https://fi.hbonordic.com/movies/Brokeback+Mountain/1f10ced-008aadabf9b'),(216,934,1,'https://fi.hbonordic.com/movies/Broken+Child/1f10ced-00661ada5bb'),(217,935,1,'https://fi.hbonordic.com/movies/Bruce+Almighty/1f10ced-00f8626b618'),(218,936,1,'https://fi.hbonordic.com/movies/Burn+After+Reading/1f10ced-00f8627a639'),(219,937,1,'https://fi.hbonordic.com/movies/Burning/1f10ced-00f8625867b'),(220,938,1,'https://fi.hbonordic.com/movies/Bury+My+Heart+at+Wounded+Knee/1f10ced-0058ba5a479');
/*!40000 ALTER TABLE `movie_streaming_service_selection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviewer`
--

DROP TABLE IF EXISTS `reviewer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reviewer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviewer`
--

LOCK TABLES `reviewer` WRITE;
/*!40000 ALTER TABLE `reviewer` DISABLE KEYS */;
/*!40000 ALTER TABLE `reviewer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scrape_insertion_error`
--

DROP TABLE IF EXISTS `scrape_insertion_error`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scrape_insertion_error` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `scrape_title` varchar(255) NOT NULL,
  `scrape_url` varchar(255) NOT NULL,
  `proposed_movie_id` int(11) DEFAULT NULL,
  `proposed_tv_series_id` int(11) DEFAULT NULL,
  `proposed_imdb_title` varchar(255) DEFAULT NULL,
  `proposed_imdb_url` varchar(255) DEFAULT NULL,
  `information` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scrape_insertion_error`
--

LOCK TABLES `scrape_insertion_error` WRITE;
/*!40000 ALTER TABLE `scrape_insertion_error` DISABLE KEYS */;
/*!40000 ALTER TABLE `scrape_insertion_error` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `streaming_service`
--

DROP TABLE IF EXISTS `streaming_service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `streaming_service` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `streaming_service`
--

LOCK TABLES `streaming_service` WRITE;
/*!40000 ALTER TABLE `streaming_service` DISABLE KEYS */;
INSERT INTO `streaming_service` VALUES (1,'hbo','https://api-hbon.hbo.clearleap.com/cloffice/client/web/browse/ea73aabd-24a3-473e-8f3a-39aeb7f0f93e?max=20&language=fi_hbon&offset=');
/*!40000 ALTER TABLE `streaming_service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tv_series`
--

DROP TABLE IF EXISTS `tv_series`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tv_series` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `imdb_url` varchar(255) DEFAULT NULL,
  `imdb_rating` varchar(4) DEFAULT NULL,
  `year` int(4) DEFAULT NULL,
  `poster_url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tv_series`
--

LOCK TABLES `tv_series` WRITE;
/*!40000 ALTER TABLE `tv_series` DISABLE KEYS */;
/*!40000 ALTER TABLE `tv_series` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tv_series_episode`
--

DROP TABLE IF EXISTS `tv_series_episode`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tv_series_episode` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tv_series_season_id` int(11) DEFAULT NULL,
  `episode_name` varchar(255) NOT NULL,
  `episode_url` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tv_series_episode`
--

LOCK TABLES `tv_series_episode` WRITE;
/*!40000 ALTER TABLE `tv_series_episode` DISABLE KEYS */;
/*!40000 ALTER TABLE `tv_series_episode` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tv_series_genre`
--

DROP TABLE IF EXISTS `tv_series_genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tv_series_genre` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tv_series_id` int(11) DEFAULT NULL,
  `genre_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tv_series_genre`
--

LOCK TABLES `tv_series_genre` WRITE;
/*!40000 ALTER TABLE `tv_series_genre` DISABLE KEYS */;
/*!40000 ALTER TABLE `tv_series_genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tv_series_review`
--

DROP TABLE IF EXISTS `tv_series_review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tv_series_review` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rating` varchar(5) NOT NULL,
  `tv_series_id` int(11) NOT NULL,
  `reviewer_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tv_series_review`
--

LOCK TABLES `tv_series_review` WRITE;
/*!40000 ALTER TABLE `tv_series_review` DISABLE KEYS */;
/*!40000 ALTER TABLE `tv_series_review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tv_series_season`
--

DROP TABLE IF EXISTS `tv_series_season`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tv_series_season` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tv_series_id` int(11) DEFAULT NULL,
  `season_number` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tv_series_season`
--

LOCK TABLES `tv_series_season` WRITE;
/*!40000 ALTER TABLE `tv_series_season` DISABLE KEYS */;
/*!40000 ALTER TABLE `tv_series_season` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tv_series_streaming_service_selection`
--

DROP TABLE IF EXISTS `tv_series_streaming_service_selection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tv_series_streaming_service_selection` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `episode_id` int(11) NOT NULL,
  `streaming_service_id` int(11) DEFAULT NULL,
  `url` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tv_series_streaming_service_selection`
--

LOCK TABLES `tv_series_streaming_service_selection` WRITE;
/*!40000 ALTER TABLE `tv_series_streaming_service_selection` DISABLE KEYS */;
/*!40000 ALTER TABLE `tv_series_streaming_service_selection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tv_show_review`
--

DROP TABLE IF EXISTS `tv_show_review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tv_show_review` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rating` varchar(5) NOT NULL,
  `tv_show_id` int(11) DEFAULT NULL,
  `reviewer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tv_show_review`
--

LOCK TABLES `tv_show_review` WRITE;
/*!40000 ALTER TABLE `tv_show_review` DISABLE KEYS */;
/*!40000 ALTER TABLE `tv_show_review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(25) NOT NULL,
  `password` varchar(255) NOT NULL,
  `salt` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`),
  KEY `username_2` (`username`,`password`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_movie_view_history`
--

DROP TABLE IF EXISTS `user_movie_view_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_movie_view_history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `movie_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_movie_view_history`
--

LOCK TABLES `user_movie_view_history` WRITE;
/*!40000 ALTER TABLE `user_movie_view_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_movie_view_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_tv_series_view_history`
--

DROP TABLE IF EXISTS `user_tv_series_view_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_tv_series_view_history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `tv_series_episode_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_tv_series_view_history`
--

LOCK TABLES `user_tv_series_view_history` WRITE;
/*!40000 ALTER TABLE `user_tv_series_view_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_tv_series_view_history` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-25  8:44:16
