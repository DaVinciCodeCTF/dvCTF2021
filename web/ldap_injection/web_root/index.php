<html>
<head>
</head>
<body>
<link rel='stylesheet' property='stylesheet' id='s' type='text/css' href='/template/s.css' media='all' />

<h1>SSO v 0.03</h1>
<div style="text-align: right;">
<a href="?action=auth">Authentication</a>&nbsp;|&nbsp;<a href="?action=team">Our team</a>
</div>
<fieldset>


<?php

$form = '

<legend>Authenticate yourself</legend>
<form action="" method="post">
<p>
	Email&nbsp;<br/>
	<input type="text" name="email" />
</p>
<p>
	Password&nbsp;<br/>
	<input type="password" name="password" /><br/>
</p>
<br/>
	<input type="submit" value="connect" />
</form>
</fieldset>
</body></html>


';

$flag = 'dvCTF{th4nk_y0u_mR_UKN}';

$ds=ldap_connect("openldap");  // doit être un serveur LDAP valide !
ldap_set_option($ds, LDAP_OPT_PROTOCOL_VERSION, 3);

if (!$ds) { die('Connection error ...'); }

$r=ldap_bind($ds, "cn=admin,dc=dvctf,dc=local","Tfron45grtgt!%GYFRgrtgt");  


if(isset($_GET['action']) && $_GET['action'] == 'team')
{
	echo 'We are 3 developers and 1 sysadmin : <br /><br />';

	$sr=ldap_search($ds, "ou=Users,dc=dvctf,dc=local", "(objectClass=person)"); 

	$info = ldap_get_entries($ds, $sr);

	for ($i=0; $i<$info["count"]; $i++) {
		echo 'Name: ' . $info[$i]["cn"][0] . '<br />';
		echo 'Mail: ' . $info[$i]["mail"][0] . '<br />';
		echo '<!-- Userpassword: REDACTED -->';
		echo '<!-- Description: REDACTED --> <br />';
	}
	
	echo 'We are currently looking for a network admin ! Please contact us if interested ! <br /><br />';
}
else
{
	if(isset($_POST['email']) && !empty($_POST['email']) && isset($_POST['password']) && !empty($_POST['password']))
	{
		$email = $_POST['email'];
		$password = "{MD5}" . base64_encode(md5($_POST['password'], true));
		$sr=ldap_search($ds, "ou=Users,dc=dvctf,dc=local", "(&(mail=$email)(objectClass=person))"); 

		$info = ldap_get_entries($ds, $sr);
		if($info["count"] === 0) 
		{
			echo($form);
			die("No such user !");
		}
		for ($i=0; $i<$info["count"]; $i++) 
		{
			if($password === $info[$i]["userpassword"][0]) 
			{
				if($info[$i]["description"][0] === "sysadmin")
				{
					 die("<center>Welcome <b>" . $info[$i]["cn"][0] . " </b>!<br>Here is your cute cat picture :<br><img src='secret_cat_pic.jpg' /><br><br><br><br><br><br><br><br><br><br><b>\nWell done, the flag is : $flag\n</b></center>");
				}
				else
				{
 					die("<center>Welcome <b>" . $info[$i]["cn"][0] . " </b>!<br>Here is your cute cat picture :<br><img src='secret_cat_pic.jpg' /><br><br><br><br><br><br><br><br><br><br><b>\nYou are not the sysadmin, go back to work !!!\n</b></center>");
				}
			}
		}
		echo($form);
		die("Invalid username/password !");
	}
	else
	{
		echo($form);
	}
}

ldap_close($ds);


?>
