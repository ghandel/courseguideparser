<html>
<head>
<script>
function sendSelection(selection) {
	//window.opener.document.getElementById('CIRCULATION-FORM-OPTIONS-GENERAL.EVENT-DESCRIPTION').value=selection;
	//window.close();
	if (window.opener != null) {
		document.write(window.opener.document.getElementById('footer').innerHTML);
		window.opener.document.write("<p>This is 'myWindow'</p>");
	}
	else {
		document.write("Fail.");
	}
}
function test(id) {
	document.getElementById(id).innerHTML=id;
}
</script>
</head>
<body>
<?php

$patron = $_GET['patron'];

$link = mysql_connect('gchandelcom.ipagemysql.com', 'dmcstaff13', '1am@MAC!'); 
if (!$link) { 
    die('Could not connect: ' . mysql_error()); 
} 
mysql_select_db('dmc_application_db_2013'); 

$query = 'SELECT * FROM courseguide 
	WHERE instructor LIKE \'%' . $patron . '%\'';
$result = mysql_query($query);

$courses = array();

if(!$result) {
	echo 'No instructor by name of: ' . $patron;
}
else {
    $num=mysql_num_rows($result);
    $i = 0;
    while ($i < $num) {
    	$course = mysql_result($result, $i, "subject number title");
    	array_push($courses, $course);
    	$i ++;
    }

	echo "Courses for <strong>" . $patron . "</strong>:<br><hr>";

	$courses_len = sizeof($courses);
	$x = 0;

	while ($x < $courses_len) {
		# Commented line below is for next version. Goal is to autofil the "Class or Event Title" field.
		# echo "<button id='" . $courses[$x] . "' onclick='sendSelection(\"" . $courses[$x] . "\")'>" . $courses[$x] . "</button><br>";
		echo "<p id='" . $courses[$x] . "'>" . $courses[$x] . "</p>";
		$x ++;
	}
}
?>
<button onclick="window.close();">Close Window!</button>
</body>
</html