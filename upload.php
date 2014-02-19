<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
  <head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <title>Digital Media Center | University of Wisconsin–Madison</title>
  <link href='application.css' rel='stylesheet' type='text/css'>
  <link rel="stylesheet" href="css/main_empty_shell.css" type="text/css" media="all" />
  <!--[if IE 6]>
    <link rel="stylesheet" href="css/ie6.css" type="text/css" media="screen" />
  <![endif]-->
  <!--[if IE 7]>
    <link rel="stylesheet" href="css/ie7.css" type="text/css" media="screen" />
  <![endif]-->
  <!--[if IE 8]>
    <link rel="stylesheet" href="css/ie8.css" type="text/css" media="screen" />
  <![endif]-->
<script type="text/javascript" src="js/jquery-1.10.2.min.js"></script>
<script type="text/javascript" src="js/hoverIntent.js"></script>
<script type="text/javascript" src="js/superfish.js"></script>
<script type="text/javascript" src="http://database.gchandel.com/js/index.js"></script>
  </head>
<body>
<div class="wrap">
  <div id="home">
    <div id="header">
      <div class="skip"><a href="#content" accesskey="S">Skip to main content</a></div>

      <a id="uwhome" href="http://www.wisc.edu"><img src="images/wordmark.gif" alt="University of Wisconsin–Madison" width="260" height="11" /></a>

      <a id="crest" href="http://www.wisc.edu"><img src="images/crest.png" alt="UW–Madison crest." width="70" height="106" /></a>

      <div id="siteTitle">
        <h1><a href="index.html"><span>Digital Media Center</span></a></h1>
        <div id="tagline"><span>Application for Employment</span></div>
      </div>

      <ul id="globalnav">
        <li id="uwsearch"><a href="http://www.wisc.edu/search/">UW Search</a></li><li><a href="http://my.wisc.edu">My UW</a></li><li><a href="http://map.wisc.edu">Map</a></li><li id="last_tool"><a href="http://www.today.wisc.edu">Calendar</a></li>
      </ul>

      <form id="search" action="post">
        <div>
          <label for="searchstring">Search this site: </label> <input name="searchstring" id="searchstring" type="text" value="" /><input name="submit" id="submit" type="submit" value="Go!" />
        </div>
      </form>
    </div>

    <ul class="main-menu">
      <li id="n_home" class="current"><h2><a href="/">Home</a></h2>
      </li><li id="n_current_ad"><h2><a href="/admissions/">Future Students</a></h2>
      <ul class="submenu">
        <li><a href="#">Undergraduate admissions</a></li>
        <li><a href="#">Graduate admissions</a></li>
        <li><a href="#">Financial aid</a></li>
        <li><a href="#">Visit us</a></li>
      </ul>
      </li><li id="n_current_st"><h2><a href="/academics/">Current Students</a></h2>
      <ul class="submenu">
        <li><a href="#">Undergraduate major</a></li>
        <li><a href="#">Graduate programs</a></li>
        <li><a href="#">Advising</a></li>
      </ul>
      </li><li id="n_alum"><h2><a href="/research/">Alumni and Friends</a></h2>
      <ul class="submenu">
        <li><a href="#">Alumni profiles</a></li>
        <li><a href="#">Alumni directory</a></li>
        <li><a href="#">Giving</a></li>
      </ul>
      </li><li id="n_staff"><h2><a href="/staff/">Faculty and Staff</a></h2>
      <ul class="submenu">
        <li><a href="#">A-Z Directory</a></li>
        <li><a href="#">Internal resources</a></li>
        <li><a href="#">Awards and honors</a></li>
      </ul>
      </li>
    </ul>


    <div id="shell">
        <div id="content" class="main col">
            <div class="container">
                <div class="form_container">
                    <center>
                        <strong>Course Guide CSV Upload</strong><br>
                    </center>
                </div>
                <form action="upload.php" method="post" enctype="multipart/form-data" name="app_form">
                <div class="form_container">
                    <div class="form_line_container">
                        <span>
                            CSV File for upload to DB: 
                        </span>
                        <span  class="form_box" id="file_box">
                            <input type="file" name="db_csv" id="file">
                        </span>
                        <br>
                        <span>
                            Allocations CSV File for Data Validation: 
                        </span>
                        <span  class="form_box" id="file_box">
                            <input type="file" name="find_allocations_page" id="file">
                        </span>
                        <br>
                        <span>
                            People CSV File for Data Validation: 
                        </span>
                        <span  class="form_box" id="file_box">
                            <input type="file" name="find_people_page" id="file">
                        </span>
                    </div>
                </div>
                <div class="form_container">
                    <center><input id="submit" type="Submit" value="Submit CSV"></center>
                </div>
            </form>
            </div>
        </div>
    </div>
  </div>

  <div id="footer">
    <p>Digital Media Center, 420 Henry Mall, Room B1131, Madison, WI 53706 | 608-265-4817</p>
    <p>Contact us at: <a href="mailto:dmc@doit.wisc.edu">dmc@doit.wisc.edu</a></p>
    <p>© 2010 Board of Regents of the <a href="http://www.wisconsin.edu">University of Wisconsin System</a></p>
    <p><a href="view_data.php">Managers Login</a></p>
  </div>
</div>
</body>
</html>

<?php
$link = mysql_connect('gchandelcom.ipagemysql.com', 'dmcstaff13', '1am@MAC!'); 
#$link = mysql_connect('localhost', 'admin', ''); 
if (!$link) { 
    die('Could not connect: ' . mysql_error()); 
} 
mysql_select_db('dmc_application_db_2013'); 
#mysql_select_db('test'); 

if($file = $_FILES['db_csv']['tmp_name']) {
    $handle = fopen($file, 'r');

    while ($data = fgetcsv($handle,1000,",","'")) {
        if ($data[0]) {
            mysql_query("INSERT INTO courseguide VALUES
                (
                    '$data[0]',
                    '$data[1]',
                    '$data[2]',
                    '$data[3]',
                    '$data[4]',
                    '$data[5]',
                    '$data[6]'
                )
            ");
        }
        else {
            echo 'Fail.';
        }
    }
}

if ($file_1 = $_FILES['find_allocations_page']['tmp_name'] && $file_2 = $_FILES['find_people_page']['tmp_name']) {
    $find_allocations_page = fopen($file_1, 'r');
    $find_people_page = fopen($file_2, 'r');

    
}
?>