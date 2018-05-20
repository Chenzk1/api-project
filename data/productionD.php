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

$sql = "CREATE TABLE productionD( ".
        "days INT NOT NULL AUTO_INCREMENT, ".
        "num INT NOT NULL, ".
        "PRIMARY KEY ( days ))ENGINE=InnoDB DEFAULT CHARSET=utf8; ";
mysqli_select_db( $conn, 'myproject' );
$retval = mysqli_query( $conn, $sql );
if(! $retval )
{
    die('数据表创建失败: ' . mysqli_error($conn));
}
echo "数据表创建成功\n";

// 设置编码，防止中文乱码
mysqli_close($conn);
?>