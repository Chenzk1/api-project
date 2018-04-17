<?php
$dbhost = 'localhost';  // mysql服务器主机地址
$dbuser = 'Chenzk';            // mysql用户名
$dbpass = 'Chenzk1';          // mysql用户名密码
$conn = mysqli_connect($dbhost, $dbuser, $dbpass);
if(! $conn )
{
    die('Could not connect: ' . mysqli_error());
}
echo '数据库连接成功！';

$sql = "CREATE TABLE reject( ".
        "month INT NOT NULL AUTO_INCREMENT, ".
        "totalProduct INT NOT NULL, ".
        "qualifyProduct INT NOT NULL, ".
        "totalWaste INT NOT NULL, ".
        "cbls INT NOT NULL, ".
        "qx INT NOT NULL, ".
        "cy INT NOT NULL, ".
        "nt INT NOT NULL, ".
        "sf INT NOT NULL, ".
        "cp INT NOT NULL, ".
        "zj INT NOT NULL, ".
        "cg INT NOT NULL, ".
        "PRIMARY KEY ( month ))ENGINE=InnoDB DEFAULT CHARSET=utf8; ";
mysqli_select_db( $conn, 'myproject' );
$retval = mysqli_query( $conn, $sql );
if(! $retval )
{
    die('数据表创建失败: ' . mysqli_error($conn));
}
echo "数据表创建成功\n";
mysqli_close($conn);
?>