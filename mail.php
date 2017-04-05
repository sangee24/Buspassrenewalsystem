<?php

$name = $_POST['name'];
$email = $_POST['email'];
$sub = $_POST['subject'];
$query = $_POST['message'];
//$message = $_POST['message'];


$to = "{{register.email}}";

$subject = "A3 Tech : Email from Contact Page";

$message = "
<html>
<head>
<title>CONTACT DETAILS</title>
</head>
<body><br />

'''''''''''''''''''''''''''''<br />
Enquiry Details<br />
'''''''''''''''''''''''''''''<br /><br />

Name  	&nbsp;&nbsp;&nbsp;	: &nbsp;		".$name."<br /><br />
Email ID&nbsp;&nbsp;	:	&nbsp;			".$email."<br /><br />
Subject &nbsp;&nbsp; 		: &nbsp;		".$sub."<br /><br />
Message	&nbsp;	:<br />&nbsp;&nbsp;&nbsp;	".$query."
</body>
</html>
";

// Always set content-type when sending HTML email
$headers = "MIME-Version: 1.0" . "\r\n";
$headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";

// More headers
$headers .= 'From: webmaster@a3.olivegrapes.in' . "\r\n";


mail($to,$subject,$message,$headers);
header("Location: http://www.a3.olivegrapes.in");?>
