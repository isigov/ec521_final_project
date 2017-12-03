<?php
/* Auth addition to evercookie
 *
 * EC521 - Avengers
 */

include dirname(__FILE__) . DIRECTORY_SEPARATOR . '_cookie_name.php';
$cookie_name = evercookie_get_cookie_name(__FILE__);

if (empty($_COOKIE[$cookie_name])) {
    /* $mycookie = $_SERVER['PHP_AUTH_USER']; */
if (!isset($_SERVER['PHP_AUTH_USER'])) {
    header('WWW-Authenticate: Basic realm="My Realm"');
    header('HTTP/1.0 401 Unauthorized');
    echo 'Text to send if user hits Cancel button';
    exit;
} else {
    echo "<p>Hello {$_SERVER['PHP_AUTH_USER']}.</p>";
    echo "<p>You entered {$_SERVER['PHP_AUTH_PW']} as your password.</p>";
}
} else {
    echo $_COOKIE[$cookie_name];
    echo $_SERVER['PHP_AUTH_USER'];
    if ($_COOKIE[$cookie_name] !== $_SERVER['PHP_AUTH_USER']) {
        echo 'Existing cookie is now equal';
        // User generated a new evercookie
        $_COOKIE[$cookie_name] = $_SERVER['PHP_AUTH_USER'];
    }
}

if(!headers_sent()) {
    header('Content-Type: text/html');
    header('Last-Modified: Wed, 30 Jun 2010 21:36:48 GMT');
    header('Expires: Tue, 31 Dec 2030 23:30:45 GMT');
    header('Cache-Control: private, max-age=630720000');
}
echo $mycookie;
?>
